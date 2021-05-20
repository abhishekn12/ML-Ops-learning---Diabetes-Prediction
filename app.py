from flask import Flask,render_template,system
import Amlworspace

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/get_mlmodels")
def get_ml_models():
    #amlws = Amlworspace()    
    return Amlworspace.get_ml_models();

@app.route('/deploy',methods = ['GET','POST'])
def deploy():
    return render_template('deploy.py')

def main():
    print("Starting app!!!")
    app.run(host='0.0.0.0')
    print("Started app!!!")

if __name__ == '__main__':
    main()


