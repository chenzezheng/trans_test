import os
# import numpy as np
import threading

from flask import Flask, request, jsonify
from access import accessToken
# from werkzeug.utils import secure_filename

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    ret = jsonify({'statusCode': 200, 'msg': 'hello'})
    return ret

@app.route("/text", methods=["POST"])
def textTranslate():
    import requests
    import random
    import json
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + accessToken
    
    q = request.get_json()['text']
    # For list of language codes, please refer to `https://ai.baidu.com/ai-doc/MT/4kqryjku9#语种列表`
    from_lang = request.get_json()['from']
    to_lang = request.get_json()['to']
    term_ids = ''


    # Build request
    headers = {'Content-Type': 'application/json'}
    payload = {'q': q, 'from': from_lang, 'to': to_lang, 'termIds' : term_ids}

    # Send request
    r = requests.post(url, params=payload, headers=headers)

    try:
        result = r.json()['result']['trans_result'][0]['dst']
        ret = jsonify({'statusCode': 200, 'msg': 'successful', 'result': result})
    except:
        msg = r.json()['error_msg']
        ret = jsonify({'statusCode': -1, 'msg': msg})

    return ret

if __name__ == "__main__":
    app.run()