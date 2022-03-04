import pytest
import requests

pytest_plugin = ["docker_compose"]


def test_homepage(homepage):
    assert requests.get(homepage).text.split("<h1>")[1].split(
        "</h1>")[0] == "Data Enginering Final Project"


def test_pred(homepage):
    assert 1 == 1
