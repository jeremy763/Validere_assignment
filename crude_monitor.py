import sys

import requests
import getopt

URL = "https://www.crudemonitor.ca/savePHPExcel.php"

acronym = "MSW"
name = "Mixed Sweet Blend"
database = "crudes"

form_data = {
    "date1noscript": "",
    "date2noscript": "",
    "trendProperty": "AbsoluteDensity",
    "acr": acronym,
    "name": name,
    "db": database,
    "basicanalysis[]": "AbsoluteDensity",
    "options": "on",
    "date1": "13072011",
    "date2": "13072021",
    "format": "Export .CSV",
    "daterangepicker_start": "",
    "daterangepicker_end": "",
}

data = requests.post(url=URL, data=form_data)


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
            start_date = arg
        elif opt in ["--end_date"]:
            end_date = arg
        elif opt in ["--operation"]:
            operation = arg
        elif opt in ["--limit"]:
            limit = arg

    print("crude_acronym:",crude_acronym)
    print('start_date: {}'.format(start_date))
    print('end_date: {}'.format(end_date))
    print("operation:",operation)
    print("limit:",limit)


get_user_input()
