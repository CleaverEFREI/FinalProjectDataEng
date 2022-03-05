import pytest
import requests
import grequests
import trio


pytest_plugin = ["docker_compose"]


def test_homepage(homepage):
    assert requests.get(homepage).text.split("<h1>")[1].split(
        "</h1>")[0] == "Data Enginering Final Project"

@pytest.mark.anyio
async def test_stress():    
    t_start =  trio.current_time()
    t = trio.current_time()-t_start
    count = 0
    while t < 59 or count < 5000:        
        r = (grequests.get('http://localhost:5000/') for u in range(20))
        assert len(grequests.map(r)) == 20
        count += 1
        t = trio.current_time()-t_start

    assert t < 61    
    assert count >= 5000
