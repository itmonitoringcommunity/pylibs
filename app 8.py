# -*- coding: utf-8 -*-
from serviceactions import BulletinThread,AssetThread,ContractThread
import Error
from flask import Flask,jsonify
app = Flask(__name__)
       
# Create new threads
thread_b = BulletinThread(1, "Thread-Bulletin", 6)  # for each 6 seconds
thread_a = AssetThread(2, "Thread-Asset", 6)        # for each 6 seconds
thread_c = ContractThread(3, "Thread-Contract", 6)  # for each 6 seconds

@app.route("/")
def hello():
    return "Hello World! (SchedulerService)"

@app.route("/start")
def start():   
    try:
        thread_b.start()
        thread_a.start()
        thread_c.start()
    except Error as e:
        return jsonify({"status":"false","message":e})
    
    return jsonify({"status":"true","value":"Scheduler Service is started"})

@app.route("/stop")
def stop():
    try:
        thread_b.stop()
        thread_a.stop()
        thread_c.stop()
    except Error as e:
        return jsonify({"status":"false","message":e})
    
    return jsonify({"status":"true","value":"Scheduler Service is stopped"})

@app.route("/restart")
def restart():
    try:
        thread_b.restart()
        thread_a.restart()
        thread_c.restart()
    except Error as e:
        return jsonify({"status":"false","message":e})
    
    return jsonify({"status":"true","value":"Scheduler Service is restarted"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5009)