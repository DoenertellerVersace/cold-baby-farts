from Route import Route


class Context:
    __instance = None

    @staticmethod
    def get_instance():
        if Context.__instance is None:
            Context()
        return Context.__instance

    def __init__(self):
        if Context.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Context.__instance = self
            self.__stations = {}
            self.__connect = {}
            self.__routes = []
            self.__load_context()

    def __load_context(self):
        self.__routes.append(Route("./ruten/u1.txt"))
        self.__routes.append(Route("./ruten/u2.txt"))
        self.__routes.append(Route("./ruten/u3.txt"))
        self.__routes.append(Route("./ruten/u4.txt"))
        self.__routes.append(Route("./ruten/u5.txt"))
        self.__routes.append(Route("./ruten/u6.txt"))
        self.__routes.append(Route("./ruten/u7.txt"))
        self.__routes.append(Route("./ruten/u8.txt"))
        self.__routes.append(Route("./ruten/u9.txt"))
        self.__routes.append(Route("./ruten/s1.txt"))
        self.__routes.append(Route("./ruten/s2.txt"))
        self.__routes.append(Route("./ruten/s25.txt"))
        self.__routes.append(Route("./ruten/s3.txt"))
        self.__routes.append(Route("./ruten/s5.txt"))
        self.__routes.append(Route("./ruten/s7.txt"))
        self.__routes.append(Route("./ruten/s8.txt"))
        self.__routes.append(Route("./ruten/s9.txt"))
        self.__routes.append(Route("./ruten/s42.txt"))
        self.__routes.append(Route("./ruten/s45.txt"))
        self.load_stations()

    def load_stations(self):
        self.__stations = {}
        for route in self.__routes:
            for stop in route.stops():
                if stop not in self.__stations:
                    self.__stations[stop] = [route]
                if stop in self.__stations:
                    if route not in self.__stations[stop]:
                        self.__stations[stop].append(route)
        self.__connect = {}
        for station in self.__stations:
            self.__connect[station] = {}
            for line in self.__stations[station]:
                for stop in line.stops():
                    if stop != self.__stations and stop in self.__connect[station]:
                        self.__connect[station][stop].append(line)
                    if stop != self.__stations and stop not in self.__connect[station]:
                        self.__connect[station][stop] = [line]

    def get_connect(self):
        return self.__connect

    def get_stations(self):
        return self.__stations

    def get_routes(self):
        return self.__routes
