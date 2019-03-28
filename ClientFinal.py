# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:06:04 2019

@author: Utkarsh1409
"""

##ClientFinal.py:
import cv2
import numpy as np
import socket
import sys
import pickle
import struct

from flask import Flask, render_template, Response
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',1234))
while True:
    ret,frame=cap.read()
    data = pickle.dumps(frame) 
    clientsocket.sendall(struct.pack("L", len(data))+data) 
    
@app.route('/calc')
def calc():
    return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

    
if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)    