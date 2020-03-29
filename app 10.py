# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from controllers import cSecurity
from services import ParameterCheck

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! (SecurityService)"

###---------------------------------------------------------------------------------------

@app.route("/generatesalt", methods=['GET'])
def generatesalt():
    return jsonify(cSecurity().generatesalt())

@app.route("/generatepassword", methods=['GET'])
def generatepassword():
    length = ParameterCheck().secure_parameter(request.form['length'])
    return jsonify(cSecurity().generatepassword(length))

@app.route("/isacceptablepassword", methods=['GET'])
def isacceptablepassword():
    password = ParameterCheck().secure_parameter(request.form['password'])
    return jsonify(cSecurity().isacceptablepassword(password))

@app.route("/gethashed", methods=['GET'])
def gethashed():
    salt = ParameterCheck().secure_parameter(request.form['salt'])
    password = ParameterCheck().secure_parameter(request.form['password'])
    return jsonify(cSecurity().gethashed(salt,password))

@app.route("/checkpassword", methods=['GET'])
def checkpassword():
    salt = ParameterCheck().secure_parameter(request.form['salt'])
    password = ParameterCheck().secure_parameter(request.form['password'])
    hashed = ParameterCheck().secure_parameter(request.form['hashed'])
    return jsonify(cSecurity().checkpassword(salt,password,hashed))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)