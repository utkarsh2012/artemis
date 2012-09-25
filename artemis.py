# -*- coding: utf-8 -*-
"""
Artemis
~~~~~~

An app tp fetch metrics which uses celery backend for distributed task processing

__author__ = 'Utkarsh Sengar'

"""

from flask import Flask, request, jsonify
from tasks import perform_collection
import markdown

app = Flask(__name__)

"""
Home of the app, for now renders the markdown README file as html
"""
@app.route('/')
def index():
    f = open("README.md", "r")
    html = markdown.markdown(f.read())
    f.close()
    return html


"""
The primary endpoint which will be called with POST request, GET is also enabled to give correct error message if called by mistake
"""
@app.route('/fetch', methods=['POST', 'GET'])
def fetch():
    if request.method == "POST":
        list_of_nodes=request.form.getlist('node')
        url_pattern=request.form['url']
        if list_of_nodes and url_pattern:
            perform_collection.delay(list_of_nodes, url_pattern)
            return jsonify(success="Request is being processed")
        else:
            return jsonify(error="Invalid request")
    else:
        return jsonify(error='Please try a POST request with: 1. List of nodes (eg: nodes=machine1.foo.com, machine2.foo.com), 2. URL Pattern of the endpoint (eg: url=metric)')


"""
This is a sample endpoint to test the celery task
"""
@app.route('/metric', methods=['GET'])
def test_metric():
    sample_response = {
        "cpu":{
            "core1":"80%",
            "core2":"33%"
        },

        "mem":{
            "used":"1234M",
            "free":"6666M"
        }
    }

    return jsonify(sample_response)


if __name__ == '__main__':
    app.run()
