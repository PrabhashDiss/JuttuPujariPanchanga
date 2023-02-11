import json


def read_panchangam():
    try:
        with open("panchangam.json", "r") as jsonData:
            panchangamJson = json.load(jsonData)
    except:
        print("Error reading \"panchangam.json\" file\n")
        exit(-1)
    else:
        return panchangamJson

def print_panchangam():
    panchangamJson = read_panchangam()
    msg = ""
    for i in panchangamJson:
        if i.find("Udaya Lagna Muhurta") != -1:
            msg = msg + i + ":\n" + panchangamJson[i] + "\n"
        else:
            msg = msg + i + ": " + panchangamJson[i] + "\n"
    print(msg)
