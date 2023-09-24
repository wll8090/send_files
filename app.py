from flask import Flask, send_file
from os import listdir

def creat_app():
    app=Flask(__name__)
    path='./static'


    return app

app=creat_app()