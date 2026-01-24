import json
import folium

# Load summarized crop and rainfall data
with open("state_prod_rain_fixed1.json", "r") as f:
    state_summary = json.load(f)

# Load India GeoJSON
with open("india_states.geojson", "r", encoding="utf-8") as f:
    india_geo = json.load(f)

# Normalize GeoJSON features with lowercase state IDs
for feature in india_geo["features"]:
    feature["id"] = feature["properties"]["NAME_1"].strip().lower()

# Prepare data for choropleth
choropleth_data = []
prod_values = []

for state, stats in state_summary.items():
    state_id = state.strip().lower()
    if state_id in [f['id'] for f in india_geo['features']]:
        choropleth_data.append([state_id, stats["Total Production"]])
        prod_values.append(stats["Total Production"])

# Determine threshold for top producers (90th percentile)
prod_threshold = sorted(prod_values)[int(0.9 * len(prod_values))]

# Create Folium map
m = folium.Map(location=[23.5, 80.5], zoom_start=5, tiles="CartoDB positron")

# Add Choropleth layer
folium.Choropleth(
    geo_data=india_geo,
    data=choropleth_data,
    columns=[0, 1],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Total Crop Production (tonnes)"
).add_to(m)

# Helper function to get centroid for placing markers
def get_centroid(geometry):
    coords = geometry["coordinates"]
    if geometry["type"] == "Polygon":
        lon_lat = coords[0][0]
    elif geometry["type"] == "MultiPolygon":
        lon_lat = coords[0][0][0]
    else:
        return None
    return [lon_lat[1], lon_lat[0]]  # Return [lat, lon]

# Add markers for high rainfall or high production states
for feature in india_geo["features"]:
    state_id = feature["id"]
    stats = state_summary.get(state_id.title()) or state_summary.get(state_id)
    if stats:
        if stats["Avg Rainfall"] > 2500 or stats["Total Production"] > prod_threshold:
            centroid = get_centroid(feature["geometry"])
            if centroid:
                folium.Marker(
                    location=centroid,
                    popup=(f"{feature['properties']['NAME_1']}<br>"
                           f"Rainfall: {stats['Avg Rainfall']:.1f} mm<br>"
                           f"Production: {stats['Total Production']:.0f} tonnes"),
                    icon=folium.Icon(color="red" if stats["Avg Rainfall"] > 2500 else "blue")
                ).add_to(m)

# Save map
m.save("cleaned_folium_map.html")
print("✅ Map saved as 'cleaned_folium_map.html'")
