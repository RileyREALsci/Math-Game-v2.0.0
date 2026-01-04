from file_access import *
import random
from math_classes import *

GAME_RUNNING = True
QUESTIONS = 10
QUESTIONS_CHECK = 10 # the purpose of this variable is to have a reference to how many questions are correct.
comment = "you have set a record, replay and try to beat it（。＾▽＾）"
positiveComments = [
    "NEW RECORD! Well done! see if you can beat it again! ;)",
    "NEW RECORD! Ohh look at you go! (*￣U￣)╭",
    "NEW RECORD! Well done I guess practice pays off. o(￣▽￣)ｄ",
    "NEW RECORD! You are realy improving at this, the new score will suffice. (～￣▽￣)～",
    "NEW RECORD! Careful! dont let your brain explode! (°ロ°)",
    "NEW RECORD! math is good for your brain ヽ(✿ﾟ▽ﾟ)ノ",
    "NEW RECORD! You can beat this record again persevere. ヾ(^▽^*)))"
]
negativeComments = [
    "Try again and see if you can beat the current score! （￣︶￣）↗　",
    "You did well but not well enough to beat the previous score U_U",
    "Sorry you might be getting worse at math that's ok your still loved I'm sure ╰(￣ω￣ｏ)",
    "No record beaten just try harder next time ok ผ(•̀_•́ผ)",
    "Try again and beat the previous score, you can do it I know you can ლ(╹◡╹ლ)",
    "practice makes perfect try again (✿◠‿◠)"
]


while GAME_RUNNING:
    level_data = {
        "dificulty_level": {
            
            "weak": {
                "weak": 10
            },
            "easy": {
                "easy": 100
            },
            "medium": {
                "medium": 1000
            },
            "hard": {
                "hard": 10000
            },
            "expert": {
                "expert": 100000
            },
            "ridiculous": {
                "ridiculous": 1000000
            },
            "impossible": {
                "impossible": 10000000
            }
        }
    }

    game = []

    modes = input(str("what mode do you want to play ? Type\nA for Addition\nS for Subtraction\nM for Maltiplucation\nD for Divission\nD/2 for Divission by two\n")).lower()
    difficulty = input(str("Choose dificulty Type\nWeak\nEasy\nMedium\nHard\nExpert\nRidiculous\nImpossible\n" )).lower()

    game.append(difficulty)

    decimals = (level_data["dificulty_level"][game[0]][game[0]])

    correctAnswers = 0    
    start = ScoreData.StampTime()

    rounds_running = True
    while rounds_running:

        num1 = random.randint(1,decimals)
        num2 = random.randint(1,decimals)

        div = MathOperations.divission(num1,1,decimals)

        div_equation = num1 / div

        if modes == "a":
            player_answer = int(input(f"""{num1} \n + \n{num2}\n= """))
            if player_answer == MathOperations.addition(num1,num2):
                print("Correct")
                correctAnswers += 1
            elif player_answer == "quit":
                rounds_running = False
            else:
                print(f"Incorrect the answer was {MathOperations.addition(num1,num2)}")
        elif modes == "s":
            player_answer = int(input(f"""{num1} \n – \n{num2}\n= """))
            if player_answer == MathOperations.subtraction(num1,num2):
                print("Correct")
                correctAnswers += 1
            elif player_answer == "quit":
                rounds_running = False
            else:
                print(f"Incorrect the answer was {MathOperations.subtraction(num1,num2)}")
        elif modes == "m":
            player_answer = int(input(f"""{num1} \n × \n{num2}\n= """))
            if player_answer == MathOperations.multiplacation(num1,num2):
                print("Correct")
                correctAnswers += 1
            elif player_answer == "quit":
                rounds_running = False
            else:
                print(f"Incorrect the answer was {MathOperations.multiplacation(num1,num2)}")
        elif modes == "d":
            player_answer = int(input(f"""{num1} \n ÷ \n{div}\n= """))
            if player_answer == div_equation:
                print("Correct")
                correctAnswers += 1
            elif player_answer == "quit":
                rounds_running = False
            else:
                print(f"Incorrect the answer was {int(num1 / div)}")
        elif modes == "d/2":
            player_answer = float(input(f"""{num1} \n ÷ \n 2\n= """))
            if player_answer == num1 / 2:
                print("Correct")
                correctAnswers += 1
            elif player_answer == "quit":
                rounds_running = False
            else:
                print(f"Incorrect the answer was {float(num1 / 2)}")

        QUESTIONS -= 1
        if QUESTIONS <= 0:
            rounds_running = False
    
    QUESTIONS += 10
    
    finish = ScoreData.StampTime()
    consiqenceFactor = (1 + QUESTIONS_CHECK - correctAnswers)
    score = int((finish - start) * 1000) / 1000 * consiqenceFactor ## giving a score to three decimal places and facroring in incorrect answers.
    
    try:

        points = ScoreData.CheckScore(modes,difficulty)

        if score > points: # Checking if time score is less for a new record
                points
                comment = random.choice(negativeComments)
        else:
                points = score
                comment = random.choice(positiveComments)
    except:
        points = score

    ScoreData.Decrypt(modes,difficulty,points)
    ScoreData.Encrypt()
    end = input(f"finished you got “{correctAnswers}” out of “10” your score is {score} the record is {points} {comment}\n\nType “Replay” to play again: ").lower()
    if end != "replay":
        GAME_RUNNING = False