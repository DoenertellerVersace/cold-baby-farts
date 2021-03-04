from flask import Flask, render_template, request
from Trip import *
from Context import *
from Result import Result

app = Flask(__name__)

connect = {}
stations = {}
routes = []


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/suche", methods=['POST'])
def search():
    start = request.form['start']
    dest = request.form['dest']
    max = request.form['max']
    print("Anfrage für %s nach %s mit max Umsteigen %s" % (start, dest, max))
    trip1 = Trip(start, dest)
    blub = trip1.get_itinerary(int(max))
    blub2 = [Result(x).print_result() for x in blub]
    for res in blub2:
        print(res)
        for leg in res[3]:
            print(leg)
        print("-------")
    return render_template("connection.html", result=blub2)


if __name__ == "__main__":
    Context()
    app.run(debug=True, host="0.0.0.0", port=3000)
