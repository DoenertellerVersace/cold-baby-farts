''' Nice to have but useless'''


class Train():
    def __init__(self, train_no, route, position, direction):
        self.train_no = train_no
        self.route = route
        self.position = int(position)
        self.direction = direction

    def __str__(self):
        liste = self.route.next_stops(self.position, self.direction)
        return "Zug Nummer " + str(
            self.train_no) + " auf der Linie " + self.route.line() + " mit den Haltestellen:\n" + "\n".join(liste)

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
