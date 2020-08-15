#######################################################################################################################
# In this code I will be determining the settings required for a camera based on inputted settings from the user in   #
# in order to allow for an effective and high quality photo to be accomplished. This code can determine aperture,     #
# shutterspeed and ISO based off the inputs of the previous three, while maintining a steady baseline. If the lighting#
# condition is brighter, the baseline brightness decreases and vice versa. If a user enters values of which a         #
# brightness baseline cannot be achieved, the program will prompt the user to increase or decrease certain settings to#
# accommodate a brightness baseline which is sought. In addition, this code is formidable against erroneous user      #
# inputs and will not crash at the plight of receiving a false or ill-typed entry. Based on the user's input, the code#
# can recommend 1, 2 or 3 settings, depending on the user's preference. I have also used some object oriented         #
# programming in this code. Selecting the lighting condition is easier as the code allows the user to enter their city#
# or suburb to generate an automatic weather report and status in their area. The code outputs a GUI table for the    #
# user to view. They must close this window to continue the code. This may be something I would change in the future. #
#######################################################################################################################

#BY JOHN PEIRIS

#######################################################################################################################
#IMPORTS AND ERRORS
#IMPORTS
from tkinter import * #Used for table output
import time #Used for timing
import math #Used for math
import numpy as np #Used for table output
from prettytable import PrettyTable #Used for table output
import requests #Used for weather data
from pprint import pprint #Used for weather data
import os #Used for the code to talk
import sys #Used for the code to talk
import simpleaudio as sa #Used to play camera sound

#File Imports
import DICTIONARIES as Dic #Import dictionaries from my dictionaries file
import FUNCTIONS as Fn #Import functions from my functions file
from table import CreateTable #File/module which I created to make a table
import ADVANCED #Import my advanced code
import BASIC #Import my basic code

#######################################################################################################################
#INTRODUCTION AND CODE CHOICE
runagain = "Y" #Assign a runagain variable which can be used to determine if the user wants to run the code again.
print("Welcome to this photography settings Python code. Follow the prompts on the screen. Enjoy! :)") #Introduction to the code
time.sleep(1)
print("Here is a table of all the available settings. This will assist in choosing the correct ISO, shutterspeed and aperture.") #Prove the user with a table of all available settings. The user can refer to this later.
time.sleep(1)
Fn.availablesettings() #Runs the available settings function referenced above
time.sleep(1)
while runagain in "Y": #Initially, runagain is true, so the code runs once. If runagain still equals yes, it will "run again".
    Fn.WeatherGenerator() #Generate weather in the user's area. Help for the user to enter lighting condition.
    Fn.PlayCameraSound()
    lc = input("What is the lighting condition? (A number between 1 and 7)? [1 - Dusk, 2 - Sunset/shade, 3 - Overcast, 4 - Cloudy, 5 - Lightly cloudy, 6 - Sunny, 7 - Snow/sand]: ") #Ask the user to enter the lighting condition
    Fn.PlayCameraSound()
    allowedanswers = {'1', '2', '3', '4', '5', '6', '7'} #List of lighting condition reference numbers which are allowed
    while lc not in allowedanswers: #If the user entered a number that is not a referenced lighting condition, it will ask the user to re-enter the lighting condition. This stops errors.
        print("you did not enter a valid lighting condition. Please try again.") #Inform the user of their error
        time.sleep(1.5)
        lc = input("What is the lighting condition? (A number between 1 and 7)? [1 - Dusk, 2 - Sunset/shade, 3 - Overcast, 4 - Cloudy, 5 - Lightly cloudy, 6 - Sunny, 7 - Snow/sand]: ") #Ask the user a second time
        Fn.PlayCameraSound()
    lcr = int(Dic.lightresult.get(lc)) #Yields the stop totals to achieve a baseline from the referenced lighting condition
    allowanswers = {'1', '2', '3'} #Create a set of allowed answers for the next input
    AdvVsBas = input("Would you like to run an advanced code (A) or a basic code (B) with modes (A|B)? ").upper() #Advanced and basic code types. Make non-case-sensitive
    while AdvVsBas not in {'A', 'B'}: #If user input invalid
        print("You did not enter a valid input. Please try again.") #Inform the user of their error
        AdvVsBas = input("Would you like to run an advanced code (A) or a basic code (B) with modes (A|B)? ") #Ask the user again

#######################################################################################################################
#ADVANCED CODE WITH DETERMINING 1, 2 OR 3 SETTINGS

    if AdvVsBas in 'A':
        runagain = ADVANCED.adv(lcr, lc) #Advanced code with callable objects. Runagain is determined in this function
#######################################################################################################################
#BASIC CODE USING MODES
    elif AdvVsBas in 'B': #Running basic code with 3 modes
        runagain = BASIC.bas(lcr, lc) #Basic code with callable objects. Runagain is determined in this function

#######################################################################################################################

#ENDING OF CODE
Fn.ask_for_rating() #Asks the user to enter a rating.
print("Thank you for using this code. If you liked it, please rate 100%", "on rubric and Google reviews. Thank you for your compliance. Goodbye!") #Flatter the user
os.system('say "Thank you for using this code. Have a nice day!"')
Fn.PlayCameraSound()
Fn.PlayCameraSound()

#######################################################################################################################
####THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END####