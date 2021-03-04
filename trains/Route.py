class Route():
    def __init__(self, filename):
        self.__line, self.__stops, self.__ring = get_route(filename)

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
            e = [e[n] for n in range(len(e) - 1, -1, -1)]
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
        else:
            return "Jesus fuck"


def get_route(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip())
        stops = []
        for a in lines[1].split(","):
            stops.append(a.strip())
    return lines[0], stops, lines[2]


def print_leg(start, dest, line, stops):
    return start + "\n---> Linie " + line.line() + " mit " + str(stops) + " Unterwegshalten --->\n" + dest + "\n"
