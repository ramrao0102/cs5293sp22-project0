import project0
import sqlite3


def test_isteredata():
    conn = sqlite3.connect('/home/ramrao0102/trial')
    c = conn.cursor()
    find = "SELECT * from incidents3";
    c.execute(find)
    rows = c.fetchall()
    return len(rows) >=1
