from project0.project0 import incidentstatus
import pytest

def test_incident():
    rows = incidentstatus()
    assert len(rows) >=1
    return 0
