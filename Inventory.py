#Inventory.py
#Functions to create read update inventory table
import sqlite3, EmployeeEdit
from Login import clear
conn = sqlite3.connect('MarksHardware.db')
cursor = conn.cursor()

def viewAll(): #Shows all employees
  clear()
  for row in conn.execute("SELECT * from INVENTORY"):
    print(f'ID: {row[0]} || Name: {row[1]} || Number in stock: {row[2]} || Price: ${row[3]:.2f} || Miscelaneos Information: {row[4]}\n')

def unique(ID): #Ensure the ID is unique to each employee
  for id in conn.execute("SELECT ID FROM INVENTORY"):
    if id[0] == ID:
      return False
  return True

def viewInventory(): #Menu to view inventory search or veiw all option
  while True:
    clear()
    choice = input("""
  ----------View Inventory----------
  Please choose:
  1 - View all
  2 - Search Products
  3 - Return
  ----------------------------------
  """) 
    if choice == "1" :
      viewAll()
      input("Press enter to continue...")
    elif choice == "2":
      search()
    elif choice == "3":
      return
    else:
      input("Invalid. \nPress enter to continue...")

def search(): #Searches the inventory
  while True:
    clear()
    try:
      choice = int(input("""
  ------------Search By-------------
  Please choose:
  1 - Item ID 
  2 - Item Name
  3 - Item Stock
  4 - Item Price
  5 - Info
  6 - Return
  ----------------------------------
  """))
      item =('ID', 'NAME', 'STOCK', 'PRICE', 'MISCINFO')
      if choice == 6:
        return
      elif choice == 1 or choice == 3 or choice == 4:
        result = EmployeeEdit.searchnum(choice,item,'INVENTORY')
      elif choice == 2 or choice==5:
        result = EmployeeEdit.searchtext(choice,item,'INVENTORY')
      clear()
      for row in result:
        print(f'Item ID: {row[0]} || Item Name: {row[1]} || Stock: {row[2]} || Price: ${row[3]} || Misc. Info: {row[4]}\n')
      input('Press enter to continue...')
      return
    except:
      input('Invalid.\nPress enter to continue...')

def AddInventory(): #Adds inventory adding inventory to existing stockpiles or adding new types of inventory
  while True:
    viewAll()
    try:
      InventoryId = int(input("""
    -----------Add Inventory----------
    Please choose:
    # - Add to serial #
    0 - Add new item
    1 - Return
    ----------------------------------
    """))
      if InventoryId == 1:
        return
      elif InventoryId == 0:
        while True:
          ID = EmployeeEdit.randserial(6)
          if unique(ID):
            break
        NAME = input('Enter name: ')
        STOCK = int(input('Enter number in stock: '))
        MISCINFO = input('Enter miscellaneous info: ')
        PRICE = float(input('Enter Price of item: '))
        val= (ID, NAME, STOCK, PRICE, MISCINFO)
        conn.execute("INSERT INTO INVENTORY VALUES (?,?,?,?,?) ",val)
        conn.commit()
        print('Success.')
        return
      elif InventoryId != 0 and unique(InventoryId):
        Add = int(input('Enter amount: '))
        cursor.execute(f"SELECT STOCK from INVENTORY where ID = {InventoryId}")
        conn.execute(f"UPDATE INVENTORY set STOCK = {Add+cursor.fetchall()[0][0]} WHERE ID = {InventoryId}")
        conn.commit()
        input('Success. \nPress enter to continue...')
        return
    except:
      pass
    input('Invalid\nPress enter to continue...')

def RemoveInventory():
  while True:
    viewAll()
    try:
      Del = int(input('Select ID. Enter 0 to canel: '))
      if Del == 0:
        input('Cancel. \nPress enter to continue...')
        return
      if unique(Del) == False:
        conn.execute(f"DELETE from INVENTORY where ID = {Del}")
        conn.commit()
        print('Success.')
        return   
    except:
      pass
    input('Invalid. Please try again. \nPress enter to continue...')

def main():
  while True:
    clear()
    choice = input("""
  -------------Inventory------------
  1 - View Inventory
  2 - Add Inventory 
  3 - Remove Inventory
  4 - Return
  ----------------------------------
  """)
    if choice == "1" :
      viewInventory()
    elif choice == "2":
      AddInventory()
    elif choice == "3":
      RemoveInventory()
    elif choice == "4":
      return
    else:
      input("Invalid. \nPress enter to continue...")