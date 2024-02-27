
from flask import render_template,request,jsonify
from app.hardware import hardwaremanager
from app import app


@app.route('/')
def index():
    return render_template('basic.html',testvar='appelflap')


@app.route('/posttest',methods=['POST'])
def command():
    pass

@app.route('/test',methods=['GET'])
def tickle():
    print('that tickels!')
    return '',204
