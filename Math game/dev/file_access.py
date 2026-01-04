## command to run auto-py-to-exe:  python -m auto_py_to_exe

import base64
import json
import time

class ScoreData(): # A class reading, encrypting, updating, and decrypting complied as base64 data.

    def Encrypt():
        with open("data/scores.mg", "r") as file: ## opening encrypted file.
            byte = file.read()
        de_b = str.encode(byte)
        de_b = base64.standard_b64encode(de_b)
        de_b = bytes.decode(de_b)
        file = open("data/scores.mg", "w") # storing data
        file.write(de_b)
        file.close()

    def Decrypt(modes,difficulty,points): # Decrypting
        with open("data/scores.mg", "rb") as file: ## opening decrypted file.
            string = file.read()

        de_f = base64.standard_b64decode(string)
        data = bytes.decode(de_f)

        convertedSingleQuotes = ''
        for s in data:
            if s == "'":
                s = '"'
                convertedSingleQuotes += s
            else:
                convertedSingleQuotes += s
        data = convertedSingleQuotes

        ## print(data) Un-comment to see the state of the scores.mg file.

        data = json.loads(data)

        with open("data/scores.mg", "w") as file:
            data["score"][f"{modes}"][f"{difficulty}"] = str(points)
            data = str(data)
            file.write(data)

    def CheckScore(modes,difficulty):
        with open("data/scores.mg", "rb") as file: ## opening encrypted file.
            scoreData = file.read()

        scoreData = base64.standard_b64decode(scoreData)
        scoreData = bytes.decode(scoreData)

        convertedSingleQuotes = ""
        for s in scoreData:
            if s == "'":
                s = '"'
                convertedSingleQuotes += str(s)
            else:
                convertedSingleQuotes += str(s)

        scoreData = json.loads(convertedSingleQuotes)

        score = float(scoreData["score"][modes][difficulty])

        return score

    def StampTime(): # printing start time.
        start = time.time()
        return start

## ScoreData.Encrypt()