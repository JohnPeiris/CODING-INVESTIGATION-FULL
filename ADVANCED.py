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

import FUNCTIONS as Fn #Imort functions from my functions file
from table import CreateTable #File/module which I created to make a table
import DICTIONARIES as Dic #Import dictionaries from Dictionaries file

def adv(lcr, lc): #Create def that can be used in another code
#######################################################################################################################
#ADVANCED CODE WITH DETERMINING 1, 2 OR 3 SETTINGS
    AdvVsBas = 'A' #Advanced mode has already been chosen
    if AdvVsBas in 'A':
        preferences = input("Would you like to determine 1, 2 or 3 settings: ") #Ask the user for how many settings they would like the program to determine
        Fn.PlayCameraSound()
        while preferences not in Dic.allowanswers: #If the user has entered a number not in the allowed list of answers for the input, they will have to keep re-entering their preference. This is a stage of error-handling
            print("You did not enter a valid setting type. Please try again.") #Inform the user of their error
            time.sleep(1.5)
            preferences = input("Would you like to determine 1, 2 or 3 settings: ") #Ask the user a second time
            Fn.PlayCameraSound()

#######################################################################################################################

#1 SETTING TO BE RECOMMENDED
        if preferences in "1": #One setting is to be recommended. I.e. two camera settings inputted by the user.
            setting = input("Which setting do you want the program to recommend (A number between 1 and 3)? [1 - ISO, 2 - Shutter speed, 3 - Aperture]: ") #Ask the user which camera setting they want the program to recommend.
            while setting not in Dic.allowanswers: #Allowed answers are 1, 2 and 3. If the user does not enter one of these numbers, they will have to keep re-entering until they do. This stops errors.
                print("You did not enter a valid setting type. Please try again.") #Inform the user of their error.
                time.sleep(1.5)
                setting = input("Which setting do you want the program to recommend (A number between 1 and 3)? [1 - ISO, 2 - Shutter speed, 3 - Aperture]: ") #Ask the user a second time

#######################################################################################################################

#FIRST CODE TYPE: DETERMINING ISO BY APERTURE AND SHUTTERSPEED SETTINGS
            if setting in '1': #ISO to be recommended
                verify = 'N' #To be used in next lines
                #The user will be asked if the information they entered is correct. If it is not, they will re-enter it:
                while verify in 'N':
                    shutterspeed = Fn.askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                    Fn.PlayCameraSound()
                    aperture = Fn.askaperture() #Sets aperture as the output of the function referenced above
                    Fn.PlayCameraSound()
                    while (lcr-int(Dic.shuuterspeedsettings.index(shutterspeed))-int(Dic.Aperturesettings.index(aperture))) < 0: #Calculate if the brightness created will be below baseline
                        print("The brightness this image will have is too low. It is recommended that you increase your shutterspeed and aperture settings by", abs(0-(lcr-int(Dic.shuuterspeedsettings.index(shutterspeed))-int(Dic.Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                        time.sleep(1.5)
                        shutterspeed = Fn.askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                        Fn.PlayCameraSound()
                        aperture = Fn.askaperture #Sets aperture as the output of the function referenced above
                        Fn.PlayCameraSound()
                    while (lcr-int(Dic.shuuterspeedsettings.index(shutterspeed))-int(Dic.Aperturesettings.index(aperture))) > 7: #Calculate if the brightness created will be above baseline
                        print("The brightness this image will have is too high. It is recommended that you decrease your shutterspeed and aperture settings by", abs(7-(lcr-int(Dic.shuuterspeedsettings.index(shutterspeed))-int(Dic.Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                        time.sleep(1.5)
                        shutterspeed = Fn.askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                        Fn.PlayCameraSound()
                        aperture = Fn.askaperture() #Sets aperture as the output of the function referenced above
                        Fn.PlayCameraSound()
                    print("You entered: Shutterspeed -",shutterspeed, ",", "Aperture -", aperture) #Inform the user what they entered.
                    verify = input("Is this correct? (Y | N) ") #Ask the user if the information they entered was correct.
                    Fn.PlayCameraSound()
                    verify.upper() #Format the user input.
                x = lcr-int(Dic.shuuterspeedsettings.index(shutterspeed))-int(Dic.Aperturesettings.index(aperture)) #Calculate the stops left to achieve a baseline.
                print("Your ISO setting should be set to", Dic.isosettings[x]) #Output the desired setting for the user
                Fn.PlayCameraSound()
                #Print the final settings:
                print("Final settings are:")
                time.sleep(1.5)
                print("Lighting condition:", Dic.lightingconditions.get(lc), " aperture setting:", aperture, " shutterspeed setting:", shutterspeed, "ISO setting:", Dic.isosettings[x])
                answerlist = [Dic.lightingconditions.get(lc), aperture, shutterspeed, Dic.isosettings[x]] #Create an answers list to be used by the generating answer table function
                Fn.PlayCameraSound()
                CreateTable(answerlist[3], answerlist[2], answerlist[1]) #Calls function to generate a table of answers from the answerlist. Function referenced above.() #Calls function to generate a table of answers from the answerlist. Function referenced above.
                Fn.PlayCameraSound()
                Fn.settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
                Fn.PlayCameraSound()
                runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
                Fn.PlayCameraSound()

#######################################################################################################################

#SECOND CODE TYPE: DETERMINING SHUTTERSPEED BY APERTURE AND ISO SETTINGS
            elif setting in '2': #Shutterspeed settings to be determined
                verify = 'N' #To be used in the following lines
                #The user will be asked if the information they entered is correct. If it is not, they will re-enter it:
                while verify in 'N':
                    ISO = Fn.askiso() #Sets ISO as the output of the function referenced above
                    Fn.PlayCameraSound()
                    aperture = Fn.askaperture() #Sets aperture as the output of the function referenced above
                    Fn.PlayCameraSound()
                    while (lcr-int(Dic.isosettings.index(ISO))-int(Dic.Aperturesettings.index(aperture))) < 0: #If the entered settings create a brightness below the baseline, ask the user to re-enter
                        print("The brightness this image will have is too low. It is recommended that you increase your ISO by", abs(0-(lcr-int(Dic.isosettings.index(ISO))-int(Dic.Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                        time.sleep(1.5)
                        ISO = Fn.askiso() #Sets ISO as the output of the function referenced above
                        Fn.PlayCameraSound()
                        aperture = Fn.askaperture() #Sets aperture as the output of the function referenced above
                        Fn.PlayCameraSound()
                    while (lcr-int(Dic.isosettings.index(ISO))-int(Dic.Aperturesettings.index(aperture))) > 7: #If the entered settings create a brightness above the baseline, ask the user to re-enter
                        print("The brightness this image will have is too high. It is recommended that you decrease your ISO by", abs(7-(lcr-int(Dic.isosettings.index(ISO))-int(Dic.Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                        time.sleep(1.5)
                        ISO = Fn.askiso() #Sets ISO as the output of the function referenced above
                        Fn.PlayCameraSound()
                        aperture = Fn.askaperture() #Sets aperture as the output of the function referenced above
                        Fn.PlayCameraSound()
                    print("You entered: ISO -",ISO, ",", "Aperture -", aperture) #Inform the user the settings they entered.
                    verify = input("Is this correct? (Y | N) ") #Ask the user if the settings they entered was correct.
                    Fn.PlayCameraSound()
                    verify.upper() #Format the user's input
                x = lcr-int(Dic.isosettings.index(ISO))-int(Dic.Aperturesettings.index(aperture)) #Calculate the number of stops required to reach the baseline brightness
                print("Your shutterspeed setting should be set to", Dic.shuuterspeedsettings[x]) #Print the shutterspeed setting determined
                Fn.PlayCameraSound()
                #Output final settings:
                print("Final settings are:")
                time.sleep(1.5)
                print("Lighting condition:", Dic.lightingconditions.get(lc), " aperture setting:", aperture, " shutterspeed setting:", Dic.shuuterspeedsettings[x], "ISO setting:", ISO)
                answerlist = [Dic.lightingconditions.get(lc), aperture, Dic.shuuterspeedsettings[x], ISO] #Create an answers list to be used by the generating answer table function
                Fn.PlayCameraSound()
                CreateTable(answerlist[3], answerlist[2], answerlist[1]) #Calls function to generate a table of answers from the answerlist. Function referenced above.() #Calls function to generate a table of answers from the answerlist. Function referenced above.
                Fn.PlayCameraSound()
                Fn.settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
                Fn.PlayCameraSound()
                runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
                Fn.PlayCameraSound()

#######################################################################################################################

#THIRD CODE TYPE: DETERMINING APERTURE BY ISO AND SHUTTERSPEED SETTINGS
            elif setting in '3': #Aperture setting to be determined
                verify = 'N' #To be used in following lines
                #The user will be asked if the information they entered is correct. If it is not, they will re-enter it:
                while verify in 'N':
                    ISO = Fn.askiso() #Sets ISO as the output of the function referenced above
                    Fn.PlayCameraSound()
                    shutterspeed = Fn.askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                    Fn.PlayCameraSound()
                    while (lcr-int(Dic.shuuterspeedsettings.index(shutterspeed))-int(Dic.isosettings.index(ISO))) < 0: #If the entered settings create a brightness below the baseline, ask the user to re-enter
                        print("The brightness this image will have is too low. It is recommended that you increase your ISO or shutterspeed by a total of", abs(0-(lcr-int(Dic.shuuterspeedsettings.index(shutterspeed))-int(Dic.isosettings.index(ISO)))), "stop(s).") #Inform the user of the error created
                        time.sleep(1.5)
                        ISO = Fn.askiso() #Sets ISO as the output of the function referenced above
                        Fn.PlayCameraSound()
                        shutterspeed = Fn.askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                        Fn.PlayCameraSound()
                    while (lcr-int(Dic.isosettings.index(ISO))-int(Dic.shuuterspeedsettings.index(shutterspeed))) > 7: #If the entered settings create a brightness above the baseline, ask the user to re-enter
                        print("The brightness this image will have is too high. It is recommended that you decrease your ISO or shutterspeed by a total of", abs((9-(lcr-int(Dic.shuuterspeedsettings.index(shutterspeed))-int(Dic.isosettings.index(ISO))))), "stop(s).") #Inform the user of the error created
                        time.sleep(1.5)
                        ISO = Fn.askiso() #Sets ISO as the output of the function referenced above
                        Fn.PlayCameraSound()
                        shutterspeed = Fn.askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                        Fn.PlayCameraSound()
                    print("You entered: Shutterspeed -",shutterspeed, ",", "ISO -", ISO) #Inform the user of their entered settings
                    verify = input("Is this correct? (Y | N) ") #Ask the user if the information they entered is correct
                    Fn.PlayCameraSound()
                    verify.upper() #Format the verification answer
                    x = lcr-int(Dic.isosettings.index(ISO))-int(Dic.shuuterspeedsettings.index(shutterspeed)) #Calculate the number of stops remaining to achieve a baseline brightness
                    apertureanswer = Dic.Aperturesettings[x] #Output the desired setting
                #Outputting final answer
                print("Your aperture setting should be set to", apertureanswer)
                Fn.PlayCameraSound()
                print("Final settings are:")
                time.sleep(1.5)
                print("Lighting condition:", Dic.lightingconditions.get(lc), " aperture setting:", apertureanswer, " shutterspeed setting:", shutterspeed, "ISO setting:", ISO)
                answerlist = [Dic.lightingconditions.get(lc), apertureanswer, shutterspeed, ISO] #Create an answers list to be used by the generating answer table function
                Fn.PlayCameraSound()
                #Generate table of settings for the user
                CreateTable(answerlist[3], answerlist[2], answerlist[1]) #Calls function to generate a table of answers from the answerlist. Function referenced above.() #Calls function to generate a table of answers from the answerlist. Function referenced above.
                Fn.PlayCameraSound()
                Fn.settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
                Fn.PlayCameraSound()
                runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
                Fn.PlayCameraSound()

#######################################################################################################################

#2 SETTINGS TO BE RECOMMENDED
        elif preferences in "2": #Two settings to be recommended
            setting = input("Which setting do you want to enter into the program (A number between 1 and 3)? [1 - ISO, 2 - Shutter speed, 3 - Aperture]: ") #Ask the user for the setting they want to enter
            Fn.PlayCameraSound()
            while setting not in Dic.allowanswers: #If the user did not enter a valid input, ask again
                print("You did not enter a valid setting type. Please try again.")
                time.sleep(1.5)
                setting = input("Which setting do you want to enter into the program (A number between 1 and 3)? [1 - ISO, 2 - Shutter speed, 3 - Aperture]: ")
            Fn.PlayCameraSound()

#######################################################################################################################

#ISO INPUTTED
            if setting in '1': #ISO inputted -> Determining shutterspeed and aperture
                ISO = Fn.askiso() #Sets ISO as the output of the function referenced above
                while (lcr - (Dic.isosettings.index(ISO))) < 0: #If the setting entered creates a brightness below the baseline brightness for the lighting condition, inform the user and ask again
                    print("The entered ISO setting is too low. Please increase by", (0-lcr+Dic.isosettings.index(ISO)), "stops") #Inform the user of the error created and how they should change their setting
                    ISO = Fn.askiso() #Sets ISO as the output of the function referenced above
                    Fn.PlayCameraSound()
                while (lcr - (Dic.isosettings.index(ISO))) > 14: #If the setting entered creates a brightness above the baseline brightness for the lighting condition, inform the user and ask again
                    print("The entered ISO setting is too high. Please decrease by", abs(14-lcr+Dic.isosettings.index(ISO)), "stops") #Inform the user of the error created and how they should adjust their setting
                    ISO = Fn.askiso() #Sets ISO as the output of the function referenced above
                    Fn.PlayCameraSound()
                x = int((lcr-Dic.isosettings.index(ISO))/2) #Calculate the stops remaining and divide it between the two settings remaining
                y = lcr - Dic.isosettings.index(ISO) - x #Calculate the stops remaining and divide it between the two settings remaining
                #Output final settings:
                print("Final settings are:")
                time.sleep(1.5)
                print("Lighting condition:", Dic.lightingconditions.get(lc), " aperture setting:", Dic.Aperturesettings[x], " shutterspeed setting:", Dic.shuuterspeedsettings[y], "ISO setting:", ISO)
                answerlist = [Dic.lightingconditions.get(lc), Dic.Aperturesettings[x], Dic.shuuterspeedsettings[y], ISO] #Create an answers list to be used by the generating answer table function
                Fn.PlayCameraSound()
                #Generate table of settings for the user
                CreateTable(answerlist[3], answerlist[2], answerlist[1]) #Calls function to generate a table of answers from the answerlist. Function referenced above.() #Calls function to generate a table of answers from the answerlist. Function referenced above.
                Fn.PlayCameraSound()
                Fn.settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
                Fn.PlayCameraSound()
                runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
                Fn.PlayCameraSound()

#######################################################################################################################

#SHUTTERSPEED INPUTTED
            elif setting in '2': #Shutter speed inputted -> Determining ISO and aperture settings
                shutterspeed = Fn.askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                Fn.PlayCameraSound()
                while (lcr - (Dic.shuuterspeedsettings.index(shutterspeed))) < 0: #If the entered setting creates a brightness below the baseline brightness for that lighting condition, ask again
                    print("The entered shutterspeed setting is too high. Please decrease by", (0-lcr+Dic.shuuterspeedsettings.index(shutterspeed)), "stops") #Inform the user of the error created and how they should adjust the settings
                    shutterspeed = Fn.askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                    Fn.PlayCameraSound()
                while (lcr - (Dic.shuuterspeedsettings.index(shutterspeed))) > 14: #If the entered setting creates a brightness above the baseline brightness for that lighting condition, ask again
                    print("The entered shutterspeed setting is too low. Please increase by", abs(14-lcr+Dic.shuuterspeedsettings.index(shutterspeed)), "stops") #Inform the user of the error created and how they should adjust the settings
                    shutterspeed = Fn.askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                    Fn.PlayCameraSound()
                    x = int((lcr-Dic.shuuterspeedsettings.index(shutterspeed))/2) #Calculate the stops remaining and divide it between the two settings remaining
                    y = lcr - Dic.shuuterspeedsettings.index(shutterspeed) - x #Calculate the stops remaining and divide it between the two settings remaining
                x = int((lcr-Dic.shuuterspeedsettings.index(shutterspeed))/2) #Calculate the stops remaining and divide between the 2 remaining settings (ISO and aperture)
                y = lcr - Dic.shuuterspeedsettings.index(shutterspeed) - x #Calculate the stops remaining and divide between the 2 remaining settings (ISO and aperture)
                #Output final settings:
                print("Final settings are:")
                time.sleep(1.5)
                print("Lighting condition:", Dic.lightingconditions.get(lc), " aperture setting:", Dic.Aperturesettings[x], " shutterspeed setting:", shutterspeed, "ISO setting:", Dic.isosettings[y])
                answerlist = [Dic.lightingconditions.get(lc), Dic.Aperturesettings[x], shutterspeed, Dic.isosettings[y]] #Create an answers list to be used by the generating answer table function
                Fn.PlayCameraSound()
                #Generate table of settings for the user
                CreateTable(answerlist[3], answerlist[2], answerlist[1]) #Calls function to generate a table of answers from the answerlist. Function referenced above.() #Calls function to generate a table of answers from the answerlist. Function referenced above.
                Fn.PlayCameraSound()
                Fn.settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
                Fn.PlayCameraSound()
                runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
                Fn.PlayCameraSound()

#######################################################################################################################

#APERTURE INPUTTED
            elif setting in '3': #Aperture inputted -> Determining shutterspeed and ISO settings
                aperture = Fn.askaperture() #Sets aperture as the output of the function referenced above
                Fn.PlayCameraSound()
                while (lcr - (Dic.Aperturesettings.index(aperture))) < 0: #If the entered setting creates a brightness below the baseline brightness for that lighting condition, ask the user to re-enter
                    print("The entered aperture setting is too high. Please decrease by", (0-lcr+Dic.Aperturesettings.index(aperture)), "stops") #Inform the user of the error created and how they should adjust their settings
                    aperture = Fn.askaperture() #Sets aperture as the output of the function referenced above
                    Fn.PlayCameraSound()
                while (lcr - (Dic.Aperturesettings.index(aperture))) > 14: #If the entered setting creates a brightness above the baseline brightness for that lighting condition, ask the user to re-enter
                    print("The entered aperture setting is too low. Please increase by", (14-lcr+Dic.Aperturesettings.index(aperture)), "stops") #Inform the user of the error created and how they should adjust their settings
                    aperture = Fn.askaperture() #Sets aperture as the output of the function referenced above
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
                CreateTable(answerlist[3], answerlist[2], answerlist[1]) #Calls function to generate a table of answers from the answerlist. Function referenced above.() #Calls function to generate a table of answers from the answerlist. Function referenced above.
                Fn.PlayCameraSound()
                Fn.settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
                Fn.PlayCameraSound()
                runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
                Fn.PlayCameraSound()

#######################################################################################################################

#3 SETTINGS TO BE RECOMMENDED
        elif preferences in "3": #Three settings to be recommended based off the lighting condition advised by the user.
            print("ISO:", Dic.isosettings[8-int(lc)],  " Shutterspeed:", Dic.shuuterspeedsettings[8-int(lc)], " Aperture:", Dic.Aperturesettings[8-int(lc)] ) #Calculate the number of stops needed to achieve a stable baseline and print the settings for ISO, shutterspeed and aperture
            answerlist = [Dic.lightingconditions.get(lc), Dic.Aperturesettings[8-int(lc)], Dic.shuuterspeedsettings[8-int(lc)], Dic.isosettings[8-int(lc)]] #Create an answers list to be used by the generating answer table function
            Fn.PlayCameraSound()
            #Generate table of settings for the user
            CreateTable(answerlist[3], answerlist[2], answerlist[1]) #Calls function to generate a table of answers from the answerlist. Function referenced above.() #Calls function to generate a table of answers from the answerlist. Function referenced above.
            Fn.PlayCameraSound()
            Fn.settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
            Fn.PlayCameraSound()
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
            Fn.PlayCameraSound()
        return runagain #Return the runagain value to the normal code