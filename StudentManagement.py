# 1st- Main Menu , 2nd- Add, 3rd- Remove, 4th- Update, 5th- View, 6th- exit ((( 1D Array ))) || Deadline(08/10/21)

import os
from colorama import Fore,Style
from print_color import print
import time
os.system("cls")
import Arnab

def Checking(ROLL):
    for l in range(len(u_Roll)):
      if(u_Roll[l] == ROLL):
        return True
      else:
        return False

def UserRoll(ROLL):
  for l in range(len(u_Roll)):
    if(u_Roll[l] == ROLL):
      return int(l)
    else:
      return False

def ADD():
  os.system("cls")
  print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"----------------------------------- "+Fore.LIGHTGREEN_EX+"ADD STUDENTS"+Fore.LIGHTBLUE_EX+Style.BRIGHT+" -----------------------------------"+Style.RESET_ALL)
  ROLL = input(Fore.LIGHTYELLOW_EX+Style.DIM+"\tRoll_No: "+Style.RESET_ALL)
  if(not Checking(ROLL)):
    u_Roll.append(ROLL)
    u_Name.append(input(Fore.LIGHTYELLOW_EX+Style.DIM+"\tName: "+Style.RESET_ALL))
    u_Age.append(input(Fore.LIGHTYELLOW_EX+Style.DIM+"\tAge: "+Style.RESET_ALL))
    u_Course.append(input(Fore.LIGHTYELLOW_EX+Style.DIM+"\tCourse: "+Style.RESET_ALL))
    print('')
    print("New Student is added.",tag='Success',tag_color='green',color='white')
    time.sleep(2)
    os.system("cls")
  else:
    print("Student data is already in records.",tag='Record Exists',tag_color='green',color='white')
    time.sleep(2)
    os.system("cls")
  return 0


def Update():
    os.system("cls")
    print(Fore.LIGHTBLUE_EX+Style.BRIGHT+">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "+Fore.GREEN+Style.BRIGHT+"UPDATED"+Fore.LIGHTBLUE_EX+Style.BRIGHT+" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"+Style.RESET_ALL+"\n")
    ROLL = input(Fore.LIGHTCYAN_EX+"Enter Roll no of the student: "+Style.RESET_ALL)
    print('')
    if(Checking(ROLL)):
      ROLL = UserRoll(ROLL)
      u_Name [ROLL] = input(Fore.BLUE+Style.BRIGHT+"\tWhat is your Name: "+Style.RESET_ALL)
      u_Age [ROLL] = input(Fore.BLUE+Style.BRIGHT+"\tWhat is your Age: "+Style.RESET_ALL)
      u_Roll [ROLL] = input(Fore.BLUE+Style.BRIGHT+"\tWhat is your Roll_No: "+Style.RESET_ALL)
      u_Course [ROLL] = input(Fore.BLUE+Style.BRIGHT+"\tWhat is your Course Name: "+Style.RESET_ALL)
      print("Record is Updated.\n",tag='updated',tag_color='green',color='white')
      time.sleep(2)
      os.system("cls")
    else:
      print("Sorry record not found.\n",tag='not found',tag_color='red',color='white')
      time.sleep(2)
      os.system("cls")
    return 0

def REmove():
      os.system("cls")
      print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"############################## "+Fore.RED+Style.BRIGHT+"REMOVEING DATA"+Style.RESET_ALL+Fore.LIGHTBLUE_EX+Style.BRIGHT+" ##############################"+Style.RESET_ALL+"\n")
      print('')                
      ROLL = input(Fore.LIGHTCYAN_EX+"Enter Roll no of the student: "+Style.RESET_ALL)
      if(Checking(ROLL)):
        ROLL = UserRoll(ROLL)
        del u_Name[ROLL]
        del u_Age[ROLL]
        del u_Roll[ROLL]
        del u_Course[ROLL]
        print("Record is removed from the system.\n",tag='Success',tag_color='green',color='white')
        time.sleep(2)
        os.system("cls")
      else:
        print("Record Not Found.",tag='not found',tag_color='red',color='white')
        time.sleep(2)
        os.system("cls")
      return 0

def Student(AD):
  if AD =='1':
    ADD()
  elif AD =='2':
    return REmove() 
  elif AD =='3':
    return Update() 
  elif AD =='4':
    return View() 
  elif AD =='5':
        os.system("cls")
        print(Fore.YELLOW+Style.BRIGHT+"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ "+Fore.GREEN+Style.BRIGHT+'\033[1m THANK YOU \033[0m'+Fore.YELLOW+Style.BRIGHT+" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"+Style.RESET_ALL)
        time.sleep(1.5)
        return exit() 
  else:
    print(Fore.RED+"Wrong Option! Please choose corectly.")
    time.sleep(1.3)
    os.system("cls")

def View():
      os.system("cls")
      print(Fore.RED+"*********************************** "+Fore.YELLOW+Style.BRIGHT+"VIEW"+Fore.RED+Style.BRIGHT+" ***********************************"+Style.RESET_ALL)
                               
      for l in range(len(u_Name)):
        print(u_Name[l], " ", u_Age[l], " ", u_Roll[l], " ", u_Course[l])
      print(Fore.RED+Style.BRIGHT+"****************************************************************************"+Style.RESET_ALL)
      time.sleep(5)
      os.system("cls")
      return 0

u_Name = []
u_Age = []
u_Roll = []
u_Course = []
user = 10000
while(user != 0):
  os.system("cls")
  print(Fore.YELLOW+Style.BRIGHT+'\033[1m  \t\tMain Menu  \033[0m')
  print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"------------------------------------------"+Style.RESET_ALL)
  print(Fore.MAGENTA+"1)Add Student\n2)Remove Student\n3)Update\n4)View\n5)Exit"+Style.RESET_ALL)
  print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"------------------------------------------"+Style.RESET_ALL)
  user = input(Fore.LIGHTCYAN_EX+'What you want to do?\n\tEnter the No. of upper options: '+Style.RESET_ALL)
  print("")
  Student(user)
