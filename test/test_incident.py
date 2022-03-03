import project0

def test_incident():
    rows = project0.incidentstatus()
    return len(rows) >=1
