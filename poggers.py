import os, time, sys
from datetime import datetime
from pytz import timezone

def clear():
  os.system('clear')

italic = "\033[3m"
red = "\033[0;31m"
green = "\033[0;32m"
orange = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m" 
black = "\033[0;30m"
reset='\033[0m'

time.sleep(1)
clear()
print(purple+"Alternative Chat!"+white)
time.sleep(3.5)
clear()

username = os.environ['REPL_OWNER']
try:
  print(green+'Welcome '+blue+f'{username}'+green+' to the '+purple+'Alternative Chat!'+white)
  time.sleep(2)
  clear()
except:
  username = 'Guest'
  print(green+'Welcome '+blue+f'{username}'+green+'! '+red+f'It also seems like you don\'t have an account yet...\nVisit {sys.exc_info()} for more!')
  os.environ['REPLIT_DB_URL']
  time.sleep(2)
  clear()

text_join=True
tz2=True
chatting=True
while chatting:
  print(purple+'Alternative Chat!'+white)
  print(italic+'\n<~> Enter \'quit\' to quit the program\n'+white)
  file = open('messages.txt','r')
  file2=file.read()
  if file2 == '':
    print(red+'There are no messages yet, you should start one!'+white)
  else:
    print(cyan+file2+orange)#This reads and prints everything in the file
  message=input('\nWhat is your message?\n[:> ')
  if tz2 == False:
    clear()
    pass
  else:
    try:
      tz = timezone(input('What is the timezone?\n[:> '))
      tz2 = False
    except:
      print(red+"Invalid time zone!"+white)
      time.sleep(2)
      clear()
      continue
    clear()

  if message == 'quit':
    mq = input('Is it a message or do you want to quit? m/q\n[:> ').lower()
    if mq == 'm':
      with open('messages.txt','a') as file:
        date = datetime.now(tz)
        file.write(f'{username}: {message} -> {date.strftime("%m/%d/%Y %H:%M:%S")}\n')
        file.close()
    elif mq == 'q':
      chatting=False
      with open('messages.txt','a') as file:#writes in the file the following:
        date = datetime.now(tz)
        file.write(f'{username} has left at {date.strftime("%m/%d/%Y %H:%M:%S")}!\n')#writes the following
        file.close()#closes the file
      clear()
    else:
      clear()
  else:
    if text_join == True:
      with open('messages.txt','a') as file:#this opens the file and appends something
        date = datetime.now(tz)
        file.write(f'{username} has joined at {date.strftime("%m/%d/%Y %H:%M:%S")}!\n')#writes in the file
        file.close()#closes the file. If you dont, you cant create more than one line.
      with open('messages.txt','a') as file:
        date = datetime.now(tz)
        file.write(f'{username}: {message} -> {date.strftime("%m/%d/%Y %H:%M:%S")}\n')
        file.close()#closes the file
      text_join=False
    else:
      with open('messages.txt','a') as file:
        date = datetime.now(tz)
        file.write(f'{username}: {message} -> {date.strftime("%m/%d/%Y %H:%M:%S")}\n')
        file.close()#closes the file
      text_join=False