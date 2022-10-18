import json


class PointError(Exception):
    ...


class Point:

    def __init__(self, x: float, y: float) -> None:
        if not isinstance(x, float) or not isinstance(y, float):
            raise PointError("x should be float")
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            if hasattr(other, "__iter__"):
                return self == Point(*other)
            else:
                raise NotImplementedError
        return self.x == other.x and self.y == other.y

    def __neg__(self) -> "Point":
        return Point(-self.x, -self.y)

    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def to_json(self) -> str:
        return json.dumps({"x": self.x, "y": self.y})

    @classmethod
    def from_json(cls, js: dict) -> "Point":
        if "lat" not in js['location'] and "lon" in js['location']:
            return cls(0, float(js["location"]["lon"]))
        elif "lat" in js['location'] and "lon" not in js['location']:
            return cls(float(js["location"]["lat"], 0))
        else:
            return cls(float(js["location"]["lat"]), float(js["location"]["lon"]))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}"

    def is_center(self: "Point") -> bool:
        return self == Point(0, 0)


class Station:
    def __init__(self, station: str):
        self.storageSt = []

        with open(station) as f:
            js = json.load(f)
        for i in js:
            if "lat" in i['location'] and "lon" in i['location']:
                self.storageSt.append(Point.from_json(i))


    def minSq(self):
        min = 32000

        for i in range(len(self.storageSt) - 2):
            for j in range(i + 1, len(self.storageSt) - 1):
                for k in range(j + 1, len(self.storageSt)):
                    side1 = Point(self.storageSt[i].x, self.storageSt[i].y).distance_to(
                        Point(self.storageSt[j].x, self.storageSt[j].y))
                    side2 = Point(self.storageSt[j].x, self.storageSt[j].y).distance_to(
                        Point(self.storageSt[k].x, self.storageSt[k].y))
                    side3 = Point(self.storageSt[k].x, self.storageSt[k].y).distance_to(
                        Point(self.storageSt[i].x, self.storageSt[i].y))
                    p = (side1 + side2 + side3) / 2
                    square_tr = (p * (p - side1) * (p - side2) * (p - side3)) ** 0.5
                    if square_tr < min:
                        min = square_tr

        return min

