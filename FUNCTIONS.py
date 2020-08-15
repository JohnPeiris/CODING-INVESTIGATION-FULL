'''
ALL FUNCTIONS USED IN WHOLE CODE
Create functions that can be used in another code
'''
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

#######################################################################################################################
#PLAYING CAMERA SOUND FUNCTION
def PlayCameraSound(): #Creates a function to play a camera sound which can be used later
    filename = '/Users/Joel/Downloads/camera-shutter-click-06.wav' #Setting the filename
    wave_obj = sa.WaveObject.from_wave_file(filename) #Converts wave file to audio and processes it
    play_obj = wave_obj.play() #Plays processed file

#######################################################################################################################
#HOW TO SET CAMERA SETTINGS VIDEO FUNCTION
def settingvid():
    showvid = str(input("Would you like to see how to set ISO, shutterspeed and aperture (Y | N)? ")) #Ask the user if they want to see a video to help them
    while showvid not in ["Y", "N"]: #If the user did not enter yes or no, ask again
        print("You did not enter a valid input. Please try again.") #Inform the user of their error
        time.sleep(1)
        showvid = str(input("Would you like to see how to set ISO, shutterspeed and aperture? (Y | N)")) #Ask the user if they want to see a video to help them
    if showvid in "Y": #The user wants to see a video on how to set ISO, shutterspeed and aperture
        import webbrowser #Import the module to open a url
        webbrowser.open('https://www.youtube.com/watch?v=6_B8pVoANyY') #Open a youtube video on how to set shutterspeed, ISO and aperture
        print("Happy photography! :)")
    elif showvid in "N": #The user does not want to see how to set their camera settings
        print("Happy photography! :)")

#######################################################################################################################
#GETTING WEATHER DATA
def WeatherGenerator():
    city = str(input("What city/suburb do you live in? This can generate weather reports and help determine settings and the lighting condition. If you do not want to enter this, type N: ")) #Ask the user to enter their city to determine weather. If the user does not want to, they can type N.
    def weather_data(query): #Java code to open a link and open the java code of it.
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
        return res.json();
    def print_weather(result,city): #Java code to access weather data from the Java code of the website
        print("{}'s temperature: {}°C ".format(city,result['main']['temp'])) #Temperature in the city
        time.sleep(0.5)
        print("Description: {}".format(result['weather'][0]['description'])) #Description of the city
        time.sleep(0.5)
        print("Weather: {}".format(result['weather'][0]['main'])) #Weather of the city
    def main():
        if city == 'N' or city == 'n': #The user does not want to disclose their city
            print("Okay. Your privacy is acknowledged.") #Accept their chose
        else: #The user will enter their city
            try: #Try to find the city. If it is not found, an error will not throw
                query='q='+city; #To open link, the city name becomes part of it
                w_data=weather_data(query); #Runs the weather_data(query) (referenced above) to access weather data on the website
                print_weather(w_data, city) #Runs the print_weather function to print the weather attributes in that area which are accessed from the website
            except: #If the city was not found, inform the user.
                print('City name not found...') #Inform the user that the city was not found
    main()

#######################################################################################################################
#TABLE FUNCTION OF AVAILABLE SETTINGS
def availablesettings(): #Creating a table of available settings. This function can be called upon later.
    x = PrettyTable() #Creates a table

    column_names = ["Stop Number:", "ISO Settings", "Shutterspeed Settings", "Aperture settings"] #Adds setting names to the table

    x.add_column(column_names[0], ["8th", "7th", "6th", "5th", "4th", "3rd", "2nd", "1st"]) #Adds the stop number column to the table
    x.add_column(column_names[1], ["6400", "3200","1600","800","400","200","100","50"]) #Adds the ISO settings column to the table
    x.add_column(column_names[2], ['1/30s', '1/60s', '1/125s', '1/250s', '1/500s', '1/1000s', '1/2000s', '1/4000s']) #Adds the shutterspeed settings column to the table
    x.add_column(column_names[3], ["f/2.0","f/2.8","f/4.0", "f/5.6","f/8.0","f/11","f/16","f/22"]) #Adds the aperture settings column to the table

    print(x) #Prints the table

#######################################################################################################################
#FUNCTION TO GENERATE A TABLE OF RESULTS FOR THE RECOMMENDED SETTINGS
def gentable(): #Creates a function for creating tables which can be used later. This saves many lines of code.
    from table import CreateTable #File/module which I created to make a table (286 lines in table file)
    CreateTable(answerlist[3], answerlist[2], answerlist[1]) #Uses table function within a module I created to generate a table

#######################################################################################################################
#FUNCTION TO ASK ISO
def askiso(): #Creates a function of asking and verifying ISO. This saves many lines of code
    ISO = str(input("Please enter the ISO setting (e.g. 800): ")) #Ask the user to enter the ISO setting
    while ISO not in Dic.isosettings: #If the ISO setting entered is not in the allowed ISO setting list, ask the user to re-enter
        print("You did not enter a valid ISO setting. Please try again.") #Inform the user of their error.
        time.sleep(1.5)
        ISO = str(input("Please enter the ISO setting (e.g. 800): ")) #Ask the user to re-enter the ISO setting
    return ISO #Returns the user's ISO

#######################################################################################################################
#FUNCTION TO ASK SHUTTERSPEED
def askshutterspeed(): #Creates a function of asking and verifying shutterspeed. This saves many lines of code
    shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000s): ")) #Ask the user to enter the shutterspeed setting
    while shutterspeed not in Dic.shuuterspeedsettings: #If the user entered a setting that is not an EXISTING SETTING, the user will be asked to re-enter.
        print("You did not enter a valid shutterspeed setting. Please try again.") #Inform the user of their error
        time.sleep(1.5)
        shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000s): ")) #Ask the user a second time
    return shutterspeed #Returns the user's shutterspeed

#######################################################################################################################
#FUNCTION TO ASK APERTURE
def askaperture(): #Creates a function of asking and verifying aperture. This saves many lines of code
    aperture = str(input("Please enter the aperture setting (in the form f/16): ")) #Ask the user to enter the aperture setting
    while aperture not in Dic.Aperturesettings: #If the user entered a setting that is not an EXISTING SETTING, the user will be asked to re-enter.
        print("You did not enter a valid aperture setting. Please try again.") #Inform the user of their error
        time.sleep(1.5)
        aperture = str(input("Please enter the aperture setting (in the form f/16): ")) #Ask the user a second time
    return aperture #Returns the user's aperture

#######################################################################################################################
#FUNCTION TO ASK FOR A RATING AFTER THE USER USES IT
def ask_for_rating(): #Creates a function
    rating = input("Did you like this code? If so, please rate out of 5 stars. If you do not want to rate, type N: ") #Asks the user to enter a rating
    if rating in "N": #if the user does not want to enter a rating, they can type N.
        print("Thank you :)") #Thanks the user
    else:
        f = open('/Users/Joel/OneDrive - education.wa.edu.au/Ratings.txt') #Opens a rating text file to store ratings by the user
        f.write(rating) #Writes in the text file the rating the user enters
        print("Thank you :)") #Thanks the user
