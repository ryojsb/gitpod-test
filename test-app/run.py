#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib3, requests, json
import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def top():
    if request.method == "POST":
        req = request.form

        arg1 = req["arg1"]
        arg2 = req["arg2"]

        sum = int(arg1) * int(arg2)
        print(sum)

        return render_template("sample.html", sum=sum)
        return render_template("sample.html")
    else:
        return render_template('sample.html')

port = os.getenv('VCAP_APP_PORT', '8000')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)