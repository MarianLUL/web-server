# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
from datetime import datetime
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    now = datetime.now()
    cas  =  now.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.tmpl',cas=cas)
@app.route('/pole')
def pole():
    arr =['pondeli','utery','streda','ctvrtek','patek','sobota','nedele']
    return render_template('pole.tmpl',arr=arr)


@app.route("/time")
def cas():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

@app.route("/hodnota/<int:cislo>")
def hodnota(cislo):
    return str(cislo)
# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()