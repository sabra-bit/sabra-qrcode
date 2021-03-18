from flask import Flask, redirect, url_for, render_template, request ,jsonify
 
app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
   return render_template("genrate.html")

@app.route("/scan", methods = ['GET','POST'])
def gen():
   return render_template("scanner.html")

if __name__ == "__main__":
   app.run()
 
