import pytest
import json
from plib import Point, PointError, Station


class TestPoint:

    def test_creation(self):
        Station("stations.json")

    def test_minSquare(self):
        assert Station("stations.json").minSq() == 9.382093856738155e-07

