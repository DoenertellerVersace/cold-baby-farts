from flask import Flask

app = Flask(__name__)

@app.route("/suche/<start>/<dest>/<max>")
def search(start, dest, max):
    from trains import Route, Train, Trip, direct_connect, get_route, load_stations, print_leg
    stations = {}
    connect = {}
    routes = []
    u1 = Route("./u1.txt")
    u2 = Route("./u2.txt")
    u3 = Route("./u3.txt")
    u4 = Route("./u4.txt")
    u5 = Route("./u5.txt")
    u6 = Route("./u6.txt")
    u7 = Route("./u7.txt")
    u8 = Route("./u8.txt")
    u9 = Route("./u9.txt")
    s1 = Route("./s1.txt")
    s2 = Route("./s2.txt")
    s25 = Route("./s25.txt")
    s3 = Route("./s3.txt")
    s5 = Route("./s5.txt")
    s7 = Route("./s7.txt")
    s8 = Route("./s8.txt")
    s9 = Route("./s9.txt")
    s42 = Route("./s42.txt")
    s45 = Route("./s45.txt")
    stations, connect = load_stations()
    trip1 = Trip(start, dest)
    trip1.get_itinerary(int(max))
    a = trip1.print_itinerary_list()
    return a;


 
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)