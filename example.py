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

