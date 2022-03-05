This is Ramkishore Rao's Project0 for CS5293

The following was performed in sequence:

1) File structure as created in the following path:  /home/ramrao0102/project0.  The file structure is what is seen on github

2) Pipfile, Pipfile.lock, setup.py and setup.cfg files were created in the project 0 directory and contained the information that can be seen in these files on github

3) The pdf file of the incident reports from the website link noted below were accessed. These reports are published daily on the city of Norman website.  They contain five fields:  Date/Time, Incident No, Location, Nature, Incident_ORI.
https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-05_daily_incident_summary.pdf

4) Two primary python files are created.  One is main.py and a second file is project0.py.  Main.py contains a function that is used to to download the file. A function was written that includes an argument parser.  The user enters the following information from the command line to push the argument into the function from which the argument is parsed to obtain the url link

pipenv run python project0/main.py --incidents <url>

5) Urlilib directory is used to download the file from the website using the urlink and within the function, code is written to write the pdf file Incidents_File.pdf to the /home/ramrao0102/project0.

6) The main.py file also has function calls to several functions written within the project0.py file.  They include calls to functions to fetch incidents from the pdf file, create a sqlite3 database, insert rows into the sqlite3 database from the pdf file and extract data via a sql statement to obtain counts of the nature of incidents to report each incident_nature and count.

7) The project0.py contains the following functions:

7A)	fetch_incidents function:  This function uses the pyPDF2 python package to extract text from the downloaded pdf file.  The code reads the number of pages in the pdf fie.

7B)	An empty list pypdf_text is created to store the data.

7C)	The pdf file is extracted to an output variable with the pyPDF2 package.

7D)	the output file is then formatted to remove the excluded words which are the headers on the first page of the pdf file.

7E)	The a flat list is created to append each string (i.e., in each field) into a python list.

7F) The flat list is formatted to check if there is wrap around text in the Location field and if there is a wrap around, the two strings that together describe the location are combined and once they are combine, then the list is updated to remove the second strip in the “wrap around” string and the index of the list is accordingly modified. 

8) Following the placement of the information in a flat python list, a series of if-then commands have been developed to check if there is any missing data in the fields.  

* In the data time field, if  we donot see 2022, then a NULL is added.
* In the Incident No. field, if we donot see 2022, then a NULL is added.
* In the Location field, we check to see if the string is not upper case and does not contain the strings that are in the incident_ORI field, namely OK0140200, EMSSTAT, 14005, and 14009, then a NULL is added.
* In the Nature, which is the only lower case, we check if it is upper case, or if it contains 2022 exists or if it contains the strings that are in the incident_ORI field, namely OK0140200, EMSSTAT, 14005, and 14009, which means Nature is Null and it adds NULL in this field.
* In the Incident_ORI, we check if the strings OK0140200, EMSSTAT, 14005, and 14009 do not exist.  If they do not then we add NULL in the field.

9) Once this is created, then we create a list of lists from this flat_list.  Each inner list has length 5, which is the number of fields in the database.
   The database name is project0database.

10) A function is then written to create a database in /home/ramrao0102/project0 and it is called trial database.  A table is added to this database with the following fields: Date/Time, Incident No, Location, Nature, Incident_ORI.

11) The table is committed to the database.

12) Once the table is created in the database, we have a function that connects back to the database and inserts one row at a time from the list of lists into the database.  The changes are then committed to the database.

13) Finally, an function is written to obtain incident status from the database by connecting data and fetching rows that contain each incident type and the number of counts by incident type.

14) Execution of all of the above elements is completed by entering the below command in /home/ramrao0102/project0

pipenv run python project0/main.py --incidents <url>

15) Once the database is created and the table is populated, we have a pytest being performed that checks the following:

15A) a function to check if the file has been downloaded.  It looks at the path in /home/ramrao0102/project0 to check if file has been downloaded following execution of command in 14.  This checks if the download function was successfully executed.

15B) a function to check if the database exists in the /home/ramrao0102/project0.  This checks if the createdatabase() function was successfully executed.

15C) a function to check if the incident_status function was successfully executed.  The test function calls the incident_status function from the project0.py file.

15D) a function to check if there is data in the database.  This is used to check if the populatedatabase() function was successfully executed.
