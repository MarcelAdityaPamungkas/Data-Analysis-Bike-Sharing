import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(style='dark')

days_df = pd.read_csv("Dashboard/days_clean.csv")
hours_df = pd.read_csv("Dashboard/hours_clean.csv")

# Defining a function called create_casual_total_df to prepare
def create_casual_total_df(df):
    casual_total_df = df.groupby(by = "date").agg({"casual": "sum"}).reset_index()
    return casual_total_df

# Defining a function called create_registered_total_df to prepare
def create_registered_total_df(df):
    registered_total_df = df.groupby(by = "date").agg({"registered": "sum"}).reset_index()
    return registered_total_df

# Defining a function called create_total_df to prepare
def create_total_df(df):
    total_df = df.groupby(by = "date").agg({"count": "sum"}).reset_index()
    return total_df

# Defining a function called create_weekday_total_df to prepare
def create_weekday_total_df(df):
    weekday_total_df = df.groupby(by = "weekday").agg({"count": "sum"}).reset_index()
    return weekday_total_df

# Defining a function called create_workingday_total_df to prepare
def create_workingday_total_df(df):
    workingday_total_df = df.groupby(by = "workingday").agg({"count": "sum"}).reset_index()
    return workingday_total_df

# Defining a function called create_holiday_total_df to prepare
def create_holiday_total_df(df):
    holiday_total_df = df.groupby(by = "holiday").agg({"count": "sum"}).reset_index()
    return holiday_total_df

# Defining a function called create_monthly_total_df to prepare
def create_monthly_total_df(df):
    monthly_total_df = df.groupby(by = "month").agg({"count": "sum"})
    months_ordered= [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    monthly_total_df = monthly_total_df.reindex(months_ordered, fill_value = 0)
    return monthly_total_df

# Defining a function called create_weather_total_df to prepare
def create_weather_total_df(df):
    weather_total_df = df.groupby(by = "weather_category").agg({"count": "sum"})
    return weather_total_df

# Defining a function called create_season_total_df to prepare
def create_season_total_df(df):
    season_total_df = df.groupby(by = "season")[["registered", "casual"]].sum().reset_index()
    return season_total_df

# Determining the start and the end of the days in days_df and hours_df
min_date_days = pd.to_datetime(days_df["date"].min())
max_date_days = pd.to_datetime(days_df["date"].max())
min_date_hour = pd.to_datetime(hours_df["date"].min())
max_date_hour = pd.to_datetime(hours_df["date"].max())

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("Dashboard/Logo_Image.png")
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label = 'Rentang Waktu',
        min_value = min_date_days,
        max_value = max_date_days,
        value=[min_date_days, max_date_days])

main_df_hour = hours_df[(hours_df["date"] >= str(start_date)) & 
                        (hours_df["date"] <= str(end_date))]

# Calling all functions to count the total
casual_total_df = create_casual_total_df(days_df)
registered_total_df = create_registered_total_df(days_df)
total_df = create_total_df(days_df)
weekday_total_df = create_weekday_total_df(days_df)
workingday_total_df = create_workingday_total_df(days_df)
holiday_total_df = create_holiday_total_df(days_df)
monthly_total_df = create_monthly_total_df(days_df)
weather_total_df = create_weather_total_df(days_df)
season_total_df = create_season_total_df(days_df)

st.header('Bike Rental Dashboard :sparkles:')
st.subheader("Total Rentals")

col1, col2, col3 = st.columns(3)
with col1:
    total_casual_df = casual_total_df["casual"].sum()
    st.metric("Casual User", value = total_casual_df)

with col2:
    total_registered_df = registered_total_df["registered"].sum()
    st.metric("Registered User", value = total_registered_df)

with col3:
    total_df = total_df["count"].sum()
    st.metric("Total User", value = total_df)

# Plotting performance on the total of bike rentals in 2011 and 2012 for each month
st.subheader("Performance on the total of bike rentals in 2011 and 2012")

# Preparing the data for chart
days_df["month"] = pd.Categorical(days_df["month"], categories =
    ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    ordered = True)

monthly_counts = days_df.groupby(by = ["year", "month"]).agg({"count": "sum"}).reset_index()

# Setting the style of the chart
fig_total_bike, ax = plt.subplots(figsize=(16, 8))
sns.lineplot(data = monthly_counts, x = "month", y = "count", hue = "year", palette = "Paired", marker = "o")

# Adding a title
plt.title(f"Total of Bike Rental Trends from ({start_date} to {end_date})", fontsize=24)

# Adding labels for x and y
plt.xlabel("Month")
plt.ylabel("Total of Bike Rentals")
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

# Adding a legend
plt.legend(title = "Year", loc = "upper right", fontsize = 16)

# Showing the line chart
st.pyplot(fig_total_bike)


# Plotting the effect of weather to the total of bike rentals in both 2011 and 2012
st.subheader("The Effect of Weather to the Total of Bike Rentals")

# Setting the style of the chart
fig_total_weather, ax = plt.subplots(figsize = (16, 8))
sns.barplot(x = "year", y = "count", hue = "weather_category", palette = "Paired", data = days_df, errorbar = None)

# Adding a title
plt.title("Bike Rentals Based on Weather", fontsize = 24)

# Adding labels for x and y
plt.xlabel("Weather Conditions")
plt.ylabel("Total of Bike Rentals")
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

# Adding a legend
plt.legend(fontsize = 16)

# Showing the bar chart
st.pyplot(fig_total_weather)


# Plotting correlation among temperature, humidity, and windspeed with the total of bike rentals

st.subheader("Correlation Between Variables")
fig_correlation, ax = plt.subplots(figsize = (16, 8))

correlation = days_df.corr(numeric_only = True)
mask = np.triu(np.ones_like(correlation, dtype=bool))

sns.heatmap(correlation, annot = True, mask = mask, cmap = "mako", center = 0, annot_kws = {"size": 16}, fmt = ".3f")
plt.title("Correlation Heatmap", fontsize = 24)

# Showing the heatmap
st.pyplot(fig_correlation)


# Plotting season with the highest and lowest total of bike rentals in 2011 and 2012

st.subheader("Season With the Highest and Lowest Total of Bike Rentals")

# Setting the style of the chart
fig_total_season, ax = plt.subplots(figsize = (16, 8))
sns.barplot(x = "season", y = "count", hue = "year", palette = "Paired", data = days_df, errorbar = None)

# Adding a title
plt.title("Bike Rentals Based on Season", fontsize = 24)

# Adding labels for x and y
plt.xlabel("Season")
plt.ylabel("Total of Bike Rentals")
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

# Adding a legend
plt.legend(fontsize = 16)

# Showing the bar chart
st.pyplot(fig_total_season)


# Plotting comparison between casual and registered user in the total of bike rentals

st.subheader("Casual vs Registered User")

data = [sum(days_df["casual"]), sum(days_df["registered"])]

# Setting the style of pie plot
fig_comparison, ax = plt.subplots()
labels = 'Casual', 'Registered'
plt.pie(data, labels = labels, autopct = '%1.2f%%', colors = sns.color_palette("Set2"))

# Adding a title
plt.title("Comparison of Registered vs Casual User")

# Showing the pie chart
st.pyplot(fig_comparison)


# Plotting total of bike rentals based on weekday

st.subheader("Total of Bike Rentals by Weekday")

days_df["weekday"] = pd.Categorical(days_df["weekday"], categories =
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    ordered = True)
weekday_counts = days_df.groupby(by = "weekday").agg({"count": "sum",}).reset_index()

# Setting the style of bar plot
sns.set(style = "whitegrid")
fig_weekday, ax = plt.subplots(figsize = (16, 8))
fig = sns.barplot(data = weekday_counts, x = "weekday", y = "count", color = "blue")

# Setting the label to be above the bar
fig.bar_label(fig.containers[0], fontsize = 10)

# Adding a title
plt.title("Total of Bike Rentals by Weekday", fontsize = 24)

# Adding labels for x and y
plt.xlabel("Day")
plt.ylabel("Total of Bike Rentals")
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

# Showing the bar chart
st.pyplot(fig_weekday)


# Plotting total of bike rentals based on workingday
st.subheader("Total of Bike Rentals by Workingday")

# Preparing the data for chart
days_df["workingday"] = pd.Categorical(days_df["workingday"], categories =
    ["Holiday/Weekend", "Workday"],
    ordered = True)

workingday_counts = days_df.groupby(by = ["year", "workingday"]).agg({"count": "sum"}).reset_index()

# Setting the style of the chart
fig_workingday, ax = plt.subplots(figsize = (16, 8))
sns.barplot(data = workingday_counts, x = "year", y = "count", hue = "workingday", errorbar = None)
plt.ticklabel_format(style = "plain", axis = "y")

# Adding a title
plt.title("Total of Bike Rentals Based on Working Days in 2011 and 2012")

# Adding labels for x and y
plt.xlabel("Year")
plt.ylabel("Total of Bike Rentals")
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

# Showing the bar plot
st.pyplot(fig_workingday)
