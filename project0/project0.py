
import tempfile
import PyPDF2
import re
import sqlite3

def fetch_incidents():

    fp =tempfile.TemporaryFile()

    datafile = open('Incidents_File.pdf', 'rb')

    fp.write(datafile.read())

    fp.seek(0)

    pdfReader = PyPDF2.PdfFileReader(fp)

    pagecount = pdfReader.getNumPages()

    #page1 = pdfReader.getPage(0)

    #page1 = pdfReader.getPage(0).extractText()

    pypdf_text = []
    excluded_word = "NORMAN POLICE DEPARTMENT"
    excluded_word1 = "Daily Incident Summary (Public)"

    for page in range(pagecount):
        output = pdfReader.getPage(page).extractText()
    
        formatted_output = output.replace(excluded_word, "")
        formatted_output1 = formatted_output.replace(excluded_word1, "") 
        formatted_output1 = formatted_output1.splitlines()
        pypdf_text.append(formatted_output1)
                

    del pypdf_text[pagecount-1][-1]
    del pypdf_text[0][-1]
    del pypdf_text[0][-1]

    flat_ls = []
    for i in pypdf_text:
        for j in i:
            flat_ls.append(j)
    
    k =0
    while k < len(flat_ls):
        if flat_ls[k].isupper() == True and 'OK0140200' not in flat_ls[k] and 'EMSSTAT' not in flat_ls[k] and '14005' not in flat_ls[k] and '14009' not in flat_ls[k]:
            if flat_ls[k-1].isupper() == True and 'OK0140200' not in flat_ls[k-1] and 'EMSSTAT' not in flat_ls[k-1] and '14005'not in flat_ls[k-1] and '14009' not in flat_ls[k-1]:
                flat_ls[k-1] += flat_ls.pop(k)
        k = k+1

    del flat_ls[0:5]

    k=0

    for k in range(len(flat_ls)):
        if k% 5 ==0:
            if re.search ('/2022' ,flat_ls[k]) == None:
                flat_ls.insert(k, 'NULL')
                continue
        elif k%5 ==1:
            if re.search('2022-',flat_ls[k]) == None :
                flat_ls.insert(k, 'NULL')
                continue
        elif k%5 ==2:
            if (any(ch.isdigit() for ch in flat_ls[k])) != True:
                if flat_ls[k].isupper() !=True or 'OK0140200' in flat_ls[k]  or 'EMSSTAT' in flat_ls[k]  or '14005' in flat_ls[k] or '14009' in flat_ls[k] :
                    flat_ls.insert(k, 'NULL')
                    continue
        elif k%5 == 3:
            if flat_ls[k].isupper() == True or '2022' in flat_ls[k]  or 'OK0140200' in flat_ls[k] or 'EMSSTAT' in flat_ls[k] or '14005' in flat_ls[k] or '14009' in flat_ls[k]:
                flat_ls.insert(k, 'NULL')
                continue
        elif k%5 == 4:
            if (re.search(r'^\S+$', flat_ls[k]) == None) or  (re.search('[a-z]', flat_ls[k])) or '2022' in flat_ls[k] or ('OK0140200' not in flat_ls[k]  and 'EMSSTAT' not in flat_ls[k] and '14005'not in flat_ls[k] and '14009' not in flat_ls[k]):
                #print(flat_ls[k])
                flat_ls.insert(k, 'NULL')
                continue

    inner_size = 5
    newlist = [ flat_ls[i:i+inner_size] for i in range(0, len(flat_ls), inner_size) ]
    return newlist


def createdatabase():

    conn = sqlite3.connect('project0database')
    c = conn.cursor()
    c.execute('CREATE TABLE incidents3 (incident_time TEXT, incident_number TEXT, incident_location TEXT, nature TEXT, incident_ori TEXT);')
    conn.commit()

def populatedatabase(newlist):

    conn = sqlite3.connect('project0database')
    c = conn.cursor()
    stmt = "INSERT INTO incidents3(incident_time, incident_number, incident_location, nature, incident_ori) VALUES (?,?,?,?,?)"
    c.executemany(stmt, newlist)
    conn.commit()

def incidentstatus():

    conn = sqlite3.connect('project0database')
    c = conn.cursor()

    find = "SELECT  nature, count(*) from incidents3 GROUP BY(nature)";

    c.execute(find)

    rows = c.fetchall()

    return rows




