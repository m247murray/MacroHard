#Databaseedit.py
# this file is used to recreate the databse 
import sqlite3
import Login, EmployeeEdit
conn = sqlite3.connect('MarksHardware.db')

conn.execute('''CREATE TABLE COMPANY
 (ID INT PRIMARY KEY    NOT NULL,
  NAME           TEXT   NOT NULL,
  AGE            INT    NOT NULL,
  ADDRESS        TEXT   NOT NULL,
  USERNAME       TEXT   NOT NULL,
  PASSWORD       TEXT   NOT NULL,
  REPORTTO       TEXT   NOT NULL,
  JOB            TEXT   NOT NULL,
  SALARY         INT    NOT NULL,
  SECURITY       INT    NOT NULL);''')

conn.execute('''CREATE TABLE INVENTORY
 (ID INT PRIMARY KEY    NOT NULL,
  NAME           TEXT   NOT NULL,
  STOCK          INT    NOT NULL,
  PRICE          REAL   NOT NULL,
  MISCINFO       TEXT   NOT NULL);''')

conn.execute('''CREATE TABLE SALES
 (SALESID INT PRIMARY KEY   NOT NULL,
  INVENTORYID         INT   NOT NULL,
  NAME                TEXT  NOT NULL,
  UNITSSOLD           INT   NOT NULL,
  SALEDATE            TEXT  NOT NULL,
  CASHIER             TEXT  NOT NULL);''')


#inserting the base people into the database
ID = [000000,699627,846671,811674,932404]
name = ['Mark Wiseau', 'Alex Pondre', 'Paul Arcam', 'Kate Stevens', 'John Apple']
Age = [30,27,38,35,41]
address = ['132 West Avenue', '42 Cranbrook Road', '7645 Holt Street', '13 Privet Drive', '551 Treelawn Road']
UserName = ['mark.w', 'alex.p', 'paul.a', 'kate.s', 'john.a']
PassWord = ['theroom', 'hunter2', 'cargofast', 'placard', 'tucker']
ReportTo = ['null' , 'Mark Wiseau','Alex Pondre','Alex Pondre', 'Mark Wiseau' ]
Job =['Owner','Manager','Sales','Sales', 'Accounting']
Salary = [100000, 60000, 40000, 40000, 60000]
Security = [1,1,2,2,1]

for i in range(0,len(ID)):
  val = (EmployeeEdit.randserial(6), name[i], Age[i], address[i], Login.encrypt(UserName[i]), Login.encrypt(PassWord[i]), ReportTo[i], Job[i], Salary[i], Security[i])
  conn.execute("INSERT INTO COMPANY VALUES(?,?,?,?,?,?,?,?,?,?)",val)
  conn.commit()

#inserting default inventory items
ItemId = [483127, 566098, 829819, 341158, 349628, 811752, 864742, 158370, 892966, 572149, 674797, 957309, 329411, 234916, 552590, 993625, 693492, 493350, 617449, 330973, 703259, 971165, 838444, 849691]
ItemName = ['Wood Screws', 'Deck Screws', 'Machine Screws', 'Drywall Screws', 'Painters Tape',
 'Duct Tape', 'Cordless Drill', 'Impact Driver', 'Cordless Sander', 'Angle Grinders',
'Saws', 'Light Switches', 'Outlet Plate Covers', 'Electrcial Boxes', 'Wire',
'Breakers', 'Extention Cords', 'Security Cameras', 'Decking Wood', 'Lumber', 
'Insulation', 'Cement', 'Concrete', 'Siding', 'Fencing']
ItemStock = 30
Itemprice = [5,6,4,5,2,3,100,120,80,85,250,7,2,3,10,50,50,150,15,10,35,40,45,12,21]
info = ['For exterior wood to wood applications', 'Star Flat-Head Wood Deck Screws (5 lbs./Pack)', 'Secure fastening without the need to pre-drill', 'For attaching drywall to wood studs', 'This paintern\'s tape is easily applied and can be used indoors or outdoors, great for DIY projects or for professional use.',
 'Perfect for temporary repairs or sealing and holding', 'Provides up to 600 RPM', 'Fastest speed in class with 3200 RPM, 1600 in. - lbs. of torque', 'Random orbit action provides a swirl-free finish', 'Grinder supplies maximum sustained power to complete the toughest grinding, surface preparation and cutting applications.',
'Heavy duty 15 Amp motor to easily cut through larger material', 'Works w/Alexa, Google Assistant, Ring and more Neutral wire required; installs in as little as 15 minutes', '8-Pack of white, 1-gang screwless outlet wall plates', 'Welded steel construction provides a versatile and durable box', '00 ft. 12/1 White Stranded THHN Wire',
'Protection from overload, short-circuit, and Class A Ground Fault', 'This indoor and outdoor extension cord can be used in heavy use applications. This extension cord offers flexibility, durability and a kink free cord when you need it most.', 'Hardwired outdoor security camera with 1080p HD Video', '5/4 in. x 6 in. x 16 ft. Ground Contact Pressure-Treated Weather Shield Pine Standard Decking Board', '2 in. x 4 in. x 96 in. Prime Whitewood Stud', 
'R-13 Pink Kraft Faced Fiberglass Insulation Continuous Roll 15 in. x 32 ft.', '50 lb. Fast-Setting Concrete Mix', '60 lb. Concrete Mix,Ideal for pouring concrete slabs and setting posts', '8.5 in. x 48 in.,comes in vinyl, brick, wood, stone and compsite', 'Pro Series 32 in. H x 93 in. W Black Steel Fence Panel']

for i in range(0,len(ItemId)):
        val = (ItemId[i], ItemName[i], ItemStock, Itemprice[i], info[i])
        conn.execute("INSERT INTO INVENTORY VALUES(?,?,?,?,?)",val)
        conn.commit()

#inserting past sales
InventoryId = [483127, 566098, 829819, 341158, 349628, 811752, 864742, 158370, 892966, 572149, 674797, 957309, 329411, 234916, 552590, 993625, 693492, 493350, 617449, 330973, 703259, 971165, 838444, 849691, 483127]
SalesId = [116954, 361765, 173738, 920530, 614664, 565032, 992530, 950759, 318316, 242338, 243101, 448777, 794411, 905683, 740107, 893160, 232045, 609580, 951280, 645040, 735623, 265959, 830609, 513125]
soldproduct = ['Wood Screws', 'Deck Screws', 'Machine Screws', 'Drywall Screws', 'Painters Tape',
 'Duct Tape', 'Cordless Drill', 'Impact Driver', 'Cordless Sander', 'Angle Grinders',
'Saws', 'Light Switches', 'Outlet Plate Covers', 'Electrcial Boxes', 'Wire',
'Breakers', 'Extention Cords', 'Security Cameras', 'Decking Wood', 'Lumber', 
'Insulation', 'Cement', 'Concrete', 'Siding', 'Fencing','Wood Screws']
unitssold = [10,40,13,15,1,2,1,1,1,1,2,4,7,8,3,23,10,2,5,30,3,6,3,5,2,6,20]
date = ['1962-11-03','1963-01-24','1963-02-12','1964-09-04','1967-06-29','1970-06-08','1971-10-29','1975-07-01','1979-02-09','1990-02-15','1992-08-09','1994-04-13','1996-12-05','1999-02-25','2000-01-23','2003-07-19','2004-04-02','2006-06-20','2006-07-02','2006-12-09','2007-03-27','2007-08-26','2008-03-23','2016-01-21','2017-06-30']
cashier = ['Mark Wiseau', 'Alex Pondre', 'Paul Arcam', 'Kate Stevens', 'John Apple','Mark Wiseau', 'Alex Pondre', 'Paul Arcam', 'Kate Stevens', 'John Apple','Mark Wiseau', 'Alex Pondre', 'Paul Arcam', 'Kate Stevens', 'John Apple','Mark Wiseau', 'Alex Pondre', 'Paul Arcam', 'Kate Stevens', 'John Apple','Mark Wiseau', 'Alex Pondre', 'Paul Arcam', 'Kate Stevens', 'John Apple']

for i in range(0,len(SalesId)):
        val = (EmployeeEdit.randserial(6), InventoryId[i], soldproduct[i], unitssold[i], date[i],cashier[i])
        conn.execute("INSERT INTO SALES VALUES(?,?,?,?,?,?)",val)
        conn.commit()