class Route():
    def __init__(self, filename):
        self.__line, self.__stops, self.__ring = get_route(filename)
        routes.append(self)

    def __str__(self):
        return "Die Linie " + self.__line + " mit den Haltestellen:\n" + "\n".join(self.__stops)
    
    def ring(self):
        return self.__ring

    def stops(self):
        return self.__stops

    def line(self):
        return self.__line

    def next_stops(self, position, direction):
        self.stopsrev = self.__stops
        if direction == "out":
            return self.__stops[position + 1:]
        if direction == "in":
            e = self.stopsrev[:position]
            e = [e[n] for n in range(len(e)-1,-1,-1)]
            return e
    def ziel(self, direction):
        if self.__ring == "True":
            if direction == "out":
                return "Ring<-"
            elif direction == "in":
                return "Ring->"
        elif self.__ring == "False":
            if direction == "out":
                return self.__stops[-1]
            elif direction == "in":
                return self.__stops[0]

class Train():
    def __init__(self, train_no, route, position, direction):
        self.train_no = train_no
        self.route = route
        self.position = int(position)
        self.direction = direction

    def __str__(self):
        liste = self.route.next_stops(self.position, self.direction)
        return "Zug Nummer " + str(self.train_no) + " auf der Linie " + self.route.line() + " mit den Haltestellen:\n" + "\n".join(liste)


    def get_position(self):
        get_station = self.route.stops()[self.position]
        return get_station

    def move_out(self):
        route_len = len(self.route.stops())
        if self.route.ring() == "False":
            self.direction = "out"
            if self.position <= route_len - 2:
                self.position = self.position + 1
            elif self.position >= route_len - 1:
                self.position = route_len - 1
        elif self.route.ring() == "True":
            self.direction = "out"
            if self.position <= route_len - 2:
                self.position = self.position + 1
            elif self.position >= route_len - 1:
                self.position = 0
        
        return self.get_position()

    def move_in(self):
        if self.route.ring() == "False":
            self.direction = "in"
            if self.position >= 1:
                self.position = self.position - 1
            elif self.position == 0:
                self.position = 0
        elif self.route.ring() == "True":
            self.direction = "in"
            if self.position >= 1:
                self.position = self.position - 1
            elif self.position == 0:
                self.position = len(self.route.stops()) - 1
        
        return self.get_position()
            

    def next_stops(self):
        return self.route.next_stops(self.position, self.direction)

class Trip():
    def __init__(self, start, destination):
        self.start = start
        self.destination = destination
        self.nbt_list = []

    def get_connection(self):
        if self.start == self.destination:
            return "Start und Ziel identisch!"
        if self.start not in stations:
            return "Start nicht korrekt!"
        if self.destination not in stations:
            return "Ziel nicht korrekt!"
        leg1 = direct_connect(self.start, self.destination)

        return leg1

    def connect(self, factor):
        start = self.start
        dest = self.destination
        itineraries = []
        direct = []
        length_direct = 1000000
        length_b = 1000000
        length_c = 1000000
        length_d = 1000000
        if direct_connect(start, dest) != None:
            for z in direct_connect(start, dest):
                line, length, direction = z
                leg = [start, dest, line, line.line(), length, direction]
                leggy = []
                leggy.append(leg)
                itineraries.append((0, length, leggy))
                if length_direct >= length:
                    length_direct = length
            #direct = [direct_connect(start, dest)[0], direct_connect(start, dest)[1]]
            #print(direct)
        for first_station in connect[start]:
            if first_station == start or first_station == dest:
                next
            else:
                counter1 = 0
                counter1l = []
                for c1 in direct_connect(start, first_station):
                    counter1l.append(counter1)
                    counter1 = counter1 + 1
                for a in counter1l:
                    line1, length1, direction1 = direct_connect(start, first_station)[a]
                    for sec_station in connect[first_station]:
                        if sec_station == start or sec_station == first_station:
                            next
                        else:
                            counter2 = 0
                            counter2l = []
                            for c2 in direct_connect(first_station, sec_station):
                                counter2l.append(counter2)
                                counter2 = counter2 + 1
                            for b in counter2l:
                                line2, length2, direction2 = direct_connect(first_station, sec_station)[b]
                                length = length1 + length2
                                if line1 != line2 and start not in line2.stops():
                                    if sec_station not in line1.stops():
                                        if length_direct != 1000000 and length >= 0.9 * factor * length_direct:
                                            next
                                        elif length_b != 1000000 and length >= 0.9 * factor * length_b:
                                            next
                                        elif sec_station == dest:
                                            if length <= length_b:
                                                length_b = length
                                            
                                            leg1 = [start, first_station, line1, line1.line(), length1, direction1]
                                            leg2 = [first_station, dest, line2, line2.line(), length2, direction2]
                                            itineraries.append((1, length, [leg1, leg2]))
                                            next
                                        else:
                                            for third_station in connect[sec_station]:
                                                if third_station == first_station or third_station == sec_station:
                                                    next
                                                else:
                                                    counter3 = 0
                                                    counter3l = []
                                                    for c3 in direct_connect(sec_station, third_station):
                                                        counter3l.append(counter3)
                                                        counter3 = counter3 + 1
                                                    for c in counter3l:
                                                        line3, length3, direction3 = direct_connect(sec_station, third_station)[c]
                                                        length = length1 + length2 + length3
                                                        if line1 != line3 and line2 != line3:
                                                            if first_station not in line3.stops() and start not in line3.stops():
                                                                if third_station not in line1.stops() and third_station not in line2.stops():
                                                                    if length_direct != 1000000 and length >= 0.6 * factor * length_direct:
                                                                        next
                                                                    elif length_b != 1000000 and length >= 0.6 * factor * length_b:
                                                                        next
                                                                    elif length_c != 1000000 and length >= 0.6 * factor * length_c:
                                                                        next
                                                                    elif third_station == dest:
                                                                        if length <= length_c:
                                                                            length_c = length
                                                                        
                                                                        leg1 = [start, first_station, line1, line1.line(), length1, direction1]
                                                                        leg2 = [first_station, sec_station, line2, line2.line(), length2, direction2]
                                                                        leg3 = [sec_station, dest, line3, line3.line(), length3, direction3]
                                                                        itineraries.append((2, length, [leg1, leg2, leg3]))
                                                                    else:
                                                                        for fourth_station in connect[third_station]:
                                                                            if third_station == fourth_station or fourth_station == sec_station:
                                                                                next
                                                                            elif fourth_station == first_station or fourth_station == start:
                                                                                next
                                                                            else:
                                                                                counter4 = 0
                                                                                counter4l = []
                                                                                for c4 in direct_connect(third_station, fourth_station):
                                                                                    counter4l.append(counter4)
                                                                                    counter4 = counter4 + 1
                                                                                for d in counter4l:
                                                                                    line4, length4, direction4 = direct_connect(third_station, fourth_station)[d]
                                                                                    length = length1 + length2 + length3 + length4
                                                                                    if length_direct != 1000000 and length >= 0.5 * factor * length_direct:
                                                                                        next
                                                                                    elif length_b != 1000000 and length >= 0.5 * factor * length_b:
                                                                                        next
                                                                                    elif length_c != 1000000 and length >= 0.5 * factor * length_c:
                                                                                        next
                                                                                    elif length_d != 1000000 and length >= 0.5 * factor * length_d:
                                                                                        next
                                                                                    elif fourth_station == dest:
                                                                                        if length <= length_d:
                                                                                            length_d = length
                                                                                        elif line1 == line4 or line2 == line4:
                                                                                            next
                                                                                        elif line3 == line4:
                                                                                            next
                                                                                        else:
                                                                                            if first_station not in line4.stops() and start not in line4.stops():
                                                                                                if sec_station not in line4.stops() and fourth_station not in line1.stops():
                                                                                                    if fourth_station not in line2.stops() and fourth_station not in line3.stops():
                                                                                                        leg1 = [start, first_station, line1, line1.line(), length1, direction1]
                                                                                                        leg2 = [first_station, sec_station, line2, line2.line(), length2, direction2]
                                                                                                        leg3 = [sec_station, third_station, line3, line3.line(), length3, direction3]
                                                                                                        leg4 = [third_station, dest, line4, line4.line(), length4, direction4]
                                                                                                        itineraries.append((3, length, [leg1, leg2, leg3, leg4]))
                                                                                                        
                                                                                                    else:
                                                                                                        next
                                                                                                else:
                                                                                                    next
                                                                                            else:
                                                                                                next
                                                                                    else:
                                                                                        next

                
                
        return itineraries
        
    def get_itinerary(self, max_changes):
        factor = 2.5
        mxc = max_changes
        itr_list = self.connect(factor)
        bwt_list = []
        beste_bewertung = 1000000
        for item in itr_list:
            this_changes, this_length, this_conn = item
            bewertung = this_length / ((this_length * ((this_changes + 1) / 10)) ** (-0.33333)) + 1
            bwt_list.append((bewertung, this_changes, this_length, this_conn))
        bwt_list.sort(key=lambda a: a[0])
        for item in bwt_list:
            this_bewertung, this_changes, this_length, this_conn = item
            if this_bewertung <= beste_bewertung:
                beste_bewertung = this_bewertung
            if this_bewertung <= 1.8 * beste_bewertung and this_changes <= mxc:
                self.nbt_list.append(item)
        return self.nbt_list

    def print_itinerary_list(self):
        self.results = []
        for item in self.nbt_list:
            if item[1] == 0:
                self.results.append(
                    str(item[3][0][0]) + "\n---> " + str(item[3][0][3]) + " --->  Richtung " + item[3][0][2].ziel(item[3][0][5]) + "\n" + 
                    str(item[3][0][1]) + "\n\n" + str(item[2]) + " Stationen zu fahren, kein Umstieg."
                    )
            elif item[1] == 1:
                self.results.append(
                    str(item[3][0][0]) + "\n---> " + str(item[3][0][3]) + " --->  Richtung " + item[3][0][2].ziel(item[3][0][5]) + "\n" + 
                    str(item[3][0][1]) + "\n++++++\n" + str(item[3][1][0]) + "\n---> " + str(item[3][1][3]) + " --->  Richtung " + item[3][1][2].ziel(item[3][1][5]) + "\n" + 
                    str(item[3][1][1]) + "\n\n" + str(item[2]) + " Stationen zu fahren, 1 Umstieg."
                    )
            elif item[1] == 2:
                self.results.append(
                    str(item[3][0][0]) + "\n---> " + str(item[3][0][3]) + " --->  Richtung " + item[3][0][2].ziel(item[3][0][5]) + "\n" + 
                    str(item[3][0][1]) + "\n++++++\n" + str(item[3][1][0]) + "\n---> " + str(item[3][1][3]) + " --->  Richtung " + item[3][1][2].ziel(item[3][1][5]) + "\n" + 
                    str(item[3][1][1]) + "\n++++++\n" + str(item[3][2][0]) + "\n---> " + str(item[3][2][3]) + " --->  Richtung " + item[3][2][2].ziel(item[3][2][5]) + "\n" + 
                    str(item[3][2][1]) + "\n\n" + str(item[2]) + " Stationen zu fahren, 2 Umstiege."
                    )
            elif item[1] == 3:
                self.results.append(
                    str(item[3][0][0]) + "\n---> " + str(item[3][0][3]) + " --->  Richtung " + item[3][0][2].ziel(item[3][0][5]) + "\n" + 
                    str(item[3][0][1]) + "\n++++++\n" + str(item[3][1][0]) + "\n---> " + str(item[3][1][3]) + " --->  Richtung " + item[3][1][2].ziel(item[3][1][5]) + "\n" + 
                    str(item[3][1][1]) + "\n++++++\n" + str(item[3][2][0]) + "\n---> " + str(item[3][2][3]) + " --->  Richtung " + item[3][2][2].ziel(item[3][2][5]) + "\n" + 
                    str(item[3][2][1]) + "\n++++++\n" + str(item[3][3][0]) + "\n---> " + str(item[3][3][3]) + " --->  Richtung " + item[3][3][2].ziel(item[3][3][5]) + "\n" + 
                    str(item[3][3][1]) + "\n\n" + str(item[2]) + " Stationen zu fahren, 3 Umstiege."
                    )
            
        print("Es gibt folgende Verbindungen:\n\n" + "\n\n--------\n\n".join(self.results))


            

        
        


def direct_connect(start, dest):
    direct_variants = []
    if start not in connect or dest not in connect[start]:
        return None
    for line in connect[start][dest]:
        longness = 0
        direction = None
        a = line.stops().index(start)
        b = line.stops().index(dest)
        last = len(line.stops()) - 1
        if line.ring() == "False":
            if a <= b:
                longness = b - a
                direction = "out"
            else:
                longness = a - b
                direction = "in"
        if line.ring() == "True":
            if a <= b and (b - a) <= ((last - b) + a):
                longness = b - a
                direction = "out"
            if a <= b and (b - a) > ((last - b) + a):
                longness = (last - b) + a + 1
                direction = "in"
            if a > b and (a - b) <= ((last - a) + b):
                longness = a - b
                direction = "in"
            if a > b and (a - b) > ((last - a) + b):
                longness = (last - a) + b + 1
                direction = "out"
        
        direct_variants.append((line, longness, direction))
    return direct_variants

def get_route(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip())
        stops = []
        for a in lines[1].split(","):
            stops.append(a.strip())
    return lines[0], stops, lines[2]

def load_stations():
    stations = {}
    for route in routes:
        for stop in route.stops():
            if stop not in stations:
                stations[stop] = [route]
            if stop in stations:
                if route not in stations[stop]:
                    stations[stop].append(route)
    connect = {}
    for station in stations:
        connect[station] = {}
        for line in stations[station]:
            for stop in line.stops():
                if stop != station and stop in connect[station]:
                    connect[station][stop].append(line)
                if stop != station and stop not in connect[station]: 
                    connect[station][stop] = [line]
    return stations, connect
     
def print_leg(start, dest, line, stops):
    return start + "\n---> Linie " + line.line() + " mit " + str(stops) + " Unterwegshalten --->\n" + dest + "\n"

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