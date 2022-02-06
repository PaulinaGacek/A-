import json

def loadParameters():
    f = open('./config/config.json')
    data = json.load(f)
    width = data['width']
    algorithm = data['algorithm']
    heuristics = data['heuristics']
    f.close()
    return width, algorithm, heuristics