import datetime
import os
import sys
import requests
import pandas as pd
import io
import getopt

URL = "https://www.crudemonitor.ca/savePHPExcel.php"

form_data = {
    "date1noscript": "",
    "date2noscript": "",
    "trendProperty": "AbsoluteDensity",
    "acr": "",
    "name": "",
    "db": "",
    "basicanalysis[]": "AbsoluteDensity",
    "options": "on",
    "date1": "",
    "date2": "",
    "format": "Export .CSV",
    "daterangepicker_start": "",
    "daterangepicker_end": "",
}


def convert_date(date):
    try:
        # check if the date entered is the correct format
        datetime.datetime.strptime(date, '%Y-%m-%d')
        date_list = list(date.split("-"))
        date_list = date_list[::-1]
        date_string = ''.join(date_list)
        return date_string

    except ValueError:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")


def get_user_input():
    crude_acronym = None
    start_date = None
    end_date = None
    operation = None
    limit = None
    database = None
    name = None

    # get data from crude_monitor_parameters.csv for verifying crude_acronym
    acr_name_df = pd.read_csv("crude_monitor_parameters.csv")
    acr_name = acr_name_df[["acr"]]

    # start with the arguments at index 1 since the index 0 is the file name
    argv = sys.argv[1:]

    # Using try and except to make it more robust
    try:
        # assumed that crude_acronym, start_date and end_date are required to enter
        opts, args = getopt.getopt(argv,"crude_acronym:start_date:end_date:", ["crude_acronym=", "start_date=", "end_date=", "operation=", "limit="])

    except getopt.GetoptError as err:
        print(err)

    # check what the input is and store them in the corresponding variables
    for opt, arg in opts:
        if opt in ["--crude_acronym"]:
            if arg.upper() in acr_name.values:
                crude_acronym = arg
                name = acr_name_df.loc[acr_name_df.acr == arg.upper(), "name"].values[0]
                database = acr_name_df.loc[acr_name_df.acr == arg.upper(), "database"].values[0]
            else:
                print("Invalid crude_acronym!")
                return
        elif opt in ["--start_date"]:
            start_date = convert_date(arg)
        elif opt in ["--end_date"]:
            end_date = convert_date(arg)
        elif opt in ["--operation"]:
            operation = arg
        elif opt in ["--limit"]:
            limit = arg

    # adding data to the form_data
    form_data["acr"] = crude_acronym
    form_data["date1"] = start_date
    form_data["date2"] = end_date
    form_data["name"] = name
    form_data["database"] = database

    # check if it is stored in local
    saved_csv = crude_acronym + start_date + end_date
    if os.path.isfile(saved_csv):
        df = pd.read_csv(saved_csv)
    else:
        # fetch data from the website
        data = requests.post(url=URL, data=form_data)
        # convert it to string
        data = io.StringIO(data.text)
        # change it to dataframe using panda
        df = pd.read_csv(data, sep=",")
        df.to_csv(crude_acronym + start_date + end_date)

    if operation != None and limit != None:
        # get the needed data
        # assumed there are only greater than and less than operations
        if (operation == "greater_than") or (operation == ">"):
            filtered_data = df.loc[df['Density (kg/m^3)'] > int(limit)]
        elif (operation == "less_than") or (operation == "<"):
            filtered_data = df.loc[df['Density (kg/m^3)'] < int(limit)]
        else:
            print("Invalid operations!")
            return
        new_df = filtered_data.reset_index()
    else:
        new_df = df.reset_index()

    # print out the data if it is not empty
    if len(new_df) != 0:
        print("+-----+------------+-----------+")
        print("|     | Date       |   Density |")
        print("|-----+------------+-----------|")
        index = 0
        for index, row in new_df.iterrows():
            if index > 9:
                print("| ", index, "|", row['Date'], "|    ", row['Density (kg/m^3)'], "|")
            elif index > 99:
                print("|", index, "|", row['Date'], "|    ", row['Density (kg/m^3)'], "|")
            else:
                print("|  ", index, "|", row['Date'], "|    ", row['Density (kg/m^3)'], "|")

        if index > 9:
            print("+------+------------+-----------+")
        elif index > 99:
            print("+-------+------------+-----------+")
        else:
            print("+-----+------------+-----------+")
    else:
        print("Empty")
        os.remove(saved_csv)


if __name__ == '__main__':
    get_user_input()


