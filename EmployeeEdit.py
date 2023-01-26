#EmployeeEdit.py
#Used for Create Read Update and deletion of employee lists 
import sqlite3, Login
from random import randint
from Login import clear
 
conn = sqlite3.connect('MarksHardware.db')
cursor = conn.cursor()

def unique(ID):
  for id in conn.execute("SELECT ID FROM COMPANY"):
    if id[0] == ID:
      return False
  return True
    
def randserial(n):
  range_start = 10 ** (n-1)
  range_end = (10**n) -1
  return randint(range_start, range_end)

def viewall():
  clear()
  for row in conn.execute("SELECT * from COMPANY ORDER BY ID"):
    print(f'Id: {row[0]} || Name: {row[1]} || Age: {row[2]} || Address:  {row[3]} || Reports to: {row[6]} || Job: {row[7]} || Salary: {row[8]} || Security Level: {row[9]}\n')

def searchnum(choice,item,db):
  while True:
    clear()
    para = input("""
  ------------Search By-------------
  Please choose:
  1 - Amount 
  2 - Minimum amount
  3 - Maximum amount
  4 - Minimum amount & Maximum amount
  5 - Return
  ----------------------------------
  """)
    if para == '1':
      search = int(input('Enter number: '))
      return conn.execute(f'SELECT * FROM {db} WHERE {item[choice-1]} = {search} ORDER BY {item[choice-1]}')
    elif para == '2':
      low = int(input('Enter lower bound: '))
      return conn.execute(f"SELECT * FROM {db} WHERE {item[choice-1]} >= {low} ORDER BY {item[choice-1]}")
    elif para == '3':
      high = int(input('Enter higher bound: '))
      return conn.execute(f"SELECT * FROM {db} WHERE {item[choice-1]}<={high} ORDER BY {item[choice-1]}")
    elif para == '4':
      low = int(input('Enter lower bound: '))
      high = int(input('Enter higher bound: '))
      return conn.execute(f"SELECT * FROM {db} WHERE ({low} <= {item[choice-1]} AND {item[choice-1]} <= {high}) ORDER BY {item[choice-1]}")
    elif para == '5':
      return
    else:
      input('Invalid. Press enter to continue...')
      continue
      
        

def searchtext(choice,item,db):
  while True:
    clear()
    para = input("""
  ------------Search By-------------
  Please choose:
  1 - Text 
  2 - Starting with
  3 - Return
  ----------------------------------
  """)
    if para == '1':
      search = input('Enter text: ')
      return conn.execute(f"SELECT * FROM {db} WHERE {item[choice-1]} = '{search}'")
    elif para == '2':
      search = input('Enter starting letter: ')
      return conn.execute(f"SELECT * FROM {db} WHERE {item[choice-1]} like '{search}%'")
    elif para == '3':
      return
    else:
      print('Invalid.')
      
      continue
    input('Press enter to continue...')

def search():
  while True:
    clear()
    try:
      choice = int(input("""
  ------------Search By-------------
  Please choose:
  1 - ID 
  2 - Name
  3 - Age
  4 - Address
  5 - Salary
  6 - Security level
  7 - Return
  ----------------------------------
  """))
      item =('ID', 'NAME', 'AGE', 'ADDRESS', 'SALARY', 'SECURIY')
      if choice == 1 or choice == 3 or choice == 5 or choice == 6:
        result = searchnum(choice,item,'COMPANY')
      elif choice == 2 or choice == 6:
        result = searchtext(choice,item,'COMPANY')
      elif choice == 7:
       return
      else:
        print('Invalid.')
        input('Press enter to continue...')
        continue
      clear()
      for row in result:
        print(f'Id: {row[0]} || Name: {row[1]} || Age: {row[2]} || Address:  {row[3]} || Reports to: {row[6]}|| Job: {row[7]} || Salary: {row[8]} || Security Level: {row[9]}\n')
      input('Press enter to continue...')
      return
    except:
      input('Invalid. \nPress enter to continue...')

def viewEmployees():
  while True:
    clear()
    choice = input("""
  ----------View Employees----------
  Please choose:
  1 - View all
  2 - Search Employees
  3 - Return
  ----------------------------------
  """) 
    if choice == "1" :
      viewall()
      input("Press enter to continue...")
    elif choice == "2":
      search()
    elif choice == "3":
      return
    else:
      input("Invalid.\nPress enter to continue...")
  
def AddEmployees():
  while True:
    clear()
    try:
      print('Loading...')
      while True:
        EMPID = randserial(6)
        if unique(EMPID):
          break
      while True:
        clear()
        print ('ID:', EMPID)
        name = input('Enter name. Enter 0 to exit: ')
        if name == '0':
          return
        Age = int(input('Enter age: '))
        address = input('Enter address: ')
        UserName = Login.encrypt(input('Enter username: '))
        PassWord = Login.encrypt(input('Enter password: '))
        Job = input('Enter employee job tile: ')
        for row in conn.execute("SELECT ID, NAME FROM COMPANY"):
          print(f'ID: {row[0]} Name: {row[1]}')
        manId = int(input('Enter manager ID: '))
        if unique(manId) == True:
          input('Error: employee not found. \nPress enter to continue...')
        else:
          cursor.execute(f"SELECT NAME from COMPANY where ID = {manId}")
          ReportsTo = cursor.fetchall()[0][0]
          break
      Salary = int(input('Enter salary: '))
      Security = int(input('Set security level: '))
      val = (EMPID, name, Age, address, UserName, PassWord, ReportsTo, Job, Salary, Security)
      conn.execute("INSERT INTO COMPANY VALUES(?,?,?,?,?,?,?,?,?,?)",val)
      conn.commit()
      input('Success \nPress enter to continue...')
      return
    except:
      input('Invalid. \nPress enter to continue...')
    
def removeEmployees():
  while True:
    viewall()
    try:
      Del = int(input('Select ID. Enter 0 to canel: '))
      if Del == 0:
        input('Cancel. \nPress enter to continue...')
        return
      if unique(Del) == False:
        conn.execute(f"DELETE from COMPANY where ID = {Del}")
        conn.commit()
        input('Success. \nPress enter to continue...')
        return   
    except:
      pass
    input('Invalid. Please try again. \nPress enter to continue...')
    
def changeEmployee():
  while True:
    viewall()
    try:
      id = int(input('Select ID to edit. Enter 0 to cancel: '))
      if id == 0:
        print('Cancel.')
        return
      cursor.execute(f"SELECT * FROM COMPANY where ID = {id}")
      row = cursor.fetchall()[0]
      while True:
        clear()
        print(f'Id: {row[0]} || Name: {row[1]} || Age: {row[2]} || Address:  {row[3]} || Reports to: {row[6]} || Job: {row[7]} || Salary: {row[8]} || Security Level: {row[9]}\n')
        choice = int(input("""
  -------------Change By------------
  1 - ID 
  2 - Name
  3 - Age
  4 - Address
  5 - Username
  6 - Password
  7 - Salary
  8 - Security level
  9 - Return
  ----------------------------------
  """))
        if choice == 9:
          input('Cancel. \nPress enter to continue...')
          return
        object = ('ID', 'NAME', 'AGE', 'ADDRESS', 'USERNAME', 'PASSWORD',  'SALARY', 'SECURITY')
        change = input(f'Enter {object[choice-1]}: ')
        if choice == 1 or choice == 3 or choice == 7 or choice == 8:
          change = int(change)
          if choice == 1 and unique(change) == False:
            input('ID already exist. \nPress enter to continue...')
            continue
        elif choice == 5 or choice == 6:
          change = Login.encrypt(change)
        conn.execute(f"UPDATE COMPANY SET {object[choice-1]} = '{change}' where ID = {id}")
        conn.commit()
        input('Success. \nPress enter to continue...')
        return
    except:
      input('Invalid. \nPress enter to continue...')

def main():
  while True:
    clear()
    choice = input("""
  -------Employee information-------
  Please choose:
  1 - View Employees
  2 - Add Employees
  3 - Edit Employee
  4 - Remove Employees
  5 - Return
  ----------------------------------
  """) 
    if choice == "1" :
      viewEmployees()
    elif choice == "2":
      AddEmployees()
    elif choice == "3":
      changeEmployee()
    elif choice == "4":
      removeEmployees()
    elif choice == "5":
      return
    else:
      input("Invalid. \nPress enter to continue...")