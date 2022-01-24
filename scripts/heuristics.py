from spot import Spot

class Heuristics:

    def manghattan(p1: Spot, p2: Spot):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)
