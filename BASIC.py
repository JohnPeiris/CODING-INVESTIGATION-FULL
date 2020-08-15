#IMPORTS
from tkinter import * #Used for table output
import time #Used for timing
import math #Used for math
from collections import OrderedDict #Used for ordering dictionaries
from PIL import Image #Used for image generation
import matplotlib.pyplot as plt; plt.rcdefaults() #Used for table output
import numpy as np #Used for table output
import matplotlib.pyplot as plt #Used for table output
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

def bas(lcr, lc): #Create def that can be used in another code
#######################################################################################################################
#BASIC CODE USING MODES
    AdvVsBas = 'B' #Run the basic code
    if AdvVsBas in 'B': #Running basic code with 3 modes
        mode_type = input("What mode would you like to run? (1 - Portrait, 2 - Landscape, 3 - sport): ") #Ask the user what mode they would like to use
        while mode_type not in ('1', '2', '3'): #While a valid mode type has not been selected, ask the user again
            print("You must choose a mode of 1, 2 or 3.") #inform the user of the error
            mode_type = input("What mode would you like to run? (1 - Portrait, 2 - Landscape, 3 - sport): ") #Ask the user again
        if mode_type in '1': #Portrait mode
            aperture = 'f/2.0' #Set aperture to lowest possible for portrait mode in low depth of field
            while (lcr - (Dic.Aperturesettings.index(aperture))) > 14: #If the entered setting creates a brightness above the baseline brightness for that lighting condition, ask the user to re-enter
                aperture = Dic.Aperturesettings[int(Dic.Aperturesettings.index(aperture))+1] #Decreases the aperture by 1 for image brightness
                Fn.PlayCameraSound()
            x = int((lcr-Dic.Aperturesettings.index(aperture))/2) #Calculate the stops remaining to achieve a baseline brightness and divide it between the 2 remaining settings (ISO and shutterspeed)
            y = lcr - Dic.Aperturesettings.index(aperture) - x #Calculate the stops remaining to achieve a baseline brightness and divide it between the 2 remaining settings (ISO and shutterspeed)
            #Output final settings:
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", Dic.lightingconditions.get(lc), " aperture setting:", aperture, " shutterspeed setting:", Dic.shuuterspeedsettings[y], "ISO setting:", Dic.isosettings[x])
            answerlist = [Dic.lightingconditions.get(lc), aperture, Dic.shuuterspeedsettings[y], Dic.isosettings[x]] #Create an answers list to be used by the generating answer table function
            Fn.PlayCameraSound()
            #Generate table of settings for the user
            CreateTable(answerlist[3], answerlist[2], answerlist[1]) #Calls function to generate a table of answers from the answerlist. Function referenced above.() #Calls function to generate a table of answers from the answerlist. Function referenced above. #Calls function to generate a table of answers from the answerlist. Function referenced above.
            Fn.PlayCameraSound()
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
            Fn.PlayCameraSound()
        elif mode_type in '2': #Landscape mode
            aperture = 'f/22' #Set aperture to highest possible for landscape mode
            while (lcr - (Dic.Aperturesettings.index(aperture))) > 14: #If the entered setting creates a brightness above the baseline brightness for that lighting condition, ask the user to re-enter
                aperture = Dic.Aperturesettings[int(Dic.Aperturesettings.index(aperture))-1] #Decreases the aperture by 1 for image brightness
                Fn.PlayCameraSound()
            x = int((lcr-Dic.Aperturesettings.index(aperture))/2) #Calculate the stops remaining to achieve a baseline brightness and divide it between the 2 remaining settings (ISO and shutterspeed)
            y = lcr - Dic.Aperturesettings.index(aperture) - x #Calculate the stops remaining to achieve a baseline brightness and divide it between the 2 remaining settings (ISO and shutterspeed)
            #Output final settings:
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", Dic.lightingconditions.get(lc), " aperture setting:", aperture, " shutterspeed setting:", Dic.shuuterspeedsettings[y], "ISO setting:", Dic.isosettings[x])
            answerlist = [Dic.lightingconditions.get(lc), aperture, Dic.shuuterspeedsettings[y], Dic.isosettings[x]] #Create an answers list to be used by the generating answer table function
            Fn.PlayCameraSound()
            #Generate table of settings for the user
            CreateTable(answerlist[3], answerlist[2], answerlist[1]) #Calls function to generate a table of answers from the answerlist. Function referenced above.() #Calls function to generate a table of answers from the answerlist. Function referenced above. #Calls function to generate a table of answers from the answerlist. Function referenced above.
            Fn.PlayCameraSound()
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
            Fn.PlayCameraSound()
        elif mode_type in '3': #Sport mode
            shutterspeed = '1/4000s' #Set shutterspeed to fastest for low motion blur in sport mode
            while (lcr - (Dic.shuuterspeedsettings.index(shutterspeed))) < 0: #If the entered setting creates a brightness below the baseline brightness for that lighting condition, ask again
                shutterspeed = Dic.shuuterspeedsettings[int(Dic.shuuterspeedsettings.index(shutterspeed))-1] #Keep decreasing by 1 until a brightness of baseline is achieved with the highest possible shutterspeed
                Fn.PlayCameraSound()
            x = int((lcr-Dic.shuuterspeedsettings.index(shutterspeed))/2) #Calculate the stops remaining and divide between the 2 remaining settings (ISO and aperture)
            y = lcr - Dic.shuuterspeedsettings.index(shutterspeed) - x #Calculate the stops remaining and divide between the 2 remaining settings (ISO and aperture)
            #Output final settings:
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", Dic.lightingconditions.get(lc), " aperture setting:", Dic.Aperturesettings[x], " shutterspeed setting:", shutterspeed, "ISO setting:", Dic.isosettings[y])
            answerlist = [Dic.lightingconditions.get(lc), Dic.Aperturesettings[x], shutterspeed, Dic.isosettings[y]] #Create an answers list to be used by the generating answer table function
            Fn.PlayCameraSound()
            #Generate table of settings for the user
            CreateTable(answerlist[3], answerlist[2], answerlist[1]) #Calls function to generate a table of answers from the answerlist. Function referenced above.() #Calls function to generate a table of answers from the answerlist. Function referenced above. #Calls function to generate a table of answers from the answerlist. Function referenced above.
            Fn.PlayCameraSound()
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
            Fn.PlayCameraSound()
        return runagain #Return the runagain value to the normal code
