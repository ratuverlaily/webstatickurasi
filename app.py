from flask import Flask, Response, request, render_template
from models import Model

app = Flask(__name__)

greeter = Model("bolt://103.89.6.76:7778", "proglan", "kelas2020")
    
@app.route('/')
def getdata_kurasi():
    
    getdata = greeter.get_kurasi()
    return render_template("index.html", data = getdata)
    
if __name__ == "__main__":
    app.run(port=80, debug=True)
