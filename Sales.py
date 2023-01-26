import sqlite3, datetime
from EmployeeEdit import randserial
from Login import clear
from Inventory import unique
conn = sqlite3.connect('MarksHardware.db')
cursor = conn.cursor()

def uniquesales(ID): #ensures unique Ids
  for id in conn.execute("SELECT SALESID FROM SALES"):
    if id[0] == ID:
      return False
    return True

def addsales(USERID): #Adds sales uses current date time and Id from who logged on to categorize sales
  clear()
  try:
    cashier = conn.execute(f"SELECT NAME from COMPANY where ID = {USERID}").fetchall()[0][0]
    while True:
      SALESID = randserial(6)
      if uniquesales(SALESID):
        break
    for row in conn.execute("SELECT ID, NAME from INVENTORY"):
      print(f'ID: {row[0]} || Name: {row[1]} ')

    while True:
      print('Sales ID:', SALESID)
      print('Cashier:', cashier)
      Sale = int(input('Enter serial #. Enter 0 to cancel: ')) # getsinventory id of item
      if Sale == 0:
        input('Cancel. \nPress ente to continue...')
        return
      if unique(Sale) == False: # decides if the serial number provided is valid
        print("Found!")
        Name = conn.execute(f"SELECT NAME FROM INVENTORY WHERE ID = {Sale}").fetchone()[0] # gets the product namewith the id from the inventory 
        date = datetime.datetime.now().date() # Gets date of sale
        unitsleft2 = conn.execute(f"SELECT STOCK FROM INVENTORY WHERE ID={Sale}").fetchone()[0] # gets units left in stock of item
        print('There are', unitsleft2, 'left in stock')
        while True: # loop asks for unts being sold and if the input is invalid loop it
          sold = int(input('Input number of units being sold: '))
          if unitsleft2 >= sold: # checks to see if there is enough in stock to sell requested amount
            break
          else:
            print('Invalid. Not enough stock.')
            continue
        salval = (SALESID, Sale, Name, sold, date, cashier)
        conn.execute("INSERT INTO SALES VALUES (?,?,?,?,?,?)", salval)
        conn.execute(f"UPDATE INVENTORY SET STOCK = {unitsleft2 - sold} where ID = {Sale}")
        conn.commit()
        input('Success. \nPress enter to continue...')
        return
      else:  # if serial Id does not match any in the inventory asks for id again
          input("Serial # does not exist. \nPress enter to continue...")
          continue
  except:
    input('Invalid. \nPress enter to continue...')

def viewsales(): #This function prints out all the past sales
  for row in conn.execute("SELECT * FROM SALES").fetchall():
    print(f'Sale ID: {row[0]} || Item ID: {row[1]}\nItem: {row[2]} || # of items sold: {row[3]}\nDate: {row[4]} || Cashier: {row[5]}\n')
  input('Press enter to continue...')

def main(id): #This function gives you choices to choose from to continue
  while True:
    clear()
    choice = input("""
  -------Sales information-------
  Please choose:
  1 - View Sales
  2 - Add Sales
  3 - Return
  ----------------------------------
  """)
    if choice == "1":
      viewsales()
    elif choice == "2":
      addsales(id)
    elif choice == "3":
      return
    else:
      input("Invalid.\nPress enter to continue:...")