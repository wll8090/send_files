from flask import Flask, send_file
from os import listdir

def creat_app():
    app=Flask(__name__)
    path='./static'

    @app.route('/')
    def index():
        text='<h2>file_list</h2><br>'
        for i in listdir(path):
            text += f"{i}<br>"
        return text
    @app.route("/<file>")
    def sendFile(file):
        print(file)
        file=f'{path}/{file}'
        return send_file(file)

    return app

app=creat_app()

app.run(debug=1)