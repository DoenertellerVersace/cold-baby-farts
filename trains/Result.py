from Trip import *
from Route import *


class Result:

    def __init__(self, element):
        self.__bwt, self.__changes, self.__stops, self.__legs = element
        self.__string = [", ".join([x[3] for x in self.__legs]), str(self.__changes) + " Umstiege", str(self.__stops) + " Stationen zu fahren"]
        for leg in self.__legs:
            start = leg[0]
            dest = leg[1]
            line = leg[3]
            stops = str(leg[4])
            dir = leg[2].ziel(leg[5])
            leg_string = ["von " + start, "nach " + dest, "Linie " + line, "Richtung " + dir, stops + " Stationen"]
            self.__string = self.__string + leg_string

    def print_result(self):
        return self.__string
