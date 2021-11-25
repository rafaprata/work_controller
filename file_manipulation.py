import json

def createJson(jfile, ponto):
    ponto_key = list(ponto.keys())[0]
    jfile[ponto_key] = ponto[ponto_key]
    pontoJson = json.dumps(jfile)
    return pontoJson

def readJsonFile():
    try:
        file = open("database.json", "r")
        try:
            jsonText = json.load(file)
            file.close()
            return jsonText
        except:
            jsonText = {}
            return jsonText
    except:
        jsonText = {}
        return jsonText

def saveJsonFile(db):
    file = open("database.json", "w")
    file.write(db)
    file.close()

def createFile():
    try:
        file = open("database.json", "r")
    except:
        file = open("database.json", "w")
    finally:
        file.close()