import pytest
import requests
import grequests
import time
import sys

pytest_plugin = ["docker_compose"]


def test_homepage(homepage):
    assert requests.get(homepage).text.split("<h1>")[1].split(
        "</h1>")[0] == "Data Enginering Final Project"


def test_pred(homepage):
    assert 1 == 1

@pytest.mark.anyio
async def test_stress(homepage):

    data = {
      'inputdata': 'Testing'
    }
    
    t_start = time.time()
    
    for i in range(10):
        r = (grequests.post('http://localhost:5000/predict', data=data) for u in range(10))
        assert len(grequests.map(r)) == 10    
    t_end = time.time()

    t = t_end-t_start

    print("Info time :",t, file=sys.stderr)
    assert t < 60
