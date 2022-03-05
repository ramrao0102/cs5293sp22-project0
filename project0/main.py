import argparse
import tempfile
import PyPDF2
import numpy as np
import pandas as pd
import sqlite3
import project0
import urllib.request

def download_file():

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
    
        parser.add_argument("--incidents", type=str, required=True, help ="Incident summary url.")

        args = parser.parse_args()

    
    import urllib.request

    pdf_path = args.incidents

    def download_file(download_url, filename):
        response = urllib.request.urlopen(download_url)
        file = open(filename + ".pdf", 'wb')
        file.write(response.read())
        file.close()

    download_file(pdf_path, "Test")

download_file()

newlist = project0.fetch_incidents()

project0.createdatabase()
project0.populatedatabase(newlist)

rows = project0.incidentstatus()

for row in rows:
    print(row[0], row[1], sep = "|")

