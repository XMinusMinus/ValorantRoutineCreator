#version 0.02 - 6/20/2023
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import tkinter as tk
from tkinter import scrolledtext, END, messagebox
from tkinter.scrolledtext import *
from datetime import datetime
from time import sleep
import math
playername = ''
rank = ''
KD = 0
HS = 0
KAST = 0

def checkConditions(time):
    H = float(HS.replace('%', ''))
    K = float(KD.replace('%', ''))
    KASTthing = float(KAST.replace('%', ''))
    hours = float(time)
    E = H / K
    Z = E * KASTthing

    conditions = {
        (Z > E * 0.73, E > H): action1,
    (Z < E * 0.73, E < H): action2,
    (Z > E * 0.73, E == H): action2,
    (Z < E * 0.73, E == H): action2,
    (Z > E * 0.73, E < H): action3,
    (Z < E * 0.73, E > H): action3,
    (Z == E * 0.73, E == H): action3,
    (Z == E * 0.73, E > H): action4,
    (Z == E * 0.73, E < H): action5,
    }
    matching_condition = next((cond for cond, action in conditions.items() if cond), None)
    if matching_condition:
        conditions[matching_condition](hours)
    else:
        print("No matching condition found.")

def action1(hours):

    deathmatches = int((hours*0.3*60)//10)
    compmatches = int((hours*0.3*60)//45)
    vodReviewTime = compmatches/2
    aimtime = hours - (compmatches*45 + deathmatches*10 + math.ceil(vodReviewTime) * 45)/60

    if round(vodReviewTime, 2) % 1 == 0 and vodReviewTime >= 1:
        vodLabel.insert(tk.END, f'{round(vodReviewTime)} Match(s)')
    else:
        vodLabel.insert(tk.END, '1 Match')

    if round(aimtime, 2) % 1 == 0 and aimtime > 0:
        aimtrainLabel.insert(tk.END, f'{round(aimtime)} Hour(s)')
    else:
        aimtrainLabel.insert(tk.END, f'{round(aimtime)} Hours and {round((aimtime % 1)*60)} minutes')
    deathmatchLabel.insert(tk.END, f'{deathmatches} Deathmatches')
    compmatchesLabel.insert(tk.END, f'{compmatches} competitive matches')

def action2(hours):
    deathmatches = int((hours*0.15*60)//10)
    compmatches = int((hours*0.45*60)//45)
    vodReviewTime = compmatches/2
    aimtime = hours - (compmatches*45 + deathmatches*10 + math.ceil(vodReviewTime) * 45)/60

    if round(vodReviewTime, 2) % 1 == 0 and vodReviewTime >= 1:
        vodLabel.insert(tk.END, f'{round(vodReviewTime)} Match(s)')
    else:
        vodLabel.insert(tk.END, '1 Match')

    if round(aimtime, 2) % 1 == 0 and aimtime > 0:
        aimtrainLabel.insert(tk.END, f'{round(aimtime)} Hour(s)')
    else:
        aimtrainLabel.insert(tk.END, f'{round(aimtime)} Hours and {round((aimtime % 1)*60)} minutes')
    deathmatchLabel.insert(tk.END, f'{deathmatches} Deathmatches')
    compmatchesLabel.insert(tk.END, f'{compmatches} competitive matches')

def action3(hours):

    deathmatches = int((hours*0.2*60)//10)
    compmatches = int((hours*0.4*60)//45)
    vodReviewTime = compmatches/2
    aimtime = hours - (compmatches*45 + deathmatches*10 + math.ceil(vodReviewTime) * 45)/60

    if round(vodReviewTime, 2) % 1 == 0 and vodReviewTime >= 1:
        vodLabel.insert(tk.END, f'{round(vodReviewTime)} Match(s)')
    else:
        vodLabel.insert(tk.END, '1 Match')

    if round(aimtime, 2) % 1 == 0 and aimtime > 0:
        aimtrainLabel.insert(tk.END, f'{round(aimtime)} Hour(s)')
    else:
        aimtrainLabel.insert(tk.END, f'{round(aimtime)} Hours and {round((aimtime % 1)*60)} minutes')
    deathmatchLabel.insert(tk.END, f'{deathmatches} Deathmatches')
    compmatchesLabel.insert(tk.END, f'{compmatches} competitive matches')

def action4(hours):

    deathmatches = int((hours*0.35*60)//10)
    compmatches = int((hours*0.25*60)//45)
    vodReviewTime = compmatches/2
    aimtime = hours - (compmatches*45 + deathmatches*10 + math.ceil(vodReviewTime) * 45)/60

    if round(vodReviewTime, 2) % 1 == 0 and vodReviewTime >= 1:
        vodLabel.insert(tk.END, f'{round(vodReviewTime)} Match(s)')
    else:
        vodLabel.insert(tk.END, '1 Match')

    if round(aimtime, 2) % 1 == 0 and aimtime > 0:
        aimtrainLabel.insert(tk.END, f'{round(aimtime)} Hour(s)')
    else:
        aimtrainLabel.insert(tk.END, f'{round(aimtime)} Hours and {round((aimtime % 1)*60)} minutes')
    deathmatchLabel.insert(tk.END, f'{deathmatches} Deathmatches')
    compmatchesLabel.insert(tk.END, f'{compmatches} competitive matches')

def action5(hours):

    deathmatches = int((hours*0.25*60)//10)
    compmatches = int((hours*0.35*60)//45)
    vodReviewTime = compmatches/2
    aimtime = hours - (compmatches*45 + deathmatches*10 + math.ceil(vodReviewTime) * 45)/60

    if round(vodReviewTime, 2) % 1 == 0 and vodReviewTime >= 1:
        vodLabel.insert(tk.END, f'{round(vodReviewTime)} Match(s)')
    else:
        vodLabel.insert(tk.END, '1 Match')

    if round(aimtime, 2) % 1 == 0 and aimtime > 0:
        aimtrainLabel.insert(tk.END, f'{round(aimtime)} Hour(s)')
    else:
        aimtrainLabel.insert(tk.END, f'{round(aimtime)} Hours and {round((aimtime % 1)*60)} minutes')
    deathmatchLabel.insert(tk.END, f'{deathmatches} Deathmatches')
    compmatchesLabel.insert(tk.END, f'{compmatches} competitive matches')

def grabInfo(riot, time):
    global playername
    global rank
    global KD
    global HS
    global KAST
    options = Options()
    options.add_argument('--incognito')
    options.add_experimental_option('detach', True)
    options.add_argument('--headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
    driver.implicitly_wait(10)

    driver.get(f'https://tracker.gg/valorant/profile/riot/{riot}/overview')
    playername = driver.find_element('xpath', '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[1]/div[2]/div[2]/div[2]/span/span[1]').text
    rank = driver.find_element('xpath', '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]').text
    KD = driver.find_element('xpath', '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/span[2]').text
    HS = driver.find_element('xpath', '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[3]/div/div[2]/span[2]').text
    KAST = driver.find_element('xpath', '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div/div[2]/span[2]').text
    
    playernameLabel.insert(tk.END, playername)
    rankLabel.insert(tk.END, rank)
    kdLabel.insert(tk.END, KD)
    headshotLabel.insert(tk.END, HS)
    kastLabel.insert(tk.END, KAST)

    checkConditions(time)

    root.update()



def submitted():
    hours = 0
    minutes = 0
    if hoursForPractice.get('1.0', tk.END).strip() != '':
        hours = hoursForPractice.get('1.0', tk.END).strip()
    if minutesForPractice.get('1.0', tk.END).strip() != '':  
        minutes = minutesForPractice.get('1.0', tk.END).strip()
    time = int(hours) + (int(minutes)/60)
    text2 = riotId.get('1.0', tk.END).strip()
    text3 = text2.replace('#', '%23')
    text4 = text3.replace(' ', '%20')
    grabInfo(text4, time)



#Gui is from here down

root = tk.Tk()
root.geometry('500x800')
root.title('Valorant Routine Creator')

riotId = tk.Text(root, height = 1, width = 20)
riotId.place(x = 180, y = 5)
riotIdLabel = tk.Label(root, text='Riot ID:')
riotIdLabel.place(x = 137, y = 3)

submitButton = tk.Button(root, text = 'submit', font = ('Arial', 14, 'bold'), background = 'LightBlue', foreground = 'White',  command = submitted)
submitButton.place(x = 200, y = 60)

hoursForPractice = tk.Text(root, height = 1, width = 3)
hoursForPractice.place(x = 180, y = 30)
hoursForPracticeLabel = tk.Label(root, text='hours:')
hoursForPracticeLabel.place(x = 140, y = 28)

minutesForPractice = tk.Text(root, height = 1, width = 3)
minutesForPractice.place(x = 260, y = 30)
minutesForPracticeLabel = tk.Label(root, text='minutes:')
minutesForPracticeLabel.place(x = 210, y= 28)

timeForPracticeInfo = tk.Label(root, text = 'Time for practice:')
timeForPracticeInfo.place(x = 40, y = 28)

statsLabel = tk.Label(root, text = '--STATS--', font=('Arial', 50, 'bold'), foreground='red')
statsLabel.place(x=95, y = 100)

programLabel = tk.Label(root, text='--PLAN--', font=('Arial', 50, 'bold'), fg='red')
programLabel.place(x = 105, y = 330)

creditsLabel = tk.Label(root, text='--CREDITS--', font=('Arial', 50, 'bold'), fg='red')
creditsLabel.place(x = 55, y = 550)

creditsLabelOK = tk.Label(root, text='GUI/Main Script:\nxminusminus -Discord\nockoebe@gmail.com -email', font=('Arial', 14, 'bold'))
creditsLabelOK.place(x = 105, y = 650)

creditsLabelNB = tk.Label(root, text='Conceptualizer: \nfakewaffles -Discord', font=('Arial', 14, 'bold') )
creditsLabelNB.place(x = 145, y = 740)

class LabelMaker(tk.Label):
    def __init__(self, parent):
        self.parent = parent
    
    def create_label(self, text, x, y, **kwargs):
        label = tk.Label(self.parent, text=text, **kwargs)
        label.configure(font=('Arial', 16, 'bold'))
        label.place(x = x, y = y)
        textBox = tk.Entry(self.parent, width=30)
        textBox.place(x = x + 135, y = y+7)
        return textBox
        
playernameLabel = LabelMaker(root).create_label('Playername:', 10, 190)
rankLabel = LabelMaker(root).create_label('Rank:', 10, 220)
kdLabel = LabelMaker(root).create_label('Kill/Death:', 10, 250)
headshotLabel = LabelMaker(root).create_label('Headshot %:', 10, 280)
kastLabel = LabelMaker(root).create_label('KAST %:', 10, 310)

aimtrainLabel = LabelMaker(root).create_label('Aim Train:', 10, 420)
deathmatchLabel = LabelMaker(root).create_label('Deathmatch:', 10, 450)
compmatchesLabel = LabelMaker(root).create_label('Matches:', 10, 480)
vodLabel = LabelMaker(root).create_label('Vod Review:', 10, 510)



root.mainloop()
