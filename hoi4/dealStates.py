import os
import re

path = "states"
list = os.listdir(path)
provinces = []
for l in list:
    l = path+"/"+l
    file = open(l, "r").read()
    id = re.findall("id\W*=\W*(\w*)", file)
    name = re.findall("name\W*=\W*(\w*)", file)
    manpower = re.findall("manpower\W*=\W*(\w*)", file)
    province = re.findall("provinces\W*=\W*{\W*(.*?)\W*\}", file)
    print(province)
