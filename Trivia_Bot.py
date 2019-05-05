#import pyautogui
import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser
from PIL import Image
from pytesseract import image_to_string
import os
import pyscreenshot as Imagegrab
import argparse
import cv2

hq=True
cs=False

hq_cords=(990,250,1550,960)
cs_cords=(990,230,1550,860)

def screen_grab(to_save):
        if hq==True:
                im = Imagegrab.grab(bbox=(hq_cords))
                im.save(to_save)
        elif cs==True:
                im = Imagegrab.grab(bbox=(cs_cords))
                im.save(to_save)
 

negative = False
remove_words = ["who",
    "what",
    "where",
    "when",
    "of",
    "that",
    "have",
    "for",
    "why",
    "the",
    "on",
    "with",
    "as",
    "this",
    "from",
    "they",
    "a",
    "an",
    "and",
    "are",
    "in",
    "to",
    "these",
    "is",
    "does",
    "which",
    "also",
    "it",
    "not",
    "we",
    "means",
    "you",
    "came",
    "come",
    "about",
    "if",
    "by",
    "from",
    "has",
    "was"]

def simplify(text):
        word_list=text.split()
        new_lst=[]
        for word in word_list:
                if word.lower() in remove_words:
                        pass
                else:
                        new_lst.append(word)
        return new_lst
                        
def readScreen():
    global answer1
    global answer2
    global answer3
    screenshot_file = "example6.jpg"
    screen_grab(screenshot_file)

    ap = argparse.ArgumentParser(description='HQ_Bot')
    ap.add_argument("-i", "--image", required=False,default=screenshot_file,help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])

    filename = "Screens/Question.png"
    filename2 = "Screens/Choice1.png"
    filename3 = "Screens/Choice2.png"
    filename4 = "Screens/Choice3.png"
    cv2.imwrite(filename, image)

    img = cv2.imread(filename)
    if hq == True:
            theQuestion = img[45:350, 15:580]
            firstAnswer = img[595:680,46:510]
            secondAnswer = img[487:565,46:510]
            thirdAnswer = img[385:470,46:510]
    elif cs == True:
            theQuestion = img[40:190, 15:570]
            firstAnswer = img[540:620,45:510]
            secondAnswer = img[420:500,45:510]
            thirdAnswer = img[300:380,45:510]

    cv2.imwrite(filename, theQuestion)
    text = image_to_string(Image.open(filename))
    cv2.imwrite(filename2, firstAnswer)
    cv2.imwrite(filename3, secondAnswer)
    cv2.imwrite(filename4, thirdAnswer)
    answer1 = image_to_string(Image.open(filename2))
    answer2 = image_to_string(Image.open(filename3))
    answer3 = image_to_string(Image.open(filename4))

    return text




def printResult():
        if edited == False:
                if choice0 > choice1 and choice0 > choice2:
                    print("MOST LIKELY: ", answerChoice[0].upper())
                    #most_likely = answerChoice[0].upper()
                    if choice1 > 0:
                            if (choice0 / choice1) < 1.35:
                                    print ("Close between "+answerChoice[0],"and "+answerChoice[1])
                    if choice2 > 0:
                            if (choice0 / choice2) < 1.35:
                                    print ("Close between "+answerChoice[0],"and "+answerChoice[2]) 
                elif choice1 > choice0 and choice1 > choice2:
                    print("MOST LIKELY: ", answerChoice[1].upper())
                    #most_likely = answerChoice[1].upper()
                    if choice0 > 0:
                            if (choice1 / choice0) < 1.35:
                                    print ("Close between "+answerChoice[1],"and "+answerChoice[0])
                    if choice2 > 0:
                            if (choice1 / choice2) < 1.35:
                                    print ("Close between "+answerChoice[1],"and "+answerChoice[2]) 
                elif choice2 > choice0 and choice2 > choice1:
                    print("MOST LIKELY: ", answerChoice[2].upper())
                    #most_likely = answerChoice[2].upper()
                    if choice0 > 0:
                            if (choice2 / choice0) < 1.35:
                                    print ("Close between "+answerChoice[2],"and "+answerChoice[0])
                    if choice1 > 0:
                            if (choice2 / choice1) < 1.35:
                                    print ("Close between "+answerChoice[2],"and "+answerChoice[1]) 
                else:
                    #most_likely = None
                    print("Aight bet, guess it nigga lmao")
                        
        else:
               print ("NOT Question")
               if choice0 < choice1 and choice0 < choice2:
                   print("MOST LIKELY: ", answerChoice[0].upper())
               elif choice1 < choice0 and choice1 < choice2:
                   print("MOST LIKELY: ", answerChoice[1].upper())
               elif choice2 < choice0 and choice2 < choice1:
                   print("MOST LIKELY: ", answerChoice[2].upper())
               else:
                   print("Aight bet, guess it nigga lmao")


def google(text):
        text=urllib.parse.quote_plus(text)
        url='https://google.com/search?q='+text
        response=requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

def bing(text):
       text=urllib.parse.quote_plus(text)
       url='https://bing.com/search?q='+text
       response=requests.get(url)
       soup = BeautifulSoup(response.text, 'lxml')
       return soup

if __name__ == "__main__":
    while(1):
        listofSites=[]
        listofSites2=[]
        listofSites3=[]
        listofSites4=[]
        listofSites5=[]
        listofSites6=[]
        question=''
        text_list=[]
        question_recording = True
        text2=''
        keypress = input('Press s to screen shot: ')
        if keypress == 's':
            text = readScreen()
            for char in text:
                text_list.append(char)
           
            for i in range(len(text_list)):
                if (text_list[i] == '\n' and text_list[i+1]=='\n') or (text_list[i] == '\n' and text_list[i+1]==' ') or (text_list[i] == ' ' and text_list[i+1]=='\n'):  
                    pass
                else:
                    text2+=text_list[i]
            text=text2
            for char in text:
                if question_recording==True:
                    if char =='?':
                        question+=char
                        question_recording=False
                                
                    elif char =='\n':
                        question+=(' ')
                    else:
                        question+=char
                else:
                    pass
        
                
        text = question
        print (text)
        edited=False
        if "NOT " in text or "not " in text or "EXCEPT " in text or "isn't " in text or "ISN'T " in text or "never " in text or "NEVER " in text:
                print ("NOT QUESTION")
                lst=[]
                string=''
                for char in text:
                        if char != ' ' and char != '?':
                                string+=char
                        else:
                                lst.append(string)
                                string = ''
                
                edited=True
                new_text=''
                for word in lst:
                        if word != "NOT " and word != "not " and word !="EXCEPT " and word != "isn't " and word != "ISN'T " and word != "never " and word != "NEVER ":
                                new_text+=word
                                new_text+=' '
                        else:
                                pass

        if edited == True:
                text=new_text
                
        answerChoice = [answer1, answer2, answer3]
        print(answerChoice)
        choice0 = 0
        choice1 = 0
        choice2 = 0
        for g in (google(text)).find_all(class_='g'):
                listofSites.append(g.text) 
                for site in listofSites:
                        for line in site.splitlines():
                                if (answerChoice[0]).lower() in line.lower():
                                        choice0+=1
                                if (answerChoice[1]).lower() in line.lower():
                                        choice1+=1
                                if (answerChoice[2]).lower() in line.lower():
                                        choice2+=1
        #for g in (bing(text)).find_all(class_='b_caption'):
        #     listofSites2.append(g.text)                               
        #     for site in listofSites:
        #                for line in site.splitlines():
        #                        if (answerChoice[0]).lower() in line.lower():
        #                                choice0+=1
        #                        if (answerChoice[1]).lower() in line.lower():
        #                                choice1+=1
        #                        if (answerChoice[2]).lower() in line.lower():
        #                                choice2+=1
        if choice0==choice1==choice2==0 or (edited==True and choice0==choice1==0) or (edited==True and choice1==choice2==0) or (edited==True and choice0==choice2==0):
                print ("RUNNING PLAN B")
                for g in (google(answerChoice[0])).find_all(class_='g'):
                        listofSites3.append(g.text) 
                        for site in listofSites3:
                            for line in site.splitlines():
                                for word in simplify(text):
                                    if word.lower() in line.lower():
                                        choice0+=1
                for g in (google(answerChoice[1])).find_all(class_='g'):
                        listofSites4.append(g.text) 
                        for site in listofSites4:
                             for line in site.splitlines():
                                 for word in simplify(text):
                                     if word.lower() in line.lower():
                                         choice1+=1
                for g in (google(answerChoice[2])).find_all(class_='g'):
                        listofSites5.append(g.text) 
                        for site in listofSites5:
                             for line in site.splitlines():
                                 for word in simplify(text):
                                     if word.lower() in line.lower():
                                         choice2+=1

        
        print('Instances of',answerChoice[0], ': ', choice0)
        print('Instances of', answerChoice[1], ': ', choice1)
        print('Instances of', answerChoice[2], ': ', choice2)
        print("--------")
        printResult()
        #secondkeypress = input('Press a to select primary choice: ')
        #if secondkeypress == 'a':
                #if most_likely == answerChoice[0]:
                        
                        




    

