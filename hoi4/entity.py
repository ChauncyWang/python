from hoi4.base import Base
import json


# 省份 包含的资源
class Resources(Base):
    def __init__(self):
        self.oil = 1
        self.aluminum = 108
        self.aluminum1 = Buildings()
        pass


class Buildings(Base):
    def __init__(self):
        self.infrastructure = 1

g = Resources()
print(json.dumps(g))
