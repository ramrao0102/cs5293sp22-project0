from project0.project0 import incidentstatus

def test_incident():
    rows = incidentstatus()
    assert len(rows) >=1
    return 0
