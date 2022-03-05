import project0
import sqlite3


def test_istheredata():
    conn = sqlite3.connect('trial')
    c = conn.cursor()
    find = "SELECT * from incidents3";
    c.execute(find)
    rows = c.fetchall()
    assert len(rows)>=1
    return 0

