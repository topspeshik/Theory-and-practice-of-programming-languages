import json

class PointError(Exception):
    ...


class Points:
    arr = []
    with open('stations.json') as f:
        file_content = f.read()
        js = json.loads(file_content)
        arr.append(Point.from_json(js))


class Point:

    def __init__(self,x: float, y:float)->None:
        if not isinstance(x, float) or not isinstance(y, float):
            raise PointError("x should be float")
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y+other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y-other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            if hasattr(other, "__iter__"):
                return self == Point(*other)
            else:
                raise NotImplementedError
        return self.x == other.x and self.y == other.y

    def __neg__(self) -> "Point":
        return Point(-self.x, -self.y)

    def distance_to(self, other: "Point")-> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 )**0.5

    def to_json(self)->str:
        return json.dumps({"x": self.x, "y": self.y})

    @classmethod
    def from_json(cls, js: str)->"Point":
        return cls(float(js[0]["location"]["lat"]), float(js[0]["location"]["lon"]))



    def __str__(self)-> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}"

    def __repr__(self)-> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}"

    def is_center(self: "Point") -> bool:
        return self == Point(0,0)
