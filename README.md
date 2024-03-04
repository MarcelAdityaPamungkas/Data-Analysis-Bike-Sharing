# Data Analysis Project: Bike Sharing Dataset

## Table of Contents

-  [Data Analysis Project: Bike Sharing Dataset](#-data-analysis-project-bike-sharing-dataset-)
  - [Table of Contents](#-table-of-contents)
  - [Introduction](#-introduction)
  - [Installation](#-installation)
  - [Project Workflow](#-project-workflow)
  - [Dashboard Explanation](#-dashboard-explanation)
 
## Introduction

This project focuses on the analysis of a public dataset about the bike sharing. This dataset contains the hourly and daily count of rental bikes between the years 2011 and 2012 in the Capital bike share system with the corresponding weather and seasonal information. This project will help any business to improve their strategies and customer experience with the meaningful and easy-to-understand insights and visualizations from the data. 

## Installation

1. Clone this repository to your local computer lokal using this command:

   ```shell
   git clone https://github.com/MarcelAdityaPamungkas/Data-Analysis-Bike-Sharing.git
   ```

2. Make sure you have all libraries that needed in this project. If you don't have, you can install it in your local computer with this command: 

    ```shell
    pip install streamlit
    pip install -r requirements.txt
    ```
3. This is optional, but it is recommended to create a virtual environment to keep the dependencies required by this project separate from your system's Python environment. You can create a virtual environment using this command:

   ```bash
   python3 -m venv env
   ```

## Project Workflow

1. Data Wrangling <br>
   This step consist of gathering data, assessing data, and cleaning data. The process includes:
   * Gathering data from the source.
   * Assessing each dataset for any missing value, duplicates, or outliers.
   * Cleaning the dataset that consist outliers.
2. Exploratory Data Analysis (EDA) <br>
   This step consist of exploring and analysing the data to find meaningful insights. This process analyse:
   * Analyse the trend of bike rentals for each hour, day, and monthly.
   * Analyse the effect of season and weather to the total of bike rentals.
   * Analyse the effect of workingday to the total of bike rentals.
   * Compare between casual and registered users.
   * Check the correlation between variables and make a scatter plot of that correlation.
3. Explanatory & Data Visualization
   This step consist of making visualization based on each question and EDA and also explaining the meaning from visualization. This process visualize:
   * The trend of bike rentals for each hour, day, and monthly.
   * The effect of season and weather to the total of bike rentals.
   * Make a heatmap from the correlation.
   * Compare between casual and registered users.
   * Analyse the effect of workingday to the total of bike rentals.
4. Dashboard
   This step consist of making dashboard in streamlit for better look. You can find the link to the dashboard in [here](url.txt)


## Dashboard Explanation

Navigate to the project directory and run the Streamlit app using the following command:

   ```sh
   streamlit run Dashboard/Dashboard.py
   ```

This will start the Streamlit server and open a new page in your default web browser with the URL of the Streamlit app. Or you can run the dashboard directly from the web browser by clicking on the following link: [LINK]()

