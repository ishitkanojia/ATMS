import mysql.connector
mycon = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '7717',
    database = 'ATMS')

mycursor = mycon.cursor()

print("*"*107)
print("\t"*5, "AIR TICKET MANAGEMENT SYSTEM")
print("*"*107)

while True :
    print("PRESS 1 FOR USER")
    print("PRESS 2 FOR ADMIN")
    login = input("You are a USER/ADMIN : ")
    print()
    if login == "1":
        while True:
            print("PRESS 1 FOR CREATING ACCOUNT")
            print("PRESS 2 FOR LOG IN")
            starting_window = input("Do you want to CREATE ACCOUNT/LOG IN : ")
            print()
            import random
            permit = ""
            if starting_window == "1":
                User_Id = random.randrange(1,10000)
                User_Name = input("Enter Name : ")
                User_Age = int(input("Enter Age : "))

                while True:
                  c = 0
                  User_Phone = input("Enter Phone Number : ")
                  mycursor.execute("Select user_phone from users")
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if User_Phone in i:
                        print("THIS PHONE NUMBER ALREADY EXISTS")
                        print()
                        c = 1
                        break
                  if c == 0:
                      break

                while True:
                  c = 0
                  User_Email = input("Enter Email Id : ")
                  mycursor.execute("Select user_email from users")
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if User_Email in i:
                        print("THIS EMAIL ID ALREADY EXISTS")
                        print()
                        c = 1
                        break
                  if c == 0:
                      break

                while True:
                  c = 0
                  User_Pwd = input("Enter Password : ")
                  mycursor.execute("Select user_pwd from users")
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if User_Pwd in i:
                        print("THIS PASSWORD ALREADY EXISTS")
                        print()
                        c = 1
                        break
                  if c == 0:
                      break
                    
                User_Info = '''insert into Users(User_Id,User_Name,User_Age,User_Email,User_Pwd,User_Phone)
       values({},'{}',{},'{}','{}','{}')'''.format(User_Id,User_Name,User_Age,User_Email,User_Pwd,User_Phone)
                mycursor.execute(User_Info)
                mycon.commit()
                print("ACCOUNT CREATED & LOGGED IN AS USER")
                print()
                permit = "YES"
                break
                
            elif starting_window == "2": 
                while True:
                  c = 0
                  User_Email = input("Enter Email Id : ")
                  mycursor.execute("Select user_email from users")
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if User_Email in i:
                        c = 1
                        break
                  if c == 0:
                      print("THIS EMAIL ID IS NOT REGISTERED")
                      print()
                  else:
                      break

                while True:
                  c = 0
                  User_Pwd = input("Enter Password : ")
                  mycursor.execute('''select * from users where user_email = '{}' '''.format(User_Email))
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if User_Pwd in i:
                       print("LOGGED IN AS USER")
                       print()
                       permit = "YES"
                       c = 1
                       break
                    else:
                       print("INCORRECT PASSWORD")
                       print()
                       permit = "NO"
                       break
                  if c == 1:
                      break
                break
        
            else :
                print("KINDLY ENTER A VALID NUMBER")
        break
        
    elif login == "2":
                while True:
                  c = 0
                  Admin_Email = input("Enter Email Id : ")
                  mycursor.execute("Select admin_email from admins")
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if Admin_Email in i:
                        c = 1
                        break
                  if c == 0:
                      print("THIS EMAIL ID IS NOT REGISTERED")
                      print()
                  else:
                      break

                while True:
                  c = 0
                  Admin_Pwd = input("Enter Password : ")
                  mycursor.execute('''select * from admins where admin_email = '{}' '''.format(Admin_Email))
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if Admin_Pwd in i:
                       print("LOGGED IN AS ADMIN")
                       print()
                       permit = "YES"
                       c = 1
                       break
                    else:
                       print("INCORRECT PASSWORD")
                       print()
                       permit = "NO"
                       break
                  if c == 1:
                      break
                break

    else:
        print("KINDLY ENTER A VALID NUMBER")

if permit == "YES" and login == "1":
    while permit == "YES":
        print("1. PRESS 1 FOR CHECKING YOUR ACCOUNT DETAILS")
        print("2. PRESS 2 FOR EDITING YOUR ACCOUNT DETAILS")
        print("3. PRESS 3 FOR CHECKING FLIGHTS AND DESTINATIONS AVAILABLE WITH US")
        print("4. PRESS 4 FOR BOOKING FLIGHT TICKETS")
        print("5. PRESS 5 FOR CHECKING DETAILS OF YOUR FLIGHT TICKETS")
        print("6. PRESS 6 FOR CANCELLING FLIGHT")
        request = input("ENTER NUMBER: ")
        print()

        if request == "1":
            mycursor.execute("select * from users where user_email = '%s'"%User_Email)
            myresult = mycursor.fetchall()
            print("##",("USER ID","USER NAME","USER AGE","USER EMAIL","USER PASSWORD","USER PHONE"),"##")
            for i in myresult:
              print(i)
            print()
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()

        elif request == "2":
            mycursor.execute("Select user_phone from users where user_email = '%s'"%User_Email)
            myresult = mycursor.fetchall()
            Phone = myresult[0][0]
            
            mycursor.execute("select * from users where user_phone = '%s'"%Phone)
            myresult = mycursor.fetchall()
            print("##",("USER ID","USER NAME","USER AGE","USER EMAIL","USER PASSWORD","USER PHONE"),"##")
            print(myresult)
            print()
            
            NAME = input("NEW NAME: ")
            AGE = int(input("NEW AGE: "))
            
            while True:
                  c = 0
                  PHONE = input("NEW PHONE: ")
                  mycursor.execute("Select user_phone from users")
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if PHONE in i:
                        print("THIS PHONE NUMBER ALREADY EXISTS")
                        print()
                        c = 1
                        break
                  if c == 0:
                      break

            while True:
                  c = 0
                  EMAIL = input("NEW EMAIL: ")
                  mycursor.execute("Select user_email from users")
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if EMAIL in i:
                        print("THIS EMAIL ID ALREADY EXISTS")
                        print()
                        c = 1
                        break
                  if c == 0:
                      break

            while True:
                  c = 0
                  PWD = input("NEW PASSWORD: ")
                  mycursor.execute("Select user_pwd from users")
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if PWD in i:
                        print("THIS PASSWORD ALREADY EXISTS")
                        print()
                        c = 1
                        break
                  if c == 0:
                      break
            
            print()
            mycursor.execute('''UPDATE users SET User_Name = '%s', User_Age = %d , User_Email = '%s',
            User_Pwd = '%s', User_Phone = '%s' where
            User_Phone = '%s' '''%(NAME,AGE,EMAIL,PWD,PHONE,Phone))
            mycon.commit()
            print("UPDATED")
            print()
            mycursor.execute("select * from users where user_phone = '%s'"%PHONE)
            myresult = mycursor.fetchall()
            print("##",("USER ID","USER NAME","USER AGE","USER EMAIL","USER PASSWORD","USER PHONE"),"##")
            print(myresult)

            print()                
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()


        elif request == "3":
            print("1. PRESS 1 FOR CHECKING ALL FLIGHTS")
            print("2. PRESS 2 FOR CHECKING DOMESTIC FLIGHTS")
            print("3. PRESS 3 FOR CHECKING INTERNATIONAL FLIGHTS")
            action = input("ENTER NUMBER: ")
            print()

            if action == "1":
                mycursor.execute("select * from destinations")
                myresult = mycursor.fetchall()
                print("##",("FLIGHT CODE","AIRLINE","FROM","TO","TYPE OF FLIGHT","AIRPORT"),"##")
                for j in myresult:
                    print(j)
                print()
            elif action == "2":
                mycursor.execute("select * from destinations where type_of_flight = 'domestic'")
                myresult = mycursor.fetchall()
                print("##",("FLIGHT CODE","AIRLINE","FROM","TO","TYPE OF FLIGHT","AIRPORT"),"##")
                for j in myresult:
                    print(j)
                print()    
            elif action == "3":
                mycursor.execute("select * from destinations where type_of_flight = 'international'")
                myresult = mycursor.fetchall()
                print("####",("FLIGHT CODE","AIRLINE","FROM","TO","TYPE OF FLIGHT","AIRPORT"),"####")
                for j in myresult:
                    print(j)
                print()
            else:
                print("KINDLY ENTER A VALID NUMBER")
                
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()
            
        elif request == "4":
            mycursor.execute("Select user_id from users where user_email = '%s'"%User_Email)
            myresult = mycursor.fetchall()
            Customer_Id = myresult[0][0]
            mycursor.execute("Select user_phone from users where user_email = '%s'"%User_Email)
            myresult = mycursor.fetchall()
            Customer_Phone = myresult[0][0]
            
            Destination = False
            while not Destination:
                    From = input("FROM : ")
                    To = input("TO : ")
                    print()
                    mycursor.execute("select * from destinations where from_ = '%s' and to_ = '%s'"%(From,To))
                    Destination = mycursor.fetchall()
                    if Destination == []:
                        print("THIS DESTINATION IS NOT AVAILABLE WITH US")
                        print("KINDLY ENTER ANOTHER DESTINATION")
                        print()
                        Destination == False
            
            while True:
                    print("1. PRESS 1 FOR ECONOMY CLASS")
                    print("2. PRESS 2 FOR BUSINESS CLASS")
                    print("3. PRESS 3 FOR FIRST CLASS")
                    Travel_Class = input("ENTER NUMBER : ")
                    print()
                    if Travel_Class == "1":
                        Travel_Class = "ECONOMY"
                        break
                    elif Travel_Class == "2":
                        Travel_Class = "BUSINESS"
                        break
                    elif Travel_Class == "3":
                        Travel_Class = "FIRST"
                        break
                    else :
                        print("ENTER A VALID NUMBER")
            
            Date = input("ON WHICH DATE YOU WANT THE FLIGHT (DD/MM/YYYY): ")
            Time = input("AT WHICH TIME YOU WANT THE FLIGHT (Hr:Min AM/PM): ")
            Tickets = int(input("HOW MANY TICKETS YOU WANT TO BOOK : "))
            print()
            mycursor.execute('''select adult,child,infant from ticket_price
                             where flight_code = %d'''%Destination[0][0])
            price = mycursor.fetchall()
            c = 0
            adult = 0
            child = 0
            infant = 0
            while c < Tickets:
                Customer_Name = input("NAME : ")
                Customer_Age = int(input("AGE : "))

                if Travel_Class == "ECONOMY":
                    adult_price = price[0][0]
                    child_price = price[0][1]
                    infant = 0
                    
                elif Travel_Class == "BUSINESS":
                    adult_price = price[0][0] *5
                    child_price = price[0][1] *5
                    infant = 0

                else :
                    adult_price = price[0][0] *10
                    child_price = price[0][1] *10
                    infant = 0

                if Customer_Age >= 12:
                    adult += 1
                    Ticket_Price = adult_price
                elif 3 <= Customer_Age <= 11:
                    child += 1
                    Ticket_Price = child_price
                else:
                    infant += 1
                    Ticket_Price = 0

                c += 1
                print()
                    
                Customer_Info = '''insert into Customers(Customer_Id, Customer_Name,
                Customer_Age, Customer_Phone, Airline, FROM_, TO_ , Travel_Class, Type_Of_Flight, Airport,
                Date, Time, Ticket_Price) values({}, '{}', {}, '{}','{}','{}','{}','{}','{}',
                '{}','{}','{}',{})'''.format(Customer_Id, Customer_Name,Customer_Age,
                                             Customer_Phone, Destination[0][1], From, To,
                                             Travel_Class, Destination[0][4], Destination[0][5],Date,
                                             Time, Ticket_Price)
                mycursor.execute(Customer_Info)
                mycon.commit()

            mycursor.execute('''select adult,child,infant from ticket_price
                             where flight_code = %d'''%Destination[0][0])
            price = mycursor.fetchall()
            if Travel_Class == "ECONOMY":
                adult_price = adult * price[0][0]
                child_price = child * price[0][1]
                infant = "ON LAP"
                
            elif Travel_Class == "BUSINESS":
                adult_price = adult * price[0][0] *5
                child_price = child * price[0][1] *5
                infant = "ON LAP"

            else :
                adult_price = adult * price[0][0] *10
                child_price = child * price[0][1] *10
                infant = "ON LAP"

            mycursor.execute("select * from customers where customer_phone = '%s'"%Customer_Phone)
            Customer_Details = mycursor.fetchall()
            print("##",("CustomerId","CustomerName","CustomerAge","CustomerPhone",
                          "Airline","FROM","TO","TravelClass","Type_Of_Flight","Airport",
                          "Date","Time","TicketPrice"),"##")
            for i in Customer_Details:
                print(i)
            print()
            print("TOTAL ADULT TICKET PRICE :",adult_price)
            print("TOTAL CHILD TICKET PRICE :",child_price)
            print("TOTAL MONEY TO BE PAID :",adult_price + child_price)
            print()
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()

        elif request == "5":
            while True:
                  c = 0
                  Customer_Phone = input("Enter Phone Number : ")
                  mycursor.execute("Select customer_phone from customers")
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if Customer_Phone in i:
                        c = 1
                        break
                  if c == 1:
                      break
                  print("NO TICKETS HAVE BEEN BOOKED USING THIS PHONE NUMBER")
                  break
                  print()
            
            mycursor.execute("select * from customers where customer_phone = '%s'"%Customer_Phone)
            Customer_Details = mycursor.fetchall()
            print("##",("CustomerId","CustomerName","CustomerAge","CustomerPhone",
                          "Airline","FROM","TO","TravelClass","Type_Of_Flight","Airport",
                          "Date","Time","TicketPrice"),"##")
            for i in Customer_Details:
                print(i)
            print()
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()

        elif request == "6":
            while True:
                  c = 0
                  Customer_Phone = input("Enter Phone Number : ")
                  mycursor.execute("Select customer_phone from customers")
                  myresult = mycursor.fetchall()
                  for i in myresult:
                    if Customer_Phone in i:
                        c = 1
                        break
                  if c == 1:
                      break
                  print("PHONE NUMBER INVALID")
                  print()

            print("1. PRESS 1 FOR CANCELLING ALL THE FLIGHT TICKETS BOOKED USING YOUR NUMBER")
            print("2. PRESS 2 FOR CANCELLING FLIGHT TICKET OF A SPECIFIC PERSON")
            action = input("ENTER NUMBER: ")
            print()

            if action == "1":
                mycursor.execute("delete from customers where customer_phone = '%s' "%Customer_Phone)
                mycon.commit()
                print("ALL FLIGHT TICKETS BOOKED USING '%s' ARE CANCELLED"%Customer_Phone)
            elif action == "2":
                action = "YES"
                while action == "YES":
                    Customer_Name = input("ENTER NAME : ")
                    mycursor.execute('''delete from customers where customer_phone = '%s'
                                    and customer_name = '%s' '''%(Customer_Phone,Customer_Name))
                    mycon.commit()
                    print("FLIGHT TICKET OF '%s' IS CANCELLED"%Customer_Name)
                    action = input("DO YOU WANT TO DELETE MORE TICKETS (YES/NO): ").upper()
            print()
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()  
            
        else:
            print("KINDLY ENTER A VALID NUMBER")
            
elif permit == "YES" and login == "2":
    while permit == "YES":
        print("1. PRESS 1 FOR CHECKING FLIGHTS AND DESTINATIONS AVAILABLE WITH US")
        print("2. PRESS 2 FOR UPDATING FLIGHTS AND DESTINATIONS AVAILABLE WITH US")
        print("3. PRESS 3 FOR ADDING MORE DESTINATIONS")
        print("4. PRESS 4 FOR DELETING ANY DESTINATION")
        print()
        print("5. PRESS 5 FOR CHECKING TICKET PRICE DETAILS")
        print("6. PRESS 6 FOR UPDATING TICKET PRICE DETAILS")
        print("7. PRESS 7 FOR ADDING MORE TICKET PRICES")
        print("8. PRESS 8 FOR DELETING ANY TICKET PRICE")
        print()
        print("9. PRESS 9 FOR CHECKING CUSTOMER TICKET DETAILS")
        print("10. PRESS 10 FOR CHECKING USER DETAILS")
        print()
        
        request = input("ENTER NUMBER: ")
        print()

        if request == "1":
            print("1. PRESS 1 FOR CHECKING ALL FLIGHTS")
            print("2. PRESS 2 FOR CHECKING DOMESTIC FLIGHTS")
            print("3. PRESS 3 FOR CHECKING INTERNATIONAL FLIGHTS")
            action = input("ENTER NUMBER: ")
            print()

            if action == "1":
                mycursor.execute("select * from destinations")
                myresult = mycursor.fetchall()
                print("##",("FLIGHT CODE","AIRLINE","FROM","TO","TYPE OF FLIGHT","AIRPORT"),"##")
                for j in myresult:
                    print(j)
                print()
            elif action == "2":
                mycursor.execute("select * from destinations where type_of_flight = 'domestic'")
                myresult = mycursor.fetchall()
                print("##",("FLIGHT CODE","AIRLINE","FROM","TO","TYPE OF FLIGHT","AIRPORT"),"##")
                for j in myresult:
                    print(j)
                print()    
            elif action == "3":
                mycursor.execute("select * from destinations where type_of_flight = 'international'")
                myresult = mycursor.fetchall()
                print("####",("FLIGHT CODE","AIRLINE","FROM","TO","TYPE OF FLIGHT","AIRPORT"),"####")
                for j in myresult:
                    print(j)
                print()
            else:
                print("KINDLY ENTER A VALID NUMBER")

            print()                
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()

        elif request == "2":
            
            Flight_Code = int(input("ENTER FLIGHT CODE : "))
            mycursor.execute("select * from destinations where flight_code = %d"%Flight_Code)
            myresult = mycursor.fetchall()
            print("##",("FLIGHT CODE","AIRLINE","FROM","TO","TYPE OF FLIGHT","AIRPORT"),"##")
            print(myresult)
            
            Airline = input("Airline: ")
            From_ = input("From: ")
            To_ = input("To: ")
            Type_of_Flight = input("Type of Flight: ")
            Airport = input("Airport: ")
            print()
            mycursor.execute('''UPDATE destinations SET Airline = '%s', From_ = '%s', To_ = '%s',
            Type_of_Flight = '%s', Airport = '%s' where
            flight_code = %d'''%(Airline,From_,To_,Type_of_Flight,Airport,Flight_Code))
            mycon.commit()
            print("UPDATED")
            print()
            mycursor.execute("select * from destinations where flight_code = %d"%Flight_Code)
            myresult = mycursor.fetchall()
            print("##",("FLIGHT CODE","AIRLINE","FROM","TO","TYPE OF FLIGHT","AIRPORT"),"##")
            print(myresult)

            print()                
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()

        elif request == "3":

            action = "YES"
            while action == "YES":
                mycursor.execute("select count(flight_code) from destinations")
                num = mycursor.fetchall()
                Flight_Code = num[0][0] + 1            
                Airline = input("Airline: ")
                From_ = input("From: ")
                To_ = input("To: ")
                Type_of_Flight = input("Type of Flight: ")
                Airport = input("Airport: ")
                print()
                sql = '''insert into destinations(Flight_Code,Airline,From_,To_,Type_of_Flight,Airport)
                values({},'{}','{}','{}','{}','{}')'''.format(Flight_Code,Airline,From_,
                                                              To_,Type_of_Flight,Airport)
                mycursor.execute(sql)
                mycon.commit()
                print("ADDED")
                print()
                mycursor.execute("select * from destinations where flight_code = %d"%Flight_Code)
                myresult = mycursor.fetchall()
                print("##",("FLIGHT CODE","AIRLINE","FROM","TO","TYPE OF FLIGHT","AIRPORT"),"##")
                print(myresult)
                action = input("DO YOU WANT TO ADD MORE DESTINATIONS (YES/NO): ").upper()
                
            print()
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()

        elif request == "4":
            action = "YES"
            while action == "YES":
               Flight_Code = int(input("ENTER FLIGHT CODE : "))
               mycursor.execute("delete from destinations where flight_code = %d"%Flight_Code)
               mycon.commit()
               print("DELETED")
               print()
               action = input("DO YOU WANT TO DELETE MORE DESTINATIONS (YES/NO) : ").upper()
            print()
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()

        elif request == "5":
            mycursor.execute(''' select destinations.FLIGHT_CODE,AIRLINE,FROM_,TO_,ADULT,CHILD,INFANT
            from destinations,ticket_price where destinations.flight_code = ticket_price.flight_code ''')
            myresult = mycursor.fetchall()
            print("##",("FLIGHT_CODE","AIRLINE","FROM_","TO_","ADULT","CHILD","INFANT"),"##")
            for i in myresult:
                print(i)

            print()
            print("#### THE GIVEN FLIGHT TICKET PRICES ARE FOR ECONOMIC CLASS ####")
            print("#### FOR BUSINESS CLASS TICKET PRICES, MULTIPLY THESE PRICES BY 5 ####")
            print("#### FOR FIRST CLASS TICKET PRICES, MULTIPLY THESE PRICES BY 10 ####")
            
            print()
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()

        elif request == "6":
            Flight_Code = int(input("ENTER FLIGHT CODE : "))
            mycursor.execute("select * from ticket_price where flight_code = %d"%Flight_Code)
            myresult = mycursor.fetchall()
            print("##",("FLIGHT CODE","ADULT","CHILD","INFANT"),"##")
            print(myresult)
            
            A_Price = int(input("ADULT TICKET PRICE : "))
            C_Price = int(input("CHILD TICKET PRICE : "))
            print()
            
            mycursor.execute('''UPDATE ticket_price SET Adult = %d , Child = %d where
            flight_code = %d''' %(A_Price,C_Price,Flight_Code))
            mycon.commit()
            print("UPDATED")
            print()
            mycursor.execute("select * from ticket_price where flight_code = %d"%Flight_Code)
            myresult = mycursor.fetchall()
            print("##",("FLIGHT CODE","ADULT","CHILD","INFANT"),"##")
            print(myresult)

            print()                
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()

        elif request == "7":
            action = "YES"
            while action == "YES":
                mycursor.execute("select count(flight_code) from ticket_price")
                num = mycursor.fetchall()
                Flight_Code = num[0][0] + 1
                
                A_Price = int(input("ADULT TICKET PRICE : "))
                C_Price = int(input("CHILD TICKET PRICE : "))
                I_Price = "ON LAP"
                print()
                sql = '''insert into ticket_price(Flight_Code,Adult,Child,Infant)
                values({},{},{},'{}')'''.format(Flight_Code,A_Price,C_Price,I_Price)
                mycursor.execute(sql)
                mycon.commit()
                print("ADDED")
                print()
                mycursor.execute("select * from ticket_price where flight_code = %d"%Flight_Code)
                myresult = mycursor.fetchall()
                print("##",("FLIGHT CODE","ADULT","CHILD","INFANT"),"##")
                print(myresult)
                action = input("DO YOU WANT TO ADD MORE FLIGHT TICKET PRICES (YES/NO): ").upper()
                
            print()
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()

        elif request == "8":
            action = "YES"
            while action == "YES":
               Flight_Code = int(input("ENTER FLIGHT CODE : "))
               mycursor.execute("delete from ticket_price where flight_code = %d"%Flight_Code)
               mycon.commit()
               print("DELETED")
               print()
               action = input("DO YOU WANT TO DELETE MORE FLIGHT TICKET PRICES (YES/NO) : ").upper()
            print()
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()
            
        elif request == "9":
            mycursor.execute("select * from customers")
            myresult = mycursor.fetchall()
            print("##",("CustomerId","CustomerName","CustomerAge","CustomerPhone",
                          "Airline","FROM","TO","TravelClass","Type_Of_Flight","Airport",
                          "Date","Time","TicketPrice"),"##")
            for i in myresult:
                print(i)
            print()
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()

        elif request == "10":
            mycursor.execute("select * from users")
            myresult = mycursor.fetchall()
            print("##",("USER ID","USER NAME","USER AGE","USER EMAIL","USER PASSWORD","USER PHONE"),"##")
            for i in myresult:
                print(i)
            print()
            permit = input("DO YOU WANT TO CONTINUE (YES/NO): ").upper()        
            
        else:
            print("KINDLY ENTER A VALID NUMBER")

else:
    print("KINDLY LOG IN AGAIN")

print("*"*107)
print("\t"*5, "   YOU HAVE LOGGED OUT")
print("\t"*5, "THANK YOU FOR CHECKING IN")
print("*"*107)
