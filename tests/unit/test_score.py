from posixpath import split
import pytest
import requests
import time
import sys


pytest_plugin = ["docker_compose"]


def test_model():
    data = [{'inputdata': '!shit'},{'inputdata': '!son of a bitch'},{'inputdata': '!you are beautifull'},{'inputdata': "!I will kill you"}]
    
    response = requests.post('http://localhost:5000/predict', data=data[0])
    rep_html = response.text.split('h2')[1].split('{')[1]
    obscene = float(rep_html.split('obscene&#39;: ')[1].split(',')[0])
    toxicity = float(rep_html.split('toxicity&#39;: ')[1].split(',')[0] )
    threat = float(rep_html.split('threat&#39;: ')[1].split(',')[0]  )
    
    assert obscene > 0.9
    assert toxicity > 0.7
    assert threat < 0.1
    

    response = requests.post('http://localhost:5000/predict', data=data[1])
    rep_html = response.text.split('h2')[1].split('{')[1] 
    insult = float(rep_html.split('insult&#39;: ')[1].split(',')[0]  )
    threat = float(rep_html.split('threat&#39;: ')[1].split(',')[0]  ) 
    obscene = float(rep_html.split('obscene&#39;: ')[1].split(',')[0])

    assert insult > 0.9
    assert threat <0.1
    assert obscene > 0.9

    response = requests.post('http://localhost:5000/predict', data=data[2])
    rep_html = response.text.split('h2')[1].split('{')[1]
    insult = float(rep_html.split('insult&#39;: ')[1].split(',')[0]  )  
    threat = float(rep_html.split('threat&#39;: ')[1].split(',')[0]  ) 
    obscene = float(rep_html.split('obscene&#39;: ')[1].split(',')[0])
    id_atack = float(rep_html.split('identity_attack&#39;: ')[1].split(',')[0].split("}")[0])

    assert insult <0.01
    assert threat <0.01
    assert obscene < 0.01
    assert id_atack < 0.01

    response = requests.post('http://localhost:5000/predict', data=data[3])
    rep_html = response.text.split('h2')[1].split('{')[1]

    toxicity = float(rep_html.split('toxicity&#39;: ')[1].split(',')[0] )
    threat = float(rep_html.split('threat&#39;: ')[1].split(',')[0]  ) 
    obscene = float(rep_html.split('obscene&#39;: ')[1].split(',')[0])
    id_atack = float(rep_html.split('identity_attack&#39;: ')[1].split(',')[0].split("}")[0])

    
    assert threat > 0.8
    assert obscene < 0.2
    assert id_atack < 0.1
    assert toxicity > 0.9

