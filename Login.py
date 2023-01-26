import sqlite3
from os import system, name
conn = sqlite3.connect('MarksHardware.db')
cursor = conn.cursor()

def encrypt(code): #Encryption function
  code = ''.join(str(ord(i) * (ord(code[0]) + ord(code[-1]))) for i in code)
  return code

def clear(): # OS ad clears based on that
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def login(): #login method to ask who is logging on and return security level and ID
  while True:
    clear()
    print('Sign in')
    UserName = encrypt(input('Enter Username: '))
    PassWord = encrypt(input('Enter Password: '))
    cursor.execute("SELECT COUNT(ID) from COMPANY")
    if cursor.fetchall()[0][0] == 0 and UserName == PassWord == '':
      return (1,1)
    for row in conn.execute("SELECT ID, USERNAME, PASSWORD, SECURITY from COMPANY"):
      if UserName == row[1] and PassWord == row[2]:
        return(row[3], row[0])
    input('Invalid. \nPress enter to continue...')
