from tkinter import *

import data_calls
import Operands
import random

# Root
root1 = Tk()
root1.attributes()

## graphics

# Variable textures
textureData = data_calls.Graphis.ReadGraphicDataFile("graphics_structs.json","background")
textureData = data_calls.Graphis.RendomizeTexture(textureData)
BACKGROUND = PhotoImage(file=textureData)


# fixed textures
CONFIRM_BUTTON = PhotoImage(file="data/images/green_button.png")
PLAY_BUTTON = PhotoImage(file="data/images/play_button.png")
LEADER_BOARD_BUTTON = PhotoImage(file="data/images/grey_button.png")
INFOMATION_BUTTON = PhotoImage(file="data/images/grey_button.png")
SETTINGS_BUTTON = PhotoImage(file="data/images/grey_button.png")
CONTACT_BUTTON = PhotoImage(file="data/images/contact_button.png")
DONATE_BUTTON = PhotoImage(file="data/images/grey_button.png")
SAVE1_BUTTON = PhotoImage(file="data/images/save1_button.png")
SAVE2_BUTTON = PhotoImage(file="data/images/save2_button.png")
SAVE3_BUTTON = PhotoImage(file="data/images/save3_button.png")
SAVE4_BUTTON = PhotoImage(file="data/images/save4_button.png")
BACK_BUTTON = PhotoImage(file="data/images/back_button.png")
PRACTICE_BUTTON = PhotoImage(file="data/images/practice_button.png")
VS_BOTS_BUTTON = PhotoImage(file="data/images/grey_button.png")
CHALLENGES_BUTTON = PhotoImage(file="data/images/challenges_button.png")
MILESTONES_BUTTON = PhotoImage(file="data/images/milestones_button.png")
STATUS_BUTTON = PhotoImage(file="data/images/status_button.png")
START_BUTTON = PhotoImage(file="data/images/start_button.png")
MODE_BUTTON = PhotoImage(file="data/images/mode_button.png")
EXIT_BUTTON = PhotoImage(file="data/images/exit_button.png")


#TEST = (gamma=1,file="data/images/sprites/head_medium_skin.gif")

# Data calling
USER_SAVE1_NAME = data_calls.GameData.CallUserData("save1.mg","name")
USER_SAVE2_NAME = data_calls.GameData.CallUserData("save2.mg","name")
USER_SAVE3_NAME = data_calls.GameData.CallUserData("save3.mg","name")
USER_SAVE4_NAME = data_calls.GameData.CallUserData("save4.mg","name")

ROAMING_DATA = data_calls.trueOrFalseSave()

# augument variables

augumentVariable = { # Strangely you cannot update indervidule variables from functions but can do it with dictionaries.
    "indexAugument":  0,
    "saveFileAugument": ''
}
# game play variables
leftOperands = Operands.CreateQuestions()
rightOperands = Operands.CreateQuestions()
answerdQuestions = []
resultQuestions = []

# classes

class debugging():
    def printTest():
        print("This worked")



class MenuFunctions():

    interval = 0

    def CreateSave(saveFile,index):
        userName = Entry.get(textBox)
        ROAMING_DATA[index] = "true"
        data_calls.trueOrFalseSaveUpdate(ROAMING_DATA) # Converting the roaming data use refrence file to true.
        data_calls.GameData.WriteData(saveFile,"name",userName)
        Menus.PlayMenu()

    def PlayOrCreateSave(saveFile,roamingData,index):
        augumentVariable["indexAugument"] = index
        augumentVariable["saveFileAugument"] = saveFile

        if roamingData == "false":
            Menus.NewSave(saveFile)
        else:
            Menus.PlayMenu()

    def UpdateAnswer():
        """Update the interval variable and insert in the formula label for display for the purpose of iterating throught generated math questions. Note depends on a int variable named 'inteval' to function"""
        Label.config(formula, text= str(leftOperands[MenuFunctions.interval]) + "\n" + str(rightOperands[MenuFunctions.interval]))
        print(rightOperands)
        MenuFunctions.interval += 1
        if MenuFunctions.interval == len(leftOperands):
            MenuFunctions.CheckAnswers(MenuFunctions.interval - 1)
            MenuFunctions.interval = 0
            print(resultQuestions)
            Menus.Main()

    def RecordAnswer():
        answer = textBox.get()
        answerdQuestions.append(answer)
        MenuFunctions.UpdateAnswer()

    def CheckAnswers(number):
        for i in range(0,number):
            if float(answerdQuestions[i]) == float(leftOperands[i]) + float(rightOperands[i]):
                resultQuestions.append(f"{answerdQuestions[i]} Is correct")
            else:
                resultQuestions.append(f"{answerdQuestions[i]} Is incorrect the answer was {leftOperands[i] + rightOperands[i]}")

    def CancelCreateSave(index):
        ROAMING_DATA[index] = "false"
        data_calls.trueOrFalseSaveUpdate(ROAMING_DATA)
        Menus.SaveMenu()

class Menus():

    def Main(): # This is executed at the very bottom of the script to avoid all instantiations.
        Menus.PoolObjects()

        Frame.place(commentBox,x=360,y=80)

        # Labels
        Label.place(menuLabel, width=100,height=20,x=350,y=5)
        Label.config(menuLabel, text="Main Menu")

        Label.place(notAvailable, width=100,height=20,x=160,y=120)
        Label.place(notAvailable2, width=100,height=20,x=160,y=200)

        # Buttons
        Button.place(play, x=80,y=80)
        Button.place(leaderBoard,x=80,y=120)
        Button.place(information,x=80,y=160)
        Button.place(settings,x=80,y=200)
        Button.place(contact,x=80,y=240)
        Button.place(donate,x=80,y=280)
        root1.mainloop()


    def SaveMenu():
        Menus.PoolObjects()

        # Labels
        Label.place(menuLabel,width=100,height=20,x=350,y=5)
        

        Label.place(img,width=230,height=230,x=365,y=85)
        Label.place(spareLabel1,width=100,height=20,x=170,y=80)
        Label.place(spareLabel2,width=100,height=20,x=170,y=120)
        Label.place(spareLabel3,width=100,height=20,x=170,y=160)
        Label.place(spareLabel4,width=100,height=20,x=170,y=200)

        Label.config(spareLabel1,text=USER_SAVE1_NAME)
        Label.config(spareLabel2,text=USER_SAVE2_NAME)
        Label.config(spareLabel3,text=USER_SAVE3_NAME)
        Label.config(spareLabel4,text=USER_SAVE4_NAME)
        Label.config(menuLabel,text="Save Menu")

        # Buttons
        Button.place(save1,x=80,y=80)
        Button.place(save2,x=80,y=120)
        Button.place(save3,x=80,y=160)
        Button.place(save4,x=80,y=200)

        Button.place(mainMenuBack,x=80,y=320)

        root1.mainloop()

    def NewSave(saveFile): # parssing the file name refernce augument.
        Menus.PoolObjects()

        ## Labels
        Label.place(menuLabel,width=100,height=20,x=350,y=5)
        Label.config(menuLabel, text="New Save")

        # Entries
        
        Entry.place(textBox,width=100,height=40,x=350,y=120)

        # Bind the return key press event to get_entry_value function

        # Buttons
        Button.place(cancelBack,x=80,y=320)
        Button.place(conferm,x=640,y=320) # Saving data to the nmminated save file

        root1.mainloop()

    def PlayMenu():
        Menus.PoolObjects()
        

        # Labels
        Frame.place(commentBox,x=360,y=80)
        Label.place(menuLabel, width=100,height=20,x=350,y=5)
        Label.config(menuLabel, text="Play Menu")

        # Buttons
        Button.place(practice,x=80,y=80)
        Button.place(challenges,x=80,y=120)
        Button.place(vSBots,x=80,y=160)
        Button.place(status,x=80,y=200)
        Button.place(milestones,x=80,y=240)
        Button.place(settings,x=80,y=280)
        Button.place(saveMenuBack,x=80,y=320)


    def PracticeMenu():

        Menus.PoolObjects()

        

        answerdQuestions.clear()
        resultQuestions.clear()

        # Labels
        Label.config(menuLabel, text="Practice Menu", width=100,height=20)
        Label.place(menuLabel,x=350,y=5)


        # Buttons
        Button.place(playMenuBack,x=80,y=320)
        Button.place(start,x=80,y=80)

    def InformationMenu():
        Menus.PoolObjects()

        # Labels
        Label.place(menuLabel, width=100,height=20,x=350,y=5)
        Label.config(menuLabel,text="Information Menu")
        


    def QuestionsMenu(number,figures): # parssing the file name refernce augument.
        Menus.PoolObjects()

        MenuFunctions.UpdateAnswer()

        Label.place(menuLabel,width=100,height=20,x=350,y=5)
        Label.config(menuLabel,text="Questions Menu")

        Button.place(practiceMenuBack,x=80,y=320)
        Button.place(confermAnswer,x=640,y=320)# Saving data to the nmminated save file

        Label.place(formula,width=80,height=40,x=80,y=80)
    
        Entry.insert(textBox,index=0,string='')
        Entry.place(textBox,width=80,height=40,x=160,y=80)

        root1.mainloop()
        
        

    def PoolObjects():
        """Call this function to reset all known widgets on window. Calls widgets away from visability ready to be re called for visability"""

        ## Frames
        Frame.place(commentBox,x=-500,y=-500)

        # main menu widgets
        Label.place(notAvailable, width=100,height=20,x=-500,y=-500)
        Label.place(notAvailable2, width=100,height=20,x=-500,y=-500)
        Button.place(play,x=-500,y=-500)
        Button.place(leaderBoard,x=-500,y=-500)
        Button.place(information,x=-500,y=-500)
        Button.place(settings,x=-500,y=-500)
        Button.place(contact,x=-500,y=-500)
        Button.place(donate,x=-500,y=-500)

        # quetions menu widgets
        Button.place(practiceMenuBack,x=-500,y=-500)
        Label.place(formula,x=-500,y=-500)
        Button.place(confermAnswer,x=-500,y=-500)
        Label.place(formula,x=-500,y=-500)

        # play menu widgets
        
        Button.place(practice,x=-500,y=-500)
        Button.place(challenges,x=-500,y=-500)
        Button.place(vSBots,x=-500,y=-500)
        Button.place(status,x=-500,y=-500)
        Button.place(milestones,x=-500,y=-500)
        Button.place(settings,x=-500,y=-500)

        # new save menu widgtes

        # practice menu widgets
        Label.place(practiceMenu,x=-500,y=-500)
        Button.place(start,x=-500,y=-500)

        # save menu widgets      
        
        Label.place(img,width=230,height=230,x=-500,y=-500)

        Button.place(save1,x=-500,y=-500)
        Button.place(save2,x=-500,y=-500)
        Button.place(save3,x=-500,y=-500)
        Button.place(save4,x=-500,y=-500)

        # Entries
        Entry.place(textBox,x=-500,y=-500)

        # Conferm buttons
        Button.place(conferm,x=-500,y=-500)

        # back buttons
        Button.place(mainMenuBack,x=-500,y=-500)
        Button.place(cancelBack,x=-500,y=-500)
        Button.place(saveMenuBack,x=-500,y=-500)
        Button.place(playMenuBack,x=-500,y=-500)

        # Universal widgets
        Label.place(menuLabel,width=100,height=20,x=-500,y=-500)
        Label.place(spareLabel1,width=100,height=20,x=-500,y=-500) # Save Labels
        Label.place(spareLabel2,width=100,height=20,x=-500,y=-500)
        Label.place(spareLabel3,width=100,height=20,x=-500,y=-500)
        Label.place(spareLabel4,width=100,height=20,x=-500,y=-500)

    
## Intantiations.
content = Frame(root1).grid(column=0, row=0)
frame = Frame(borderwidth=5, relief="ridge", width=800, height=400).grid(column=0, row=0, columnspan=3, rowspan=2)
background = Label(image=BACKGROUND).place(x=0,y=0)
commentBox = Frame(borderwidth=5, width=240, height=240)

# Entries
textBox = Entry() # is global to window states.

# main menu widgets
play = Button(image=PLAY_BUTTON, command=Menus.SaveMenu)
leaderBoard = Button(image=LEADER_BOARD_BUTTON)
information = Button(image=INFOMATION_BUTTON)
settings = Button(image=SETTINGS_BUTTON)
contact = Button(image=CONTACT_BUTTON)
donate = Button(image=DONATE_BUTTON)
img = Label(text="you have done well,\nareas you may need improvment in are:\n\n\tAddition\n\tSubtraction")
mainMenu = Label(text="Main menu")
notAvailable = Label(background="black", foreground="white",text="Not Available")
notAvailable2 = Label(background="black", foreground="white",text="Not Available")

# Save Menu widgets
save1 = Button(command= lambda: MenuFunctions.PlayOrCreateSave(saveFile="save1.mg",roamingData=ROAMING_DATA[0],index=0),image=SAVE1_BUTTON)
save2 = Button(command= lambda: MenuFunctions.PlayOrCreateSave(saveFile="save2.mg",roamingData=ROAMING_DATA[1],index=1),image=SAVE2_BUTTON)
save3 = Button(command= lambda: MenuFunctions.PlayOrCreateSave(saveFile="save3.mg",roamingData=ROAMING_DATA[2],index=2),image=SAVE3_BUTTON)
save4 = Button(command= lambda: MenuFunctions.PlayOrCreateSave(saveFile="save4.mg",roamingData=ROAMING_DATA[3],index=3),image=SAVE4_BUTTON)


# new save menu widgets
conferm = Button(image=CONFIRM_BUTTON,command= lambda: MenuFunctions.CreateSave(augumentVariable["saveFileAugument"],index=augumentVariable["indexAugument"])) # Saving data to the nominated save file
cancelBack = Button(image=BACK_BUTTON,command= lambda: MenuFunctions.CancelCreateSave(augumentVariable["indexAugument"])) # TODO force a function to intantiate a variable outside the function to make this call possible

# play menu widgets
practice = Button(image=PRACTICE_BUTTON, command= Menus.PracticeMenu)
challenges = Button(image=CHALLENGES_BUTTON)
vSBots = Button(image=VS_BOTS_BUTTON)
status = Button(image=STATUS_BUTTON)
milestones = Button(image=MILESTONES_BUTTON)
settings = Button(image=SETTINGS_BUTTON)
start = Button(image=BACK_BUTTON,command = Menus.PracticeMenu)

# practice menu widgets
start = Button(image=START_BUTTON,command= lambda: Menus.QuestionsMenu(10,1000))
practiceMenu = Label(text="Practice Menu")

# questions menu widgets
confermAnswer = Button(image=CONFIRM_BUTTON,command=MenuFunctions.RecordAnswer)
formula = Label()


# Back Buttons
saveMenuBack = Button(image=BACK_BUTTON,command=Menus.SaveMenu)
mainMenuBack = Button(image=BACK_BUTTON,command = Menus.Main)
practiceMenuBack = Button(image=EXIT_BUTTON,command = Menus.PracticeMenu)
playMenuBack = Button(image=BACK_BUTTON,command = Menus.PlayMenu)

#Universal Widgets
menuLabel = Label(text="Questions Menu")

spareLabel1 = Label()
spareLabel2 = Label()
spareLabel3 = Label()
spareLabel4 = Label()
spareLabel5 = Label()
spareLabel6 = Label()


# scroll widgets


#MainMenu.__init__() # At the bottem
Menus.Main()