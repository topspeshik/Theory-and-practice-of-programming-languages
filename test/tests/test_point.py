import pytest
import json
from plib import Point, PointError



class TestPoint:

    def test_creation(self):
        Point(1.2 ,2.2)

    def test_check(self):
        arr =[]
        with open('stations.json') as f:
            file_content = f.read()
            js = json.loads(file_content)
            arr.append(Point.from_json(js))




    # def test_addition(self, points):
    #     p1, p2 = points
    #     assert p1 + p2 == p2
    #
    # def test_substract(self, points):
    #     p1, p2 = points
    #     assert p1 - p2 == -p2


    # @pytest.mark.parametrize(
    #     "p1, p2, distance",
    #     [(Point(0,0), Point(0,10), 10),
    #      (Point(0,0), Point(10,0), 10),
    #      (Point(0, 0), Point(1, 1), 1.4)])
    # def test_distance_all_axis(self, p1, p2, distance):
    #     assert p1.distance_to(p2) == pytest.approx(distance,0.1)

    # def test_to_json(self):
    #     js = '{"x": 0, "y": 0}'
    #     assert Point(0, 0).to_json() == js

    def test_from_json(self):
        with open('stations.json') as f:
            file_content = f.read()
            js = json.loads(file_content)
            assert Point.from_json(js)

    # def test_center(self, points):
    #     p1, p2 = points
    #     assert p1.is_center()
    #     assert not p2.is_center()
    #
    # def test_eq_with_other_type(self, points):
    #     p1, p2 = points
    #     assert p1 == [0, 0]
    #     assert p2 == [0, 5]

