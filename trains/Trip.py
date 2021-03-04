from typing import Any

from Context import *



class Trip:

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
        connect = Context.get_instance().get_connect()
        start = self.start
        dest = self.destination
        itineraries = []
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
            # direct = [direct_connect(start, dest)[0], direct_connect(start, dest)[1]]
            # print(direct)
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
                                                        line3, length3, direction3 = \
                                                            direct_connect(sec_station, third_station)[c]
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

                                                                        leg1 = [start, first_station, line1,
                                                                                line1.line(), length1, direction1]
                                                                        leg2 = [first_station, sec_station, line2,
                                                                                line2.line(), length2, direction2]
                                                                        leg3 = [sec_station, dest, line3, line3.line(),
                                                                                length3, direction3]
                                                                        itineraries.append(
                                                                            (2, length, [leg1, leg2, leg3]))
                                                                    else:
                                                                        for fourth_station in connect[third_station]:
                                                                            if third_station == fourth_station or fourth_station == sec_station:
                                                                                next
                                                                            elif fourth_station == first_station or fourth_station == start:
                                                                                next
                                                                            else:
                                                                                counter4 = 0
                                                                                counter4l = []
                                                                                for c4 in direct_connect(third_station,
                                                                                                         fourth_station):
                                                                                    counter4l.append(counter4)
                                                                                    counter4 = counter4 + 1
                                                                                for d in counter4l:
                                                                                    line4, length4, direction4 = \
                                                                                        direct_connect(third_station,
                                                                                                       fourth_station)[
                                                                                            d]
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
                                                                                                        leg1 = [start,
                                                                                                                first_station,
                                                                                                                line1,
                                                                                                                line1.line(),
                                                                                                                length1,
                                                                                                                direction1]
                                                                                                        leg2 = [
                                                                                                            first_station,
                                                                                                            sec_station,
                                                                                                            line2,
                                                                                                            line2.line(),
                                                                                                            length2,
                                                                                                            direction2]
                                                                                                        leg3 = [
                                                                                                            sec_station,
                                                                                                            third_station,
                                                                                                            line3,
                                                                                                            line3.line(),
                                                                                                            length3,
                                                                                                            direction3]
                                                                                                        leg4 = [
                                                                                                            third_station,
                                                                                                            dest, line4,
                                                                                                            line4.line(),
                                                                                                            length4,
                                                                                                            direction4]
                                                                                                        itineraries.append(
                                                                                                            (3, length,
                                                                                                             [leg1,
                                                                                                              leg2,
                                                                                                              leg3,
                                                                                                              leg4]))

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


def direct_connect(start, dest):
    direct_variants = []
    connect = Context.get_instance().get_connect()
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
