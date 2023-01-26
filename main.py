import sqlite3, time, Login, Sales, EmployeeEdit, Inventory
from Login import clear

print("""
===============================================
 _______              _______             ____
|        \          /        |           |    |
|         \        /         |           |    |
|    |\    \      /    /|    |___________|    |
|    | \    \    /    / |                     |
|    |  \    \  /    /  |     ___________     |
|    |   \    \/    /   |    |           |    |
|    |    \        /    |    |           |    |
|    |     \      /     |    |           |    |
|____|      \____/      |____|           |____|
===============================================""")
time.sleep(1)
sqlite3.connect('MarksHardware.db')
print("\nDatabase accessed\n".center(50, '-'))
time.sleep(1)

def killswitch(): #Kill switch to ensure that user wants to logout
  while True:
    kill = input('Logout confirm?(Y/N) ').lower()
    if kill == 'y':
      return True
    elif kill == 'n':
      return False
    print('Invalid. Please try again.')

while True:
  log = Login.login()
  sec = log[0]
  if sec <= 1:
    while True:
      clear()
      choice = input("""\033[0;29;
  ---------------Menu---------------
  Please choose:
  1 - Employee information 
  2 - Inventory information
  3 - Sales
  4 - Logout
  ----------------------------------
  """) 
      if choice == "1" :
        EmployeeEdit.main()
      elif choice == "2":
        Inventory.main()
      elif choice == "3":
        Sales.main(log[1])
      elif choice == "4":
        if killswitch() == True:
          break
      elif choice == "69":
        import Eastereggs
        Eastereggs.main()
      else:
        input("Invalid. \nPress enter to continue...")

  elif sec <= 2:
    while True:
      EmployeeEdit.clear()
      choice = input("""
  ---------------Menu---------------
  Please choose:
  1 - View Employee information 
  2 - Inventory information
  3 - Sales
  4 - Logout
  ----------------------------------
  """) 
      if choice == "1" :
        EmployeeEdit.viewEmployees()
      elif choice == "2":
        Inventory.main()
      elif choice == "3":
        Sales.main(log[1])
      elif choice == "4":
        if killswitch() == True:
          break
      else:
        input("Invalid. \nPress enter to continue...")

  else:
    while True:
      clear()
      choice = input("""
  ---------------Menu---------------
  Please choose:
  1 - Add Inventory 
  2 - Add Sales
  3 - Logout
  ----------------------------------
  """) 
      if choice == "1" :
        Inventory.AddInventory()
      elif choice == "2":
        Sales.addsales(log[1])
      elif choice == "3":
        if killswitch() == True:
          break
      else:
        input("Invalid. \nPress enter to continue...")