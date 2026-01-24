import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px # type: ignore

# Importing datasetsimport pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Importing datasets
cp_df = pd.read_csv("crop_yield.csv")
rf_df = pd.read_csv("rainfall_in_india.csv")

# Managing and filling the null values 
crop_df = cp_df.fillna(0)
rainfall_df = rf_df.fillna(0)

# Removing fertilizer and pesticide column as they are not needed for the following visualization 
crop_df = crop_df.drop(columns=["Fertilizer", "Pesticide"], errors="ignore")

# Filtering the data from year 2000-2015
crop_df = crop_df[(crop_df["Crop_Year"] >= 2000) & (crop_df["Crop_Year"] <= 2015)]
rainfall_df = rainfall_df[(rainfall_df["YEAR"] >= 2000) & (rainfall_df["YEAR"] <= 2015)]

# Displaying datasets
print(crop_df.head())
print(rainfall_df.head())

# Function to create line plot
def create_line_plot(df, x, y, hue, title):
    plt.figure(figsize=(14, 8))
    for unique_value in df[hue].unique():
        data = df[df[hue] == unique_value]
        plt.plot(data[x], data[y], label=unique_value)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Create line plots
create_line_plot(crop_df, 'Crop_Year', 'Production', 'State', "Crop Production Over Time by State")
create_line_plot(rainfall_df, 'YEAR', 'ANNUAL', 'SUBDIVISION', "Annual Rainfall Over Time by Subdivision")

# Function to create pie chart
def create_pie_chart(df, x, y, title):
    df.groupby(x)[y].sum().nlargest(6).plot(kind="pie", autopct="%1.1f%%", title=title)
    plt.ylabel("")
    plt.show()

# Create pie charts
create_pie_chart(crop_df, "State", "Production", "Top 6 Crop Producing States")
create_pie_chart(rainfall_df, "SUBDIVISION", "ANNUAL", "Top 6 Rainfall Receiving Regions")

# Function to create area plot
def create_area_plot(df, x, y, hue, title):
    pivot_df = df.pivot_table(index=x, columns=hue, values=y, aggfunc="sum")
    fig = px.area(pivot_df, title=title)
    fig.show()

# Create area plots
create_area_plot(crop_df, "Crop_Year", "Production", "State", "Area Plot: Crop Production by State")
create_area_plot(rainfall_df, "YEAR", "ANNUAL", "SUBDIVISION", "Area Plot: Rainfall by Subdivision")

# Function to create bar plot
def create_bar_plot(df, x, y, hue, title):
    plt.figure(figsize=(14, 8))
    for unique_value in df[hue].unique():
        data = df[df[hue] == unique_value]
        plt.bar(data[x], data[y], label=unique_value)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Create bar plots
create_bar_plot(crop_df, 'Crop_Year', 'Production', 'State', "Bar Plot: Crop Production by Year and State")
create_bar_plot(rainfall_df, 'YEAR', 'ANNUAL', 'SUBDIVISION', "Bar Plot: Annual Rainfall by Year and Subdivision")

# Function to create histogram
def create_histogram(df, x, hue, title):
    plt.figure(figsize=(12, 6))
    for unique_value in df[hue].unique():
        data = df[df[hue] == unique_value]
        sns.histplot(data[x], label=unique_value, kde=False, bins=10)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Create histograms
create_histogram(crop_df, 'Production', 'State', "Histogram: Crop Production Distribution by State")
create_histogram(rainfall_df, 'ANNUAL', 'SUBDIVISION', "Histogram: Rainfall Distribution by Subdivision")

# Function to create scatter plot
def create_scatter_plot(df, x, y, hue, title):
    plt.figure(figsize=(14, 8))
    for unique_value in df[hue].unique():
        data = df[df[hue] == unique_value]
        plt.scatter(data[x], data[y], label=unique_value)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Create scatter plots
create_scatter_plot(crop_df, 'Crop_Year', 'Production', 'State', "Scatter Plot: Crop Production Over Years by State")
create_scatter_plot(rainfall_df, 'YEAR', 'ANNUAL', 'SUBDIVISION', "Scatter Plot: Rainfall Over Years by Subdivision")

# Function to create heatmap
def create_heatmap(df, x, y, hue, title):
    pivot_df = df.pivot_table(index=x, columns=y, values=hue)
    plt.figure(figsize=(14, 10))
    sns.heatmap(pivot_df, cmap="YlGnBu", linewidths=0.5)
    plt.title(title)
    plt.xlabel(y)
    plt.ylabel(x)
    plt.tight_layout()
    plt.show()

# Create heatmaps
create_heatmap(rainfall_df, 'SUBDIVISION', 'YEAR', 'ANNUAL', "Rainfall Heatmap (Subdivision vs Year)")
create_heatmap(crop_df, 'State', 'Crop_Year', 'Production', "Crop Production Heatmap (State vs Year)")

# Function to create box plot
def create_box_plot(df, x, y, title):
    plt.figure(figsize=(14, 6))
    sns.boxplot(data=df, x=x, y=y)
    plt.xticks(rotation=90)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.show()

# Create box plots
create_box_plot(rainfall_df, 'SUBDIVISION', 'ANNUAL', "Box Plot: Rainfall Distribution by Subdivision (2000–2015)")
create_box_plot(crop_df, 'State', 'Production', "Box Plot: Crop Production Distribution by State (2000–2015)")
cp_df = pd.read_csv("crop_yield.csv")
rf_df = pd.read_csv("rainfall_in_india.csv")

#mananging and filling the null values 
crop_df= cp_df.fillna(0)
rainfall_df= rf_df.fillna(0)
# Removing fertilizer and pesticide column as they are not needed for the following visualization 
crop_df = crop_df.drop(columns=["Fertilizer", "Pesticide"], errors="ignore")

# Filtering the data from year 2000-2015
crop_df = crop_df[(crop_df["Crop_Year"] >= 2000) & (crop_df["Crop_Year"] <= 2015)]
rainfall_df = rainfall_df[(rainfall_df["YEAR"] >= 2000) & (rainfall_df["YEAR"] <= 2015)]

#displaying datasets
print(crop_df.head())
print(rainfall_df.head())

# LINE PLOT
#for crop yield dataset
plt.figure(figsize=(14, 8))
for state in crop_df['State'].unique():
    state_data = crop_df[crop_df['State'] == state]
    plt.plot(state_data['Crop_Year'], state_data['Production'], label=state)
plt.title("Crop Production Over Time by State")
plt.xlabel("Year")
plt.ylabel("Production")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# for rainfall dataset
plt.figure(figsize=(14, 8))
for sub in rainfall_df['SUBDIVISION'].unique():
    sub_data = rainfall_df[rainfall_df['SUBDIVISION'] == sub]
    plt.plot(sub_data['YEAR'], sub_data['ANNUAL'], label=sub)
plt.title("Annual Rainfall Over Time by Subdivision")
plt.xlabel("Year")
plt.ylabel("Rainfall (mm)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#PIE CHART
# Crop production by state 
crop_df.groupby("State")["Production"].sum().nlargest(6).plot(kind="pie", autopct="%1.1f%%", title="Top 6 Crop Producing States")
plt.ylabel("")
plt.show()

# Rainfall distribution across states
rainfall_df.groupby("SUBDIVISION")["ANNUAL"].mean().nlargest(6).plot(kind="pie", autopct="%1.1f%%", title="Top 6 Rainfall Receiving Regions")
plt.ylabel("")
plt.show()

# AREA PLOT using Plotly 
#for crop yield dataset
crop_area = crop_df.pivot_table(index="Crop_Year", columns="State", values="Production", aggfunc="sum")
fig_crop_area = px.area(crop_area, title="Area Plot: Crop Production by State")
fig_crop_area.show()

#for rainfall dataset
rainfall_area = rainfall_df.pivot_table(index="YEAR", columns="SUBDIVISION", values="ANNUAL", aggfunc="mean")
fig_rainfall_area = px.area(rainfall_area, title="Area Plot: Rainfall by Subdivision")
fig_rainfall_area.show()

# BAR PLOT 
#for crop yield dataset
plt.figure(figsize=(14, 8))
for state in crop_df['State'].unique():
    state_data = crop_df[crop_df['State'] == state]
    plt.bar(state_data['Crop_Year'], state_data['Production'], label=state)
plt.title("Bar Plot: Crop Production by Year and State")
plt.xlabel("Year")
plt.ylabel("Production")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#for rainfall dataset
plt.figure(figsize=(14, 8))
for sub in rainfall_df['SUBDIVISION'].unique():
    sub_data = rainfall_df[rainfall_df['SUBDIVISION'] == sub]
    plt.bar(sub_data['YEAR'], sub_data['ANNUAL'], label=sub)
plt.title("Bar Plot: Annual Rainfall by Year and Subdivision")
plt.xlabel("Year")
plt.ylabel("Rainfall (mm)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# HISTOGRAM 
# for crop yield dataset
plt.figure(figsize=(12, 6))
for state in crop_df['State'].unique():
    sns.histplot(crop_df[crop_df['State'] == state]['Production'], label=state, kde=False, bins=10)
plt.title("Histogram: Crop Production Distribution by State")
plt.xlabel("Production")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()

#for rainfall dataset
plt.figure(figsize=(12, 6))
for sub in rainfall_df['SUBDIVISION'].unique():
    sns.histplot(rainfall_df[rainfall_df['SUBDIVISION'] == sub]['ANNUAL'], label=sub, kde=False, bins=10)
plt.title("Histogram: Rainfall Distribution by Subdivision")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()

# SCATTER PLOT 
#for crop yield dataset
plt.figure(figsize=(14, 8))
for state in crop_df['State'].unique():
    state_data = crop_df[crop_df['State'] == state]
    plt.scatter(state_data['Crop_Year'], state_data['Production'], label=state)
plt.title("Scatter Plot: Crop Production Over Years by State")
plt.xlabel("Year")
plt.ylabel("Production")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#for rainfall dataset
plt.figure(figsize=(14, 8))
for sub in rainfall_df['SUBDIVISION'].unique():
    sub_data = rainfall_df[rainfall_df['SUBDIVISION'] == sub]
    plt.scatter(sub_data['YEAR'], sub_data['ANNUAL'], label=sub)
plt.title("Scatter Plot: Rainfall Over Years by Subdivision")
plt.xlabel("Year")
plt.ylabel("Rainfall (mm)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#HEATMAP
# Pivot rainfall data for heatmap: Subdivision vs Year
rainfall_pivot = rainfall_df.pivot_table(index="SUBDIVISION", columns="YEAR", values="ANNUAL")

plt.figure(figsize=(14, 10))
sns.heatmap(rainfall_pivot, cmap="YlGnBu", linewidths=0.5)
plt.title("Rainfall Heatmap (Subdivision vs Year)")
plt.xlabel("Year")
plt.ylabel("Subdivision")
plt.tight_layout()
plt.show()

# Pivot crop data for heatmap: State vs Year
crop_pivot = crop_df.pivot_table(index="State", columns="Crop_Year", values="Production", aggfunc="sum")

plt.figure(figsize=(14, 10))
sns.heatmap(crop_pivot, cmap="YlOrBr", linewidths=0.5)
plt.title("Crop Production Heatmap (State vs Year)")
plt.xlabel("Year")
plt.ylabel("State")
plt.tight_layout()
plt.show()

#BOX PLOT
#for rainfall dataset 
plt.figure(figsize=(14, 6))
sns.boxplot(data=rainfall_df, x="SUBDIVISION", y="ANNUAL")
plt.xticks(rotation=90)
plt.title("Box Plot: Rainfall Distribution by Subdivision (2000–2015)")
plt.xlabel("Subdivision")
plt.ylabel("Annual Rainfall (mm)")
plt.tight_layout()
plt.show()

#for crop yield dataset
plt.figure(figsize=(14, 6))
sns.boxplot(data=crop_df, x="State", y="Production")
plt.xticks(rotation=90)
plt.title("Box Plot: Crop Production Distribution by State (2000–2015)")
plt.xlabel("State")
plt.ylabel("Production (tonnes)")
plt.tight_layout()
plt.show()
