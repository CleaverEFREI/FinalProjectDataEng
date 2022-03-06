import pytest
import requests
import time


pytest_plugin = ["docker_compose"]


def test_homepage(homepage):
    assert requests.get(homepage).text.split("<h1>")[1].split(
        "</h1>")[0] == "Data Enginering Final Project"

def test_stress(homepage):    
    t_start =  time.time()
    t = time.time()-t_start
    count = 0
    while count < 100:        
        r = requests.get(homepage)
        assert r.status_code == 200
        count += 1
        t = time.time()-t_start

    assert t < 60
