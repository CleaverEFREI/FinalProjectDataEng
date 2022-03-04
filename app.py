from flask import Flask, render_template
import sys
import requests

app = Flask(__name__)

try:    
    from detoxify import Detoxify
    error_install = False
except:
    error_install = True
    def call_API(inp):

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36',
            'sec-ch-ua-platform': '"Android"',
            'Accept': '*/*',
            'Origin': 'https://huggingface.co',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://huggingface.co/',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        json_data = {
            'inputs': inp,
        }

        response = requests.post('https://api-inference.huggingface.co/models/unitary/toxic-bert', headers=headers, json=json_data)
        return response.json()[0]
    # Start API:
    call_API('')


@app.route('/')
def index():
    """
    Render the index base template
    """
    return render_template('index.html')


@app.route('/health_check')
def health_check():
    """
    Used to verify that the app is up and running
    """
    return "ok"


@app.route('/predict', methods = ["POST"])
def predict():
    """
    Get data from index form, use the pretrainned model pickle and return the setiment in prediction_text
    """
    r = request.form.get('inputdata', "This is a default value")
    if r[0] == '!':
        r = r[1:]
        debug = 1
    else:
        debug = 0
    print("Info request :",r, file=sys.stderr)
    if error_install:
        prediction = call_API(r)
    else:
        prediction = Detoxify('original').predict(r)
    
    pred_v = 0.5
    pred = 'Not toxic :)'
    for i in range(len(prediction)):
        if prediction[i]['score'] > pred_v:
            pred = prediction[i]['label'] 

    if debug :
        return render_template("index.html",prediction_text = 'The sentence "{}" is {}. {} '.format(r,pred,prediction))
    else :
        return render_template("index.html",prediction_text = 'The sentence "{}" is {}.'.format(r,pred))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')