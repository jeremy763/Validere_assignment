import datetime
import sys
import numpy as np
import requests
import pandas as pd
import re
import io
import getopt

URL = "https://www.crudemonitor.ca/savePHPExcel.php"

#acronym = "msw"
name = "Mixed Sweet Blend"
database = "crudes"

form_data = {
    "date1noscript": "",
    "date2noscript": "",
    "trendProperty": "AbsoluteDensity",
    "acr": "",
    "name": name,
    "db": database,
    "basicanalysis[]": "AbsoluteDensity",
    "options": "on",
    "date1": "",
    "date2": "",
    "format": "Export .CSV",
    "daterangepicker_start": "",
    "daterangepicker_end": "",
}

data = requests.post(url=URL, data=form_data)

def convert_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        date_list = list(date.split("-"))
        date_list = date_list[::-1]
        date_string = ''.join(date_list)
        return date_string

    except ValueError:
        print("This is the incorrect date string format. This is the incorrect date string format. It should be YYYY-MM-DD")

def get_user_input():
    crude_acronym = None
    start_date = None
    end_date = None
    operation = None
    limit = None

    # start with the arguments at index 1 since the index 0 is the file name
    argv = sys.argv[1:]

    # Using try and except to make it more robust
    try:
        opts, args = getopt.getopt(argv,"crude_acronym:start_date:end_date:operation:limit:", ["crude_acronym=", "start_date=", "end_date=", "operation=", "limit="])

    except getopt.GetoptError as err:
        print(err)

    # check what the input is and store them in the correstponding variables
    for opt, arg in opts:
        if opt in ["--crude_acronym"]:
            crude_acronym = arg
        elif opt in ["--start_date"]:
            start_date = convert_date(arg)
        elif opt in ["--end_date"]:
            end_date = convert_date(arg)
        elif opt in ["--operation"]:
            operation = arg
        elif opt in ["--limit"]:
            limit = arg

    form_data["acr"] = crude_acronym
    form_data["date1"] = start_date
    form_data["date2"] = end_date

    print("crude_acronym:", crude_acronym)
    print("start_date:",start_date)
    print("end_date:",end_date)
    print("operation:", operation)
    print("limit:", limit)

    # fetch data from the website
    data = requests.post(url=URL, data=form_data)
    # convert it to string
    data = io.StringIO(data.text)
    # change it to dataframe using panda
    df = pd.read_csv(data, sep=",")
    # get the needed data
    filtered_data = df.loc[df['Density (kg/m^3)'] > int(limit)]
    filtered_data = filtered_data.rename(columns={'Density (kg/m^3)': 'Density'})
    new = filtered_data[["Date","Density"]]
    print(new)


get_user_input()
