# PubliBike Data Extraction and Analysis

This project aims to extract data from the PubliBike API, process and analyze it, and save the results in a structured CSV format for further analysis. The project uses Python and popular libraries like Pandas and Requests for data manipulation and extraction.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Data Extraction](#data-extraction)
- [Data Processing](#data-processing)
- [Data Analysis](#data-analysis)
- [Data Saving](#data-saving)

## Introduction

Public transportation and bike-sharing systems generate valuable data that can be used for various purposes, including optimization of services and research. This project focuses on extracting data from the PubliBike API, processing the data, and saving it in a CSV format for further analysis.

## Requirements

To run this project, you need the following requirements:

- Python 3.x
- Pandas
- Requests

You can install the required libraries using `pip`:

```bash
pip install -r requirements.txt
```
# Installation
Clone the GitHub repository:

```bash
git clone https://github.com/MathiasSteilen/publibike-data.git
```
Change to the project directory:

```bash
cd publibike-data-analysis
```
# Usage
To use this project, follow these steps:

Run the Python script main.py:

```bash
python main.py
```
The script will fetch data from the PubliBike API, process it, and save it as a CSV file in the Data directory.

# Data Extraction
The data extraction process involves fetching data from the PubliBike API using the requests library. The data includes information about bike stations, bikes, and sponsors associated with each station. The extracted data is in JSON format.

# Data Processing
The extracted data is processed using the Pandas library to create structured dataframes. The dataframes are cleaned and organized to facilitate further analysis.

# Data Analysis
This project focuses on data extraction and processing, but you can extend it to perform various data analysis tasks on the processed data. You can use tools like Jupyter Notebook or other data analysis libraries for in-depth analysis.

# Data Saving
The final processed data is saved as a CSV file in the Data directory. The filename includes a timestamp to ensure uniqueness. You can use this CSV file for further analysis or reporting.
