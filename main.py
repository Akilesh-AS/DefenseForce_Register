# BEGINNING OF THE PROJECT

import mysql.connector as mysql
from datetime import date
import time
from turtle import speed
import turtle

# Setting the Connection-Object and the Cursor-Object
connect = mysql.connect(user='root',
                        passwd='akilesh@12345',
                        host='localhost',
                        database='Agnipath_Yojana',
                        charset='utf8')

cursor = connect.cursor()


class agniipath:
    def create_admin_user_passwd(self):
        # Username and Password of the admin section
        try:
            query6 = " CREATE TABLE IF NOT EXISTS admin_section\
                          (\
                            username                VARCHAR(100),\
                            password                VARCHAR(100)\
                          ) "
            cursor.execute(query6)
            connect.commit()
            i = 1
        except:
            i = 0

        if i == 1:
            # Inserting the username and password
            query7 = " INSERT INTO admin_section(username, password)\
                          VALUES('agnipath', '12345') "
            cursor.execute(query7)
            connect.commit()

    def use_database(self):
        query = "USE Agnipath_Yojana"
        cursor.execute(query)
        connect.commit()

    def create_table(self):
        query1 = " CREATE TABLE IF NOT EXISTS new_enrollment" \
                 "(" \
                 "   State_Name_UT_Name                            VARCHAR(50)," \
                 "   Region                                        VARCHAR(50)," \
                 "   Nationality                                   VARCHAR(100)," \
                 "   Aadhar_No                                     VARCHAR(50)," \
                 "   Candidate_Name                                VARCHAR(100)," \
                 "   Gender                                        VARCHAR(10)," \
                 "   Father_Name                                   VARCHAR(100)," \
                 "   Mother_Name                                   VARCHAR(100)," \
                 "   Date_Of_Birth                                 VARCHAR(10)," \
                 "   Candidate_Age                                 INTEGER," \
                 "   Email_Address                                 VARCHAR(100)," \
                 "   Mobile_No                                     VARCHAR(15)," \
                 "   Martial_Status                                VARCHAR(10)," \
                 "   Higher_Education                              VARCHAR(100)," \
                 "   Matriculation_Board                           VARCHAR(100)," \
                 "   Username                                      VARCHAR(100)                    PRIMARY KEY," \
                 "   Password                                      VARCHAR(100)," \
                 "   House_No                                      VARCHAR(50)," \
                 "   Address                                       TEXT," \
                 "   Village                                       VARCHAR(100)," \
                 "   City_Town                                     VARCHAR(100)," \
                 "   District                                      VARCHAR(100)," \
                 "   Tensil                                        VARCHAR(100)," \
                 "   Block_Locality                                VARCHAR(100)," \
                 "   Pin_No                                        VARCHAR(10)," \
                 "   Police_Station                                VARCHAR(100)," \
                 "   Post_Office                                   VARCHAR(100)," \
                 "   Telegram_Office                               VARCHAR(100)," \
                 "   Category                                      VARCHAR(100)," \
                 "   Sport                                         VARCHAR(50)," \
                 "   NCC                                           VARCHAR(10)," \
                 "   Special_Category                              VARCHAR(100)," \
                 "   Highest_Education                             VARCHAR(100)," \
                 "   Qualifying_Course                             VARCHAR(100)," \
                 "   Board_Education_University                    VARCHAR(50)," \
                 "   Name_of_the_University_Board                  VARCHAR(100)," \
                 "   Name_in_Matriculation_Certificate             VARCHAR(100)," \
                 "   Year_Of_Passing                               VARCHAR(10)," \
                 "   Roll_No                                       VARCHAR(100)," \
                 "   Certificate_No                                VARCHAR(100)," \
                 "   Medical_Test                                  VARCHAR(10)," \
                 "   Physical_Test                                 VARCHAR(10)," \
                 "   Written_Test                                  INTEGER" \
                 ")"

        cursor.execute(query1)
        connect.commit()

        query2 = " CREATE TABLE IF NOT EXISTS eligible_candidate" \
                 "(" \
                 "   State_Name_UT_Name                            VARCHAR(50)," \
                 "   Region                                        VARCHAR(50)," \
                 "   Nationality                                   VARCHAR(100)," \
                 "   Aadhar_No                                     VARCHAR(50)," \
                 "   Candidate_Name                                VARCHAR(100)," \
                 "   Gender                                        VARCHAR(10)," \
                 "   Father_Name                                   VARCHAR(100)," \
                 "   Mother_Name                                   VARCHAR(100)," \
                 "   Date_Of_Birth                                 VARCHAR(10)," \
                 "   Candidate_Age                                 INTEGER," \
                 "   Email_Address                                 VARCHAR(100)," \
                 "   Mobile_No                                     VARCHAR(15)," \
                 "   Martial_Status                                VARCHAR(10)," \
                 "   Higher_Education                              VARCHAR(100)," \
                 "   Matriculation_Board                           VARCHAR(100)," \
                 "   Username                                      VARCHAR(100)                    PRIMARY KEY," \
                 "   Password                                      VARCHAR(100)," \
                 "   House_No                                      VARCHAR(50)," \
                 "   Address                                       TEXT," \
                 "   Village                                       VARCHAR(100)," \
                 "   City_Town                                     VARCHAR(100)," \
                 "   District                                      VARCHAR(100)," \
                 "   Tensil                                        VARCHAR(100)," \
                 "   Block_Locality                                VARCHAR(100)," \
                 "   Pin_No                                        VARCHAR(10)," \
                 "   Police_Station                                VARCHAR(100)," \
                 "   Post_Office                                   VARCHAR(100)," \
                 "   Telegram_Office                               VARCHAR(100)," \
                 "   Category                                      VARCHAR(100)," \
                 "   Sport                                         VARCHAR(50)," \
                 "   NCC                                           VARCHAR(10)," \
                 "   Special_Category                              VARCHAR(100)," \
                 "   Highest_Education                             VARCHAR(100)," \
                 "   Qualifying_Course                             VARCHAR(100)," \
                 "   Board_Education_University                    VARCHAR(50)," \
                 "   Name_of_the_University_Board                  VARCHAR(100)," \
                 "   Name_in_Matriculation_Certificate             VARCHAR(100)," \
                 "   Year_Of_Passing                               VARCHAR(10)," \
                 "   Roll_No                                       VARCHAR(100)," \
                 "   Certificate_No                                VARCHAR(100)," \
                 "   Medical_Test                                  VARCHAR(10)," \
                 "   Physical_Test                                 VARCHAR(10)," \
                 "   Written_Test                                  INTEGER" \
                 ")"

        cursor.execute(query2)
        connect.commit()

    # For calculating the age of the person
    def age(self, birthdate):
        today = date.today()
        present_age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return present_age

    # Final Layout
    def last_screen(self):
        # screen for output
        screen = turtle.Screen()
        screen.setup(width=0.99999999999999999999999999999999999, height=0.999999999999999999999999999999999999)

        # Defining a turtle Instance
        t = turtle.Turtle()
        speed(0)

        # initially penup()
        t.penup()
        t.goto(-400, 250)
        t.pendown()

        # Orange Rectangle
        # white rectangle
        t.color("orange")
        t.begin_fill()
        t.forward(800)
        t.right(90)
        t.forward(167)
        t.right(90)
        t.forward(800)
        t.end_fill()
        t.left(90)
        t.penup()
        t.goto(-400, -83)
        t.pendown()

        # Green Rectangle
        t.color("green")
        t.begin_fill()
        t.forward(167)
        t.left(90)
        t.forward(800)
        t.left(90)
        t.forward(167)
        t.end_fill()

        # Big Blue Circle
        t.penup()
        t.goto(70, 0)
        t.pendown()
        t.color("navy")
        t.begin_fill()
        t.circle(70)
        t.end_fill()

        # Big White Circle
        t.penup()
        t.goto(60, 0)
        t.pendown()
        t.color("white")
        t.begin_fill()
        t.circle(60)
        t.end_fill()

        # Mini Blue Circles
        t.penup()
        t.goto(-57, -8)
        t.pendown()
        t.color("navy")
        for i in range(24):
            t.begin_fill()
            t.circle(3)
            t.end_fill()
            t.penup()
            t.forward(15)
            t.right(15)
            t.pendown()

        # Small Blue Circle
        t.penup()
        t.goto(20, 0)
        t.pendown()
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        # Spokes
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.pensize(2)
        for i in range(24):
            t.forward(60)
            t.backward(60)
            t.left(15)

        # to write Agnipath  Yojana Entey Scheme
        t.penup()
        t.goto(0, 340)
        t.pendown()
        t.color('red')
        style = ('Arial', 40, 'bold')
        t.write('***** Agnipath  Yojana Entry Scheme *****', font=style, align='center')

        # to write proud to be an indian
        t.penup()
        t.goto(0, 295)
        t.pensize()
        t.color('blue')
        style = ('Arial', 25, 'bold')
        t.write('PROUD TO BE AN INDIAN', font=style, align='center')

        # to write Thanks
        t.penup()
        t.goto(0, -320)
        t.pendown()
        t.color('red')
        style = ('Arial', 30, 'bold')
        t.write('Thanks for Visiting', font=style, align='center')

        # to hold the
        # output window
        turtle.done()

    # For exiting the section
    def exit(self):
        print("\nDo you want to exit? (Y/N)")
        ch = input()
        if ch in 'Yy':
            time.sleep(3)
            agniipath.last_screen(self)
            quit("Thanks for visiting..........\nCome again..........")

    # Zonal Recruitment Office in Ambala
    def ambala(self):
        print("=" * 150)
        print(" " * 50 + "*** About the Zonal Recruitment Office in Ambala ***")
        print("=" * 150 + "\n")
        print("""                 
                                                  1.	Headquarters Recruiting Zone Ambala
                                                                 Address : Chandrasekher Marg, Ambala Cantt - Pin - 133001.
                                                                 Telephone No 0171-2640826
                                                                 E-mail : pracha.99916@gov.in
                                                  2.	Army Recruiting Office Rohtak	
                                                                 Address : Civil Road, Rohtak - Pin - 124001.
                                                                 Telephone No 01262-268568
                                                                 E-mail : rohtakaro.123@gov.in
                                                  3.	Army Recruiting Office Hisar	
                                                                 Address : Hisar Military Station - Pin - 125001.
                                                                 Telephone No 0166-2297961
                                                                 E-mail : rainbow-109@gov.in
                                                  4.	Army Recruiting Office Charkhi Dadri	
                                                                 Address : Charkhi Dadri - Pin - 123306.
                                                                 Telephone No 01250-220037
                                                                 E-mail : gsatyajeet.580y@gov.in
                                                  5.	Army Recruiting Office Palampur
                                                                 Address : Palampur (HP) - Pin - 176001.
                                                                 Telephone No 01894-235526
                                                                 E-mail : hpps1828@nic.in
                                                  6.	Army Recruiting Office Shimla	
                                                                 Address : Shimla (HP) - Pin - 171003.
                                                                 Tele No 0177-2652804
                                                                 E-mail : gana.ga73@nic.in
                                                  7.	Army Recruiting Office Hamirpur	
                                                                 Address : Hira Nagar, Hamirpur (HP) - Pin - 177001.
                                                                 Telephone No 01972-222214
                                                                 E-mail : virbhumi.01@gov.in
                                                  8.	Army Recruiting Office Mandi	
                                                                 Address : Vijay Palace, Mandi (HP) - Pin - 175001.
                                                                 Telephone No 01905-222740
                                                                 E-mail : somgul.87539@gov.in\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in Bangalore
    def bangalore(self):
        print("=" * 150)
        print(" " * 50 + "*** About the Zonal Recruitment Office in Bangalore ***")
        print("=" * 150 + "\n")
        print("""                          
                                              1.	Headquarters Recruiting Zone Bangalore	
                                                             Address : 148, Field Marshal KM Cariappa Road, Bangalore - Pin - 560025.
                                                             Telephone No :080-29516517
                                                             E-mail : arobengaluru@gmail.com
                                              2.	Army Recruiting Office Belgaum
                                                             Address : Fort Belgaum, Belgaum - Pin - 590016.
                                                             Telephone No :0831-2950001
                                                             E-mail : arobgm4@gmail.com
                                              3.	Army Recruiting Office Calicut
                                                             Address : West Hill Barracks, Calicut - Pin - 673005.
                                                             Telephone No :0495-2383953
                                                             E-mail : malabarhill-67@gov.in
                                              4.	Army Recruiting Office Mangalore
                                                             Address : Kulur Post, Mangalore - Pin - 575013.
                                                             Telephone No :0824-2951279
                                                             E-mail : teamman-2021@gov.in
                                              5.	Army Recruiting Office Trivendrum
                                                             Address : Thirumala Post, Trivendrum - Pin - 695006.
                                                             Telephone No :0471-2352373
                                                             E-mail : meraoffice-94@gov.in\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in Chennai
    def chennai(self):
        print("=" * 150)
        print(" " * 50 + "*** About the Zonal Recruitment Office in Chennai ***")
        print("=" * 150 + "\n")
        print("""                          
                                          1.	Headquarters Recruiting Zone Chennai	
                                                         Address : Fort Saint George, Chennai - PIN - 600009
                                                         Telephone Number : 044-25675262
                                                         E-mail address : ground.warrious@gov.in
                                                                        : overwork@nic.in
                                          2.	Army Recruiting Office Coimbatore
                                                         Address : Red Fields, Coimbatore (TN) - PIN - 641018.
                                                         Telephone Number : 0422-2223056
                                                         E-mail address : coimaro13.tncbe@nic.in
                                          3.	Army Recruiting Office Guntur
                                                         Address : Pattabipuram Post, Ravindra Nagar Guntur (AP) - PIN - 522006.
                                                         Telephone Number : 0863-2230008
                                                         E-mail address : rogun-ap@nic.in
                                          4.	Army Recruiting Office Visakhapatnam
                                                         Address : Railway New Colony, Station Road, Visakhapatnam (AP) - PIN - 530004.
                                                         Telephone Number : 0891-2754680
                                                         E-mail address : arovizag.123@gov.in
                                          5.	Army Recruiting Office Trichy
                                                         Address : Guruda Lines, Trichy (TN) - PIN - 620001.
                                                         Telephone Number : 0431-2412254
                                                         E-mail address : recruiting0443.tn@nic.in
                                          6.	Army Recruiting Office, Secunderabad	
                                                         Address : Manovikas Nagar Post, Secunderabad (TS) - PIN - 500009
                                                         Telephone Number : 040-27740205
                                                         E-mail address : arosbad-ap@nic.in
                                          7.	Director Recruiting RO (HQ) Chennai	
                                                         Address : Fort Saint Gearge, Chennai - PIN - 600009
                                                         Telephone Number : 044-25674924
                                                         E-mail address : rohqchennai.tn@nic.in\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in Danapur
    def danapur(self):
        print("=" * 150)
        print(" " * 50 + "*** About the Zonal Recruitment Office in Danapur ***")
        print("=" * 150 + "\n")
        print("""                          
                                                          1.	Headquarters Recruiting Zone Danapur	
                                                                         Address : (Bihar & Jharkhand) - Pin - 801503.
                                                                         Tele No : 06115-291057 & 220328
                                                                         E-mail : maur.maha@nic.in
                                                          2.	Army Recruiting Office Muzaffarpur
                                                                         Address : Muzaffarpur - Pin - 842001.
                                                                         Telephone No : 0621-2215442
                                                                         E-mail : bjasrotia.427@gov.in
                                                          3.	Army Recruiting Office Gaya
                                                                         Address : Paharpur, Gaya - Pin - 823005.
                                                                         Telephone No : 0631-2970818
                                                                         E-mail : arogaya2983@gmail.com
                                                          4.	Army Recruiting Office Katihar
                                                                         Address : Military Camp, Katihar - Pin - 854106.
                                                                         Telephone No : 06452-239035
                                                                         E-mail : sirsa.ktri@nic.in
                                                          5.	Army Recruiting Office Ranchi
                                                                         Address : Ranchi (Jharkhand) - Pin - 834001.
                                                                         Telephone No : 0651-2332349
                                                                         E-mail : rncro.69@nic.in\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in Jabalpur
    def jabalpur(self):
        print("=" * 150)
        print(" " * 50 + "*** About the Zonal Recruitment Office in Jabalpur ***")
        print("=" * 150 + "\n")
        print("""                          
                                             1.	Headquarters Recruiting Zone Jabalpur	
                                                            Address : T-23, Ridge Road, Jabalpur (MP) - Pin - 482001.
                                                            Telephone No : 0761-2607401 & 2607636
                                                            E-mail : orange-gold@nic.in
                                             2.	Army Recruiting Office Bhopal
                                                            Address : Bhopal - Pin - 462001.
                                                            Telephone No : 0755-2539948
                                                            E-mail : raobho_mp@nic.in
                                             3.	Army Recruiting Office Gwalior
                                                            Address : P-7 Garam Sadak, Near Head Post Office, Gwalior (MP) - Pin - 474004.
                                                            Telephone No : 0751-2466414
                                                            E-mail : arogwa-mp@nic.in
                                             4.	Army Recruiting Office Mhow
                                                            Address : 4 Bakery Road, Mhow (MP), Near Post Office Mhow - Pin - 453441.
                                                            Telephone No : 07324-292567
                                                            E-mail : aromhow@gmail.com
                                             5.	Army Recruiting Office Raipur
                                                            Address : Near Shaheed Veer Narayan Singh International Cricket Stadium, 
                                                                      Naya Raipur(CG) (Chhattisgarh) - Pin - 492101.
                                                            Telephone No : 0771-2965214
                                                            E-mail : aro.raipur.cg@nic.in\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in Jaipur
    def jaipur(self):
        print("=" * 150)
        print(" " * 50 + "*** About the Zonal Recruitment Office in Jaipur ***")
        print("=" * 150 + "\n")
        print("""                          
                                                         1.	Headquarters Recruiting Zone Jaipur	
                                                                        Address : c/o 56 APO - Pin - 900337
                                                                        Telephone No : 0141-2776128
                                                                        E-mail : kailashjha.557k@gov.in
                                                         2.	Army Recruiting Office Alwar	
                                                                        Address : c/o 56 APO - Pin - 901301 
                                                                        Telephone No : 0144-2703169
                                                                        E-mail : lalgulab@nic.in
                                                         3.	Army Recruiting Office Jodhpur	
                                                                        Address : c/o 56 APO - Pin - 900066
                                                                        Telephone No : 0291-25141556
                                                                        E-mail : kalagulab@nic.in
                                                         4.	Army Recruiting Office Kota	
                                                                        Address : c/o 56 APO - Pin - 901151
                                                                        Telephone No : 0744-2322505
                                                                        E-mail : ahsbk@nic.in
                                                         5.	Army Recruiting Office Jhunjhunu	
                                                                        Address : c/o 56 APO - Pin - 333001 
                                                                        Telephone No : 01592-250192
                                                                        E-mail : haveli@nic.in
                                                         6.	Recruiting Office (HQ) Jaipur	
                                                                        Address : c/o 56 APO - Pin - 900337
                                                                        Telephone No : 0141-2235774
                                                                        E-mail : prwaman.046m@gov.in\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in Jalandhar
    def jalandhar(self):
        print("=" * 150)
        print(" " * 50 + "*** About the Zonal Recruitment Office in Jalandhar ***")
        print("=" * 150 + "\n")
        print("""                          
                                                      1.	Headquarters Recruiting Zone Jalandhar	
                                                                     Address : Jalandhar Cantt - Pin - 144005
                                                                     Telephone No : 0181-2660085
                                                                     E-mail : 3emini3na.45@gov.in
                                                      2.	Army Recruiting Office Amritsar cantt	
                                                                     Address : Amritsar Cantt - Pin - 143001
                                                                     Telephone No : 01832223361
                                                                     E-mail : tveerandra328f@gov.in 
                                                      3.	Army Recruiting Office Ferozpur cantt	
                                                                     Address : 41, Dass Road, Ferozpur Cantt - Pin - 152001,
                                                                     Telephone No : 0163-2249119
                                                                     E-mail : udaasee.mun@gov.in
                                                      4.	Army Recruiting Office Ludhiana	
                                                                     Address : Ludhiana - Pin - 141001
                                                                     Telephone No : 0161-2412123
                                                                     E-mail : 3emini.janed@gov.in
                                                      5.	Army Recruiting Office Patiala	
                                                                     Address : 27, The Mail, Patiala - Pin - 147001,
                                                                     Telephone No : 0175-2300013
                                                                     E-mail :terrafirma.45@gov.in 
                                                      6.	Army Recruiting Office Jammu	
                                                                     Address : Jammu - Pin - 185005,
                                                                     Telephone No : 0191-2582574
                                                                     E-mail :aroheadclk.2019@gov.in
                                                      7.	Army Recruiting Office Srinagar	
                                                                     Address : Srinagar, c/o 31 Sub Area,
                                                                     Telephone No : 0194-2311282
                                                                     E-mail :pikora1s.65@gov.in\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in Kolkata
    def kolkata(self):
        print("=" * 150)
        print(" " * 50 + "*** About the Zonal Recruitment Office in Kolkata ***")
        print("=" * 150 + "\n")
        print("""                          
                                       1.	Headquarters Recruiting Zone Kolkata	
                                                      Address : 1 Gokhale Road, Kolkata - Pin -700020
                                                      Telephone No : 033-22237152
                                                      E-mail : exidemorh@nic.in
                                       2.	Recruiting Headquarters Kolkata	
                                                      Address : 1 Gokhale Road, Kolkata - Pin -700020
                                                      Telephone No : 033-22237150
                                                      E-mail : victoria.queen@nic.in 
                                       3.	Army Recruiting Office Cuttack
                                                      Address : Cantonment Road PO - Buxi Bazar Dist - Cuttack - Pin - 753001
                                                      Telephone No : 0671-2305280
                                                      E-mail : raja.buxi@nic.in
                                       4.	Army Recruiting Office Sambalpur
                                                      Address : Building No 254, Dhanipali Professor Colony, 
                                                                Sambalpur (Orissa) - Pin - 768004
                                                      Telephone No : 0663-2520845
                                                      E-mail : budhar.raj@nic.in
                                       5.	Army Recruiting Office Gopalpur
                                                      Address : Gopalpur Military Station, PO- Golabandha Dist - Ganjam, Pin - 761052
                                                      Telephone No : 0680-2343911
                                                      E-mail : golabandha@nic.in
                                       6.	Army Recruiting Office Barraackpore
                                                      Address : 43 Middle Road, Barrackpore Cantt District - 24,
                                                                Parganas (WB) - Pin - 700120
                                                      Telephone No : 033-25452958 & 29770813
                                                      E-mail : live@nic.in
                                       7.	Army Recruiting Office Siliguri
                                                      Address : Near Main Gate, Sevoke Road Military Station, PO - Salugra,
                                                                District - Jalpaiguri, Pin - 734008
                                                      Telephone No : 0353-2590040
                                                      E-mail : creatorsil@nic.in
                                       8.	Army Recruiting Office Berhampore
                                                      Address : Panchanantala Opposite BDO Office, 
                                                                PO-Chaltiya District - Murshidabad (WB) Pin - 7422407
                                                      Telephone No : 03482-274016
                                                      E-mail : bhr2005.70@nic.in\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in Lucknow
    def lucknow(self):
        print("=" * 150)
        print(" " * 50 + "*** About the Zonal Recruitment Office in Lucknow ***")
        print("=" * 150 + "\n")
        print("""                          
                                            1.	Headquarters Recruiting Zone Lucknow	
                                                           Address : 236 Mahatma Gandhi Road, Lucknow Cantt - Pin - 226002
                                                           Telephone No : 0522-2292864 & 2483938
                                                           E-mail : quizzing.3639@nic.in
                                            2.	Army Recruiting Office Varanasi Cantt	
                                                           Address : OGB, 24 Ranbakure Stadium Near DM Residence, Varanasi - Pin - 221002
                                                           Telephone No : 0542-2506655
                                                           E-mail : vararo@nic.in
                                            3.	Army Recruiting Office Agra Cantt	
                                                           Address : 65, Taj Road, Agra Cantt - Pin - 282001
                                                           Telephone No : 0562-2226084
                                                           E-mail : shivshakti@nic.in
                                            4.	Army Recruiting Office Bareilly	
                                                           Address : Fort Raod, Bareilly Cantt, Bareilly (UP) - Pin - 243001
                                                           Telephone No : 0581-2972877, 0581-2972880
                                                           E-mail : b4fhls4@nic.in
                                            5.	Army Recruiting Office Meerut Cantt
                                                           Address : Western Road, Meerut Cantt (UP) PIN-250001
                                                           Telephone No : 460115-6916
                                                           E-mail : tigerbharti@gov.in
                                            6.	Army Recruiting Office Amethi Cantt	
                                                           Address : 24 IDSMT Building, Biseshar Ganj,
                                                                     Kithawar Road District - Amethi - Pin - 247405
                                                           Telephone No : 05368-297251
                                                           E-mail : amero.66@nic.in
                                            7.	Army Recruiting Office Almora	
                                                           Address : Almora (Uttrakhand) - Pin - 263601
                                                           Telephone No : 05962-298449 & 297192
                                                           E-mail : vijaydwar@nic.in
                                            8.	Army Recruiting Office Pithoragarh	
                                                           Address : Pithoragarh (Uttrakhand) - Pin 262520
                                                           Telephone No : 05964-297850
                                                           E-mail : barkatia@nic.in
                                            9.	Army Recruiting Office Lansdowne	
                                                           Address : Lansdowne, Dist-Pauri Garhwal (Uttrakhand) - Pin 246155
                                                           Telephone No : 7417799317
                                                           E-mail : bmsta@nic.in\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in Pune
    def pune(self):
        print("=" * 150)
        print(" " * 50 + "*** About the Zonal Recruitment Office in Pune ***")
        print("=" * 150 + "\n")
        print("""                          
                                            1.	Headquarters Recruiting Zone Pune	
                                                           Address : Pune, Rajendra Sinhji Road, Pune - Pin - 411001
                                                           Telephone No :020-26360349
                                                           E-mail : ashiapp.55990@nic.in
                                            2.	Army Recruiting Office Mumbai	
                                                           Address : Mumbai near Afghan Church, Navy Nagar, Colaba, Mumbai, 
                                                                     Maharashtra - Pin - 400005
                                                           Tele No :022-22153510
                                                           E-mail : navkad.55990@gov.in
                                            3.	Army Recruiting Office Aurangabad	
                                                           Address : T/39, Assey Lines, Aurangabad, Maharashtra - Pin - 431002 
                                                           Telephone No :240-2371418
                                                           E-mail : maratha-8899@gov.in
                                            4.	Army Recruiting Office Nagpur	
                                                           Addess : Nagpur - Pin - 900419, C/o 56 APO
                                                           Telephone No :0712-2558020
                                                           E-mail : yuvapalan@nic.in
                                            5.	Army Recruiting Office Kolhapur
                                                           Address : Kolhapur, Temblai Hill, Maharashtra - Pin - 416004
                                                           Telephone No :0231-2605491
                                                           E-mail : kolmar.atha@nic.in
                                            6.	Army Recruiting Office Jamnagar	
                                                           Address : Jamnagar - Pin - 900265, c/o 56 APO
                                                           Telephone No :0288-2550346
                                                           E-mail : arojamnagar@gmail.com
                                            7.	Army Recruiting Office Ahmedabad	
                                                           Address : Ahmedabad, Airport Road, Gujarat - Pin - 380003
                                                           Telephone No :079-22861338
                                                           E-mail : sriche.19416@gov.in
                                            8.	Headquarters Artillery Centre Nasik Road Camp	
                                                           Address : c/o 56 APO - Pin - 908802
                                                           Telephone No- 0253-2418574
                                            9.	RO HQ Pune	
                                                           Address : Recruiting Office (HQ), HQ Recruiting Zone, Pune - Pin - 900449
                                                           Telephone No- 020-26345005
                                                           E-mail : dirrohqpune@gmail.com\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in Shillong
    def shillong(self):
        print("=" * 150)
        print(" " * 49 + "*** About the Zonal Recruitment Office in Shillong ***")
        print("=" * 150 + "\n")
        print("""                          
                                          1.	Headquarters Recruiting Zone Shillong	
                                                         Address : Shillong - Pin - 793001
                                                         Telephone No : 0364-2505024
                                                         E-mail : rainwater@nic.in
                                          2.	Army Recruiting Office Silchar Cantt	
                                                         Address : Silchar Cantt, District-Cachar (Assam),
                                                                   PO - Arunachal - Pin - 788025
                                                         Telephone No : 03842-261978
                                                         Email : Sweet.65@nic.in
                                          3.	Army Recruiting Office Rangapahar	
                                                         Address : Rangapahar, Dimapur, Nagaland - Pin - 797112
                                                         Telephone No : 03862-249012
                                                         E-mail : arorangapahar17@gmail.com & swarkoila@nic.in
                                          4.	Army Recruiting Office Jorhat	
                                                         Address : Jorhat, District - Jorhat (Assam) - Pin - 785001
                                                         Telephone No : 0376-2333136
                                                         E-mail : Ap.upper@nic.in
                                          5.	Army Recruiting Office Narangi	
                                                         Address : Narangi (Guwahati) - Pin - 780027, c/o 101 Area Postal Unit
                                                         Telephone No : 0361-2641985
                                                         E-mail : sisputana@nic.in
                                          6.	Army Recruiting Office Aizawl	
                                                         Address : Aizawl, Aizawl (Mizoram), c/o 806 FPO, Pin - 796001
                                                         Telephone No : 0389-2351518 & 2351166
                                                         E-mail : tarzan.boy@nic.in\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in GRD Kunraghat Gorakhpur
    def grd(self):
        print("=" * 150)
        print(" " * 45 + "*** About the Zonal Recruitment Office in GRD Kunraghat Gorakhpur ***")
        print("=" * 150 + "\n")
        print("""                          
                                          1.	Gorkha Recruiting Depot Kunraghat
                                                         Address : Gorkha Recruiting Depot, Kunraghat, Gorakhpur (UP) Pin - 273008
                                                         Telephone No : 0551- 2271751
                                          2.	Gorkha Recruiting Depot Ghoom
                                                         Address : Gorkha Recruiting Depot Ghoom, Darjeeling (WB) Pin - 734102
                                                         Telephone No : 0357 - 2257118\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Zonal Recruitment Office in IRO Delhi Cantt
    def iro(self):
        print("=" * 150)
        print(" " * 45 + "*** About the Zonal Recruitment Office in IRO Delhi Cantt ***")
        print("=" * 150 + "\n")
        print("""                          
                                                          1.	Independent Recruiting Office Delhi Cantt
                                                          Address : Near Base Hospital, Delhi Cantt - Pin - 110010
                                                          Email Id - reachak@golden.nic.in
                                                          Tel No - 011-25686451\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.zonal(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Zonal Recruitment Office
    def zonal(self):
        print("=" * 150)
        print(" " * 49 + "*** Information About Zonal Recruitment Office ***")
        print("=" * 150 + "\n")
        print(" " * 60 + " 1. Ambala")
        print(" " * 60 + " 2. Bangalore")
        print(" " * 60 + " 3. Chennai")
        print(" " * 60 + " 4. Danapur")
        print(" " * 60 + " 5. Jabalpur")
        print(" " * 60 + " 6. Jaipur")
        print(" " * 60 + " 7. Jalandhar")
        print(" " * 60 + " 8. Kolkata")
        print(" " * 60 + " 9. Lucknow")
        print(" " * 60 + "10. Pune")
        print(" " * 60 + "11. Shillong")
        print(" " * 60 + "12. GRD Kunraghat Gorakhpur")
        print(" " * 60 + "13. IRO Delhi Cantt\n")
        print("+" * 150 + "\n")
        print(" " * 60 + " a. Enter 14 to Go Back")
        print(" " * 60 + " b. Enter 15 to Exit\n")
        print("=" * 150)

        while True:
            try:
                choose = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if choose == 1:
                agniipath.ambala(self)
                break

            elif choose == 2:
                agniipath.bangalore(self)
                break

            elif choose == 3:
                agniipath.chennai(self)
                break

            elif choose == 4:
                agniipath.danapur(self)
                break

            elif choose == 5:
                agniipath.jabalpur(self)
                break

            elif choose == 6:
                agniipath.jaipur(self)
                break

            elif choose == 7:
                agniipath.jalandhar(self)
                break

            elif choose == 8:
                agniipath.kolkata(self)
                break

            elif choose == 9:
                agniipath.lucknow(self)
                break

            elif choose == 10:
                agniipath.pune(self)
                break

            elif choose == 11:
                agniipath.shillong(self)
                break

            elif choose == 12:
                agniipath.grd(self)
                break

            elif choose == 13:
                agniipath.iro(self)
                break

            elif choose == 14:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.about(self)

            elif choose == 15:
                agniipath.exit(self)

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Eligibility Criteria for Recruitment Process
    def eligibility_criteria(self):
        print("=" * 150)
        print(" " * 40 + "*** Information About Eligibility Criteria for Recruitment Process ***")
        print("=" * 150 + "\n")
        print("""             
                             MINIMUM EDUCATION QUALIFICATION AND AGE CRITERIA TEST :

                             -----------------------------------------------------------------------------------------------------------
                             |  Ser. No	 |       Category      |                          Education                        |    Age    |
                             ------------|---------------------|-----------------------------------------------------------|-----------|
                             |    1.     |       Agniveer      | Class 10th /Matric with 45% marks in aggregate and 33% in | 17.5 - 21 |
                             |           |    (General Duty)   | each subject. For boards following grading system of D    |    Yrs    |
                             |           |      (All Arms)     | grade (33% - 40%) in individual subjects or equivalent of |           |
                             |           |                     | grade which contains 33% and overall aggregate in C2      |           |
                             |           |                     | grade or equivalent corresponding to 45% in aggregate.    |           |
                             |           |                     |                                                           |           |
                             |           |                     | Note : Candidates with valid Light Motor Vehicle (LMV)    |           |
                             |           |                     |        Driving License will be given preference for       |           |
                             |           |                     |        Driver requirements.                               |           |
                             |-----------|---------------------|-----------------------------------------------------------|-----------|
                             |    2.     |       Agniveer      | 10+2/Intermediate Exam Pass in Science with Physics,      | 17.5 - 21 |
                             |           |        (Tech)       | Chemistry, Maths and English with min 50% marks in        |    Yrs    |
                             |           |      (All Arms)     | aggregate and 40% in each subject.                        |           |
                             |           |                     |                                                           |           |
                             |           |                     |                           ( OR )                          |           |
                             |           |                     |                                                           |           |
                             |           |                     | 10+2 /Intermediate Exam Pass in Science with Physics,     |           |
                             |           |                     | Chemistry, Maths and English from any recognized State    |           |
                             |           |                     | Education Board or Central Education Board to include     |           |
                             |           |                     | NIOS and ITI course of minimum one year in required field |           |
                             |           |                     | with NSQF level 4 or above.                               |           |
                             |-----------|---------------------|-----------------------------------------------------------|-----------| 
                             |     3.    |    Agniveer Clerk   | 10+2 / Intermediate Exam Pass in any stream (Arts,        | 17.5 - 21 |
                             |           |          /          | Commerce, Science) with 60% marks in aggregate and        |    Yrs    |
                             |           |      Store Keeper   | minimum 50% in each subject. Securing 50% in English and  |           |
                             |           |       Technical     | Maths/Accounts /Book Keeping in Class XII is mandatory.   |           |
                             |           |       (All Arms)    |                                                           |           |
                             |-----------|---------------------|-----------------------------------------------------------|-----------|
                             |     4.    |  Agniveer Tradesmen | (i) Class 10th simple pass.                               | 17.5 - 21 |
                             |           |      (All Arms)     | (ii) No stipulation in aggregate percentage, but should   |    Yrs    |
                             |           |       10th pass     |      have scored 33% in each subject.                     |           |
                             |-----------|---------------------|-----------------------------------------------------------|-----------|
                             |     5.    |  Agniveer Tradesmen |(i) Class 8th simple pass.                                 | 17.5 - 21 |
                             |           |      (All Arms)     |(ii) No stipulation in aggregate percentage, but should    |    Yrs    |
                             |           |       8th pass      |     have scored 33% in each subject.                      |           |
                             |-----------|---------------------|-----------------------------------------------------------|-----------|
                             |     6.    |       Agniveer      | Class 10th /Matric with 45% marks in aggregate and 33% in | 17.5 - 21 |
                             |           |    (General Duty)   | each subject. For boards following grading system of D    |    Yrs    |
                             |           |  Women in Corps of  | grade (33% - 40%) in individual subjects or equivalent of |           |
                             |           |   Military Police   | grade which contains 33% and overall aggregate in C2 grade|           |
                             |           |                     | or equivalent corresponding to 45% in aggregate.          |           |
                             |           |                     |                                                           |           |
                             |           |                     | Note : Candidates with valid Light Motor Vehicle (LMV)    |           |
                             |           |                     |        Driving License will be given preference for       |           |
                             |           |                     |        Driver requirements.                               |           |
                             -----------------------------------------------------------------------------------------------------------

                              * Note :The upper age limit has been relaxed from 21 Years to 23 Years as a one time measure for the 
                                      Recruiting Year 2022-23.
        """)
        print()
        print("Press ENTER to continue...........")
        i = input()
        print("""

                              STANDARD MINIMUM HEIGHT, UNEXPANDED CHEST AND WEIGHT OF RECRUITS AT THE TIME OF ENROLMENT FOR AGNIVEER :

                              ----------------------------------------------------------------------------------------------------------
                              |    Regions   |       States       |                Height (cm)               |   Chest   |    Weight   |
                              |--------------|--------------------|------------------------------------------|-----------|-------------|
                              |              |                    |  Agniveer   |   Agniveer   |  Agniveer   |    (cm)   |     (Kg)    |
                              |              |                    | General Duty|   Technical  |  Clerk /    |           |             |
                              |              |                    |       &     |              | Store Keeper|           |             |
                              |              |                    |  Tradesmen  |              |  Technical  |           |             |
                              |--------------|--------------------|-------------|--------------|-------------|-----------|-------------|
                              |   Western    | Jammu & Kashmir,   |     163     |      163     |     162     |     77    |      48     |
                              |  Himalayan   | Himachal Pradesh,  |             |              |             |           |             |
                              |   Region     | Punjab Hills (Area |             |              |             |           |             |
                              |              | South and West of  |             |              |             |           |             |
                              |              | the Inter State    |             |              |             |           |             |
                              |              | Border between     |             |              |             |           |             |
                              |              | Himachal Pradesh   |             |              |             |           |             |
                              |              | and Punjab and     |             |              |             |           |             |
                              |              | North and East of  |             |              |             |           |             |
                              |              | Road Mukerian,     |             |              |             |           |             |
                              |              | Hoshiarpur, Garh   |             |              |             |           |             |
                              |              | Shankar, Ropar and |             |              |             |           |             |
                              |              | Chandigarh),       |             |              |             |           |             |
                              |              | Garhwal and Kumaon |             |              |             |           |             |
                              |              | (Uttarakhand)      |             |              |             |           |             |
                              |--------------|--------------------|-------------|--------------|-------------|-----------|-------------|
                              |    Eastern   | Sikkim, Nagaland,  |     160     |      157     |     160     |     77    |      48     |
                              |   Himalayan  | Arunachal Pradesh, |             |              |             |           |             |
                              |     Region   | Manipur, Tripura,  |             |              |             |           |             |
                              |              | Mizoram, Meghalaya,|             |              |             |           |             |
                              |              | Assam and Hill     |             |              |             |           |             |
                              |              | Region of West     |             |              |             |           |             |
                              |              | Bengal (Gangtok,   |             |              |             |           |             |
                              |              | Darjeeling and     |             |              |             |           |             |
                              |              | Kalimpong          |             |              |             |           |             |
                              |              | Districts)         |             |              |             |           |             |
                              |--------------|--------------------|-------------|--------------|-------------|-----------|-------------|
                              |    Western   | Punjab, Haryana,   |     170     |      170     |     162     |     77    | 	    50     |
                              |     Plains   | Chandigarh,Delhi,  |             |              |             |           |             |
                              |     Region   | Rajasthan and      |             |              |             |           |             |
                              |              | Western Uttar      |             |              |             |           |             |
                              |              | Pradesh (Meerut and|             |              |             |           |             |
                              |              | Agra Division)     |             |              |             |           |             |
                              |--------------|--------------------|-------------|--------------|-------------|-----------|-------------|
                              |    Eastern   | Eastern Uttar      |     169     |      169     |     162     |     77    |      50     |
                              |     Plains   | Pradesh, Bihar,    |             |              |             |           |             |
                              |     Region   | West Bengal,       |             |              |             |           |             |
                              |              | Jharkhand and      |             |              |             |           |             |
                              |              | Orissa             |             |              |             |           |             |
                              |--------------|--------------------|-------------|--------------|-------------|-----------|-------------|
                              |    Central   | Madhya Pradesh,    |     168     |      167     |     162     |     77    |      50     |
                              |     Region   | Chattisgarh,       |             |              |             |           |             |
                              |              | Gujarat,           |             |              |             |           |             |
                              |              | Maharashtra,       |             |              |             |           |             |
                              |              | Dadar,Nagar Haveli,|             |              |             |           |             |
                              |              | Daman and Diu      |             |              |             |           |             |
                              |--------------|--------------------|-------------|--------------|-------------|-----------|-------------|
                              |   Southern   | Andhra Pradesh,    |     166     |      165     |     162     |     77    |      50     |
                              |    Region    | Karnataka,Tamil    |             |              |             |           |             |
                              |              | Nadu, Kerala, Goa  |             |              |             |           |             |
                              |              | and Puducherry     |             |              |             |           |             |
                              ----------------------------------------------------------------------------------------------------------
        """)
        print()
        print("Press ENTER to continue.................")
        i = input()
        print("""

                              SPECIAL PHYSICAL STANDARDS :

                              Minimum physical standards as given below will apply to the followings:

                              ----------------------------------------------------------------------------------------------------------
                              |  Ser. No  |                 Physical Standards            |  Height (cm)  |  Chest (cm)  | Weight (Kg) |
                              |-----------|-----------------------------------------------|---------------|--------------|-------------|
                              |     1.    | Ladakhi                                       |	     157	  |       77 	 |      50     |
                              |-----------|-----------------------------------------------|---------------|--------------|-------------|
                              |     2.    | Gorkhas both Nepalese and Indian              | 	 157	  |       77	 |      48     |
                              |-----------|-----------------------------------------------|---------------|--------------|-------------|
                              |     3.    | Candidates from Andaman and Nicobar Islands,  |               |              |             |
                              |           | Lakshadweep Group of Islands including Minicoy|               |              |             |
                              |           |-----------------------------------------------|---------------|--------------|-------------|
                              |			  | (i) Settlers	                              |      165	  |       77	 |      50     | 
                              |           |-----------------------------------------------|---------------|--------------|-------------|
                              |           | (ii) Locals	                                  |      155	  |       77     |  	50     |
                              |-----------|-----------------------------------------------|---------------|--------------|-------------|
                              |      4.   | Tribals of Recognized Tribal Areas	          |      162	  |       77     |   	48     |
                              |-----------|-----------------------------------------------|---------------|--------------|-------------|
                              |      5.   | The Brigade of Guards	                      |      173	  |       77	 |      50     |
                              |-----------|-----------------------------------------------|---------------|--------------|-------------|
                              |      6.   | Medium Artillery	                          |      170	  |       77	 |      50     |
                              |-----------|-----------------------------------------------|---------------|--------------|-------------|
                              |      7.   | Corps of Military Police	                  |      173	  |       77	 |      50     |
                              |-----------|-----------------------------------------------|---------------|--------------|-------------|
                              |      8.   | Agniveer (General Duty) Women in Corps of     | 162 (04 cms   | 	  -      |Proportionate|
                              |           | Military Police	                              |    Height     |              |  to height  |
                              |           |                                               | relaxation for|              |  and age as |
                              |           |                                               |    certain    |              |   per Army  |
                              |           |                                               |  dispensation |              |   medical   |
                              |           |                                               | areas as given|              |  standards. |
                              |           |                                               |     in the    |              |             |
                              |           |                                               | notification) |              |             |
                              |-----------|-----------------------------------------------|---------------|--------------|-------------|
                              |     9.    |	Agniveer Clerk (Staff Duty) /                 |       162	  |        77    |   	50     | 
                              |           | Store Keeper Technical	                      |               |              |             |
                              |-----------|-----------------------------------------------|---------------|--------------|-------------|
                              |    10.    | RT JCO                                        |       160     |        77    |      50     |
                              |           | RT JCO (Gorkhas & Ladakhi region Candidates ) |       157     |        77    |      48     |
                              |-----------|-----------------------------------------------|--------------------------------------------|
                              |    11.    | Agniveer Tradesmen	                          | Minimum physical standards of the regions  |
                              |           |                                               | given above, minus 1 Cm chest and 2 Kg     |
                              |           |                                               | weight. Ht criteria would be as par with   |
                              |           |                                               | Soldier General Duty as relevant to the    |
                              |           |                                               | region.                                    |
                              |-----------|-----------------------------------------------|--------------------------------------------|
                              |    12.    | JCO Catering (ASC) / Survey Automated         | As applicable to Soldier General Duty for  |
                              |           | Cartographer (Engineers) / Havildar Education |	various regions.                           |
                              ----------------------------------------------------------------------------------------------------------
        """)
        print()
        print("Press ENTER to continue...............")
        i = input()
        print("""

                              RELAXATIONS IN PHYSICAL STANDARD :

                              The following categories will be permitted relaxations in physical standards as mentioned against each:

                              ----------------------------------------------------------------------------------------------------------
                              |  Ser. No |                Physical Standards               | Height (cm) |  Chest (cm)  |  Weight (Kg) |
                              |----------|-------------------------------------------------|-------------|--------------|--------------|
                              |    1.    | Son of Serving Soldier (SOS) / Ex-Servicemen    |      2      |      1       |    	2      |
                              |          | (SOEX), Son-in-Law of a War Widow (SOWW) and    |             |              |              |
                              |          | Widow of Ex-Servicemen Adopted Son/Son-in-Law   |             |              |              |
                              |          | of a War Widow, if she has no son and including |             |              |              |
                              |          | a legally adopted son of serving Soldier /      |             |              |              |
                              |          | Ex-Servicemen	                               |             |              |              |
                              |----------|-------------------------------------------------|-------------|--------------|--------------|
                              |    2.    | Outstanding Sportsmen (National / State & those |      2 	 |      3  	    |       5      |
                              |          | who represented District / College / School in  |             |              |              |
                              |          | State / University / Board Championship &       |             |              |              |
                              |          | earned 1st/ 2nd position)	                   |             |              |              |
                              |----------|-------------------------------------------------|-------------|--------------|--------------|
                              |    3.    | Agniveer (General Duty) Women in Corps of       |             |              |              |
                              |          | Military Police.			                       |             |              |              |
                              |          |-------------------------------------------------|-------------|--------------|--------------|
                              |          | (i) Daughter of Servicemen (DOS) & Daughter of  |      2      | 	    -       |  	    2      |
                              |          |     Ex-Servicemen (DOES), Daughter of War Widow |             |              |              |
                              |          |     (DOWW) and Daughter of Widow of             |             |              |              |
                              |          |     Ex-servicemen (DOW). For adopted daughter/  |             |              |              |
                              |          |     daughter in-law of a war widow, if she has  |             |              |              |
                              |          |     no daughter and including a legally adopted |             |              |              |
                              |          |     daughter(for consideration of daughter      |             |              |              |
                              |          |     in-law) of serving Soldier/Ex-Servicemen.   |             |              |              |
                              |          |     Adoption should have been done during the   |             |              |              |
                              |          |     lifetime of the Servicemen/Ex-servicemen.   |             |              |              |
                              |          |-------------------------------------------------|-------------|--------------|--------------|
                              |          | Widows of Defence pers who have died in harness.|	   2	 |       -	    |       2      |
                              |          |-------------------------------------------------|-------------|--------------|--------------|
                              |          | Outstanding Sportswomen (National/State & those |       2	 |       -	    |       5      |
                              |          | who represented District, College/School State/ |             |              |              |
                              |          | University Championship).	                   |             |              |              |
                              ----------------------------------------------------------------------------------------------------------
        """)
        print()
        print("Press ENTER to continue...............")
        i = input()
        print("""

                              AWARD OF BONUS MARKS FOR AGNIVEERS :

                              The following Bonus Marks will be awarded on qualifying in the written examination to under mentioned 
                              categories :

                              ----------------------------------------------------------------------------------------------------------
                              | Ser. No |              Category             |      Agniveer     |  Agniveer Clerk/ |       Agniveer    |
                              |         |                                   |   (General Duty)  |    Store Keeper  |  Tradesmen (Total |
                              |         |                                   |   (Total Maximum  |     Technical,   | maximum Marks 200)|
                              |         |                                   |     Marks 200)    |     Agniveer     |                   |
                              |         |                                   |                   | Technical (Total |                   |
                              |         |                                   |                   |Maximum Marks 200)|                   |
                              |---------|-----------------------------------|-------------------|------------------|-------------------|
                              |    1.   | Son of Serving (SOS) Soldier /    |      20 Marks	    |      20 Marks	   |      20 Marks     |
                              |         | Ex-Servicemen(SOEX) /Son-in-Law   |                   |                  |                   |
                              |         | of a War Widow(SOWW) / Son of     |                   |                  |                   |
                              |         | Widow (SOW) (One son only)	    |                   |                  |                   |
                              |---------|-----------------------------------|-------------------|------------------|-------------------|
                              |    2.   | Sportsmen:-			            |                   |                  |                   |
                              |         |-----------------------------------|-------------------|------------------|-------------------|
                              |         | (i) Represented India at the      |     20 Marks	    |     20 Marks	   |      20 Marks     |
                              |         |     International level	        |                   |                  |                   |
                              |         |-----------------------------------|-------------------|------------------|-------------------|
                              |         | (ii) Represented State at the     |     15 Marks	    |     15 Marks	   |      15 Marks     |
                              |         |      Senior/Junior National level |                   |                  |                   |
                              |         |      and have won any medal in    |                   |                  |                   |
                              |         |      individual event or have     |                   |                  |                   |
                              |         |      reached upto eighth position |                   |                  |                   |
                              |         |      in Team event	            |                   |                  |                   |
                              |         |-----------------------------------|-------------------|------------------|-------------------|
                              |         | (iii) Represented College /       |     10 Marks	    |     10 Marks	   |      10 Marks     |
                              |         |       University in Inter         |                   |                  |                   |
                              |         |       University Championship and |                   |                  |                   |
                              |         |       have won any medal in       |                   |                  |                   |
                              |         |       individual event or have    |                   |                  |                   |
                              |         |       reached up to sixth position|                   |                  |                   |
                              |         |       in the Team event	        |                   |                  |                   |
                              |         |-----------------------------------|-------------------|------------------|-------------------|
                              |         | (iv) Represented State at National|     10 Marks	    |     10 Marks	   |      10 Marks     |
                              |         |      Level in Khelo India Games   |                   |                  |                   |
                              |         |      and have won any medal in    |                   |                  |                   |
                              |         |      individual event or have     |                   |                  |                   |
                              |         |      reached upto sixth position  |                   |                  |                   |
                              |         |      in the team event	        |                   |                  |                   |
                              |         |-----------------------------------|-------------------|------------------|-------------------|
                              |         | (v) Represented Dist at the State |      05 Marks	    |     05 Marks	   |      05 Marks     |
                              |         |     Level and have won any medal  |                   |                  |                   |
                              |         |     in individual event or have   |                   |                  |                   |
                              |         |     reached upto fourth position  |                   |                  |                   |
                              |         |     in the Team event	            |                   |                  |                   |
                              |         |-----------------------------------|-------------------|------------------|-------------------|
                              |         | (vi) Represented the State school |      05 Marks 	|     05 Marks     |  	  05 Marks     |
                              |         |      team in the events org by All|                   |                  |                   |
                              |         |      India School Games Federation|                   |                  |                   |
                              |         |      and have won any medal in    |                   |                  |                   |
                              |         |      individual event or upto     |                   |                  |                   |
                              |         |      sixth position in the Team   |                   |                  |                   |
                              |         |      event	                    |                   |                  |                   |
                              |---------|-----------------------------------|-------------------|------------------|-------------------|
                              |    4.   | NCC 'A' Certificate	            |      05 Marks	    |     05 Marks	   |      05 Marks     |
                              |---------|-----------------------------------|-------------------|------------------|-------------------|
                              |    5.   | NCC 'B' Certificate	            |      10 Marks	    |     10 Marks	   |      10 Marks     |
                              |---------|-----------------------------------|-------------------|------------------|-------------------|
                              |    6.   | NCC 'C' Certificate               | Exempted from CEE	|     15 Marks	   | Exempted from CEE |
                              |---------|-----------------------------------|-------------------|------------------|-------------------|
                              |    7.   | NCC ‘C’ Certificate and           | Exempted from CEE	|Exempted from CEE | Exempted from CEE |
                              |         | participated in Republic Day      |                   |                  |                   |
                              |         | Parade	                        |                   |                  |                   |
                              |---------|-----------------------------------|-------------------|------------------|-------------------|
                              |    8.   | Candidates for Agniveer Clk/SKT   |	      --     	|       15 Marks   |          --       |  
                              |         | cat having ‘O’ level (IT) Course  |                   |                  |                   |
                              |         | Certificate issued by NIELIT and  |                   |                  |                   |
                              |         | having higher level IT Courses    |                   |                  |                   |
                              |         | Certificate from NIELIT           |                   |                  |                   |
                              |         | ie., ‘A’, ‘B’ or ‘C’ level. (‘O’  |                   |                  |                   |
                              |         | level (IT) course certificate     |                   |                  |                   |
                              |         | under DOEACC scheme issued only   |                   |                  |                   |
                              |         | by NIELIT on or after 01 Jan 2020.|                   |                  |                   |
                              |---------|-----------------------------------|-------------------|------------------|-------------------|
                              |    9.   | Bonus Marks for ITI/Skill         |                   |                  |                   |
                              |         | qualified candidates is as        |                   |                  |                   |
                              |         | under :-.			                |                   |                  |                   |
                              |         |-----------------------------------|-------------------|------------------|-------------------|
                              |         | (i) One year course at ITI	    |         --	    |       30 Marks   |	      --       |
                              |         |-----------------------------------|-------------------|------------------|-------------------|
                              |         | (ii) Two year course at ITI       |         --	    |       40 Marks   |          --       |
                              |         |-----------------------------------|-------------------|------------------|-------------------|
                              |         | (iii) Diploma holder	            |         --	    |       50 Marks   |  	      --       |
                              ----------------------------------------------------------------------------------------------------------

                              Note :
                              1. Maximum bonus marks that can be given is 20 Marks even if a candidate qualifies for more than one
                                 type of bonus marks except Agniveer (Technical).
                              2. Maximum bonus marks that can be given is 50 Mks even if a candidates qualifies fo more than one type
                                 of bonus marks to Agniveer (Technical).

        """)
        print()
        print("Press ENTER to continue.................")
        i = input()
        print("""

                              AGNIVEER (GENERAL DUTY) WOMEN IN CORPS OF MILITARY POLICE :

                              The following Bonus Marks will be awarded on qualifying in the written examination to Agniveer
                              (General Duty) Women in Corps of Military Police :

                              ----------------------------------------------------------------------------------------------------------
                              |   Ser. No   |                           Category                           |   Agniveer (General Duty) |
                              |             |                                                              | Women in Corps of Military|
                              |             |                                                              |    Police (Total Maximum  |
                              |             |                                                              |           Marks 200)      |
                              |-------------|--------------------------------------------------------------|---------------------------|
                              |      1.     | Daughter of Servicemen (DOS), Daughter of Ex-Servicemen      |          20 Marks         |
                              |             | (DOES), Daughter of War Widow(DOWW), Daughter of Widow of    |                           |
                              |             | Ex-Servicemen(DOW)	                                       |                           |
                              |-------------|--------------------------------------------------------------|---------------------------|
                              |      2.     | Widows of Def pers who have died in harness	               |          20 Marks         |
                              |-------------|--------------------------------------------------------------|---------------------------|
                              |      3.     | Sportswomen:-	                                               |                           |
                              |             |--------------------------------------------------------------|---------------------------|
                              |             | (i) Represented India at the International level	           |          20 Marks         |
                              |             |--------------------------------------------------------------|---------------------------|
                              |             | (ii) Represented State at the Senior/Junior National level   |          15 Marks         |
                              |             |      and have won any medal in individual event or have      |                           |
                              |             |      reached upto eighth posn in Team event	               |                           |
                              |             |--------------------------------------------------------------|---------------------------|
                              |             | (iii) Represented College / University in Inter University   |          10 Marks         |
                              |             |       Championship and have won any medal in individual      |                           |
                              |             |       event or have reached up to sixth posn in the          |                           |
                              |             |       Team event	                                           |                           |
                              |             |--------------------------------------------------------------|---------------------------|
                              |             | (iv) Represented State at National Level in Khelo India      |          10 Marks         |
                              |             |      Games and have won any medal in individual event or     |                           |
                              |             |      have reached upto sixth posn in the team event	       |                           |
                              |             |--------------------------------------------------------------|---------------------------|
                              |             | (v) Represented Dist at the State Level and have won any     |          05 Marks         |
                              |             |     medal in individual event or have reached upto fourth    |                           |
                              |             |     posn in the Team event                                   |                           |
                              |             |--------------------------------------------------------------|---------------------------|
                              |             | (vi) Represented the State school team in the events org by  |          05 Marks         |
                              |             |      All India School Games Federation and have won any      |                           |
                              |             |      medal in individual event or upto sixth posn in the     |                           |
                              |             |      Team event	                                           |                           |
                              |-------------|--------------------------------------------------------------|---------------------------|
                              |     4.      | NCC 'A' Certificate	                                       |          05 Marks         |
                              |-------------|--------------------------------------------------------------|---------------------------|
                              |     5.      | NCC 'B' Certificate	                                       |          10 Marks         |
                              |-------------|--------------------------------------------------------------|---------------------------|
                              |     6.      | NCC 'C' Certificate	                                       |     Exempted from CEE     |
                              ----------------------------------------------------------------------------------------------------------

                              Note :
                              1. Only one type of Bonus Marks (Max of the permissible) will be added to the total.
                              2. Bonus marks will be accorded on qualifying in the written examination.
                              3. Only one ward (daughter/son) of Service/Ex-Servicemen/War Widow/Widow of Ex-servicemen can avail
                                 bonus marks in written examination.
                              4. Original Certificates to be carried by all above categories at rally site.
                              5. Sports Certificate are valid for two years from the issue date as on first day of the recruitment 
                                 rally for which the candidate is being screened.
        """)
        print()
        print("Press ENTER to continue.................")
        i = input()
        print("""

                              DETAILS OF HQ RECRUITING ZONES AND ARMY RECRUITING OFFICES (AROs) :

                              ----------------------------------------------------------------------------------------------------------
                              |  Ser. No  |    HQ Recruiting Zone   |              STATE, UNION TERRITORY AND DISTRICTS                |
                              |-------------------------------------|------------------------------------------------------------------|
                              |     HQ RECRUITING ZONE, AMBALA	    |   HARYANA, (EXCEPT DISTRICTS OF GURGAON, FARIDABAD, MEWAT AND    |
                              |                                     |             PALWAL) HIMANCHAL PRADESH AND CHANDIGARH             |
                              |--------------------------------------------------------------------------------------------------------|
                              | HARYANA (Except Districts of Gurgaon, Faridabad, Mewat and Palwal)                                     |
                              |--------------------------------------------------------------------------------------------------------|
                              |    1.	  | RO (HQ), Ambala	        | Districts of Ambala, Karnal, Kurukshetra, Kaithal, Yamunanagar,  |
                              |           |                         | Panchkula and Union Terriroty of Chandigarh .                    |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    2.	  | Army Recruiting Office, | Districts of Rohtak, Sonipat, Jhajjar and Panipat.               |
                              |           | Rohtak	                |                                                                  |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    3. 	  | Army Recruiting Office, | Districts of Hisar, Sirsa, Jind, and Fatehabad.                  |
                              |           | Hisar	                |                                                                  |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    4.	  | Army Recruiting Office, | Districts of Mohindergarh, Bhiwani, Rewari and Charkhi Dadri.    |
                              |           | Charkhi Dadri	        |                                                                  |
                              |--------------------------------------------------------------------------------------------------------|
                              | HIMACHAL PRADESH                                                                                       |
                              |--------------------------------------------------------------------------------------------------------|
                              |    5.	  | Army Recruiting Office, | Districts of Chamba and Kangra.                                  |
                              |           | Palampur	            |                                                                  |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    6.	  | Army Recruiting Office, | Districts of Hamirpur, Una and Bilaspur.                         |
                              |           | Hamirpur	            |                                                                  |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    7.	  | Army Recruiting Office, | Districts of Shimla, Solan, Sirmaour and Kinnaur.                |
                              |           | Shimla	                |                                                                  |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    8.	  | Army Recruiting Office, | Districts of Mandi, Kullu and Lahaul Spiti Sub Division.         |
                              |           | Mandi	                |                                                                  |
                              |-------------------------------------|------------------------------------------------------------------|
                              |    HQ RECRUITING ZONE, BANGALORE    | KARNATAKA, KERALA AND UNION TERRITORY OF MAHE & LAKSHADWEEP      |
                              |--------------------------------------------------------------------------------------------------------|
                              | KARNATAKA                                                                                              |
                              |--------------------------------------------------------------------------------------------------------|
                              |    9.	  | RO (HQ), Bangalore	    | Districts of Bangalore Urban, Bangalore Rural, Kolar,            |
                              |           |                         | Chamrajnagar, Mysore, Mandya, Tumkur, Ramanagara, Chikaballapura,|
                              |           |                         | Bellary, Kodagu, Hassan, Chitradurga and Vijayanagara.           |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    10.	  | Army Recruiting Office, |Districts of Belgaum, Bidar, Gulbarga, Raichur, Koppal and Yadgir.|
                              |           | Belgaum	                |                                                                  |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    11.	  | Army Recruiting Office, | Districts of Chikmagalur, Dakshina Kannada, Uttar Kannada,       |
                              |           | Mangalore	            | Shimoga, Udupi, Davangere, Vijayapura, Bagalkot, Gadag,Haveri    |
                              |           |                         | and Dharwad.                                                     |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    12.	  | Army Recruiting Office, | Districts of Trivandrum, Kollam, Alleppey, Ernakulam, Kottayam,  |
                              |           | Trivandrum	            | Idukki and Pathanamthitta.                                       |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    13.    | Army Recruiting Office, | Districts of Calicut, Kasargod, Palghat, Malapuram, Wynad,       |
                              |           | Calicut	                | Cannanore, Trichur and UTs Mahe and Lakshadweep.                 |
                              |-------------------------------------|------------------------------------------------------------------|
                              | HQ RECRUITING ZONE, CHENNAI	        | TAMILNADU, ANDHRA PRADESH, UT OF PUDUCHERRY AND ANDAMAN &        |
                              |                                     | NICOBAR GROUP OF ISLANDS)                                        |
                              |--------------------------------------------------------------------------------------------------------|
                              | TAMIL NADU                                                                                             |
                              |--------------------------------------------------------------------------------------------------------|
                              |    14.	  | RO (HQ), Chennai	    | Districts of Chennai, Tiruvallur, Kancheepuram, Vellore,         |
                              |           |                         | Cuddalore, Viluppuram and Tiruvannamalai.UNION TERRITORY of      |
                              |           |                         | Puducherry District of Puducherry. Andaman and Nicobar Group of  |
                              |           |                         | Islands District of Andaman and Nicobar.                         |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    15.	  | Army Recruiting Office, | Districts of Tiruchirapalli, Karur, Perambalur, Ariyalur,        |
                              |           | Tiruchirapalli	        | Thanjaavur, Ramanathapuram, Tirunvelli, Pudukottai, Sivaganga,   |
                              |           |                         | Virudhunagar, Thoothukudi (Tuticorin), Kanniyakumari,            |
                              |           |                         | Nagapattinam and Thiruvarur.UNION TERRITORY of Puducherry        |
                              |           |                         | Karaikal                                                         |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    16.	  | Army Recruiting Office, | Districts of Coimbatore, Salem, Namakkal, The Nilgiris, Madurai, |
                              |           | Coimbatore	            |  Theni, Dharamapuri, Erode, Dindigul, Krishnagiri and Tiruppur.  |
                              |--------------------------------------------------------------------------------------------------------|
                              | ANDHRA PRADESH                                                                                         |
                              |--------------------------------------------------------------------------------------------------------|
                              |    17.    | Army Recruiting Office, | Districts of Guntur, YSR Kadapaa, Kurnool, Nellore, Prakasham,   |
                              |           | Guntur	                | Anantapur, Chittoor, Bapatla, Palnadu, Nandyal, Sri Sathya Sai,  |
                              |           |                         | Annamayya and Tirupati.                                          |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    18.	  | Army Recruiting Office, | Districts of Vishakapatnam, Srikakulam, East and West Godawari,  |
                              |           | Vishakapatnam           | Vizainagaram and Krishna (Vijaywada), Anakapalli, Alluri         |
                              |           |                         | Sitharama Raju, NTR, Parvathipuram, Manyam, Kakinada, Konaseema, |
                              |           |                         | Eluru andUNION TERRITORY of Puducherry. Districts of Yanam.      |
                              |--------------------------------------------------------------------------------------------------------|
                              | TELANGANA                                                                                              |
                              |--------------------------------------------------------------------------------------------------------|
                              |    19.    | Army Recruiting Office, | Districts of Adilabad, Bhadradri Kothagudem, Mancherial, Nirmal, |
                              |           | Secunderabad	        | Komaram Bheem, Jagtial, Jogulamba Gadwal, Peddapalli, Rajanna    |
                              |           |                         | Sircilla, Kamareddy, Hyderabad, Karimnagar, Nizamabad,           |
                              |           |                         | Mehbubnagar, Medak, Medchal Malkajgiri, Nalgonda, Nagarkurnool,  |
                              |           |                         | Warangal(Urban), Warangal(Rural), Jayashankar Bhupalpally,       |
                              |           |                         | Jangaon, Mahabubabad, Khammam and Ranga Reddy, Sangareddy,       |
                              |           |                         | Siddipet, Surypet, Vikarabad, Yadadri, Wanaparthy .              |
                              |-------------------------------------|------------------------------------------------------------------|
                              | HQ RECRUITING ZONE, DANAPUR	        | BIHAR AND JHARKHAND                                              |
                              |--------------------------------------------------------------------------------------------------------|
                              | BIHAR                                                                                                  |
                              |--------------------------------------------------------------------------------------------------------|
                              |    20.    | RO (HQ), Danapur	    | Districts of Patna, Bhojpur, Vaishali, Saran (Chhapra), Buxer,   |
                              |           |                         | Siwan and Gopalganj.                                             |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    21.    | Army Recruiting Office, | Districts of Muzaffarpur, Dharbhanga, Madhubani, East and West   |
                              |           | Muzaffarpur	            | Champaran, Sitamarhi, Samastipur and Sheohar.                    |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    22.	  | Army Recruiting Office, | Districts of Gaya, Aurangabad, Nawada, Nalanda, Rohtas, Kaimur   |
                              |           | Gaya                    | (Bhabua), Jahanabad, Sekhpura, Lakhi Sarai, Arwal and Jamui.     |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    23.	  | Army Recruiting Office, | Katihar	Districts of Katihar, Saharsha (Kosi), Bhagalpur,      |
                              |           | Gaya                    | Munger, Madhepura, Purnea, Banka, Araria, Kishanganj, Supaul,    |
                              |           |                         | Khagaria and Begusarai.                                          |
                              |--------------------------------------------------------------------------------------------------------|
                              | JHARKHAND                                                                                              |
                              |--------------------------------------------------------------------------------------------------------|
                              |    24.	  | Army Recruiting Office, | Districts of Ranchi, East and West Singhbhum, Dhanbad,           |
                              |           | Ranchi	                | Hazaribagh, Giridhih, Gumla, Lohardaga, Chatra, Bokaro, Koderma, |
                              |           |                         | Deoghar, Dumka, Jamtada, Saraikela, Simdega, Godda, Sahebgang,   |
                              |           |                         | Pakur, Jamtara, Palamu, Garwah, Latehar and Khunti.              |
                              |-------------------------------------|------------------------------------------------------------------|
                              |    HQ RECRUITING ZONE, JABALPUR	    | MADHYA PRADESH AND CHHATTISGARH                                  |
                              |--------------------------------------------------------------------------------------------------------|
                              | MADHYA PRADESH                                                                                         |
                              |--------------------------------------------------------------------------------------------------------|
                              |    25.    | RO (HQ), Jabalpur	    | Districts of Jabalpur, Anupur, Balaghat, Dindori, Jabalpur,      |
                              |           |                         | Katni, Mandla, Narsinghpur, Rewa, Satna, Seoni, Shahdol, Sidhi,  |
                              |           |                         | Singrauli and Umaria.                                            |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    26.    | Army Recruiting Office, | Districts of Gwalior, Ashoknagar, Bhind, Chhatapur, Damoh, Datia,|
                              |           | Gwalior	                | Guna, Gwalior, Morena, Niwari, Panna, Sagour, Shivpuri, Sheopur  |
                              |           |                         | and Tikamgarh.                                                   |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    27.    | Army Recruiting Office, | Districts of Mhow, Agar Malwa, Alirjpur, Barwani, Burhanpur,     |
                              |           | Mhow	                | Dewas, Dhar, Indore, Jhabua, East Nimar Khandwa, Khargone,       |
                              |           |                         | Mandsaur, Neemuch, Ratlam, Shajpur and Ujjain.                   |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    28.	  | Army Recruiting Office, | Districts of Bhopal, Betul, Chhindwada, Hoshangabad, Harda,      |
                              |           | Bhopal	                | Rajgarh, Raisen, Sehore and Vidisha.                             |
                              |--------------------------------------------------------------------------------------------------------|
                              | CHHATISGARH                                                                                            |
                              |--------------------------------------------------------------------------------------------------------|
                              |    29.    | Army Recruiting Office, | Districts of Raipur, Balrampur, Korea, Surajpur, Sarguja,        |
                              |           | Raipur	                | Joshpur, Gaurela Penda, Korba, Bilaspur, Mungeli, Raigarh,       |
                              |           |                         | Jangir Chamba, Kabirdham, Bemetra, Baloda Bazar, Durg, Raipur,   |
                              |           |                         | Mahassamund, Rajnandgaon, Balod, Gariabad, Dhamtari, Kanker,     |
                              |           |                         | Kondagaon, Narayanpur, Bastar, Bijapur, Dantewada and Sukma.     |
                              |-------------------------------------|------------------------------------------------------------------|
                              |      HQ RECRUITING ZONE, JAIPUR     | RAJASTHAN                                                        |
                              |-------------------------------------|------------------------------------------------------------------|
                              |    30.	  | RO (HQ), Jaipur	        | Districts of Jaipur and Sikar.                                   |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    31.	  | Army Recruiting Office, | Districts of Alwar, Bharatpur and Dholpur.                       |
                              |           | Alwar	                |                                                                  |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    32.	  | Army Recruiting Office, | Districts of Jhunjhunu, Hanumangarh, Bikaner, Sri Ganganagar and |
                              |           | Jhujhunu	            | Churu.                                                           |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    33.	  | Army Recruiting Office, | Districts of Jodhpur, Sirohi, Jalore, Barmer, Jaisalmer and      |
                              |           | Jodhpur	                | Nagpur.                                                          |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    34.	  | Army Recruiting Office, | Districts of Kota, Baran, Bundi, Jhalawar, Tonk, Karauli, Dausa, |
                              |           | Kota	                | Sawai Madhopur, Ajmer, Bhilwara, Chhitorgarh, Rajsamand, Pali,   |
                              |           |                         | Banswara, Dungarpur, Pratapgarh and Udaipur.                     |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    HQ RECRUITING ZONE, JALANDHAR	| PUNJAB AND JAMMU & KASHMIR                                       |
                              |--------------------------------------------------------------------------------------------------------|
                              | PUNJAB                                                                                                 |
                              |--------------------------------------------------------------------------------------------------------|
                              |    35. 	  | RO (HQ), Jalandhar	    | Districts of Jalandhar, Hoshiarpur, Kapurthala and SBS           |
                              |           |                         | Nagar(Nawashahar).                                               |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    36.	  | Army Recruiting Office, | Districts of Amritsar, Gurdaspur ,Tarn Taran and Pathankot.      |
                              |           | Amritsar	            |                                                                  |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    37.	  | Army Recruiting Office, | Districts of Ferozepur, Faridkot, Bhatinda ,Muktsar and Fazilka. |
                              |           | Ferozpur	            |                                                                  |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    38.	  | Army Recruiting Office, | Districts of Patiala, Sangur, Fatehgarh Sahib ,Mansa and barnala.|
                              |           | Patiala	                |                                                                  |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    39.	  | Army Recruiting Office, | Districts of Ludhiana, Rupnagar, SAS Nagar (Mohali) and Moga.    |
                              |--------------------------------------------------------------------------------------------------------|
                              | JAMMU & KASHMIR                                                                                        |
                              |--------------------------------------------------------------------------------------------------------|
                              |    40.	  | Army Recruiting Office, | Districts of Jammu, Kathua, Poonch, Udhampur, Doda, Rajouri,     |
                              |           | Jammu	                | Samba, Ramban, Reasi and Kistwar.                                |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    41.	  | Army Recruiting Office, | Districts of Srinagar, Anantnag, Ganderbal, Badgam, Baramulla    |
                              |           | Srinagar	            | and Kupwara.UNION TERRITORY of Ladakh (Districts of Leh and      |
                              |           |                         | Kargil).                                                         |
                              |-------------------------------------|------------------------------------------------------------------|
                              |      HQ RECRUITING ZONE, KOLKATA	| WEST BENGAL, SIKKIM AND ORISSA                                   |
                              |--------------------------------------------------------------------------------------------------------|
                              | WEST BENGAL                                                                                            |
                              |--------------------------------------------------------------------------------------------------------|
                              |    42.	  | RO (HQ), Kolkata	    | Districts of 24 Parganas (South), Kolkata, Midnapore (both East  |
                              |           | Srinagar	            | and West) and Howrah.                                            |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    43.	  | Army Recruiting Office, | Districts of Cooch Behar, Jalpaiguri, Uttar Dinajpur, Dakshin    |
                              |           | Siliguri	            | Dinajpur, Malda, Darjeeling, Kalimpong & State of Sikkim.        |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    44.	  | Army Recruiting Office, | Barrackpore Cantt	Districts of 24 Parganas (North), Hoogly,      |
                              |           | Siliguri	            | Bankura and Purulia.                                             |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    45.	  | Army Recruiting Office, | Districts of Murshidabad, Burdwan, Nadia, Birbhum, Purba         |
                              |           | Behrampore	            | Bardhaman and Paschim Bardhman.                                  |
                              |--------------------------------------------------------------------------------------------------------|
                              | ORISSA                                                                                                 |
                              |--------------------------------------------------------------------------------------------------------|
                              |    46.	  | Army Recruiting Office, | Districts of Cuttack, Puri, Balasore, Mayurbhanj, Bhadrak,       |
                              |           | Cuttack	                | Jagatsinghpur, Jajpur, Kendrapara, Khurda and Nayagarh.          |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    47.	  | Army Recruiting Office, | Districts of Sambalpur, Keonjhar, Sundergarh, Bargarh, Angul,    |
                              |           | Sambalpur	            | Deogarh, Jharsugura, Sonapur, Bolangir and Dhenkanal.            |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    48.	  | Army Recruiting Office, | Districts of Kalahandi, Koraput, Boudh, Gajapati, Malkangiri,    |
                              |           | Gopalpur Cantt	        | Nowapada, Nowrangpur, Kandhamal (Bhulbani) Rayagada and Ganjam.  |
                              |-------------------------------------|------------------------------------------------------------------|
                              |     HQ RECRUITING ZONE, LUCKNOW	    | UTTAR PRADESH AND UTTARAKHAND                                    |
                              |--------------------------------------------------------------------------------------------------------|
                              | UTTAR PRADESH                                                                                          |
                              |--------------------------------------------------------------------------------------------------------|
                              |    49.	  | RO (HQ), Lucknow	    | Districts of Lucknow, Gonda,  Unnao, Kanpur Dehat, Barabanki,    |
                              |           |                         | Kanpur Nagar, Fatehpur, Hamirpur, Mahoba, Banda, Chitrakut,      |
                              |           |                         | Ambedkar Nagar, Auraiya and Kannauj.                             |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    50.	  | Army Recruiting Office, | Districts of Meerut, Saharanpur, Bijnor, Muzaffarnagar,          |
                              |           | Meerut	                | Ghaziabad, Bulandshahar, Bagpat, Gautam Buddh Nagar, Jyotiba     |
                              |           |                         | Phule Nagar, Moradabad and Rampur.                               |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    51.	  | Army Recruiting Office, | Districts of Bareilly, Badaun, Pilibhit, Shahjahanpur, Hardoi,   |
                              |           | Bareilly	            | Sitapur, Lakhimpur Khiri, Farrukhabad, Bahraich, Shravasti and   |
                              |           |                         | Balrampur.                                                       |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    52.	  | Army Recruiting Office, | Districts of Agra, Mathura, Etawah, Jhansi, Jalaun, Firozabad,   |
                              |           | Agra	                | Lalitpur, Mainpuri, Maha Maya Nagar, Etah and Aligarh.           |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    53.	  | Army Recruiting Office, | Districts of Mirzapur, Varanasi, Jaunpur, Ghazipur, Sant Ravi    |
                              |           | Varanasi	            | Das Nagar, Azamgarh, Balia, Gorakhpur, Mau, Sonbhadra, Chandauli |
                              |           |                         | and Deoria.                                                      |
                              |-----------|-------------------------|------------------------------------------------------------------|
                              |    54.	  | Army Recruiting Office, | Districts of Raebareli, Allahabad, Pratapgarh, Koshambi,         |
                              |           | Amethi	                | Ambedkar Nagar, Faizabad, Sultanpur, Basti, Sant Kabir Nagar,    |
                              |           |                         | Sidharth Nagar, Kushinagar, and Maharajganj.                     |
                              |--------------------------------------------------------------------------------------------------------|
                              | UTTARAKHAND                                                                                            |
                              |--------------------------------------------------------------------------------------------------------|
                              |    55.     | Army Recruiting Office, | Districts of Tehri Garhwal, Uttarkashi, Rudra Prayag, Chamoli,  |
                              |            | Lansdowne	             | Dehradun, Pauri Garhwal and Haridwar.                           |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    56.	   | Army Recruiting Office, | Districts of Almora, Bageshwar, Udham Singh Nagar and Nainital. |
                              |            | Almora	                 |                                                                 |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    57.	   | Army Recruiting Office, | Districts of Pithoragarh and Chambhawat.                        |
                              |            | Pithoragarh	         |                                                                 |
                              |--------------------------------------|-----------------------------------------------------------------|
                              |        HQ RECRUITING ZONE, PUNE	     | MAHARASHTRA, GUJARAT AND UNION TERRITORIES OF DAMAN, DIU, DADAR |
                              |                                      | AND NAGAR HAVELI AND GOA                                        |
                              |--------------------------------------------------------------------------------------------------------|
                              | MAHARASHTRA                                                                                            |
                              |--------------------------------------------------------------------------------------------------------|
                              |    58.	   | RO (HQ), Pune	         | Districts of Pune, Ahmednagar, Osmanabad, Beed and Latur.       |
                              |------------|-------------------------|-----------------------------------------------------------------| 
                              |    59.	   | Army Recruiting Office, | Districts of Mumbai, Thane, Nasik, Mumbai Suburb and Raigad.    |
                              |            | Mumbai	                 |                                                                 |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    60.	   | Army Recruiting Office, | Districts of Nagpur, Wardha, Bhandara, Yavatmal, Akola,         |
                              |            | Nagpur	                 | Amaravati, Chandrapur, Gadchiroli, Gondia and Washim.           |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    61.	   | Army Recruiting Office, | Districts of Satara, Kolhapur, Sangli, Ratnagiri, Sindhudurg,   |
                              |            | Kolhapur	             | Sholapur and State of Goa.                                      |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    62.	   | Army Recruiting Office, | Districts of Aurangabad, Parbhani, Nanded, Jalna, Buldana,      |
                              |            | Aurangabad	             | Hingoli, Nandurbar, Dhule and Jalgaon.                          |
                              |--------------------------------------------------------------------------------------------------------|
                              | GUJARAT                                                                                                |
                              |--------------------------------------------------------------------------------------------------------|
                              |    63.	   | Army Recruiting Office, | Districts of Baroda, Ahmedabad, Kheda, Surat, Valsad, Bharuch,  |
                              |            | Ahmedabad	             | Mehsana, Sabarkantha, Anand, Dahod, Narmada, Navasari, Patan,   |
                              |            |                         | Panchmahal, Dang, Banaskanatha, Gandhinagar and Tapi. Daman     |
                              |            |                         | (Union Territory) & Dadra & Nagar Haveli (UT)                   |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    64.	   | Army Recruiting Office, | Districts of Rajkot, Jamnagar, Amreli, Bhavnagar, Junagarh,     |
                              |            | Jamnagar	             | Bhuj, Surendranagar and Porbandar. Diu (Union Territory)        |
                              |--------------------------------------|-----------------------------------------------------------------| 
                              |      HQ RECRUITING ZONE, SHILLONG	 | ASSAM, MEGHALAYA, ARUNACHAL PRADESH, NAGALAND, MANIPUR AND      |
                              |                                      | TRIPURA                                                         |
                              |--------------------------------------|-----------------------------------------------------------------|
                              |    65.	   | RO (HQ), Shillong	     | MEGHALAYA Districts of East Khasi Hills, West Khasi Hills,      |
                              |            |                         | Jaintia Hills, Ri Bhoi, East GARO Hills, South GARO Hills and   |
                              |            |                         | West GARO Hills. ASSAM Morigaon, Nagaon and Sonitpur.           |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    66.	   | Army Recruiting Office, | ARUNACHAL PRADESH Districts of West and East Siang, Dibang,     |
                              |            | Jorhat	                 | Valley, Lohit, Tirap, Changland, Lower Subansiri, Upper         |
                              |            |                         | Subansiri, Tawang, East Kameng, West Kameng, Upper Siang, Kurung|
                              |            |                         | Kamang, Papumpare, Anjan Hawai and Lower Dibang Valley. Jorhat. |
                              |            |                         | ASSAM. Tinsukia, Sibsagar, Dhemaji, North Lakhimpur, Dibrugarh, |
                              |            |                         | Golaghat and Karbi Anglong.                                     |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    67.	   | Army Recruiting Office, | ASSAM Districts of Barpeta, Goalpara, Darrang, Kamrup, Nalbari, |
                              |            | Narangi	             | Kokrajhar, Dhubri, Bongaigaon, Baksa, Udalguri and Chirang.     |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    68.	   | Army Recruiting Office, | NAGALAND Districts of Kohima, Phek, Mon, Zunheboto, Wokha,      |
                              |            | Rangapahar	             | Mokouchung, Tuensang, Dimapur, Pern, Kephere and Longleng.      |
                              |            |                         | houbal, Churachandpur, Tamenglong, Senapati, Chandel, Imphal    |
                              |            |                         | East and Imphal West                                            |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    69.	   | Army Recruiting Office, | ASSAM Districts of Cachar, North Cachar Hills, Karimganj and    |
                              |            | Silchar	             | Hailakandi. TRIPURA. West Tripura, North Tripura, South Tripura |
                              |            |                         | and Dhalai.                                                     |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    70.	   | Army Recruiting Office, | MIZORAM Districts of Aizawl, Lunglei, Mamit, Chhimtuipui,       |
                              |            | Aizawl	                 | Lawngtalai, Champai, Serchhip and Kolasib.                      |
                              |--------------------------------------|-----------------------------------------------------------------|
                              |       GRD KUNRAGHAT (GORAKHPUR)	     | NEPAL                                                           |
                              |--------------------------------------|-----------------------------------------------------------------|
                              |    71.	   | GRD, Kunraghat	         | Anchals of Mahakali, Seti, Bheri, Rapti, Karnali, Dhaulagiri,   |
                              |            |                         | Lumbini, Gandaki, Narayani and Bagmati of Nepal.                |
                              |------------|-------------------------|-----------------------------------------------------------------|
                              |    72.	   | GRD, Ghoom	             | NNG from Eastern Nepal to include Anchals of Janakpur,          |
                              |            |                         | Sagarmatha, Koshi, Mechi & ING from Darjeeling District         |
                              |            |                         | (Except Kalimpong Sub Division).                                |
                              |--------------------------------------|-----------------------------------------------------------------|
                              | INDEPENDENT RECRUITING OFFICE (IRO), |  DELHI AND DISTRICTS OF GURGAON, FARIDABAD, MEWAT AND PALWAL OF |
                              |           DELHI CANTT	             |                          HARYANA STATE                          |
                              |--------------------------------------|-----------------------------------------------------------------|
                              |    73.	   | Independent Recruiting  | DELHI. State of Delhi. HARYANA. Districts of Gurgaon, Faridabad,|
                              |            | Office (IRO), Delhi     | Mewat and Palwal.                                               |
                              |            | Cantt                   |                                                                 |
                              ----------------------------------------------------------------------------------------------------------\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.about(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Beware of Touts
    def beware(self):
        print("=" * 150)
        print(" " * 50 + "*** Information About Beware of Touts ***")
        print("=" * 150 + "\n")
        print("""                           
                                      1. Please be Wary of Touts(Dalal).They cannot influence the recruiting procedure
                                         at all. They are liars and take advantage of your lack of knowledge of the recruiting 
                                         procedure. Army recruiting is absolutely free, fair and totally merit based. Individual 
                                         having the required qualifications and capability will get selected on his own steam. No
                                         one can change the procedure to push in undeserving candidates since the procedure has 
                                         stringent checks and balances and mostly automated. Therefore when you come for 
                                         recruitment, have self belief. Anyone offering guarantee of recruitment must be reported
                                         to police or the rally officials immediately. Over a period we have identified many 
                                         methods a tout adopts to lure candidates. They are given below for you to ward off any 
                                         such offers.

                                      2. Likely Victim. Before a tout targets a candidate, he checks the candidate thoroughly. 
                                         Normally he selects boys who are physically fit with no medical problems and would in all
                                         probability be good in studies. Such candidates generally pass on their own steam. He 
                                         gives false assurances and says "You just pass the run. I will get the rest of it done.”
                                         When a candidate passes, in such case, the tout will take the credit. If the candidate 
                                         gets rejected, the tout returns the money or at least a major part of it with a lie that
                                         "some money, I can’t give back since I gave it to officials. However they have assured me
                                         that they will definitely do something next time, since there was lot of strictness this
                                         time”.

                                      3. Tricks To Acquire Candidates Trust. The tout will do anything to acquire the candidate’s
                                         faith so that they give him money easily e.g. in the middle of a recruitment rally, the
                                         tout will go up and make a deliberate effort to shake hands with recruiting personnel 
                                         claiming to be an ex-servicemen or any other identity. Mind you, he will want 
                                         you(candidate) to notice this and then he capitalizes on this hand shake.

                                      4. Telling Candidates False Indicators. Tout will misleadingly say "wear this coloured vest
                                         (baniyan)/Shorts, I’ve told the people concerned. They won’t ask you anything but will 
                                         know that you are my man.” or

                                      5."When you go for the interview of the Director Recruiting, say ‘Namaste’ or touch his feet.
                                         He will understand.”

                                      6. No one but only you can make it through the recruitment process, if you have the 
                                         qualification and capability. Don’t lose your parents hard earned money to unscrupulous
                                         touts.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.about(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Do's & Don'ts
    def do(self):
        print("=" * 150)
        print(" " * 53 + "*** Information About Do's & Don'ts ***")
        print("=" * 150 + "\n")
        print("""                           
                                         DO'S :

                                         * Before Rally :
                                           1. Prepare at least 2-3 months in advance for 1.6 Km run and other physical tests.
                                           2. Prepare necessary documents as required.
                                           3. Clarify doubts/ queries from nearest Recruitment Office.
                                           4. Get minor medical ailments treated to avoid rejection.
                                           5. Go through ‘eligibility’ requirements thoroughly to apply for most suitable 
                                              trade / category.
                                           6. Rectify any anomalies in your documents before rally (e.g. variation in name in 10th 
                                              and 12th Marks sheet).
                                           7. Prepare for the Tradesmen Aptitude Test (if applying for the same).

                                         * After Rally:
                                           1. Report and get medical review done in time (Permanent Unfit Cases- 21 days, Temporary
                                              Unfit Cases- 42 days).
                                           2. Prepare for written exam CEE (Common Entrance Exam).
                                           3. Check date of results and check personally results either through IVRS or your ARO.
                                           4. If selected, submit relevant documents in time and report for dispatch to training 
                                              centers on due date with necessary belongings.

                                         DONT'S :

                                         * Before Rally :
                                           1. Do not come to rally with incorrect or fake documents.
                                           2. Do not approach anybody other than Recruitment Office Staff for clarification regarding
                                              recruitment.
                                           3. Do not come to rally with major medical ailments/ injuries or if operated upon recently
                                              and wounds not yet healed.
                                           4. Do not pay heed to any one claiming to get you recruited.

                                         * During Rally :
                                           1. Do not get lured by any strangers/touts. Army recruitment is absolutely free and 
                                              transparent.
                                           2. Do not run on a date not allotted for your district or trade.
                                           3. Do not carry mobile handsets or costly personal belongings to the rally site.
                                           4. Do not fight or argue with other candidates/ recruitment staff.
                                           5. Do not litter the rally site inside or outside. Do not damage public/ private property.
                                           6. Do not misbehave with public and women in particular.
                                           7. Do not indulge in any anti social activity.

                                         * After Rally :
                                           1. Do not travel atop bus or train while coming to or going from rally location.
                                           2. Do not be late for medical review to the nominated Military Hospital.
                                           3. Do not be late for CEE or absent for result declaration. Result will not be disclosed
                                              to anyone else on your behalf.
                                           4. Do not be late/ absent for dispatch to Training Centre.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.about(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Documents to be prepared before entering for Online Application
    def document(self):
        print("=" * 150)
        print(" " * 29 + "*** Information About Documents to be prepared before entering for Online Application ***")
        print("=" * 150 + "\n")
        print("""                           
                                         1. Matric Certificate - 
                                            The following details will be filled strictly as per matric certificate :
                                                  a. Candidate Name.
                                                  b. Father Name.
                                                  c. Mother Name.
                                                  d. Date of Birth.
                                                  e. Matric Certificate number as issued by Education Board.
                                         2. Valid E mail address - 
                                            Each candidate is required to have personal Email Id which will be his user Id. 
                                            All messages will be sent to the Email Id regarding Short Listing, Call Ups, 
                                            Joining Instruction, Results, etc.
                                         3. Mobile Number - 
                                            Each Candidate will be required to have an individual mobile number. 
                                            Sharing of mobile number between candidates will not be permitted. OTP key and 
                                            other message will be sent to mobile number.
                                         4. Details about your State, District and Tehsil/ Block of Domicile (Only for JCO / OR 
                                            Enrolment Application).
                                         5. Scanned passport size photo of size between 10 Kb to 20 Kb in jpg format. 
                                            This photo will be uploaded on the application form.
                                         6. Scanned photo of signature of size between 5 Kb to 10 Kb in jpg format. 
                                            This photo will be uploaded on the application form.
                                         7. Detailed mark sheet of Class X, and other higher education qualification, 
                                            required to be filled in the application form as per the eligibility criteria of 
                                            the category/ entry applied for.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.about(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # About Agni veer Enrolment
    def about(self):
        print("=" * 150)
        print(" " * 50 + "*** Information About Agniveer Enrollment ***")
        print("=" * 150 + "\n")
        print(" " * 50 + "1. Zonal Recruitment Office")
        print(" " * 50 + "2. Eligibility Criteria for Recruitment Process")
        print(" " * 50 + "3. Beware of Touts")
        print(" " * 50 + "4. Do's & Don'ts")
        print(" " * 50 + "5. Documents to be prepared before entering for Online Application\n")
        print("+" * 150 + "\n")
        print(" " * 59 + "a. Enter 6 to Go Back")
        print(" " * 59 + "b. Enter 7 to Exit\n")
        print("=" * 150)

        while True:
            try:
                choose = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if choose == 1:
                agniipath.zonal(self)
                break

            elif choose == 2:
                agniipath.eligibility_criteria(self)
                break

            elif choose == 3:
                agniipath.beware(self)
                break

            elif choose == 4:
                agniipath.do(self)
                break

            elif choose == 5:
                agniipath.document(self)
                break

            elif choose == 6:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.main(self)
                    break

            elif choose == 7:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Description About the Indian Army
    def des(self):
        print("=" * 150)
        print(" " * 53 + "*** Description About the Indian Army ***")
        print("=" * 150 + "\n")
        print("""                               
                                         Grit and experience affect the growth of an institution. Fighting four major
                                         wars, insurgency and other low intensity wars has indeed made the Indian Army an 
                                         eminently and efficient battle trained, war machine.

                                         Changing times bring changing needs. Battle training must tell also on the structuring
                                         of the army, for it is this function that extracts the most from the assets available,
                                         both men and material. A look at the command and structuring of the Indian Army shows 
                                         how finely these have been tuned to meet India's threat perceptions, based on the 
                                         experience of the major wars that it has fought and the present-day geo-political 
                                         context.

                                         The largest standing volunteer Army in the world has never had to scour the populace for
                                         draft or conscription. There are always more men eager to don olive green than the 
                                         demand at any one time. But this does not reflect a situation where a large unemployed 
                                         workforce would get into uniform to keep body and soul together. More to the point is 
                                         the basic attitude of our people to the call of arms, discovered also by the British, 
                                         some three centuries before. There are very many who join up for long service tenures 
                                         under the colors, by inclination and choice - also familial habit and honour. If a young
                                         man or woman, sound of body and mind, and of Indian origin, is inclined to spend most of
                                         his useful working years in the kind of desolation that the country's Field areas' 
                                         adjoining the borders provide, can he or she cannot be refused.

                                         For the purpose of recruitment, the country is divided into recruiting zones. Every zone
                                         is allotted a quota for recruitment based on a percentage of its population and ethnic
                                         grouping. A legacy, slowly being diluted, is that of combat arm units or regiments 
                                         recruiting from a particular zone or mixture of ethnic groups.

                                         Once a man has joined up, it is for keeps. Many fall out at the basic training stage 
                                         when they find that there is much more to it than getting into a smart uniform. The one
                                         who hear the sound of the trumpet clearly without missing a note, take their oath and 
                                         for the greatness of the nation go into service - not servitude.

                                         Indian Army Headquarters began its life in the Red Fort - Delhi. Imposing edifice that
                                         it is, it was hardly suitable to house a complex entity such as this. Supreme 
                                         Headquarters at that time retained its seat in South Block and refused to share space.
                                         Mercifully, it was wound up in short order. Today Army Headquarters occupies portions of
                                         South Block along with a gigantic, architecturally modern Sena Bhavan adjacent.

                                         In the Indian context, Command Headquarter can be likened to a Field Army or even an 
                                         Army Group Headquarter with a General Officer Commanding-in-Chief presiding over matters
                                         in the rank of a (three-star) Lieutenant General. Next the line are the Corps 
                                         Headquarters, which are Field Army Headquarters elsewhere. The Indian Army's combat 
                                         formations are now grouped and tailored under many such Corps Headquarters (with some 
                                         forces being retained under static Area Commands).

                                         The static Areas, Sub Areas, or Independent Sub Areas span the length and breadth of the
                                         country. These look after infrastructural (and lines of communications) assets, 
                                         relieving field formations from the tedium of administering a multiplicity of support 
                                         installations located in an area. Area boundaries conform to state (or a group of states)
                                         administrative boundaries. All Headquarters are tasked also to maintain full 
                                         civil-military liaison. Static Areas (or even field formations in some cases) set up 
                                         Station Headquarters whose area of responsibility usually coincides with a district or a
                                         group of districts. Field formations located in Areas are always contingently tasked to
                                         assist the civil administration through these static Headquarters. Strangely enough, 
                                         this system works.

                                         The Chief of Army Staff (COAS) wears multiple hats. To the entire army, now some 1.1 
                                         million men and women strong, he is the Chief. A number of Staff Officers assist him, 
                                         such as Principal Staff Officers (PSOs), Heads of Arms and Services, etc. It would take
                                         a book of considerable length to even set down their designations and functions.

                                         Until the 1960s, staff coordination was a one-man affair in the form of a three-star 
                                         General Officer designated the Chief of the General Staff, with direct access to the 
                                         Chief available to 'some' - the PSOs. Today a Vice Chief and two Deputy Chiefs of Army
                                         Staff handle coordination. The command channel is absolutely one to one between the 
                                         Chief and his Army Commanders -with no one - but no one authorized even to say hold the
                                         line'.

                                         PSOs at Army Headquarters (and others down the line) have retained their 
                                         nineteenth-century designations, not having succumbed to new managerial nomenclatures 
                                         or alpha-numeric designations. The Quartermaster General, Master General of Ordnance, 
                                         Adjutant General, Military Secretary, Engineer-in-Chief, Signal Officer-in-Chief, 
                                         therefore, find traditional mention. At the sharp end a brigade-level General Staff 
                                         Officer and his logistic equivalents are still called GSO, Deputy Assistant Adjutant 
                                         General and Deputy Assistant Quartermaster General respectively.

                                         The field force is grouped into Corps. Some of these are defensively oriented and have,
                                         over the years, acquired an unofficial - 'Holding'. The others are called reserve or, 
                                         unofficially again, 'Strike' Corps. The former is really a misnomer since these contain
                                         ample offensive potential.

                                         Corps Headquarters are designed to handle an all-arms field army- of three to five 
                                         divisions or their equivalents. Army Headquarters reserves could be mammoth-size or 
                                         small, but powerful in either case. Heavy-tracked-Corps are an instance of the former,
                                         and the three parachute commandos (battalion-size units), which perform special-forces
                                         duties, of the latter. Airborne, Air Assault or Parachute troops are usually held 
                                         centralized. The mounts', in all cases, are provided by the Indian Air Force.

                                         The Army has in its Order of Battle, mountain divisions, infantry divisions, armoured 
                                         divisions (in which tank units predominate) and mechanized divisions (in which 
                                         mechanized infantry units predominate). Independent brigade groups may be armoured, 
                                         mechanized, air defence (missile or gun), parachute, engineer, field artillery, 
                                         electronic warfare or even standard infantry and mountain. These form 'Corps/Army 
                                         troops', that is, they are held at Corps and Army levels for balancing out missions and
                                         task forces. At these levels, one would find heavy logistic support units in terms of 
                                         supply, transport, field ordnance depots, and medical facilities.

                                         Organizationally, the field forces have never been static. Reorganization and creation
                                         of new field forces is the norm, prompted by constant rethinking on threats and the 
                                         emergence of new technology. To put it simply, if our organizations are basically 
                                         triangular, there is no bar on making them square or pentagonal for a given mission.

                                         Piecemeal 'modernisation' is of no use to anyone. All arms have gone through two and a
                                         half modernisation cycles since independence. For people with less than the usual quota
                                         of a sense of humour it amounts to a three-legged arms race in which the Joneses are 
                                         driving the Javeds, Joshis and Jiangs to follow suit.

                                         At least with the Indian Army it is not really so. It is conscious of working out an 
                                         edge or even proximate ability to see that a catastrophic disadvantage does not 
                                         undermine operational viability. Even the most articulate and vehement critic would 
                                         agree that the army is appreciative of what the country has provided to it in material,
                                         though it is somewhat hard pressed to do so.

                                         The Underpinning The timeless creed of the warriors and their feeling of comradeship in
                                         war and pestilence. The individual styles of the arms actually complement each other in
                                         combat. The pivot The ability of our field commanders to accept organizational, 
                                         doctrinal, and equipment changes (not in that order) plus a finer perception of the 
                                         strategic issues involved. With that, is their ability to mix individual assets into a
                                         combined arms and logistics team of very high combat worth.

                                         Technology and Equipment It is in this narrow area that modernization is usually talked
                                         about. By themselves, 'equipment' may just remain well-produced ironmongery or an 
                                         intricate series of integrated circuits. But when these are synthesized in a 
                                         complementary mix, they come to life - and present a threat out of all proportion to 
                                         their arithmetical aggregate on inventory.

                                         Overall, the Indian Army is adequately equipped. There certainly remain areas where 
                                         improvements or 'modernization' is pending, but that does not, in any way, detract from
                                         the fact that overall the Army has achieved a dissuasive quality, in which a potential
                                         aggressor will go into lip-biting conclave before deciding upon a violent course of 
                                         action.

                                         The mechanized armies in the Western Sector are mobile, balanced groupings of high 
                                         striking power. The fine synthesization of cutting-edge weaponry into high-value, 
                                         capital-intensive combat groups is seen at its best here. The T-72, BMP series Infantry
                                         Combat Vehicle, Anti-tank Guided Missiles of many varieties, Aviation, fast 
                                         reconnaissance vehicles, the FH-77/B-02 Medium Gun together with a number of other field
                                         pieces indigenously designed and developed, varieties of self-propelled air defence 
                                         missile and gun systems, Black' Electronic Warfare arrays, first-class assault bridging
                                         for dry and wet crossings are found together in supportive mixes. Here, all ballyhoo of
                                         ‘We are the queens/kings of the battlefield' is easily given a quiet burial.

                                         In the mountains, it is light infantry and artillery, supported by engineers, signals,
                                         helicopters and animals, which make for the combined-arms approach. The most visible 
                                         manifestation of modernization in equipment is in Siachen, which without these assets,
                                         cannot be garrisoned much less defended. This includes a combative logistical 
                                         infrastructure to prevail 'AGAINST ALL ODDS'. Two things remain to be stated without 
                                         equivocation.

                                         The Indian Army gives due respect to its adversaries and finds no need to cozen itself
                                         with whistling in the dark about 'One of US is equal to ten of them.’

                                         It does not accept being considered second to anyone - anywhere.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 65 + "1. Go Back")
        print(" " * 65 + "2. Exit\n")
        print("=" * 150)
        while True:
            try:
                cho = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if cho == 1:
                print("\nAre you sure to go back? (Y/N)")
                inp = input()
                if inp in "Yy":
                    agniipath.india(self)
                    break

            elif cho == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Gallantry Awards
    def awards(self):
        print("=" * 150)
        print(" " * 50 + "*** Information About Gallantry Awards ***")
        print("=" * 150 + "\n")
        print("""                             
                                                   Gallantry Awards are classified into two Categories :
                                                      1. Gallantry in the Face of Enemy
                                                      2. Gallantry Other than in the Face of Enemy

                                                   First Category of Gallantry Awards Comprises of the following Awards :
                                                      a. Param Vir Chakra (PVC)
                                                      b. Mahavir Chakra (MVC)
                                                      c. Vir Chakra
                                                      d. Sena Medal, Nao Sena Medal, Vayu Sena Medal
                                                      e. Mention in Dispatches
                                                      f. Chiefs of Staff Commendation Card

                                                   Second Category of Gallantry Awards Comprises of the following Awards :
                                                      a. Ashok Chakra
                                                      b. Kirti Chakra
                                                      c. Shaurya Chakra
                                                      d. Sena Medal, Nao Sena Medal, Vayu Sena Medal
                                                      e. Mention in Dispatches
                                                      f. Chiefs of Staff Commendation Card\n\n""")
        print("+" * 150 + "\n")
        print(" " * 65 + "1. Go Back")
        print(" " * 65 + "2. Exit\n")
        print("=" * 150)
        while True:
            try:
                cho = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if cho == 1:
                print("\nAre you sure to go back? (Y/N)")
                inp = input()
                if inp in "Yy":
                    agniipath.india(self)
                    break

            elif cho == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Ethos of Indian Army
    def ethos(self):
        print("=" * 150)
        print(" " * 47 + "*** Information about the Ethos of Indian Army ***")
        print("=" * 150 + "\n")
        print("""                           
                                          The infusion of high technology based precision weaponry has enhanced the 
                                          lethality  of future warfare manifold. The spectrum of threat ranges from the nuclear to the
                                          conventional and the asymmetric, with terrorism emerging like a hydra-headed monster. Add 
                                          to this the rigours of climate i.e. the glacial heights and extreme cold, dense mountainous
                                          jungles and the heat and simoom of the deserts. Such are the trying environs in which a 
                                          soldier operates. However, to a soldier facing such challenges and going beyond the call 
                                          of duty is but second nature. Life's turbulences and turmoils have a special flavour for 
                                          him. For those not exposed to a war or war like environment, this flavour is beyond the 
                                          realms of imagination. The Indian Army soldier is infused by a set of values that make the 
                                          soldier willingly face a plethora of challenges and difficulties, and when the call may come,
                                          to give the ultimate sacrifice in the service of the Nation. The ethos of the Army is 
                                          ingrained in all soldiers with an unwavering will to succeed, accepting their grave 
                                          responsibility and an unbridled ability to give their lives for others; confident that in 
                                          return the nation will look after them and their families. The values of the army infused in
                                          the soldier through the years of training are enumerated below :

                                          * Espirit-de-Corps - 
                                                        The spirit of comradeship and brotherhood of the brave, regardless of caste,
                                                        creed or religion. The motto is, "One for all and all for one"!
                                          * Spirit of Selfless Sacrifice - 
                                                        The tradition is never to question, but to do or die for the three "Ns"; Naam,
                                                        i.e. name-honour- of the unit/Army/Nation, 'Namak'(salt) i.e. loyalty to the 
                                                        Nation, and 'Nishan', i.e. the insignia or flag of his unit/regiment/Army/
                                                        Nation which the soldiers hold afloat willingly.
                                          * Valour -
                                                        Fearlessness in combat and in the face of the enemy even when fighting against 
                                                        great odds or even when facing sure death.
                                          * Non-discrimination -
                                                        The Indian Army does not discriminate on account of caste, creed or religion. 
                                                        A soldier is a soldier first and anything else later. He prays under a common 
                                                        roof. It is this unique character, which makes him bind in a team despite such 
                                                        diversity.
                                          * Fairness and Honesty -
                                                        The spirit of honesty and fair play. He fights for a just cause that extends 
                                                        even to the enemy (prisoner or wounded).
                                          * Discipline and Integrity -
                                                        Discipline and integrity impart the feeling of patriotism, honesty and courage 
                                                        under all circumstances, however strong be the provocation otherwise.
                                          * Fidelity, Honour and Courage -
                                                        He is a man on whose shoulders lies the honour and integrity of his nation. 
                                                        He knows that he is the last line of defence and he cannot fail the Nation.
                                          * Death to Dishonour -
                                                        A close bond amongst soldiers forces them to choose death to dishonour. The 
                                                        concept of 'IZZAT' (HONOUR) in the clan / unit enables them to shun the fear 
                                                        of death; to be called a coward in the peer group is worse than death.
                                          * Forthrightness -
                                                        A soldier has to be forthright, for on his word the men he leads are going to 
                                                        lay down their lives without questioning why.
                                          * These values stoke the attitude of Service before Self in every soldier. The famous credo 
                                            of Chetwode Hall is deeply imbibed in the men in Olive Green. It is the spirit of this 
                                            credo, imbibed in every officer that binds him with his men in an unshakeable bond of 
                                            camaraderie.

                                          The safety, honour and welfare of your country comes first always and every time.
                                          The honour, welfare and comfort of the men you command comes next.

                                          Your own ease, comfort and safety comes last always and every time.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 65 + "1. Go Back")
        print(" " * 65 + "2. Exit\n")
        print("=" * 150)
        while True:
            try:
                cho = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if cho == 1:
                print("\nAre you sure to go back? (Y/N)")
                inp = input()
                if inp in "Yy":
                    agniipath.india(self)
                    break

            elif cho == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about How to join the Indian Army
    def india_join(self):
        print("=" * 150)
        print(" " * 50 + "*** Information About How to join the Indian Army ***")
        print("=" * 150 + "\n")
        print("""

                       --------------------------------------      -------------------------       --------------------------------------
                       | TGC (EDUCATION)                    |      |        GENERAL        |       | NATIONAL DEFENCE ACADEMY           |
                       | AGE-23-27 YEARS                    | <--| -------------------------    -->| AGE-16 1/2 -19 1/2 YEARS           |
                       | QUALIFICATION-MA/MSC IN 1ST OR 2ND |    |              ^               |  | QUALIFICATION - 10+2               |
                       | DIVISION                           |    |              |               |  --------------------------------------
                       --------------------------------------    |              |               |
                       --------------------------------------    |  -------------------------   |  --------------------------------------
                       | UES                                |    |  |     LT GENERAL        |   |  | INDIAN MILITARY ACADEMY(NON TECH)  |
                       | AGE-18-24 YEARS                    | <--|  -------------------------   -->|                                    |
                       | QUALIFICATION-PRE FINAL STUDENT OF |    |             ^                |  | AGE-19 -25 YEARS                   |
                       | ENGINEERING DEGREE COURSE          |    |             |                |  | QUALIFICATION-GRADUATE             |
                       --------------------------------------    |             |                |  --------------------------------------
                                                                 | -------------------------    |
                       --------------------------------------    | |     MAJOR GENERAL     |    |   -------------------------------------
                       | TGC                                |    | -------------------------    |   | SHORT SEVICE COMMISION (NON TECH) |
                       | AGE-21-27 YEARS                    |<---|            ^                 --> |                                   |
                       | QUALIFICATION - BE / B.TECH STREAM |    |            |                 |   | AGE-19-25 YEARS                   |
                       | OF ENGINEERING/B.ARCH MSC          |    |            |                 |   | QUALIFICATION - GRADUATE          |
                       | COMPUTER                           |    | -------------------------    |   -------------------------------------
                       |                                    |    | |     BRIGADIER         |    |
                       --------------------------------------    | -------------------------    |
                                                                 |            ^                 |    ------------------------------------
                       --------------------------------------    |            |                 |    | SHORT SEVICE COMMISION           |
                       | JAC(MEN & WOMEN)                   |    |            |                 |    | (TECH MEN & WOMEN )              |
                       | AGE-21-27 YEARS                    |<---|  -------------------------   |    | AGE-19-27 YEARS                  |
                       | QUALIFICATION-LAW GRADUATE LLB     |    |  |        MAJOR          |   -->  | QUALIFICATION-BE/BTECH STEARM OF |
                       | WITH 55% MARKS REGISTERED WITH     |    |  -------------------------   |    | ENGINEERING/B.ARCH, MSC COMPUTER |
                       | BARS COUNCIL OF INDIA/STATE        |    |            ^                 |    ------------------------------------
                       --------------------------------------    |            |                 |
                                                                 |            |                 |    ------------------------------------
                                                                 |  -------------------------   -->  | NCC SPECIAL (MEN & WOMEN)        |
                                                                 |--|      LIEUTENANT       |---|    | AGE-19-25 YEARS                  |
                                                                    -------------------------   |    | QUALIFICATION- GRADUATE 50%      |
                                                                                                |    | AGGREGATE "A" OR "B" GRADE IN    |
                                                                                                |    | NCC "C" CERTIFICATE              |
                                                                                                |    ------------------------------------
                                                                                                |
                                                                                                |    ------------------------------------
                                                                                                |    | 10 + 2 TECH                      |
                                                                                                |--> | AGE-16 1/2 -19 1/2 YEARS         |
                                                                                                     | QUALIFICATION - 10+2 ( 70% MARKS |
                                                                                                     | WITH PCM )                       |
                                                                                                     |                                  |
                                                                                                     ------------------------------------

        """)
        print()
        print("Press ENTER to continue.................")
        i = input()
        print("""

                                                                 ------------------------------                                 
                                                                 |        SUBEDAR MAJOR       |                                 
                                                                 ------------------------------
                                                                                ^                    
                                                                                |                    
               ----------------------------------------         -------------------------------
               | CATERING JCO(ASC                     |         |            SUBEDAR          |
               | AGE-21-27 YEARS                      |         -------------------------------
               | QUALIFICATION-10+2 WITH DIPLOMA IN   |<---|                   ^
               | HOTEL MANAGEMENT & CATERING          |    |                   |                     ------------------------------------------------------
               | TECHNOLOGY                           |    |    --------------------------------     | RELIGIOUS TEACHER (JCO)                            |
               ----------------------------------------    |--- |      NAIB SUBEDAR            |---->| AGE-27-34 YEARS                                    |
                                                                --------------------------------     | QUALIFICATIONS-GRADUATE + HE IS QUALIFIED IN HIS   |
                                                                              ^                      | RELIGION                                           |
               -------------------------------------------                    |                      ------------------------------------------------------ 
               | HAVILDAR(EDUCATION)                     |       -------------------------------
               | AGE-21-25 YEARS                         |<------|          HAVILER            |
               | QUALIFACTION-FOR GROUP X-MA/MSC/MCA OR  |     | -------------------------------        --------------------------------------------------- 
               | BA/BSC/BCA WITH BED BSC(IT) FOR GROUP Y |     |              ^                         | SOLDIER GENERAL DUTY                            |
               | BSE/BA/BCA(IT)WITHOUT BED               |     |              |                    |--->| AGE-17 1/2-21 YEARS                             |
               -------------------------------------------     | -------------------------------   |    | QUALIFICATION-10TH PASS WITH 45% & EACH SUBJECT |
                                                               | |           NAIK              |   |    | MUST CONTAIN 33%                                |
               ----------------------------------------------  | -------------------------------   |    ---------------------------------------------------
               | SURVEYOR AUTO CARTO(ENGINEERS)             |<-|              ^                    |    ---------------------------------------------------  
               | AGE-20-25 YEARS                            |                 |                    |    | SOLDIER CLERK/STORE KEEPER                      |
               | QUALIFICATION-BA/BSC WITH MATHS 10+2 (MATH |     ------------------------------   |--->| AGE-17 1/2-21 YEARS                             |
               | & SCIENCE)                                 |     |           SEPOY            |---|    | QUALIFICATION-10+2 PASS (60 % MARKS)            |
               ----------------------------------------------     ------------------------------   |    | ( EACH SUBJECT MUST HAVE 40% MARKS )            |
                                                                                                   |    | WITH PHYSICS , CHEMISTRY , BIOLOGY              |
                                                                                                   |    ---------------------------------------------------
                                                                                                   |
                                                                                                   |    ---------------------------------------------------
                                                                                                   |    | SOLDIER NURSING ASSISTANT/TECH(RVC)             |
                                                                                                   |--->| AGE -17 1/2-23 YEARS                            |  
                                                                                                   |    | QUALIFICATION-10+2 PASS (50 % MARKS)            |
                                                                                                   |    | ( EACH SUBJECT MUST HAVE 40% MARKS )            |
                                                                                                   |    | WITH PHYSICS , CHEMISTRY , BIOLOGY              |
                                                                                                   |    ---------------------------------------------------
                                                                                                   |
                                                                                                   |
                                                                                                   |    ---------------------------------------------------
                                                                                                   |    | SOLDIER TRADESMAN                               |
                                                                                                   |--->| AGE -17 1/2-23 YEARS                            |
                                                                                                        | QUALIFICATION-10TH/ITI AND 8TH PASS(FOR SOME    |
                                                                                                        | TRADES)                                         |
                                                                                                        ---------------------------------------------------


        """)
        print("+" * 150 + "\n")
        print(" " * 65 + "1. Go Back")
        print(" " * 65 + "2. Exit\n")
        print("=" * 150)
        while True:
            try:
                cho = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if cho == 1:
                print("\nAre you sure to go back? (Y/N)")
                inp = input()
                if inp in "Yy":
                    agniipath.india(self)
                    break

            elif cho == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # About Indian Army
    def india(self):
        print("=" * 150)
        print(" " * 50 + "*** Information About Indian Army ***")
        print("=" * 150 + "\n")
        print(" " * 50 + "1. Description About the Indian Army")
        print(" " * 50 + "2. How to join the Indian Army")
        print(" " * 50 + "3. Gallantry Awards")
        print(" " * 50 + "4. The Ethos of Indian Army\n")
        print("+" * 150 + "\n")
        print(" " * 65 + "5. Go Back")
        print(" " * 65 + "6. Exit\n")
        print("=" * 150)
        while True:
            try:
                choose = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if choose == 1:
                agniipath.des(self)
                break

            elif choose == 2:
                agniipath.india_join(self)
                break

            elif choose == 3:
                agniipath.awards(self)
                break

            elif choose == 4:
                agniipath.ethos(self)
                break

            elif choose == 5:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.main(self)
                    break

            elif choose == 6:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Professional Advancement
    def professional(self):
        print("=" * 150)
        print(" " * 50 + "*** Information About Professional Advancement ***")
        print("=" * 150 + "\n")
        print("""                          
                                                       The promotional avenues available to an Army officer are:

                                                                   * By Time Scale :
                                                                        1. Captain
                                                                        2. Major
                                                                        3. Lieutenant Colonel

                                                                   * By Selection :
                                                                        1. Colonel
                                                                        2. Brigadier
                                                                        3. Major General
                                                                        4. Lieutenant General
                                                                        5. General\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.offer(self)
                    break

            elif ch == 2:
                exit()
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Job Satisfaction
    def job_satisfaction(self):
        print("=" * 150)
        print(" " * 53 + "*** Information About Job Satisfaction ***")
        print("=" * 150 + "\n")
        print("""                           
                                         Lack of job satisfaction leads to tremendous frustration and results in 
                                         job-hopping. Jobs in the civil world whether with the government or the corporate leave one 
                                         with no  alternate avenues if stuck with a frustrating portfolio or setup. On the contrary, 
                                         the sheer variety, sense of purpose, responsibility and pride, negate any job 
                                         dissatisfaction in the Army.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.offer(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Job Security
    def job_security(self):
        print("=" * 150)
        print(" " * 53 + "*** Information About Job Security ***")
        print("=" * 150 + "\n")
        print("""                               
                                           For an effective career, a long-term strategy is essential and this is 
                                           possible only if continuity and job security is assured. The Army has been structured to 
                                           ensure that its personnel work with unhindered dignity. Additionally, statutory rules and 
                                           regulations exist to safeguard the interests of the servicemen adequately both while in 
                                           service and after retirement.

                                           FOREIGN COURSES AND POSTINGS :

                                           The service also offers opportunity for courses and postings abroad. The India Army is 
                                           renowned all over the world and interaction with foreign armies is extensive. Service 
                                           with UN Forces provides exposure and travel opportunities across the globe.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)
        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.offer(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Social Status in Service
    def social(self):
        print("=" * 150)
        print(" " * 48 + "*** Information About Social Status in Service ***")
        print("=" * 150 + "\n")
        print("""                              
                                         All of us have our own opinion about what constitutes "social status”. 
                                         However it is an undisputed fact that the status of a ‘warrior’ has stood the test of 
                                         time. History and society have both held the soldier in esteem and offered him a unique 
                                         status in society. By joining the Army, one becomes a member of an exclusive and elite 
                                         brotherhood, which is the envy of one and all.

                                         POST RETIREMENT :

                                         Even after laying down the uniform, Army officers continue to have the status of the 
                                         most respected citizens of our country. This added to their ingrained code of conduct 
                                         and ethical values enable them to occupy a special social niche in society. Since he is 
                                         much fitter due to the active lifestyle he has led, a second career or lateral 
                                         absorption in parallel employment is always eminently feasible. His do or die attitude 
                                         and mental agility ensures that he never really grows into old age, but continues to 
                                         contribute and thus remain a valued member of society.

                                         LIFETIME OPPORTUNITY FOR PROFESSIONALS :

                                         The Army provides lifetime opportunities to professionals like Doctors, Nurse, Engineers, 
                                         Lawyers, and Teachers. Commissioned into the various Corps, one can pursue his or her 
                                         passion to your heart’s content. An excellent infrastructure, dedicated support staff, 
                                         and healthy environment provide unlimited growth. The Army invests heavily in human and 
                                         technical resources. The latest and the best tools are made available for research and 
                                         employment. Periodic forays into the academic world are encouraged in order to imbibe 
                                         and practice current technology in your chosen field.

                                         POSTING/TENURES SUBSEQUENT TO COMMISSIONING :

                                         Training is a judicious mix of technical, military and managerial instruction, in top 
                                         class institutions run by the Army and a host of other prestigious institutes and 
                                         establishments including IITs and DRDO. In accordance with the training received, 
                                         proficiency acquired and aptitude shown, one gets posted on a variety of regimental, 
                                         staff, or instructional appointments in organizations throughout the country. 
                                         Additionally officers proceed on deputation to various organizations and foreign 
                                         appointments.

                                         Unlike in a civil environment where a posting means virtual uprooting of a household and
                                         starting a fresh new station, in the Army it is merely a change of scene. With more and 
                                         more stations falling under the purview of peace stations and with better infrastructure 
                                         facilities coming up even in small stations, the pangs of moving are speedily easing up.

                                         FOOD FOR THOUGHT

                                         Here it would be apt to reiterate – That all professions serve our motherland – but none 
                                         of them is in the same league as the Indian Army – for this is the only profession which 
                                         affords you the opportunity to live up to these stirring lines.


                                                        "To every man upon this earth, death comes sooner or later.
                                                         And how can a man die better facing fearful odds
                                                         For the ashes of his father and the temple of his Gods”

                                                                                                             -Macauley\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.offer(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Quality of Life
    def quality(self):
        print("=" * 150)
        print(" " * 51 + "*** Information About Quality of Life ***")
        print("=" * 150 + "\n")
        print("""                               
                                          As an Indian Army officer at 21, you’d be looking at a lifestyle that one 
                                          cannot imagine in any other profession, so early in life. What compromises "Quality of 
                                          Life”? On one hand is a job with a thick pay packet but with the drudgery of 9AM to 9PM 
                                          schedule, no avenues and time for extracurricular activities, no scope for adventure and 
                                          excitement, no social status, lack of family life, threat of being terminated with a 
                                          month’s salary, working in suffocating environment with no self respect and honour. 
                                          On the other hand is a job which offers you challenge, adventure, excitement, honour, 
                                          prestige, self respect, whole some family life, safety and security for the family and 
                                          to top it all the love, respect and esteem of our great India. In the somewhat chaotic 
                                          social and economic conditions that prevail in our country, Army life is an island of 
                                          sanity and social order that is the envy of our countrymen. Quality of life is an 
                                          important attribute of Army life, and has no parallel in any other service.

                                          Some of the intangibles, which go to make the quality of life in the Army, are:-
                                               1. Service of the motherland.
                                               2. A profession to be proud of
                                               3. Opportunity to travel and know the country and its people/culture/flora 
                                                  and fauna
                                               4. Opportunity to serve and represent the nation abroad
                                               5. A pure and noble profession
                                               6. Honour and social status
                                               7. No stagnation, a new challenge every day.
                                               8. Opportunity for growth
                                               9. Sports and adventure activity
                                              10. Messes, clubs and institutions facilities
                                              11. Education facilities – Both school and professional colleges for children
                                              12. AWWA hostel for girls in metros
                                              13. Army ensures your physical and mental health.
                                              14. Quality of life ensured not only for officers, but also families.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.offer(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the Variety and Adventures
    def variety(self):
        print("=" * 150)
        print(" " * 50 + "*** Information About Variety and Adventures ***")
        print("=" * 150 + "\n")
        print("""                               
                                          Variety and adventure are the spice and romance of life. No profession has 
                                          the  kind of recreational and adventure facilities to offer as the Army does; from 
                                          membership  of the best clubs in country to horse riding, swimming, golfing, 
                                          mountaineering, trekking and sailing. Posting to exotic stations gives one an opportunity 
                                          to see India and its different cultures, in all its vivid glory. You may also get a 
                                          chance to go abroad on course or on posting. So, if one is looking for a profession, 
                                          which goes beyond being a mere job, accept the challenge and join the Indian Army.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                ch = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if ch == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.offer(self)
                    break

            elif ch == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the What the Army Offers
    def offer(self):
        print("=" * 150)
        print(" " * 50 + "*** Information About What the Army Offers ***")
        print("=" * 150 + "\n")
        print("""                           
                                         As a Candidate, all of you have aspirations and dreams, of what your education 
                                         will  finally yield. If you are looking for a fat pay packet, a corporate job is the answer. 
                                         But above and beyond this should be the question of what the job offer in totality. 
                                         Let us see what attributes go into making an excellent career. The attributes that one 
                                         expects from a satisfying profession are :

                                                                         1. Professional Advancement
                                                                         2. Job Satisfaction
                                                                         3. Job Security
                                                                         4. Social Status
                                                                         5. Quality of Life
                                                                         6. Variety and Adventure

                                         If these are what you too are looking forward to, then Army is the profession for you, as 
                                         these in the Army, compare far more than favourably with any other service.

                                         All of us are aware that, professions are competitive, in so far as promotions are concerned. 
                                         Army is no different. However, as said earlier the competition in the Army is clean and 
                                         devoid of any other factor but competence.


                                                   TO KNOW BRIEF ABOUUT EACH RESPECTIVE TOPIC'S ENTER THEIR RESPECTIVE NO.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 7 to Go Back")
        print(" " * 60 + "b. Enter 8 to Exit\n")
        print("=" * 150)

        while True:
            try:
                choose = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if choose == 1:
                agniipath.professional(self)
                break

            elif choose == 2:
                agniipath.job_satisfaction(self)
                break

            elif choose == 3:
                agniipath.job_security(self)
                break

            elif choose == 4:
                agniipath.social(self)
                break

            elif choose == 5:
                agniipath.quality(self)
                break

            elif choose == 6:
                agniipath.variety(self)
                break

            elif choose == 7:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.life(self)
                    break

            elif choose == 8:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about An Officer and A Gentleman
    def gentle_man(self):
        print("=" * 150)
        print(" " * 50 + "*** Information About An Officer and A Gentleman ***")
        print("=" * 150 + "\n")
        print("""                          
                                         An officer in the Indian Army inherits glorious heritage and lasting traditions, 
                                         blended perfectly with the latest advances in technology in the fields of armament, 
                                         management, engineering and medical sciences. It offers a golden opportunity to be a part 
                                         of the world's finest Army and get trained not only to be an Officer but also a Gentleman 
                                         for life.

                                         WHERE GROWTH IS A WAY OF LIFE :

                                         The Indian Army promises both professional and personal growth at every stage of the career.
                                         Opportunities to excel through various courses are abundant including opportunities to 
                                         enhance your educational qualification by availing two years paid study leave. 
                                         The inherent adventure and extra-curricular activities in the Army ensure an all round 
                                         development essential in today's world. Art of War-Engineering-Medicine-Administration-Human 
                                         Resource Development and Management; the army teaches you all. Moulding the officers into 
                                         leaders capable of leading from the front in any field. Joining the Army is possible both 
                                         after finishing school as well as after graduation.

                                         Apart from attractive pay and perks, Army offers you the best in Life Style, better than 
                                         all other professions. Be it social interaction, finest clubs, sports facilities, medical 
                                         facilities and ample opportunities, Army has it all. In fact you are paid to lead a healthy 
                                         life in a healthy environment.

                                         Facilities like subsidized housing, free medical for self & family, canteen facilities, 
                                         group insurance cover, soft loans for house and/or vehicle and above all the feeling of 
                                         belonging to a family which cares for you, are the perks of the Army which no other 
                                         organization provides.



                                                                       'DO YOU HAVE IT IN YOU'
                                                                To be a part of the elite Indian Army?\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            try:
                choose = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if choose == 1:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.life(self)
                    break

            elif choose == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # About Life in the Indian Army
    def life(self):
        while True:
            print("=" * 150)
            print(" " * 53 + "*** Information About Life in Indian Army ***")
            print("=" * 150 + "\n\n")
            print(" " * 60 + "1. What the Army Offers")
            print(" " * 60 + "2. An Officer and A Gentleman\n\n")
            print("+" * 150 + "\n")
            print(" " * 60 + "a. Enter 3 to Go Back")
            print(" " * 60 + "b. Enter 4 to Exit\n")
            print("=" * 150)

            try:
                choose = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if choose == 1:
                agniipath.offer(self)
                break

            elif choose == 2:
                agniipath.gentle_man(self)
                break

            elif choose == 3:
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.main(self)
                    break

            elif choose == 4:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    def c_username_exist(self, username):
        try:
            query = "SELECT * FROM new_enrollment WHERE Username = '%s'" % username
            cursor.execute(query)
            data = cursor.fetchone()
            if data is None:
                return True
            else:
                return False
        except:
            return True

    def new_enrollment(self):
        print("=" * 150)
        print(" " * 43 + "*** For New Enrollment in Agnipath Yojana Entry Scheme ***")
        print("=" * 150 + "\n")
        print("""                 
                                              IMPORTANT INSTRUCTION TO FILL ONLINE APPLICATION FORM :

                                                       1. Read all the instruction for registration carefully and then proceed further.
                                                       2. Check your Job Eligibility for joining Indian Army as JCO/OR and then Register.
                                                       3. Fill in all your personal details strictly as given in your matriculation 
                                                          Certificates. (I.e. Your Name, DOB, Father Name & Educational Qualification.)
                                                       4. Candidate must ensure that Email Id and mobile No entered at the time of 
                                                          registration process are active and unique. Sharing/Usage of Email Id /Mobile no 
                                                          of friends is strictly prohibited.
                                                       5. Ensure all the field are filled in correctly and then click on enter.
                                                       6. Registration process is mandatory for all the candidates to apply online for 
                                                          various Entries.
                                                       7. By default your Email Id will also be your user name but candidate must select 
                                                          their own password (Not more than 10 Characters). All Candidates are advised to 
                                                          remember their user name and password.
                                                       8. If you are an existing User/Already Registered on your website you can login 
                                                          using your User name and Password.
                                                       9. Thereafter your profile page will open and you can view your Dashboard on the 
                                                          screen.
                                                      10. Don't forget your Username and Password.
                                                      11. Ensure all the detail you enter are correct.


                                              Press ENTER to go to Registration.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back\n")
        print("=" * 150)
        print()

        while True:
            choose = input()

            if choose == '1':
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.main(self)
                    break

            else:
                break

        print()
        print("PERSONAL DATAILS :")
        print()

        while True:
            aadhar = input("\nEnter your aadhar no. :")
            if aadhar.isnumeric() is True and len(aadhar) == 12:
                break
            else:
                print(
                    "\n" + " " * 30 + "-------------------------------------INVALID AADHAR NO.-----------------------------------------")

        while True:
            c_name = input("\nEnter the candidate name :")
            if c_name.isalpha() is True and (c_name != '' or c_name != ' '):
                break
            else:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID CANDIDATE NAME---------------------------------------")

        while True:
            f_name = input("\nEnter your father name :")
            if f_name.isalpha() is True and (f_name != '' or f_name != ' '):
                break
            else:
                print(
                    "\n" + " " * 30 + "-------------------------------------INVALID FATHER NAME----------------------------------------")
        while True:
            m_name = input("\nEnter your mother name :")
            if m_name.isalpha() is True and (m_name != '' or m_name != ' '):
                break
            else:
                print(
                    "\n" + " " * 30 + "-------------------------------------INVALID MOTHER NAME----------------------------------------")

        while True:
            today = date.today()
            try:
                b_year = int(input("\nEnter the year of birth :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------INVALID YEAR OF BIRTH---------------------------------------")
            if b_year < today.year and b_year != None:
                break
            else:
                print(
                    "\n" + " " * 30 + "------------------------------------INVALID YEAR OF BIRTH---------------------------------------")
        while True:
            pos = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
            try:
                b_month = int(input("\nEnter the month of birth :"))
            except:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID MONTH OF BIRTH---------------------------------------")
            if b_month in pos and b_month != None:
                break
            else:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID MONTH OF BIRTH---------------------------------------")

        while True:
            try:
                b_day = int(input("\nEnter the day of birth :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------INVALID DAY OF BIRTH----------------------------------------")
            p1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                  27, 28, 29, 30, 31]
            p2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                  27, 28, 29, 30]
            p3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                  27, 28]
            p4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                  27, 28, 29]

            if b_month in (1, 3, 5, 7, 8, 10, 12):
                if b_day in p1:
                    break
                else:
                    print(
                        "\n" + " " * 30 + "------------------------------------INVALID DAY OF BIRTH----------------------------------------")
            elif b_month in (4, 6, 9, 11):
                if b_day in p2:
                    break
                else:
                    print(
                        "\n" + " " * 30 + "------------------------------------INVALID DAY OF BIRTH----------------------------------------")
            elif b_month == 2 and b_year % 4 == 0:
                if b_day in p4:
                    break
                else:
                    print(
                        "\n" + " " * 30 + "------------------------------------INVALID DAY OF BIRTH----------------------------------------")
            elif b_month == 2 and b_year % 4 != 0:
                if b_day in p3:
                    break
                else:
                    print(
                        "\n" + " " * 30 + "------------------------------------INVALID DAY OF BIRTH----------------------------------------")

        dob = date(b_year, b_month, b_day)

        c_age = agniipath.age(self, dob)

        while True:
            gendr = input("\nEnter your gender (M/F) :")
            if gendr in 'mM':
                gender = 'Male'
                break
            elif gendr in 'fF':
                gender = 'Female'
                break
            else:
                print(
                    "\n" + " " * 30 + "---------------------------------------INALID GENDER--------------------------------------------")

        while True:
            nationality = input("\nEnter your nationality :")
            if nationality.isalpha() is True and (nationality != '' or nationality != ' '):
                break
            else:
                print(
                    "\n" + " " * 30 + "-------------------------------------INALID NATIONALITY-----------------------------------------")

        while True:
            print()
            print(" " * 47 + "-" * 62)
            print(" " * 47 + "|      Choice for the matrial status:                        |")
            print(" " * 47 + "|" + " " * 60 + "|")
            print(" " * 47 + "|" + " " * 25 + "1. Divorcee" + " " * 24 + "|")
            print(" " * 47 + "|" + " " * 25 + "2. Married" + " " * 25 + "|")
            print(" " * 47 + "|" + " " * 25 + "3. Unmarried" + " " * 23 + "|")
            print(" " * 47 + "|" + " " * 25 + "4. Widower" + " " * 25 + "|")
            print(" " * 47 + "-" * 62)
            try:
                m_status = int(input("\nEnter your choose :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if m_status == 1:
                status = "Divorcee"
                break
            elif m_status == 2:
                status = "Married"
                break
            elif m_status == 3:
                status = "Unmarried"
                break
            elif m_status == 4:
                status = "Widower"
                break
            else:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID MATRIAL STATUS---------------------------------------")

        print("\nPress ENTER to continue the registration process...............................")
        print()
        i = input()

        time.sleep(2)

        print()
        print("CONTACT DETAILS :")
        print()

        while True:
            c_email = input("\nEnter your email address :")
            if c_email == " " or c_email == "":
                print(
                    "\n" + " " * 30 + "------------------------------------INVALID EMAIL ADDRESS---------------------------------------")
            else:
                break

        while True:
            c_mobile = input("\nEnter your mobile no. :")
            if c_mobile.isnumeric() == True and len(c_mobile) == 10 and c_mobile != "":
                break
            else:
                print(
                    "\n" + " " * 30 + "--------------------------------------INVALID PHONE NO.-----------------------------------------")

        print("\nPress ENTER to continue the registration process...............................")
        print()
        j = input()

        time.sleep(2)

        print()
        print("EDUCATION DETAILS :")
        print()

        while True:
            higher_qualification = input("\nEnter your hiqh school qualification (8th, 10th, 12th) :")
            if higher_qualification in ('8th', '10th', '12th'):
                break
            else:
                print(
                    "\n" + " " * 30 + "---------------------------------INVALID HIGHER QUALIFICATION-----------------------------------")

        print(" " * 15 + "-" * 126)
        print(
            " " * 15 + "|              Choice for Matriculation Board :                                                                              |")
        print(" " * 15 + "|" + " " * 20 + " 1. CENTRAL BOARD OF SECONDARY EDUCATION" + " " * 64 + "|")
        print(" " * 15 + "|" + " " * 20 + " 2. NATIONAL INSTITUTE OF OPEN SCHOOLING, NEW DELHI" + " " * 53 + "|")
        print(
            " " * 15 + "|" + " " * 20 + " 3. COUNCIL FOR THE INDIAN SCHOOL CERTIFICATE EXAMINATIONS, NEW DELHI" + " " * 35 + "|")
        print(" " * 15 + "|" + " " * 20 + " 4. BOARD OF INTERMEDIATE EDUCATION, ANDHRA PRADESH" + " " * 53 + "|")
        print(" " * 15 + "|" + " " * 20 + " 5. BOARD OF SECONDARY EDUCATION, ANDHRA PRADESH" + " " * 56 + "|")
        print(" " * 15 + "|" + " " * 20 + " 6. A.P. OPEN SCHOOL SOCIETY, ANDHRA PRADESH" + " " * 60 + "|")
        print(" " * 15 + "|" + " " * 20 + " 7. ASSAM HIGHER SECONDARY EDUCATION COUNCIL, ASSAM" + " " * 53 + "|")
        print(" " * 15 + "|" + " " * 20 + " 8. BOARD OF SECONDARY EDUCATION, ASSAM" + " " * 65 + "|")
        print(" " * 15 + "|" + " " * 20 + " 9. BIHAR SCHOOL EXAMINATION BOARD, BIHAR" + " " * 63 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "10. BIHAR BOARD OF OPEN SCHOOLING AND EXAMINATION(BBOSE), BIHAR" + " " * 41 + "|")
        print(" " * 15 + "|" + " " * 20 + "11. CHHATISGARH BOARD OF SECONDARY EDUCATION, CHHATISGARH" + " " * 47 + "|")
        print(" " * 15 + "|" + " " * 20 + "12. CHHATISGARH STATE OPEN SCHOOL, CHHATISGARH" + " " * 58 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "13. GOA BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, GOA" + " " * 42 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "14. GUJARAT SECONDARY AND HIGHER SECONDARY EDUCATION BOARD, GUJARAT" + " " * 37 + "|")
        print(" " * 15 + "|" + " " * 20 + "15. BOARD OF SCHOOL EDUCATION, HARYANA" + " " * 66 + "|")
        print(" " * 15 + "|" + " " * 20 + "16. H.P.BOARD OF SCHOOL EDUCATION, HIMACHAL PRADESH" + " " * 53 + "|")
        print(" " * 15 + "|" + " " * 20 + "17. THE J & K STATE BOARD OF SCHOOL EDUCATION, JAMMU" + " " * 52 + "|")
        print(" " * 15 + "|" + " " * 20 + "18. JHARKHAND ACADEMIC COUNCIL, RANCHI" + " " * 66 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "19. GOVT.OF KARNATAKA DEPT.OF PRE - UNIVERSITY EDUCATION, KARNATAKA" + " " * 37 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "20. KARNATAKA SECONDARY EDUCATION, EXAMINATION BOARD, KARNATAKA" + " " * 41 + "|")
        print(" " * 15 + "|" + " " * 20 + "21. KERALA BOARD OF PUBLIC EXAMINATION, KERALA" + " " * 58 + "|")
        print(" " * 15 + "|" + " " * 20 + "22. KERALA BOARD OF HIGHER SECONDARY EDUCATION, KERALA" + " " * 50 + "|")
        print(" " * 15 + "|" + " " * 20 + "23. BOARD OF VOCATIONAL HIGHER SECONDARY EDUCATION, KERALA" + " " * 46 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "24. MAHARASHTRA STATE BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, MAHARASHTRA" + " " * 20 + "|")
        print(" " * 15 + "|" + " " * 20 + "25. BOARD OF SECONDARY EDUCATION, MADHYA PRADESH" + " " * 56 + "|")
        print(" " * 15 + "|" + " " * 20 + "26. M.P.STATE OPEN SCHOOL EDUCATION BOARD, MADHYA PRADESH" + " " * 47 + "|")
        print(" " * 15 + "|" + " " * 20 + "27. BOARD OF SECONDARY EDUCATION, MANIPUR" + " " * 63 + "|")
        print(" " * 15 + "|" + " " * 20 + "28. COUNCIL OF HIGHER SECONDARY EDUCATION, MANIPUR" + " " * 54 + "|")
        print(" " * 15 + "|" + " " * 20 + "29. MEGHALAYA BOARD OF SCHOOL EDUCATION, MEGHALAYA" + " " * 54 + "|")
        print(" " * 15 + "|" + " " * 20 + "30. MIZORAM BOARD OF SCHOOL EDUCATION, MIZORAM" + " " * 58 + "|")
        print(" " * 15 + "|" + " " * 20 + "31. NAGALAND BOARD OF SCHOOL EDUCATION, NAGALAND" + " " * 56 + "|")
        print(" " * 15 + "|" + " " * 20 + "32. BOARD OF SECONDARY EDUCATION, ODISHA" + " " * 64 + "|")
        print(" " * 15 + "|" + " " * 20 + "33. COUNCIL OF HIGHER SECONDARY EDUCATION, ODISHA" + " " * 55 + "|")
        print(" " * 15 + "|" + " " * 20 + "34. PUNJAB SCHOOL EDUCATION BOARD, PUNJAB" + " " * 63 + "|")
        print(" " * 15 + "|" + " " * 20 + "35. BOARD OF SECONDARY EDUCATION, RAJASTHAN" + " " * 61 + "|")
        print(" " * 15 + "|" + " " * 20 + "36. RAJASTHAN STATE OPEN SCHOOL, RAJASTHAN" + " " * 62 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "37. STATE BOARD OF SCHOOL EXAMINATIONS(SEC.) & BOARD OF HIGHER SECONDARY, TAMIL NADU" + " " * 20 + "|")
        print(" " * 15 + "|" + " " * 20 + "38. BOARD OF SECONDARY EDUCATION, TELANGANA STATE" + " " * 55 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "39. TELANGANA STATE BOARD OF INTERMEDIATE EDUCATION, TELANGANA" + " " * 42 + "|")
        print(" " * 15 + "|" + " " * 20 + "40. TELANGANA OPEN SCHOOL SOCIETY, TELANGANA" + " " * 60 + "|")
        print(" " * 15 + "|" + " " * 20 + "41. TRIPURA BOARD OF SECONDARY EDUCATION, TRIPURA" + " " * 55 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "42. U.P.BOARD OF HIGH SCHOOL & INTERMEDIATE EDUCATION, UTTAR PRADESH" + " " * 36 + "|")
        print(" " * 15 + "|" + " " * 20 + "43. BOARD OF SCHOOL EDUCATION, UTTARAKHAND" + " " * 62 + "|")
        print(" " * 15 + "|" + " " * 20 + "44. WEST BENGAL BOARD OF SECONDARY EDUCATION, WEST BENGAL" + " " * 47 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "45. WEST BENGAL COUNCIL OF HIGHER SECONDARY EDUCATION, WEST BENGAL" + " " * 38 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "46. THE WEST BENGAL COUNCIL OF RABINDRA OPEN SCHOOLING, WEST BENGAL" + " " * 37 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "47. WEST BENGAL STATE COUNCIL OF TECHNICAL & VOCATIONAL EDUCATION & SKILL DEVELOPMENT, WEST BENGAL" + " " * 6 + "|")
        print(" " * 15 + "|" + " " * 20 + "48. MAHARISHI PATANJALI SANSKRIT SANSTHAN, NEW DELHI" + " " * 52 + "|")
        print(" " * 15 + "|" + " " * 20 + "49. URDU EDUCATION  BOARD, NEW DELHI" + " " * 68 + "|")
        print(" " * 15 + "|" + " " * 20 + "50. BIHAR SANSKRIT SHIKSHA BOARD, BIHAR" + " " * 65 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "51. U.P.BOARD OF SEC.SANSKRIT EDUCATION SANSKRIT BHAWAN, UTTAR PRADESH" + " " * 34 + "|")
        print(" " * 15 + "|" + " " * 20 + "52. ASSAM SANSKRIT BOARD, ASSAM" + " " * 73 + "|")
        print(" " * 15 + "|" + " " * 20 + "53. JAMIA MILIA ISLAMIA, NEW DELHI" + " " * 70 + "|")
        print(" " * 15 + "|" + " " * 20 + "54. UTTRAKHAND SANSKRIT SHIKSHA PARISHAD, UTTRAKHAND" + " " * 52 + "|")
        print(" " * 15 + "|" + " " * 20 + "55. STATE MADRASSA EDUCATION BOARD, ASSAM" + " " * 63 + "|")
        print(" " * 15 + "|" + " " * 20 + "56. BIHAR STATE MADRASA EDUCATION BOARD, BIHAR" + " " * 58 + "|")
        print(" " * 15 + "|" + " " * 20 + "57. WEST BENGAL BOARD OF MADRASAH EDUCATION, WEST BENGAL" + " " * 48 + "|")
        print(" " * 15 + "|" + " " * 20 + "58. CHHATTISGARH MADRASA BOARD, CHHATTISGARH" + " " * 60 + "|")
        print(" " * 15 + "|" + " " * 20 + "59. UTTARAKHAND MADRASA EDUCATION BOARD, UTTARAKHAND" + " " * 52 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "60. ALIGARH MUSLIM UNIVERSITY BOARD OF SECONDARY & SR.SECONDARY EDUCATION, UTTAR PARDESH" + " " * 16 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "61. INDIAN COUNCIL FOR HINDI & SANSKRIT EDUCATION, NEW DELHI" + " " * 44 + "|")
        print(" " * 15 + "|" + " " * 20 + "62. DAYALBAGH EDUCATIONAL INSTITUTE, AGRA" + " " * 63 + "|")
        print(" " * 15 + "|" + " " * 20 + "63. BANASTHALI VIDYAPITH P.O., RAJASTHAN" + " " * 64 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "64. BHUTAN COUNCIL FOR SCHOOL EXAMINATIONS & ASSESSMENT, BHUTAN" + " " * 41 + "|")
        print(" " * 15 + "|" + " " * 20 + "65. CAMBRIDGE ASSESSMENT INTERNATIONAL EXAMINATIONS, UK" + " " * 49 + "|")
        print(" " * 15 + "|" + " " * 20 + "66. CHHATTISGARH SANSKRIT BOARD, RAIPUR" + " " * 65 + "|")
        print(" " * 15 + "|" + " " * 20 + "67. MAURITIUS EXAMINATION SYNDICATE, MAURITIUS" + " " * 58 + "|")
        print(" " * 15 + "|" + " " * 20 + "68. NATIONAL EXAMINATIONS BOARD, NEPAL" + " " * 66 + "|")
        print(" " * 15 + "|" + " " * 20 + "69. PEARSON EDEXCEL LTD., UK" + " " * 76 + "|")
        print(" " * 15 + "|" + " " * 20 + "70. INTERNATIONAL BACCALAUREATE, GENEVA" + " " * 65 + "|")
        print(" " * 15 + "|" + " " * 20 + "71. NORTHWEST ACCREDITATION COMMISSION(NWAC), USA" + " " * 55 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "72. SINGHANIA UNIVERSITY BOARD OF SECONDARY & SENIOR SECONDARY EDUCATION, RAJASTHAN" + " " * 21 + "|")
        print(" " * 15 + "-" * 126)

        while True:
            try:
                c = int(input("\nEnter marticulation board :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")

            if c == 1:
                m_board = "CENTRAL BOARD OF SECONDARY EDUCATION"
                break
            elif c == 2:
                m_board = "NATIONAL INSTITUTE OF OPEN SCHOOLING, NEW DELHI"
                break
            elif c == 3:
                m_board = "COUNCIL FOR THE INDIAN SCHOOL CERTIFICATE EXAMINATIONS, NEW DELHI"
                break
            elif c == 4:
                m_board = "BOARD OF INTERMEDIATE EDUCATION, ANDHRA PRADESH"
                break
            elif c == 5:
                m_board = "BOARD OF SECONDARY EDUCATION, ANDHRA PRADESH"
                break
            elif c == 6:
                m_board = "A.P. OPEN SCHOOL SOCIETY, ANDHRA PRADESH"
                break
            elif c == 7:
                m_board = "ASSAM HIGHER SECONDARY EDUCATION COUNCIL, ASSAM"
                break
            elif c == 8:
                m_board = "BOARD OF SECONDARY EDUCATION, ASSAM"
                break
            elif c == 9:
                m_board = "BIHAR SCHOOL EXAMINATION BOARD, BIHAR"
                break
            elif c == 10:
                m_board = "BIHAR BOARD OF OPEN SCHOOLING AND EXAMINATION(BBOSE), BIHAR"
                break
            elif c == 11:
                m_board = "CHHATISGARH BOARD OF SECONDARY EDUCATION, CHHATISGARH"
                break
            elif c == 12:
                m_board = "CHHATISGARH STATE OPEN SCHOOL, CHHATISGARH"
                break
            elif c == 13:
                m_board = "GOA BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, GOA"
                break
            elif c == 14:
                m_board = "GUJARAT SECONDARY AND HIGHER SECONDARY EDUCATION BOARD, GUJARAT"
                break
            elif c == 15:
                m_board = "BOARD OF SCHOOL EDUCATION, HARYANA"
                break
            elif c == 16:
                m_board = "H.P.BOARD OF SCHOOL EDUCATION, HIMACHAL PRADESH"
                break
            elif c == 17:
                m_board = "THE J & K STATE BOARD OF SCHOOL EDUCATION, JAMMU"
                break
            elif c == 18:
                m_board = "JHARKHAND ACADEMIC COUNCIL, RANCHI"
                break
            elif c == 19:
                m_board = "GOVT.OF KARNATAKA DEPT.OF PRE - UNIVERSITY EDUCATION, KARNATAKA"
                break
            elif c == 20:
                m_board = "KARNATAKA SECONDARY EDUCATION, EXAMINATION BOARD, KARNATAKA"
                break
            elif c == 21:
                m_board = "KERALA BOARD OF PUBLIC EXAMINATION, KERALA"
                break
            elif c == 22:
                m_board = "KERALA BOARD OF HIGHER SECONDARY EDUCATION, KERALA"
                break
            elif c == 23:
                m_board = "BOARD OF VOCATIONAL HIGHER SECONDARY EDUCATION, KERALA"
                break
            elif c == 24:
                m_board = "MAHARASHTRA STATE BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, MAHARASHTRA"
                break
            elif c == 25:
                m_board = "BOARD OF SECONDARY EDUCATION, MADHYA PRADESH"
                break
            elif c == 26:
                m_board = "M.P.STATE OPEN SCHOOL EDUCATION BOARD, MADHYA PRADESH"
                break
            elif c == 27:
                m_board = "BOARD OF SECONDARY EDUCATION, MANIPUR"
                break
            elif c == 28:
                m_board = "COUNCIL OF HIGHER SECONDARY EDUCATION, MANIPUR"
                break
            elif c == 29:
                m_board = "MEGHALAYA BOARD OF SCHOOL EDUCATION, MEGHALAYA"
                break
            elif c == 30:
                m_board = "MIZORAM BOARD OF SCHOOL EDUCATION, MIZORAM"
                break
            elif c == 31:
                m_board = "NAGALAND BOARD OF SCHOOL EDUCATION, NAGALAND"
                break
            elif c == 32:
                m_board = "BOARD OF SECONDARY EDUCATION, ODISHA"
                break
            elif c == 33:
                m_board = "COUNCIL OF HIGHER SECONDARY EDUCATION, ODISHA"
                break
            elif c == 34:
                m_board = "PUNJAB SCHOOL EDUCATION BOARD, PUNJAB"
                break
            elif c == 35:
                m_board = "BOARD OF SECONDARY EDUCATION, RAJASTHAN"
                break
            elif c == 36:
                m_board = "RAJASTHAN STATE OPEN SCHOOL, RAJASTHAN"
                break
            elif c == 37:
                m_board = "STATE BOARD OF SCHOOL EXAMINATIONS(SEC.) & BOARD OF HIGHER SECONDARY, TAMIL NADU"
                break
            elif c == 38:
                m_board = "BOARD OF SECONDARY EDUCATION, TELANGANA STATE"
                break
            elif c == 39:
                m_board = "TELANGANA STATE BOARD OF INTERMEDIATE EDUCATION, TELANGANA"
                break
            elif c == 40:
                m_board = "TELANGANA OPEN SCHOOL SOCIETY, TELANGANA"
                break
            elif c == 41:
                m_board = "TRIPURA BOARD OF SECONDARY EDUCATION, TRIPURA"
                break
            elif c == 42:
                m_board = "U.P.BOARD OF HIGH SCHOOL & INTERMEDIATE EDUCATION, UTTAR PRADESH"
                break
            elif c == 43:
                m_board = "BOARD OF SCHOOL EDUCATION, UTTARAKHAND"
                break
            elif c == 44:
                m_board = "WEST BENGAL BOARD OF SECONDARY EDUCATION, WEST BENGAL"
                break
            elif c == 45:
                m_board = "WEST BENGAL COUNCIL OF HIGHER SECONDARY EDUCATION, WEST BENGAL"
                break
            elif c == 46:
                m_board = "THE WEST BENGAL COUNCIL OF RABINDRA OPEN SCHOOLING, WEST BENGAL"
                break
            elif c == 47:
                m_board = "WEST BENGAL STATE COUNCIL OF TECHNICAL & VOCATIONAL EDUCATION & SKILL DEVELOPMENT, WEST BENGAL"
                break
            elif c == 48:
                m_board = "MAHARISHI PATANJALI SANSKRIT SANSTHAN, NEW DELHI"
                break
            elif c == 49:
                m_board = "URDU EDUCATION  BOARD, NEW DELHI"
                break
            elif c == 50:
                m_board = "BIHAR SANSKRIT SHIKSHA BOARD, BIHAR"
                break
            elif c == 51:
                m_board = "U.P.BOARD OF SEC.SANSKRIT EDUCATION SANSKRIT BHAWAN, UTTAR PRADESH"
                break
            elif c == 52:
                m_board = "ASSAM SANSKRIT BOARD, ASSAM"
                break
            elif c == 53:
                m_board = "JAMIA MILIA ISLAMIA, NEW DELHI"
                break
            elif c == 54:
                m_board = "UTTRAKHAND SANSKRIT SHIKSHA PARISHAD, UTTRAKHAND"
                break
            elif c == 55:
                m_board = "STATE MADRASSA EDUCATION BOARD, ASSAM"
                break
            elif c == 56:
                m_board = "BIHAR STATE MADRASA EDUCATION BOARD, BIHAR"
                break
            elif c == 57:
                m_board = "WEST BENGAL BOARD OF MADRASAH EDUCATION, WEST BENGAL"
                break
            elif c == 58:
                m_board = "CHHATTISGARH MADRASA BOARD, CHHATTISGARH"
                break
            elif c == 59:
                m_board = "UTTARAKHAND MADRASA EDUCATION BOARD, UTTARAKHAND"
                break
            elif c == 60:
                m_board = "ALIGARH MUSLIM UNIVERSITY BOARD OF SECONDARY & SR.SECONDARY EDUCATION, UTTAR PARDESH"
                break
            elif c == 61:
                m_board = "INDIAN COUNCIL FOR HINDI & SANSKRIT EDUCATION, NEW DELHI"
                break
            elif c == 62:
                m_board = "DAYALBAGH EDUCATIONAL INSTITUTE, AGRA"
                break
            elif c == 63:
                m_board = "BANASTHALI VIDYAPITH P.O., RAJASTHAN"
                break
            elif c == 64:
                m_board = "BHUTAN COUNCIL FOR SCHOOL EXAMINATIONS & ASSESSMENT, BHUTAN"
                break
            elif c == 65:
                m_board = "CAMBRIDGE ASSESSMENT INTERNATIONAL EXAMINATIONS, UK"
                break
            elif c == 66:
                m_board = "CHHATTISGARH SANSKRIT BOARD, RAIPUR"
                break
            elif c == 67:
                m_board = "MAURITIUS EXAMINATION SYNDICATE, MAURITIUS"
                break
            elif c == 68:
                m_board = "NATIONAL EXAMINATIONS BOARD, NEPAL"
                break
            elif c == 69:
                m_board = "PEARSON EDEXCEL LTD., UK"
                break
            elif c == 70:
                m_board = "INTERNATIONAL BACCALAUREATE, GENEVA"
                break
            elif c == 71:
                m_board = "NORTHWEST ACCREDITATION COMMISSION(NWAC), USA"
                break
            elif c == 72:
                m_board = "SINGHANIA UNIVERSITY BOARD OF SECONDARY & SENIOR SECONDARY EDUCATION, RAJASTHAN"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        print("\nPress ENTER to continue the registration process...............................")
        print()
        k = input()

        time.sleep(2)

        print()
        print("PASSWORD REQUIREMENT :")
        print()

        print("                                NOTE :")
        print("                                      1. Remember your username and password.\n"
              "                                      2. You can access and modify your registration details using your username and password.")
        print("\nPress ENTER to continue the registration process...............................")
        print()
        k = input()

        while True:
            c_username = input("\nEnter your username :")
            con = agniipath.c_username_exist(self, c_username)
            if con is True:
                break
            else:
                print(
                    "\n" + " " * 30 + "----------------------------------THE USERNAME ALREADY EXISTS-----------------------------------")
                print(
                    "\n" + " " * 30 + "---------------------------------PLEASE ENTER A VALID USERNAME----------------------------------")

        while True:
            password = input("\nEnter the password :")
            if password == '' or password == ' ':
                print(
                    "\n" + " " * 30 + "--------------------------------PLEASE ENTER A VALID CORRECTLY----------------------------------")
            else:
                confirm_password = input("\nEnter the confirm password :")
                if password == confirm_password:
                    break
                else:
                    print(
                        "\n" + " " * 30 + "-----------------------------PLEASE ENTER THE PASSWORD CORRECTLY--------------------------------")

        print("\nPress ENTER to continue the registration process...............................")
        print()
        l = input()

        time.sleep(2)

        print()
        print("COMMUNICATION INFORMATION :")
        print()

        while True:
            house_no = int(input("\nEnter your House No. :"))
            if house_no == ' ' or house_no == '':
                print(
                    "\n" + " " * 30 + "----------------------------------------INVALID HOUSE NO.---------------------------------------")
            else:
                break

        while True:
            address = input("\nEnter your Address :")
            if address == ' ' or address == '':
                print(
                    "\n" + " " * 30 + "-----------------------------------------INVALID ADDRESS----------------------------------------")
            else:
                break

        while True:
            village = input("\nEnter your Village Name (optional if NO press 1) :")
            if village == '1':
                village = 'NO'
                break
            if village == '' or village == ' ':
                print(
                    "\n" + " " * 30 + "--------------------------------------INVALID VILLAGE NAME--------------------------------------")
            else:
                break

        while True:
            city_town = input("\nEnter your City/Town Name :")
            if city_town.isalpha() is False:
                print(
                    "\n" + " " * 30 + "-------------------------------------INVALID CITY/TOWN NAME-------------------------------------")
            else:
                break

        print(
            """                         
                                         --------------------------------------------------------------------------
                                         |      Sl.no.      |               State/Union Territory Name            |
                                         |------------------|-----------------------------------------------------|
                                         |         1.       | Andhra Pradesh                                      |
                                         |         2.       | Arunachal Pradesh                                   |
                                         |         3.       | Assam                                               |
                                         |         4.       | Bihar                                               |
                                         |         5.       | Chattisgrarh                                        |
                                         |         6.       | Goa                                                 |
                                         |         7.       | Gujarat                                             |
                                         |         8.       | Haryana                                             |
                                         |         9.       | Himachal Pradesh                                    |
                                         |        10.       | Jammu & Kashmir                                     |
                                         |        11.       | Jharkhand                                           |
                                         |        12.       | Karnataka                                           |
                                         |        13.       | Kerala                                              |
                                         |        14.       | Madhya Pradesh                                      |
                                         |        15.       | Maharashtra                                         |
                                         |        16.       | Manipur                                             |
                                         |        17.       | Meghalaya                                           |
                                         |        18.       | Mizoram                                             |
                                         |        19.       | Nagaland                                            |
                                         |        20.       | Odisha                                              |
                                         |        21.       | Punjab                                              |
                                         |        22.       | Rajasthan                                           |
                                         |        23.       | Sikkim                                              |
                                         |        24.       | Tamil Nadu                                          |
                                         |        25.       | Telangana                                           |
                                         |        26.       | Tripura                                             |
                                         |        27.       | Uttar Pradesh                                       |
                                         |        28.       | Uttarakhand                                         |
                                         |        29.       | West Bengal                                         |
                                         |        30.       | Andaman & Nicobar                                   |
                                         |        31.       | Chandigarh                                          |
                                         |        32.       | Dadra and Nagar Haveli and Daman and Diu            |
                                         |        33.       | Delhi                                               |
                                         |        34.       | Lakshadweep                                         |
                                         |        35.       | Ladakh                                              |
                                         |        36.       | Puducherry                                          |
                                         --------------------------------------------------------------------------
            """)
        while True:
            s_u = int(input("\nChoose your State/Union Territory Name :"))
            if s_u == 1:
                st_ut = 'Andhra Pradesh'
                break
            elif s_u == 2:
                st_ut = 'Arunachal Pradesh'
                break
            elif s_u == 3:
                st_ut = 'Assam'
                break
            elif s_u == 4:
                st_ut = 'Bihar'
                break
            elif s_u == 5:
                st_ut = 'Chattisgrarh'
                break
            elif s_u == 6:
                st_ut = 'Goa'
                break
            elif s_u == 7:
                st_ut = 'Gujarat'
                break
            elif s_u == 8:
                st_ut = 'Haryana'
                break
            elif s_u == 9:
                st_ut = 'Himachal Pradesh'
                break
            elif s_u == 10:
                st_ut = 'Jammu & Kashmir'
                break
            elif s_u == 11:
                st_ut = 'Jharkhand'
                break
            elif s_u == 12:
                st_ut = 'Karnataka'
                break
            elif s_u == 13:
                st_ut = 'Kerala'
                break
            elif s_u == 14:
                st_ut = 'Madhya Pradesh'
                break
            elif s_u == 15:
                st_ut = 'Maharashtra'
                break
            elif s_u == 16:
                st_ut = 'Manipur'
                break
            elif s_u == 17:
                st_ut = 'Meghalaya'
                break
            elif s_u == 18:
                st_ut = 'Mizoram'
                break
            elif s_u == 19:
                st_ut = 'Nagaland'
                break
            elif s_u == 20:
                st_ut = 'Odisha'
                break
            elif s_u == 21:
                st_ut = 'Punjab'
                break
            elif s_u == 22:
                st_ut = 'Rajasthan'
                break
            elif s_u == 23:
                st_ut = 'Sikkim'
                break
            elif s_u == 24:
                st_ut = 'Tamil Nadu'
                break
            elif s_u == 25:
                st_ut = 'Telangana'
                break
            elif s_u == 26:
                st_ut = 'Tripura'
                break
            elif s_u == 27:
                st_ut = 'Uttar Pradesh'
                break
            elif s_u == 28:
                st_ut = 'Uttarakhand'
                break
            elif s_u == 29:
                st_ut = 'West Bengal'
                break
            elif s_u == 30:
                st_ut = 'Andaman & Nicobar'
                break
            elif s_u == 31:
                st_ut = 'Chandigarh'
                break
            elif s_u == 32:
                st_ut = 'Dadra and Nagar Haveli and Daman and Diu'
                break
            elif s_u == 33:
                st_ut = 'Delhi'
                break
            elif s_u == 34:
                st_ut = 'Lakshadweep'
                break
            elif s_u == 35:
                st_ut = 'Ladakh'
                break
            elif s_u == 36:
                st_ut = 'Puducherry'
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        if st_ut == "Andhra Pradesh":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Andhra Pradesh:            |
                                                |                       1. Anantapur                          |
                                                |                       2. Chittoor                           |
                                                |                       3. East Godavari                      |
                                                |                       4. Alluri Sitarama Raju               | 
                                                |                       5. Anakapalli                         |
                                                |                       6. Annamaya                           |
                                                |                       7. Bapatla                            |
                                                |                       8. Eluru                              | 
                                                |                       9. Guntur                             | 
                                                |                      10. Kadapa                             |
                                                |                      11. Kakinada                           | 
                                                |                      12. Konaseema                          |
                                                |                      13. Krishna                            |
                                                |                      14. Kurnool                            |
                                                |                      15. Manyam                             |
                                                |                      16. N T Rama Rao                       |
                                                |                      17. Nandyal                            |
                                                |                      18. Nellore                            | 
                                                |                      19. Palnadu                            |
                                                |                      20. Prakasam                           | 
                                                |                      21. Sri Balaji                         |
                                                |                      22. Sri Satya Sai                      |
                                                |                      23. Srikakulam                         |
                                                |                      24. Visakhapatnam                      |
                                                |                      25. Vizianagaram                       |
                                                |                      26. West Godavari                      |
                                                ---------------------------------------------------------------               
            """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Anantapur'
                    break
                elif d == 2:
                    district = 'Chittoor'
                    break
                elif d == 3:
                    district = 'East Godavari'
                    break
                elif d == 4:
                    district = 'Alluri Sitarama Raju'
                    break
                elif d == 5:
                    district = 'Anakapalli'
                    break
                elif d == 6:
                    district = 'Annamaya'
                    break
                elif d == 7:
                    district = 'Bapatla'
                    break
                elif d == 8:
                    district = 'Eluru'
                    break
                elif d == 9:
                    district = 'Guntur'
                    break
                elif d == 10:
                    district = 'Kadapa'
                    break
                elif d == 11:
                    district = 'Kakinada'
                    break
                elif d == 12:
                    district = 'Konaseema'
                    break
                elif d == 13:
                    district = 'Krishna'
                    break
                elif d == 14:
                    district = 'Kurnool'
                    break
                elif d == 15:
                    district = 'Manyam'
                    break
                elif d == 16:
                    district = 'N T Rama Rao'
                    break
                elif d == 17:
                    district = 'Nandyal'
                    break
                elif d == 18:
                    district = 'Nellore'
                    break
                elif d == 19:
                    district = 'Palnadu'
                    break
                elif d == 20:
                    district = 'Prakasam'
                    break
                elif d == 21:
                    district = 'Sri Balaji'
                    break
                elif d == 22:
                    district = 'Sri Satya Sai'
                    break
                elif d == 23:
                    district = 'Srikakulam'
                    break
                elif d == 24:
                    district = 'Visakhapatnam'
                    break
                elif d == 25:
                    district = 'Vizianagaram'
                    break
                elif d == 26:
                    district = 'West Godavari'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Arunachal Pradesh":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Arunachal Pradesh:         |
                                                |                       1. Anjaw                              |
                                                |                       2. Siang                              |
                                                |                       3. Changlang                          |
                                                |                       4. Dibang Valleyu                     | 
                                                |                       5. East Kameng                        |
                                                |                       6. East Siang                         |
                                                |                       7. Kamle                              |
                                                |                       8. Kra Daadi                          | 
                                                |                       9. Kurung Kumey                       | 
                                                |                      10. Lepa Rada                          |
                                                |                      11. Lohit                              | 
                                                |                      12. Longding                           |
                                                |                      13. Lower Dibang Valley                |
                                                |                      14. Lower Siang                        |
                                                |                      15. Lower Subansiri                    |
                                                |                      16. Namsai                             |
                                                |                      17. Pakke Kessang                      |
                                                |                      18. Papum Pare                         | 
                                                |                      19. Shi Yomi                           |
                                                |                      20. Tawang                             | 
                                                |                      21. Tirap                              |
                                                |                      22. Upper Siang                        |
                                                |                      23. Upper Subansiri                    |
                                                |                      24. West Kameng                        |
                                                |                      25. West Siang                         |
                                                ---------------------------------------------------------------                                    
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Anjaw'
                    break
                elif d == 2:
                    district = 'Siang'
                    break
                elif d == 3:
                    district = 'Changlang'
                    break
                elif d == 4:
                    district = 'Dibang Valley'
                    break
                elif d == 5:
                    district = 'East Kameng'
                    break
                elif d == 6:
                    district = 'East Siang'
                    break
                elif d == 7:
                    district = 'Kamle'
                    break
                elif d == 8:
                    district = 'Kra Daadi'
                    break
                elif d == 9:
                    district = 'Kurung Kumey'
                    break
                elif d == 10:
                    district = 'Lepa Rada'
                    break
                elif d == 11:
                    district = 'Lohit'
                    break
                elif d == 12:
                    district = 'Longding'
                    break
                elif d == 13:
                    district = 'Lower Dibang Valley'
                    break
                elif d == 14:
                    district = 'Lower Siang'
                    break
                elif d == 15:
                    district = 'Lower Subansiri'
                    break
                elif d == 16:
                    district = 'Namsai'
                    break
                elif d == 17:
                    district = 'Pakke Kessang'
                    break
                elif d == 18:
                    district = 'Papum Pare'
                    break
                elif d == 19:
                    district = 'Shi Yomi'
                    break
                elif d == 20:
                    district = 'Tawang'
                    break
                elif d == 21:
                    district = 'Tirap'
                    break
                elif d == 22:
                    district = 'Upper Siang'
                    break
                elif d == 23:
                    district = 'Upper Subansiri'
                    break
                elif d == 24:
                    district = 'West Kameng'
                    break
                elif d == 25:
                    district = 'West Siang'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Assam":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Assam:                     |
                                                |                       1. Bajali                             |
                                                |                       2. Baksa                              |
                                                |                       3. Barpeta                            |
                                                |                       4. Biswanath                          | 
                                                |                       5. Bongaigaon                         |
                                                |                       6. Cachar                             |
                                                |                       7. Charaideo                          |
                                                |                       8. Chirang                            | 
                                                |                       9. Darrang                            | 
                                                |                      10. Dhemaji                            |
                                                |                      11. Dhubri                             | 
                                                |                      12. Dibrugarh                          |
                                                |                      13. Dima Hasao                         |
                                                |                      14. Goalpara                           |
                                                |                      15. Golaghat                           |
                                                |                      16. Hailakandi                         |
                                                |                      17. Hojai                              |
                                                |                      18. Jorhat                             | 
                                                |                      19. Kamrup                             |
                                                |                      20. Kamrup Metropolitan                | 
                                                |                      21. Karbi Anglong                      |
                                                |                      22. Karimganj                          |
                                                |                      23. Kokrajhar                          |
                                                |                      24. Lakhimpur                          |
                                                |                      25. Majuli                             |
                                                |                      26. Morigaon                           |
                                                |                      27. Nagaon                             |
                                                |                      28. Nalbari                            |
                                                |                      29. Sivasagar                          |
                                                |                      30. Sonitpur                           |
                                                |                      31. South Salmara-Mankachar            |
                                                |                      32. Tamulpur                           |
                                                |                      33. Tinsukia                           |
                                                |                      34. Udalguri                           |
                                                |                      35. West Karbi Anglong                 |
                                                ---------------------------------------------------------------
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Bajali'
                    break
                elif d == 2:
                    district = 'Baksa'
                    break
                elif d == 3:
                    district = 'Barpeta'
                    break
                elif d == 4:
                    district = 'Biswanath'
                    break
                elif d == 5:
                    district = 'Bongaigaon'
                    break
                elif d == 6:
                    district = 'Cachar'
                    break
                elif d == 7:
                    district = 'Charaideo'
                    break
                elif d == 8:
                    district = 'Chirang'
                    break
                elif d == 9:
                    district = 'Darrang'
                    break
                elif d == 10:
                    district = 'Dhemaji'
                    break
                elif d == 11:
                    district = 'Dhubri'
                    break
                elif d == 12:
                    district = 'Dibrugarh'
                    break
                elif d == 13:
                    district = 'Dima Hasao'
                    break
                elif d == 14:
                    district = 'Goalpara'
                    break
                elif d == 15:
                    district = 'Golaghat'
                    break
                elif d == 16:
                    district = 'Hailakandi'
                    break
                elif d == 17:
                    district = 'Hojai'
                    break
                elif d == 18:
                    district = 'Jorhat'
                    break
                elif d == 19:
                    district = 'Kamrup'
                    break
                elif d == 20:
                    district = 'Kamrup Metropolitan'
                    break
                elif d == 21:
                    district = 'Karbi Anglong'
                    break
                elif d == 22:
                    district = 'Karimganj'
                    break
                elif d == 23:
                    district = 'Kokrajhar'
                    break
                elif d == 24:
                    district = 'Lakhimpur'
                    break
                elif d == 25:
                    district = 'Majuli'
                    break
                elif d == 26:
                    district = 'Morigaon'
                    break
                elif d == 27:
                    district = 'Nagaon'
                    break
                elif d == 28:
                    district = 'Nalbari'
                    break
                elif d == 29:
                    district = 'Sivasagar'
                    break
                elif d == 30:
                    district = 'Sonitpur'
                    break
                elif d == 31:
                    district = 'South Salmara-Mankachar'
                    break
                elif d == 32:
                    district = 'Tamulpur'
                    break
                elif d == 33:
                    district = 'Tinsukia'
                    break
                elif d == 34:
                    district = 'Udalguri'
                    break
                elif d == 35:
                    district = 'West Karbi Anglong'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Bihar":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Bihar:                     |
                                                |                       1. Araria                             |
                                                |                       2. Arwal                              |
                                                |                       3. Aurangabad                         |
                                                |                       4. Banka                              | 
                                                |                       5. Begusarai                          |
                                                |                       6. Bhagalpur                          |
                                                |                       7. Bhojpur                            |
                                                |                       8. Buxar                              | 
                                                |                       9. Darbhanga                          | 
                                                |                      10. East Champaran                     |
                                                |                      11. Gaya                               | 
                                                |                      12. Gopalganj                          |
                                                |                      13. Jamui                              |
                                                |                      14. Jehanabad                          |
                                                |                      15. Kaimur                             |
                                                |                      16. Katihar                            |
                                                |                      17. Khagaria                           |
                                                |                      18. Kishanganj                         | 
                                                |                      19. Lakhisarai                         |
                                                |                      20. Madhepura                          | 
                                                |                      21. Madhubani                          |
                                                |                      22. Munger                             |
                                                |                      23. Muzaffarpur                        |
                                                |                      24. Nalanda                            |
                                                |                      25. Nawada                             |
                                                |                      26. Patna                              |
                                                |                      27. Purnia                             |
                                                |                      28. Rohtas                             |
                                                |                      29. Saharsa                            |
                                                |                      30. Samastipur                         |
                                                |                      31. Saran                              |
                                                |                      32. Sheikhpura                         |
                                                |                      33. Sheohar                            |
                                                |                      34. Sitamarhi                          |
                                                |                      35. Siwan                              |
                                                |                      36. Supaul                             |
                                                |                      37. Vaishali                           |
                                                |                      39. West Champaran                     | 
                                                ---------------------------------------------------------------
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Araria'
                    break
                elif d == 2:
                    district = 'Arwal'
                    break
                elif d == 3:
                    district = 'Aurangabad'
                    break
                elif d == 4:
                    district = 'Banka'
                    break
                elif d == 5:
                    district = 'Begusarai'
                    break
                elif d == 6:
                    district = 'Bhagalpur'
                    break
                elif d == 7:
                    district = 'Bhojpur'
                    break
                elif d == 8:
                    district = 'Buxar'
                    break
                elif d == 9:
                    district = 'Darbhanga'
                    break
                elif d == 10:
                    district = 'East Champaran'
                    break
                elif d == 11:
                    district = 'Gaya'
                    break
                elif d == 12:
                    district = 'Gopalganj'
                    break
                elif d == 13:
                    district = 'Jamui'
                    break
                elif d == 14:
                    district = 'Jehanabad'
                    break
                elif d == 15:
                    district = 'Kaimur'
                    break
                elif d == 16:
                    district = 'Katihar'
                    break
                elif d == 17:
                    district = 'Khagaria'
                    break
                elif d == 18:
                    district = 'Kishanganj'
                    break
                elif d == 19:
                    district = 'Lakhisarai'
                    break
                elif d == 20:
                    district = 'Madhepura'
                    break
                elif d == 21:
                    district = 'Madhubani'
                    break
                elif d == 22:
                    district = 'Munger'
                    break
                elif d == 23:
                    district = 'Muzaffarpur'
                    break
                elif d == 24:
                    district = 'Nalanda'
                    break
                elif d == 25:
                    district = 'Nawada'
                    break
                elif d == 26:
                    district = 'Patna'
                    break
                elif d == 27:
                    district = 'Purnia'
                    break
                elif d == 28:
                    district = 'Rohtas'
                    break
                elif d == 29:
                    district = 'Saharsa'
                    break
                elif d == 30:
                    district = 'Samastipur'
                    break
                elif d == 31:
                    district = 'Saran'
                    break
                elif d == 32:
                    district = 'Sheikhpura'
                    break
                elif d == 33:
                    district = 'Sheohar'
                    break
                elif d == 34:
                    district = 'Sitamarhi'
                    break
                elif d == 35:
                    district = 'Siwan'
                    break
                elif d == 36:
                    district = 'Supaul'
                    break
                elif d == 37:
                    district = 'Vaishali'
                    break
                elif d == 38:
                    district = 'West Champaran'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Chattisgrarh":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Chattisgarh:               |
                                                |                       1. Balod                              |
                                                |                       2. Baloda Bazar                       |
                                                |                       3. Balrampur Ramanujganj              |
                                                |                       4. Bastar                             | 
                                                |                       5. Bemetara                           |
                                                |                       6. Bijapur                            |
                                                |                       7. Bilaspur                           |
                                                |                       8. Dantewada                          | 
                                                |                       9. Dhamtari                           | 
                                                |                      10. Durg                               |
                                                |                      11. Gariaband                          | 
                                                |                      12. Gaurela Pendra Marwahi             |
                                                |                      13. Janjgir Champa                     |
                                                |                      14. Jashpur                            |
                                                |                      15. Kabirdham                          |
                                                |                      16. Kanker                             |
                                                |                      17. Khairagarh                         |
                                                |                      18. Kondagaon                          | 
                                                |                      19. Korba                              |
                                                |                      20. Koriya                             | 
                                                |                      21. Mahasamund                         |
                                                |                      22. Manendragarh                       |
                                                |                      23. Mohla Manpur                       |
                                                |                      24. Mungeli                            |
                                                |                      25. Narayanpur                         |
                                                |                      26. Raigarh                            |
                                                |                      27. Raipur                             |
                                                |                      28. Rajnandgaon                        |
                                                |                      29. Sakti                              |
                                                |                      30. Sarangarh Bilaigarh                |
                                                |                      31. Sukma                              |
                                                |                      32. Surajpur                           |
                                                |                      33. Surguja                            |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Balod'
                    break
                elif d == 2:
                    district = 'Baloda Bazar'
                    break
                elif d == 3:
                    district = 'Balrampur Ramanujganj'
                    break
                elif d == 4:
                    district = 'Bastar'
                    break
                elif d == 5:
                    district = 'Bemetara'
                    break
                elif d == 6:
                    district = 'Bijapur'
                    break
                elif d == 7:
                    district = 'Bilaspur'
                    break
                elif d == 8:
                    district = 'Dantewada'
                    break
                elif d == 9:
                    district = 'Dhamtari'
                    break
                elif d == 10:
                    district = 'Durg'
                    break
                elif d == 11:
                    district = 'Gariaband'
                    break
                elif d == 12:
                    district = 'Gaurela Pendra Marwahi'
                    break
                elif d == 13:
                    district = 'Janjgir Champa'
                    break
                elif d == 14:
                    district = 'Jashpur'
                    break
                elif d == 15:
                    district = 'Kabirdham'
                    break
                elif d == 16:
                    district = 'Kanker'
                    break
                elif d == 17:
                    district = 'Khairagarh'
                    break
                elif d == 18:
                    district = 'Kondagaon'
                    break
                elif d == 19:
                    district = 'Korba'
                    break
                elif d == 20:
                    district = 'Koriya'
                    break
                elif d == 21:
                    district = 'Mahasamund'
                    break
                elif d == 22:
                    district = 'Manendragarh '
                    break
                elif d == 23:
                    district = 'Mohla Manpur '
                    break
                elif d == 24:
                    district = 'Mungeli'
                    break
                elif d == 25:
                    district = 'Narayanpur'
                    break
                elif d == 26:
                    district = 'Raigarh'
                    break
                elif d == 27:
                    district = 'Raipur'
                    break
                elif d == 28:
                    district = 'Rajnandgaon'
                    break
                elif d == 29:
                    district = 'Sakti '
                    break
                elif d == 30:
                    district = 'Sarangarh Bilaigarh'
                    break
                elif d == 31:
                    district = 'Sukma'
                    break
                elif d == 32:
                    district = 'Surajpur'
                    break
                elif d == 33:
                    district = 'Surguja'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Goa":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Goa:                       |
                                                |                       1. North Goa                          |
                                                |                       2. South Goa                          |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'North Goa'
                    break
                elif d == 2:
                    district = 'South Goa'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Gujarat":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Gujarat:                   |
                                                |                       1. Ahmedabad                          |
                                                |                       2. Amreli                             |
                                                |                       3. Anand                              |
                                                |                       4. Aravalli                           | 
                                                |                       5. Banaskantha                        |
                                                |                       6. Bharuch                            |
                                                |                       7. Bhavnagar                          |
                                                |                       8. Botad                              | 
                                                |                       9. Chhota Udaipur                     | 
                                                |                      10. Dahod                              |
                                                |                      11. Dang                               | 
                                                |                      12. Devbhoomi Dwarka                   |
                                                |                      13. Gandhinagar                        |
                                                |                      14. Gir Somnath                        |
                                                |                      15. Jamnagar                           |
                                                |                      16. Junagadh                           |
                                                |                      17. Kheda                              |
                                                |                      18. Kutch                              | 
                                                |                      19. Mahisagar                          |
                                                |                      20. Mehsana                            | 
                                                |                      21. Morbi                              |
                                                |                      22. Narmada                            |
                                                |                      23. Navsari                            |
                                                |                      24. Panchmahal                         |
                                                |                      25. Patan                              |
                                                |                      26. Porbandar                          |
                                                |                      27. Rajkot                             |
                                                |                      28. Sabarkantha                        |
                                                |                      29. Surat                              |
                                                |                      30. Surendranagar                      |
                                                |                      31. Tapi                               |
                                                |                      32. Vadodara                           |
                                                |                      33. Valsad                             |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Ahmedabad'
                    break
                elif d == 2:
                    district = 'Amreli'
                    break
                elif d == 3:
                    district = 'Anand'
                    break
                elif d == 4:
                    district = 'Aravalli'
                    break
                elif d == 5:
                    district = 'Banaskantha'
                    break
                elif d == 6:
                    district = 'Bharuch'
                    break
                elif d == 7:
                    district = 'Bhavnagar'
                    break
                elif d == 8:
                    district = 'Botad'
                    break
                elif d == 9:
                    district = 'Chhota Udaipur'
                    break
                elif d == 10:
                    district = 'Dahod'
                    break
                elif d == 11:
                    district = 'Dang'
                    break
                elif d == 12:
                    district = 'Devbhoomi Dwarka'
                    break
                elif d == 13:
                    district = 'Gandhinagar'
                    break
                elif d == 14:
                    district = 'Gir Somnath'
                    break
                elif d == 15:
                    district = 'Jamnagar'
                    break
                elif d == 16:
                    district = 'Junagadh'
                    break
                elif d == 17:
                    district = 'Kheda'
                    break
                elif d == 18:
                    district = 'Kutch'
                    break
                elif d == 19:
                    district = 'Mahisagar'
                    break
                elif d == 20:
                    district = 'Mehsana'
                    break
                elif d == 21:
                    district = 'Morbi'
                    break
                elif d == 22:
                    district = 'Narmada'
                    break
                elif d == 23:
                    district = 'Navsari'
                    break
                elif d == 24:
                    district = 'Panchmahal'
                    break
                elif d == 25:
                    district = 'Patan'
                    break
                elif d == 26:
                    district = 'Porbandar'
                    break
                elif d == 27:
                    district = 'Rajkot'
                    break
                elif d == 28:
                    district = 'Sabarkantha'
                    break
                elif d == 29:
                    district = 'Surat'
                    break
                elif d == 30:
                    district = 'Surendranagar'
                    break
                elif d == 31:
                    district = 'Tapi'
                    break
                elif d == 32:
                    district = 'Vadodara'
                    break
                elif d == 33:
                    district = 'Valsad'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Haryana":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Haryana:                   |
                                                |                       1. Ambala                             |
                                                |                       2. Bhiwani                            |
                                                |                       3. Charkhi Dadri                      |
                                                |                       4. Faridabad                          | 
                                                |                       5. Fatehabad                          |
                                                |                       6. Gurugram                           |
                                                |                       7. Hisar                              |
                                                |                       8. Jhajjar                            | 
                                                |                       9. Jind                               | 
                                                |                      10. Kaithal                            |
                                                |                      11. Karnal                             | 
                                                |                      12. Kurukshetra                        |
                                                |                      13. Mahendragarh                       |
                                                |                      14. Mewat                              |
                                                |                      15. Palwal                             |
                                                |                      16. Panchkula                          |
                                                |                      17. Panipat                            |
                                                |                      18. Rewari                             | 
                                                |                      19. Rohtak                             |
                                                |                      20. Sirsa                              | 
                                                |                      21. Sonipat                            |
                                                |                      22. Yamunanagar                        |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Ambala'
                    break
                elif d == 2:
                    district = 'Bhiwani'
                    break
                elif d == 3:
                    district = 'Charkhi Dadri'
                    break
                elif d == 4:
                    district = 'Faridabad'
                    break
                elif d == 5:
                    district = 'Fatehabad'
                    break
                elif d == 6:
                    district = 'Gurugram'
                    break
                elif d == 7:
                    district = 'Hisar'
                    break
                elif d == 8:
                    district = 'Jhajjar'
                    break
                elif d == 9:
                    district = 'Jind'
                    break
                elif d == 10:
                    district = 'Kaithal'
                    break
                elif d == 11:
                    district = 'Karnal'
                    break
                elif d == 12:
                    district = 'Kurukshetra'
                    break
                elif d == 13:
                    district = 'Mahendragarh '
                    break
                elif d == 14:
                    district = 'Mewat'
                    break
                elif d == 15:
                    district = 'Palwal'
                    break
                elif d == 16:
                    district = 'Panchkula'
                    break
                elif d == 17:
                    district = 'Panipat'
                    break
                elif d == 18:
                    district = 'Rewari'
                    break
                elif d == 19:
                    district = 'Rohtak'
                    break
                elif d == 20:
                    district = 'Sirsa'
                    break
                elif d == 21:
                    district = 'Sonipat'
                    break
                elif d == 22:
                    district = 'Yamunanagar'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Himachal Pradesh":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Himachal Pradesh:          |
                                                |                       1. Bilaspur                           |
                                                |                       2. Chamba                             |
                                                |                       3. Hamirpur                           |
                                                |                       4. Kangra                             | 
                                                |                       5. Kinnaur                            |
                                                |                       6. Kullu                              |
                                                |                       7. Lahaul Spiti                       |
                                                |                       8. Mandi                              | 
                                                |                       9. Shimla                             | 
                                                |                      10. Sirmaur                            |
                                                |                      11. Solan                              | 
                                                |                      12. Una                                |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Bilaspur'
                    break
                elif d == 2:
                    district = 'Chamba'
                    break
                elif d == 3:
                    district = 'Hamirpur'
                    break
                elif d == 4:
                    district = 'Kangra'
                    break
                elif d == 5:
                    district = 'Kinnaur'
                    break
                elif d == 6:
                    district = 'Kullu'
                    break
                elif d == 7:
                    district = 'Lahaul Spiti'
                    break
                elif d == 8:
                    district = 'Mandi'
                    break
                elif d == 9:
                    district = 'Shimla'
                    break
                elif d == 10:
                    district = 'Sirmaur'
                    break
                elif d == 11:
                    district = 'Solan'
                    break
                elif d == 12:
                    district = 'Una'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Jammu & Kashmir":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Jammu & Kashmir:           |
                                                |                       1. Anantnag                           |
                                                |                       2. Bandipora                          |
                                                |                       3. Baramulla                          |
                                                |                       4. Budgam                             | 
                                                |                       5. Doda                               |
                                                |                       6. Ganderbal                          |
                                                |                       7. Jammu                              |
                                                |                       8. Kathua                             | 
                                                |                       9. Kishtwar                           | 
                                                |                      10. Kishtwar                           |
                                                |                      11. Kupwara                            | 
                                                |                      12. Poonch                             |
                                                |                      13. Pulwama                            |
                                                |                      14. Rajouri                            |
                                                |                      15. Ramban                             |
                                                |                      16. Reasi                              |
                                                |                      17. Samba                              |
                                                |                      18. Shopian                            | 
                                                |                      19. Srinagar                           |
                                                |                      20. Udhampur                           |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Anantnag'
                    break
                elif d == 2:
                    district = 'Bandipora'
                    break
                elif d == 3:
                    district = 'Baramulla'
                    break
                elif d == 4:
                    district = 'Budgam'
                    break
                elif d == 5:
                    district = 'Doda'
                    break
                elif d == 6:
                    district = 'Ganderbal'
                    break
                elif d == 7:
                    district = 'Jammu'
                    break
                elif d == 8:
                    district = 'Kathua'
                    break
                elif d == 9:
                    district = 'Kishtwar'
                    break
                elif d == 10:
                    district = 'Kulgam'
                    break
                elif d == 11:
                    district = 'Kupwara'
                    break
                elif d == 12:
                    district = 'Poonch'
                    break
                elif d == 13:
                    district = 'Pulwama'
                    break
                elif d == 14:
                    district = 'Rajouri'
                    break
                elif d == 15:
                    district = 'Ramban'
                    break
                elif d == 16:
                    district = 'Reasi'
                    break
                elif d == 17:
                    district = 'Reasi'
                    break
                elif d == 18:
                    district = 'Shopian'
                    break
                elif d == 19:
                    district = 'Srinagar'
                    break
                elif d == 20:
                    district = 'Udhampur'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Jharkhand":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Jharkhand :                |
                                                |                       1. Bokaro                             |
                                                |                       2. Chatra                             |
                                                |                       3. Deoghar                            |
                                                |                       4. Dhanbad                            | 
                                                |                       5. Dumka                              |
                                                |                       6. East Singhbhum                     |
                                                |                       7. Garhwa                             |
                                                |                       8. Giridih                            | 
                                                |                       9. Godda                              | 
                                                |                      10. Gumla                              |
                                                |                      11. Hazaribagh                         | 
                                                |                      12. Jamtara                            |
                                                |                      13. Khunti                             |
                                                |                      14. Koderma                            |
                                                |                      15. Latehar                            |
                                                |                      16. Lohardaga                          |
                                                |                      17. Pakur                              |
                                                |                      18. Palamu                             | 
                                                |                      19. Ramgarh                            |
                                                |                      20. Ranchi                             |  
                                                |                      21. Sahebganj                          |
                                                |                      22. Seraikela Kharsawan                |
                                                |                      23. Simdega                            |
                                                |                      24. West Singhbhum                     |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Bokaro'
                    break
                elif d == 2:
                    district = 'Chatra'
                    break
                elif d == 3:
                    district = 'Deoghar'
                    break
                elif d == 4:
                    district = 'Dhanbad'
                    break
                elif d == 5:
                    district = 'Dumka'
                    break
                elif d == 6:
                    district = 'East Singhbhum'
                    break
                elif d == 7:
                    district = 'Garhwa'
                    break
                elif d == 8:
                    district = 'Giridih'
                    break
                elif d == 9:
                    district = 'Godda'
                    break
                elif d == 10:
                    district = 'Gumla'
                    break
                elif d == 11:
                    district = 'Hazaribagh'
                    break
                elif d == 12:
                    district = 'Jamtara'
                    break
                elif d == 13:
                    district = 'Khunti'
                    break
                elif d == 14:
                    district = 'Koderma'
                    break
                elif d == 15:
                    district = 'Latehar'
                    break
                elif d == 16:
                    district = 'Lohardaga'
                    break
                elif d == 17:
                    district = 'Pakur'
                    break
                elif d == 18:
                    district = 'Palamu'
                    break
                elif d == 19:
                    district = 'Ramgarh'
                    break
                elif d == 20:
                    district = 'Ranchi'
                    break
                elif d == 21:
                    district = 'Sahebganj'
                    break
                elif d == 22:
                    district = 'Seraikela Kharsawan'
                    break
                elif d == 23:
                    district = 'Simdega'
                    break
                elif d == 24:
                    district = 'West Singhbhum'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Karnataka":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Karnataka :                |
                                                |                       1. Bagalkot                           |
                                                |                       2. Bangalore Rural                    |
                                                |                       3. Bangalore Urban                    |
                                                |                       4. Belgaum                            | 
                                                |                       5. Bellary                            |
                                                |                       6. Bidar                              |
                                                |                       7. Chamarajanagar                     |
                                                |                       8. Chikkaballapur                     | 
                                                |                       9. Chikkamagaluru                     | 
                                                |                      10. Chitradurga                        |
                                                |                      11. Dakshina Kannada                   | 
                                                |                      12. Davanagere                         |
                                                |                      13. Dharwad                            |
                                                |                      14. Gadag                              |
                                                |                      15. Kalaburagi                         |
                                                |                      16. Hassan                             |
                                                |                      17. Haveri                             |
                                                |                      18. Kodagu                             | 
                                                |                      19. Kolar                              |
                                                |                      20. Koppal                             | 
                                                |                      21. Mandya                             |
                                                |                      22. Mysore                             |
                                                |                      23. Raichur                            |
                                                |                      24. Ramanagara                         |
                                                |                      25. Shimoga                            |
                                                |                      26. Tumkur                             |
                                                |                      27. Udupi                              |
                                                |                      28. Uttara Kannada                     |
                                                |                      29. Vijayanagara                       |
                                                |                      30. Vijayapura                         |
                                                |                      31. Yadgir                             |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Bagalkot'
                    break
                elif d == 2:
                    district = 'Bangalore Rural'
                    break
                elif d == 3:
                    district = 'Bangalore Urban'
                    break
                elif d == 4:
                    district = 'Belgaum'
                    break
                elif d == 5:
                    district = 'Bellary'
                    break
                elif d == 6:
                    district = 'Bidar'
                    break
                elif d == 7:
                    district = 'Chamarajanagar'
                    break
                elif d == 8:
                    district = 'Chikkaballapur'
                    break
                elif d == 9:
                    district = 'Chikkamagaluru'
                    break
                elif d == 10:
                    district = 'Chitradurga'
                    break
                elif d == 11:
                    district = 'Dakshina Kannada'
                    break
                elif d == 12:
                    district = 'Davanagere'
                    break
                elif d == 13:
                    district = 'Dharwad'
                    break
                elif d == 14:
                    district = 'Gadag'
                    break
                elif d == 15:
                    district = 'Kalaburagi'
                    break
                elif d == 16:
                    district = 'Hassan'
                    break
                elif d == 17:
                    district = 'Haveri'
                    break
                elif d == 18:
                    district = 'Kodagu'
                    break
                elif d == 19:
                    district = 'Kolar'
                    break
                elif d == 20:
                    district = 'Koppal'
                    break
                elif d == 21:
                    district = 'Mandya'
                    break
                elif d == 22:
                    district = 'Mysore'
                    break
                elif d == 23:
                    district = 'Raichur'
                    break
                elif d == 24:
                    district = 'Ramanagara'
                    break
                elif d == 25:
                    district = 'Shimoga'
                    break
                elif d == 26:
                    district = 'Tumkur'
                    break
                elif d == 27:
                    district = 'Udupi'
                    break
                elif d == 28:
                    district = 'Uttara Kannada'
                    break
                elif d == 29:
                    district = 'Vijayanagara'
                    break
                elif d == 30:
                    district = 'Vijayapura'
                    break
                elif d == 31:
                    district = 'Yadgir'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Kerala":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Kerala :                   |
                                                |                       1. Alappuzha                          |
                                                |                       2. Ernakulam                          |
                                                |                       3. Idukki                             |
                                                |                       4. Kannur                             | 
                                                |                       5. Kasaragod                          |
                                                |                       6. Kollam                             |
                                                |                       7. Kottayam                           |
                                                |                       8. Kozhikode                          | 
                                                |                       9. Malappuram                         | 
                                                |                      10. Palakkad                           |
                                                |                      11. Pathanamthitta                     | 
                                                |                      12. Thiruvananthapuram                 |
                                                |                      13. Thrissur                           |
                                                |                      14. Wayanad                            |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Alappuzha'
                    break
                elif d == 2:
                    district = 'Ernakulam'
                    break
                elif d == 3:
                    district = 'Idukki'
                    break
                elif d == 4:
                    district = 'Kannur'
                    break
                elif d == 5:
                    district = 'Kasaragod'
                    break
                elif d == 6:
                    district = 'Kollam'
                    break
                elif d == 7:
                    district = 'Kottayam'
                    break
                elif d == 8:
                    district = 'Kozhikode'
                    break
                elif d == 9:
                    district = 'Malappuram'
                    break
                elif d == 10:
                    district = 'Palakkad'
                    break
                elif d == 11:
                    district = 'Pathanamthitta'
                    break
                elif d == 12:
                    district = 'Thiruvananthapuram'
                    break
                elif d == 13:
                    district = 'Thrissur'
                    break
                elif d == 14:
                    district = 'Wayanad'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Madhya Pradesh":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Madhya Pradesh:            |
                                                |                       1. Agar Malwa                         |
                                                |                       2. Alirajpur                          |
                                                |                       3. Anuppur                            |
                                                |                       4. Ashoknagar                         | 
                                                |                       5. Balaghat                           |
                                                |                       6. Barwani                            |
                                                |                       7. Betul                              |
                                                |                       8. Bhind                              | 
                                                |                       9. Bhopal                             | 
                                                |                      10. Burhanpur                          |
                                                |                      11. Chachaura                          | 
                                                |                      12. Chhatarpur                         |
                                                |                      13. Chhindwara                         |
                                                |                      14. Damoh                              |
                                                |                      15. Datia                              |
                                                |                      16. Dewas                              |
                                                |                      17. Dhar                               |
                                                |                      18. Dindori                            | 
                                                |                      19. Guna                               |
                                                |                      20. Gwalior                            | 
                                                |                      21. Harda                              |
                                                |                      22. Hoshangabad                        |
                                                |                      23. Indore                             | 
                                                |                      24. Jabalpur                           |
                                                |                      25. Jhabua                             |
                                                |                      26. Katni                              |
                                                |                      27. Khandwa                            |
                                                |                      28. Khargone                           |
                                                |                      29. Maihar                             |
                                                |                      30. Mandla                             |
                                                |                      31. Mandsaur                           |
                                                |                      32. Morena                             |
                                                |                      33. Nagda                              |
                                                |                      34. Narsinghpur                        |
                                                |                      35. Neemuch                            |
                                                |                      36. Niwari                             |
                                                |                      37. Panna                              |
                                                |                      38. Raisen                             |
                                                |                      39. Rajgarh                            |
                                                |                      40. Ratlam                             |
                                                |                      41. Rewa                               |
                                                |                      42. Sagar                              |
                                                |                      43. Satna                              |
                                                |                      44. Sehore                             |
                                                |                      45. Seoni                              |
                                                |                      46. Shahdol                            |
                                                |                      47. Shajapur                           |
                                                |                      48. Sheopur                            |
                                                |                      49. Shivpuri                           |
                                                |                      50. Sidhi                              |
                                                |                      51. Singrauli                          |
                                                |                      52. Tikamgarh                          |
                                                |                      53. Ujjain                             |
                                                |                      54. Umaria                             |
                                                |                      55. Umaria                             |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Agar Malwa'
                    break
                elif d == 2:
                    district = 'Alirajpur'
                    break
                elif d == 3:
                    district = 'Anuppur'
                    break
                elif d == 4:
                    district = 'Ashoknagar'
                    break
                elif d == 5:
                    district = 'Balaghat'
                    break
                elif d == 6:
                    district = 'Barwani'
                    break
                elif d == 7:
                    district = 'Betul'
                    break
                elif d == 8:
                    district = 'Bhind'
                    break
                elif d == 9:
                    district = 'Bhopal'
                    break
                elif d == 10:
                    district = 'Burhanpur'
                    break
                elif d == 11:
                    district = 'Chachaura'
                    break
                elif d == 12:
                    district = 'Chhatarpur'
                    break
                elif d == 13:
                    district = 'Chhindwara'
                    break
                elif d == 14:
                    district = 'Damoh'
                    break
                elif d == 15:
                    district = 'Datia'
                    break
                elif d == 16:
                    district = 'Dewas'
                    break
                elif d == 17:
                    district = 'Dhar'
                    break
                elif d == 18:
                    district = 'Dindori'
                    break
                elif d == 19:
                    district = 'Guna'
                    break
                elif d == 20:
                    district = 'Gwalior'
                    break
                elif d == 21:
                    district = 'Harda'
                    break
                elif d == 22:
                    district = 'Hoshangabad'
                    break
                elif d == 23:
                    district = 'Indore'
                    break
                elif d == 24:
                    district = 'Jabalpur'
                    break
                elif d == 25:
                    district = 'Jhabua'
                    break
                elif d == 26:
                    district = 'Katni'
                    break
                elif d == 27:
                    district = 'Khandwa'
                    break
                elif d == 28:
                    district = 'Khargone'
                    break
                elif d == 29:
                    district = 'Maihar'
                    break
                elif d == 30:
                    district = 'Mandla'
                    break
                elif d == 31:
                    district = 'Mandsaur'
                    break
                elif d == 32:
                    district = 'Morena'
                    break
                elif d == 33:
                    district = 'Nagda'
                    break
                elif d == 34:
                    district = 'Narsinghpur'
                    break
                elif d == 35:
                    district = 'Neemuch'
                    break
                elif d == 36:
                    district = 'Niwari '
                    break
                elif d == 37:
                    district = 'Panna'
                    break
                elif d == 38:
                    district = 'Raisen'
                    break
                elif d == 39:
                    district = 'Rajgarh'
                    break
                elif d == 40:
                    district = 'Ratlam'
                    break
                elif d == 41:
                    district = 'Rewa'
                    break
                elif d == 42:
                    district = 'Sagar'
                    break
                elif d == 43:
                    district = 'Satna'
                    break
                elif d == 44:
                    district = 'Sehore'
                    break
                elif d == 45:
                    district = 'Seoni'
                    break
                elif d == 46:
                    district = 'Shahdol'
                    break
                elif d == 47:
                    district = 'Shajapur'
                    break
                elif d == 48:
                    district = 'Sheopur'
                    break
                elif d == 49:
                    district = 'Shivpuri'
                    break
                elif d == 50:
                    district = 'Sidhi'
                    break
                elif d == 51:
                    district = 'Singrauli'
                    break
                elif d == 52:
                    district = 'Tikamgarh'
                    break
                elif d == 53:
                    district = 'Ujjain'
                    break
                elif d == 54:
                    district = 'Umaria'
                    break
                elif d == 55:
                    district = 'Vidisha'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Maharashtra":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Maharashtra :              |
                                                |                       1. Ahmednagar                         |
                                                |                       2. Akola                              |
                                                |                       3. Amravati                           |
                                                |                       4. Aurangabad                         | 
                                                |                       5. Beed                               |
                                                |                       6. Bhandara                           |
                                                |                       7. Bhandara                           |
                                                |                       8. Chandrapur                         | 
                                                |                       9. Dhule                              | 
                                                |                      10. Gadchiroli                         |
                                                |                      11. Gondia                             | 
                                                |                      12. Hingoli                            |
                                                |                      13. Jalgaon                            |
                                                |                      14. Jalna                              |
                                                |                      15. Kolhapur                           |
                                                |                      16. Latur                              |
                                                |                      17. Mumbai City                        |
                                                |                      18. Mumbai Suburban                    | 
                                                |                      19. Nagpur                             |
                                                |                      20. Nanded                             | 
                                                |                      21. Nandurbar                          |
                                                |                      22. Nashik                             |
                                                |                      23. Osmanabad                          |
                                                |                      24. Palghar                            |
                                                |                      25. Parbhani                           |
                                                |                      26. Pune                               |
                                                |                      27. Raigad                             |
                                                |                      28. Ratnagiri                          |
                                                |                      29. Sangli                             |
                                                |                      30. Satara                             |
                                                |                      31. Sindhudurg                         |
                                                |                      32. Solapur                            |
                                                |                      33. Thane                              |
                                                |                      34. Wardha                             |
                                                |                      35. Washim                             |
                                                |                      36. Yavatmal                           |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Ahmednagar'
                    break
                elif d == 2:
                    district = 'Akola'
                    break
                elif d == 3:
                    district = 'Amravati'
                    break
                elif d == 4:
                    district = 'Aurangabad'
                    break
                elif d == 5:
                    district = 'Beed'
                    break
                elif d == 6:
                    district = 'Bhandara'
                    break
                elif d == 7:
                    district = 'Buldhana'
                    break
                elif d == 8:
                    district = 'Chandrapur'
                    break
                elif d == 9:
                    district = 'Dhule'
                    break
                elif d == 10:
                    district = 'Gadchiroli'
                    break
                elif d == 11:
                    district = 'Gondia'
                    break
                elif d == 12:
                    district = 'Hingoli'
                    break
                elif d == 13:
                    district = 'Jalgaon'
                    break
                elif d == 14:
                    district = 'Jalna'
                    break
                elif d == 15:
                    district = 'Kolhapur'
                    break
                elif d == 16:
                    district = 'Latur'
                    break
                elif d == 17:
                    district = 'Mumbai City'
                    break
                elif d == 18:
                    district = 'Mumbai Suburban'
                    break
                elif d == 19:
                    district = 'Nagpur'
                    break
                elif d == 20:
                    district = 'Nanded'
                    break
                elif d == 21:
                    district = 'Nandurbar'
                    break
                elif d == 22:
                    district = 'Nashik'
                    break
                elif d == 23:
                    district = 'Osmanabad'
                    break
                elif d == 24:
                    district = 'Palghar'
                    break
                elif d == 25:
                    district = 'Parbhani'
                    break
                elif d == 26:
                    district = 'Pune'
                    break
                elif d == 27:
                    district = ''
                    break
                elif d == 28:
                    district = 'Ratnagiri'
                    break
                elif d == 29:
                    district = 'Sangli'
                    break
                elif d == 30:
                    district = 'Satara'
                    break
                elif d == 31:
                    district = 'Sindhudurg'
                    break
                elif d == 32:
                    district = 'Solapur'
                    break
                elif d == 33:
                    district = 'Thane'
                    break
                elif d == 34:
                    district = 'Wardha'
                    break
                elif d == 35:
                    district = 'Washim'
                    break
                elif d == 36:
                    district = 'Yavatmal'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Manipur":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Manipur :                  |
                                                |                       1. Bishnupur                          |
                                                |                       2. Chandel                            |
                                                |                       3. Churachandpur                      |
                                                |                       4. Imphal East                        | 
                                                |                       5. Imphal West                        |
                                                |                       6. Jiribam                            |
                                                |                       7. Kakching                           |
                                                |                       8. Kamjong                            | 
                                                |                       9. Kangpokpi                          | 
                                                |                      10. Noney                              |
                                                |                      11. Pherzawl                           | 
                                                |                      12. Senapati                           |
                                                |                      13. Tamenglong                         |
                                                |                      14. Tamenglong                         |
                                                |                      15. Thoubal                            |
                                                |                      16. Ukhrul                             |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Bishnupur'
                    break
                elif d == 2:
                    district = 'Chandel'
                    break
                elif d == 3:
                    district = 'Churachandpur'
                    break
                elif d == 4:
                    district = 'Imphal East'
                    break
                elif d == 5:
                    district = 'Imphal West'
                    break
                elif d == 6:
                    district = 'Jiribam'
                    break
                elif d == 7:
                    district = 'Kakching'
                    break
                elif d == 8:
                    district = 'Kamjong'
                    break
                elif d == 9:
                    district = 'Kangpokpi'
                    break
                elif d == 10:
                    district = 'Noney'
                    break
                elif d == 11:
                    district = 'Pherzawl'
                    break
                elif d == 12:
                    district = 'Senapati'
                    break
                elif d == 13:
                    district = 'Tamenglong'
                    break
                elif d == 14:
                    district = 'Tengnoupal'
                    break
                elif d == 15:
                    district = 'Thoubal'
                    break
                elif d == 16:
                    district = 'Ukhrul'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Meghalaya":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Meghalaya :                |
                                                |                       1. East Garo Hills                    |
                                                |                       2. East Jaintia Hills                 |
                                                |                       3. East Khasi Hills                   |
                                                |                       4. Mairang (Eastern West Khasi Hills) | 
                                                |                       5. North Garo Hills                   |
                                                |                       6. Ri Bhoi                            |
                                                |                       7. South Garo Hills                   |
                                                |                       8. South West Garo Hills              | 
                                                |                       9. South West Khasi Hills             | 
                                                |                      10. West Garo Hills                    |
                                                |                      11. West Jaintia Hills                 | 
                                                |                      12. West Khasi Hills                   |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'East Garo Hills'
                    break
                elif d == 2:
                    district = 'East Jaintia Hills'
                    break
                elif d == 3:
                    district = 'East Khasi Hills'
                    break
                elif d == 4:
                    district = 'Mairang (Eastern West Khasi Hills)'
                    break
                elif d == 5:
                    district = 'North Garo Hills'
                    break
                elif d == 6:
                    district = 'Ri Bhoi'
                    break
                elif d == 7:
                    district = 'South Garo Hills'
                    break
                elif d == 8:
                    district = 'South West Garo Hills'
                    break
                elif d == 9:
                    district = 'South West Khasi Hills'
                    break
                elif d == 10:
                    district = 'West Garo Hills'
                    break
                elif d == 11:
                    district = 'West Jaintia Hills'
                    break
                elif d == 12:
                    district = 'West Khasi Hills'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Mizoram":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Mizoram :                  |
                                                |                       1. Aizawl                             |
                                                |                       2. Champhai                           |
                                                |                       3. Hnahthial                          |
                                                |                       4. Khawzawl                           | 
                                                |                       5. Kolasib                            |
                                                |                       6. Lawngtlai                          |
                                                |                       7. Lunglei                            |
                                                |                       8. Mamit                              | 
                                                |                       9. Saiha                              | 
                                                |                      10. Saitual                            |
                                                |                      11. Serchhip                           | 
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Aizawl'
                    break
                elif d == 2:
                    district = 'Champhai'
                    break
                elif d == 3:
                    district = 'Hnahthial'
                    break
                elif d == 4:
                    district = 'Khawzawl'
                    break
                elif d == 5:
                    district = 'Kolasib'
                    break
                elif d == 6:
                    district = 'Lawngtlai'
                    break
                elif d == 7:
                    district = 'Lunglei'
                    break
                elif d == 8:
                    district = 'Mamit'
                    break
                elif d == 9:
                    district = 'Saiha'
                    break
                elif d == 10:
                    district = 'Saitual'
                    break
                elif d == 11:
                    district = 'Serchhip'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Nagaland":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Nagaland :                 |
                                                |                       1. Chumukedima                        |
                                                |                       2. Dimapur                            |
                                                |                       3. Kiphire                            |
                                                |                       4. Kohima                             | 
                                                |                       5. Longleng                           |
                                                |                       6. Mokokchung                         |
                                                |                       7. Mon                                |
                                                |                       8. Niuland                            | 
                                                |                       9. Noklak                             | 
                                                |                      10. Peren                              |
                                                |                      11. Phek                               | 
                                                |                      12. Shamator                           |
                                                |                      13. Tseminyu                           |
                                                |                      14. Tuensang                           |
                                                |                      15. Wokha                              |
                                                |                      16. Zunheboto                          |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Chumukedima '
                    break
                elif d == 2:
                    district = 'Dimapur'
                    break
                elif d == 3:
                    district = 'Kiphire'
                    break
                elif d == 4:
                    district = 'Kohima'
                    break
                elif d == 5:
                    district = 'Longleng'
                    break
                elif d == 6:
                    district = 'Mokokchung'
                    break
                elif d == 7:
                    district = 'Mon'
                    break
                elif d == 8:
                    district = 'Niuland '
                    break
                elif d == 9:
                    district = 'Noklak'
                    break
                elif d == 10:
                    district = 'Peren'
                    break
                elif d == 11:
                    district = 'Phek'
                    break
                elif d == 12:
                    district = 'Shamator'
                    break
                elif d == 13:
                    district = 'Tseminyu '
                    break
                elif d == 14:
                    district = 'Tuensang'
                    break
                elif d == 15:
                    district = 'Wokha'
                    break
                elif d == 16:
                    district = 'Zunheboto'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Odisha":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Odisha :                   |
                                                |                       1. Angul                              |
                                                |                       2. Balangir                           |
                                                |                       3. Balasore                           |
                                                |                       4. Bargarh                            | 
                                                |                       5. Bhadrak                            |
                                                |                       6. Boudh                              |
                                                |                       7. Cuttack                            |
                                                |                       8. Debagarh                           | 
                                                |                       9. Dhenkanal                          | 
                                                |                      10. Gajapati                           |
                                                |                      11. Ganjam                             | 
                                                |                      12. Jagatsinghpur                      |
                                                |                      13. Jajpur                             |
                                                |                      14. Jharsuguda                         |
                                                |                      15. Kalahandi                          |
                                                |                      16. Kandhamal                          |
                                                |                      17. Kendrapara                         |
                                                |                      18. Kendujhar                          | 
                                                |                      19. Khordha                            |
                                                |                      20. Koraput                            | 
                                                |                      21. Malkangiri                         |
                                                |                      22. Mayurbhanj                         |
                                                |                      23. Nabarangpur                        |
                                                |                      24. Nayagarh                           |
                                                |                      25. Nuapada                            |
                                                |                      26. Puri                               |
                                                |                      27. Rayagada                           |
                                                |                      28. Sambalpur                          |
                                                |                      29. Subarnapur                         |
                                                |                      30. Sundergarh                         |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Angul'
                    break
                elif d == 2:
                    district = 'Balangir'
                    break
                elif d == 3:
                    district = 'Balasore'
                    break
                elif d == 4:
                    district = 'Bargarh'
                    break
                elif d == 5:
                    district = 'Bhadrak'
                    break
                elif d == 6:
                    district = 'Boudh'
                    break
                elif d == 7:
                    district = 'Cuttack'
                    break
                elif d == 8:
                    district = 'Debagarh'
                    break
                elif d == 9:
                    district = 'Dhenkanal'
                    break
                elif d == 10:
                    district = 'Gajapati'
                    break
                elif d == 11:
                    district = 'Ganjam'
                    break
                elif d == 12:
                    district = 'Jagatsinghpur'
                    break
                elif d == 13:
                    district = 'Jajpur'
                    break
                elif d == 14:
                    district = 'Jharsuguda'
                    break
                elif d == 15:
                    district = 'Kalahandi'
                    break
                elif d == 16:
                    district = 'Kandhamal'
                    break
                elif d == 17:
                    district = 'Kendrapara'
                    break
                elif d == 18:
                    district = 'Kendujhar'
                    break
                elif d == 19:
                    district = 'Khordha '
                    break
                elif d == 20:
                    district = 'Koraput'
                    break
                elif d == 21:
                    district = 'Malkangiri'
                    break
                elif d == 22:
                    district = 'Mayurbhanj'
                    break
                elif d == 23:
                    district = 'Nabarangpur'
                    break
                elif d == 24:
                    district = 'Nayagarh'
                    break
                elif d == 25:
                    district = 'Nuapada'
                    break
                elif d == 26:
                    district = 'Puri'
                    break
                elif d == 27:
                    district = 'Rayagada'
                    break
                elif d == 28:
                    district = 'Sambalpur'
                    break
                elif d == 29:
                    district = 'Subarnapur'
                    break
                elif d == 30:
                    district = 'Sundergarh'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Punjab":
            print("""
                                            ---------------------------------------------------------------
                                            |          List of all District in Punjab :                   |
                                            |                       1. Amritsar                           |
                                            |                       2. Barnala                            |
                                            |                       3. Bathinda                           |
                                            |                       4. Faridkot                           | 
                                            |                       5. Fatehgarh Sahib                    |
                                            |                       6. Fazilka                            |
                                            |                       7. Firozpur                           |
                                            |                       8. Gurdaspur                          | 
                                            |                       9. Hoshiarpur                         | 
                                            |                      10. Jalandhar                          |
                                            |                      11. Kapurthala                         | 
                                            |                      12. Ludhiana                           |
                                            |                      13. Malerkotla                         |
                                            |                      14. Mansa                              |
                                            |                      15. Moga                               |
                                            |                      16. Mohali                             |
                                            |                      17. Muktsar                            |
                                            |                      18. Pathankot                          | 
                                            |                      19. Patiala                            |
                                            |                      20. Rupnagar                           | 
                                            |                      21. Sangrur                            |  
                                            |                      22. Shaheed Bhagat Singh Nagar         |
                                            |                      23. Tarn Taran                         |
                                            ---------------------------------------------------------------

                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Amritsar'
                    break
                elif d == 2:
                    district = 'Barnala'
                    break
                elif d == 3:
                    district = 'Bathinda'
                    break
                elif d == 4:
                    district = 'Faridkot'
                    break
                elif d == 5:
                    district = 'Fatehgarh Sahib'
                    break
                elif d == 6:
                    district = 'Fazilka'
                    break
                elif d == 7:
                    district = 'Firozpur'
                    break
                elif d == 8:
                    district = 'Gurdaspur'
                    break
                elif d == 9:
                    district = 'Hoshiarpur'
                    break
                elif d == 10:
                    district = 'Jalandhar'
                    break
                elif d == 11:
                    district = 'Kapurthala'
                    break
                elif d == 12:
                    district = 'Ludhiana'
                    break
                elif d == 13:
                    district = 'Malerkotla '
                    break
                elif d == 14:
                    district = 'Mansa'
                    break
                elif d == 15:
                    district = 'Moga'
                    break
                elif d == 16:
                    district = 'Mohali'
                    break
                elif d == 17:
                    district = 'Muktsar'
                    break
                elif d == 18:
                    district = 'Pathankot'
                    break
                elif d == 19:
                    district = 'Patiala'
                    break
                elif d == 20:
                    district = 'Rupnagar'
                    break
                elif d == 21:
                    district = 'Sangrur'
                    break
                elif d == 22:
                    district = 'Shaheed Bhagat Singh Nagar'
                    break
                elif d == 23:
                    district = 'Tarn Taran'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Rajasthan":
            print("""                                        
                                                ---------------------------------------------------------------
                                                |          List of all District in Rajasthan:                 |
                                                |                       1. Ajmer                              |
                                                |                       2. Alwar                              |
                                                |                       3. Banswara                           |
                                                |                       4. Baran                              | 
                                                |                       5. Barmer                             |
                                                |                       6. Bharatpur                          |
                                                |                       7. Bhilwara                           |
                                                |                       8. Bikaner                            | 
                                                |                       9. Bundi                              | 
                                                |                      10. Chittorgarh                        |
                                                |                      11. Churu                              | 
                                                |                      12. Dausa                              |
                                                |                      13. Dholpur                            |
                                                |                      14. Dungarpur                          |
                                                |                      15. Sri Ganganagar                     |
                                                |                      16. Hanumangarh                        |
                                                |                      17. Jaipur                             |
                                                |                      18. Jaisalmer                          | 
                                                |                      19. Jalore                             |
                                                |                      20. Jhalawar                           | 
                                                |                      21. Jhunjhunu                          |
                                                |                      22. Jodhpur                            |
                                                |                      23. Karauli                            |
                                                |                      24. Kota                               |
                                                |                      25. Nagaur                             |
                                                |                      26. Pali                               |
                                                |                      27. Pratapgarh                         |
                                                |                      28. Rajsamand                          |
                                                |                      29. Sawai Madhopur                     |
                                                |                      30. Sikar                              |
                                                |                      31. Sirohi                             |
                                                |                      32. Tonk                               |
                                                |                      33. Udaipur                            |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Ajmer'
                    break
                elif d == 2:
                    district = 'Alwar'
                    break
                elif d == 3:
                    district = 'Banswara'
                    break
                elif d == 4:
                    district = 'Baran'
                    break
                elif d == 5:
                    district = 'Barmer'
                    break
                elif d == 6:
                    district = 'Bharatpur'
                    break
                elif d == 7:
                    district = 'Bhilwara'
                    break
                elif d == 8:
                    district = 'Bikaner'
                    break
                elif d == 9:
                    district = 'Bundi'
                    break
                elif d == 10:
                    district = 'Chittorgarh'
                    break
                elif d == 11:
                    district = 'Churu'
                    break
                elif d == 12:
                    district = 'Dausa'
                    break
                elif d == 13:
                    district = 'Dholpur'
                    break
                elif d == 14:
                    district = 'Dungarpur'
                    break
                elif d == 15:
                    district = 'Sri Ganganagar'
                    break
                elif d == 16:
                    district = 'Hanumangarh'
                    break
                elif d == 17:
                    district = 'Jaipur'
                    break
                elif d == 18:
                    district = 'Jaisalmer'
                    break
                elif d == 19:
                    district = 'Jalore'
                    break
                elif d == 20:
                    district = 'Jhalawar'
                    break
                elif d == 21:
                    district = 'Jhunjhunu'
                    break
                elif d == 22:
                    district = 'Jodhpur'
                    break
                elif d == 23:
                    district = 'Karauli'
                    break
                elif d == 24:
                    district = 'Kota'
                    break
                elif d == 25:
                    district = 'Nagaur'
                    break
                elif d == 26:
                    district = 'Pali'
                    break
                elif d == 27:
                    district = 'Pratapgarh'
                    break
                elif d == 28:
                    district = 'Rajsamand'
                    break
                elif d == 29:
                    district = 'Sawai Madhopur'
                    break
                elif d == 30:
                    district = 'Sikar'
                    break
                elif d == 31:
                    district = 'Sirohi'
                    break
                elif d == 32:
                    district = 'Tonk'
                    break
                elif d == 33:
                    district = 'Udaipur'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Sikkim":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Sikkim:                    |
                                                |                       1. East Sikkim                        |
                                                |                       2. North Sikkim                       |
                                                |                       3. Pakyong                            |
                                                |                       4. Soreng                             | 
                                                |                       5. South Sikkim                       |
                                                |                       6. West Sikkim                        |
                                                ---------------------------------------------------------------

                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'East Sikkim'
                    break
                elif d == 2:
                    district = 'North Sikkim'
                    break
                elif d == 3:
                    district = 'Pakyong'
                    break
                elif d == 4:
                    district = 'Soreng'
                    break
                elif d == 5:
                    district = 'South Sikkim'
                    break
                elif d == 6:
                    district = 'West Sikkim'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Tamil Nadu":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Tamil Nadu:                |
                                                |                       1. Ariyalur                           |
                                                |                       2. Chengalpattu                       |
                                                |                       3. Chennai                            |
                                                |                       4. Coimbatore                         | 
                                                |                       5. Cuddalore                          |
                                                |                       6. Dharmapuri                         |
                                                |                       7. Dindigul                           |
                                                |                       8. Erode                              | 
                                                |                       9. Kallakurichi                       | 
                                                |                      10. Kanchipuram                        |
                                                |                      11. Kanyakumari                        | 
                                                |                      12. Karur                              |
                                                |                      13. Krishnagiri                        |
                                                |                      14. Madurai                            |
                                                |                      15. Mayiladuthurai                     |
                                                |                      16. Nagapattinam                       |
                                                |                      17. Namakkal                           |
                                                |                      18. Nilgiris                           | 
                                                |                      19. Perambalur                         |
                                                |                      20. Pudukkottai                        | 
                                                |                      21. Ramanathapuram                     |
                                                |                      22. Ranipeti                           |
                                                |                      23. Salem                              |
                                                |                      24. Sivaganga                          |
                                                |                      25. Tenkasi                            |
                                                |                      26. Thanjavur                          |
                                                |                      27. Theni                              |
                                                |                      28. Thoothukudi                        |
                                                |                      29. Tiruchirappalli                    |
                                                |                      30. Tirunelveli                        |
                                                |                      31. Tirupattur                         |
                                                |                      32. Tiruppur                           |
                                                |                      33. Tiruvallur                         |
                                                |                      34. Tiruvannamalai                     |
                                                |                      35. Tiruvarur                          |
                                                |                      36. Vellore                            |
                                                |                      37. Viluppuram                         |
                                                |                      38. Virudhunagar                       |
                                                ---------------------------------------------------------------
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Ariyalur'
                    break
                elif d == 2:
                    district = 'Chengalpattu '
                    break
                elif d == 3:
                    district = 'Chennai'
                    break
                elif d == 4:
                    district = 'Coimbatore'
                    break
                elif d == 5:
                    district = 'Cuddalore'
                    break
                elif d == 6:
                    district = 'Dharmapuri'
                    break
                elif d == 7:
                    district = 'Dindigul'
                    break
                elif d == 8:
                    district = 'Erode'
                    break
                elif d == 9:
                    district = 'Kallakurichi '
                    break
                elif d == 10:
                    district = 'Kanchipuram'
                    break
                elif d == 11:
                    district = 'Kanyakumari'
                    break
                elif d == 12:
                    district = 'Karur'
                    break
                elif d == 13:
                    district = 'Krishnagiri'
                    break
                elif d == 14:
                    district = 'Madurai'
                    break
                elif d == 15:
                    district = 'Mayiladuthurai'
                    break
                elif d == 16:
                    district = 'Nagapattinam'
                    break
                elif d == 17:
                    district = 'Namakkal'
                    break
                elif d == 18:
                    district = 'Nilgiris'
                    break
                elif d == 19:
                    district = 'Perambalur'
                    break
                elif d == 20:
                    district = 'Pudukkottai'
                    break
                elif d == 21:
                    district = 'Ramanathapuram'
                    break
                elif d == 22:
                    district = 'Ranipet'
                    break
                elif d == 23:
                    district = 'Salem'
                    break
                elif d == 24:
                    district = 'Sivaganga'
                    break
                elif d == 25:
                    district = 'Tenkasi '
                    break
                elif d == 26:
                    district = 'Thanjavur'
                    break
                elif d == 27:
                    district = 'Theni'
                    break
                elif d == 28:
                    district = 'Thoothukudi'
                    break
                elif d == 29:
                    district = 'Tiruchirappalli'
                    break
                elif d == 30:
                    district = 'Tirunelveli'
                    break
                elif d == 31:
                    district = 'Tirupattur'
                    break
                elif d == 32:
                    district = 'Tiruppur'
                    break
                elif d == 33:
                    district = 'Tiruvallur'
                    break
                elif d == 34:
                    district = 'Tiruvannamalai'
                    break
                elif d == 35:
                    district = 'Tiruvarur'
                    break
                elif d == 36:
                    district = 'Vellore'
                    break
                elif d == 37:
                    district = 'Viluppuram'
                    break
                elif d == 38:
                    district = 'Virudhunagar'
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Telangana":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Telangana:                 |
                                                |                       1. Adilabad                           |
                                                |                       2. Bhadradri Kothagudem               |
                                                |                       3. Hyderabad                          |
                                                |                       4. Jagtial                            | 
                                                |                       5. Jangaon                            |
                                                |                       6. Jayashankar Bhupalpally            |
                                                |                       7. Jogulamba Gadwal                   |
                                                |                       8. Kamareddy                          | 
                                                |                       9. Karimnagar                         | 
                                                |                      10. Khammam                            |
                                                |                      11. Komaram Bheem                      | 
                                                |                      12. Mahabubabad                        |
                                                |                      13. Mahbubnagar                        |
                                                |                      14. Mancherial                         |
                                                |                      15. Medak                              |
                                                |                      16. Medchal Malkajgiri                 |
                                                |                      17. Mulugu                             |
                                                |                      18. Nagarkurnool                       | 
                                                |                      19. Nalgonda                           |
                                                |                      20. Narayanpet                         | 
                                                |                      21. Nirmal                             |
                                                |                      22. Nizamabad                          |
                                                |                      23. Peddapalli                         |
                                                |                      24. Peddapalli                         |
                                                |                      25. Ranga Reddy                        |
                                                |                      26. Sangareddy                         |
                                                |                      27. Siddipet                           |
                                                |                      28. Suryapet                           |
                                                |                      29. Wanaparthy                         |
                                                |                      30. Warangal                           |
                                                |                      31. Hanamkonda                         |
                                                |                      32. Yadadri Bhuvanagiri                |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Adilabad'
                    break
                elif d == 2:
                    district = 'Bhadradri Kothagudem'
                    break
                elif d == 3:
                    district = 'Hyderabad'
                    break
                elif d == 4:
                    district = 'Jagtial'
                    break
                elif d == 5:
                    district = 'Jangaon'
                    break
                elif d == 6:
                    district = 'Jayashankar Bhupalpally'
                    break
                elif d == 7:
                    district = 'Jogulamba Gadwal'
                    break
                elif d == 8:
                    district = 'Kamareddy'
                    break
                elif d == 9:
                    district = 'Karimnagar'
                    break
                elif d == 10:
                    district = 'Khammam'
                    break
                elif d == 11:
                    district = 'Komaram Bheem'
                    break
                elif d == 12:
                    district = 'Mahabubabad'
                    break
                elif d == 13:
                    district = 'Mahbubnagar'
                    break
                elif d == 14:
                    district = 'Mancherial'
                    break
                elif d == 15:
                    district = 'Medak'
                    break
                elif d == 16:
                    district = 'Medchal Malkajgiri'
                    break
                elif d == 17:
                    district = 'Mulugu'
                    break
                elif d == 18:
                    district = 'Nagarkurnool'
                    break
                elif d == 19:
                    district = 'Nalgonda'
                    break
                elif d == 20:
                    district = 'Narayanpet '
                    break
                elif d == 21:
                    district = 'Nirmal'
                    break
                elif d == 22:
                    district = 'Nizamabad'
                    break
                elif d == 23:
                    district = 'Peddapalli'
                    break
                elif d == 24:
                    district = 'Rajanna Sircilla'
                    break
                elif d == 25:
                    district = 'Ranga Reddy'
                    break
                elif d == 26:
                    district = 'Sangareddy'
                    break
                elif d == 27:
                    district = 'Siddipet'
                    break
                elif d == 28:
                    district = 'Suryapet'
                    break
                elif d == 29:
                    district = 'Vikarabad'
                    break
                elif d == 30:
                    district = 'Wanaparthy'
                    break
                elif d == 31:
                    district = 'Warangal'
                    break
                elif d == 32:
                    district = 'Hanamkonda'
                    break
                elif d == 33:
                    district = 'Yadadri Bhuvanagiri'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Tripura":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Tripura:                   |
                                                |                       1. Dhalai                             |
                                                |                       2. Gomati                             |
                                                |                       3. Khowai                             |
                                                |                       4. North Tripura                      | 
                                                |                       5. Sepahijala                         |
                                                |                       6. South Tripura                      |
                                                |                       7. Unakoti                            |
                                                |                       8. West Tripura                       | 
                                                ---------------------------------------------------------------

                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Dhalai'
                    break
                elif d == 2:
                    district = 'Gomati'
                    break
                elif d == 3:
                    district = 'Khowai'
                    break
                elif d == 4:
                    district = 'North Tripura'
                    break
                elif d == 5:
                    district = 'Sepahijala'
                    break
                elif d == 6:
                    district = 'South Tripura'
                    break
                elif d == 7:
                    district = 'Unakoti'
                    break
                elif d == 8:
                    district = 'West Tripura'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Uttar Pradesh":
            print("""
                                            ---------------------------------------------------------------
                                            |          List of all District in Uttar Pradesh:             |
                                            |                       1. Agra                               |
                                            |                       2. Aligarh                            |
                                            |                       3. Prayagraj                          |
                                            |                       4. Ambedkar Nagar                     | 
                                            |                       5. Amethi                             |
                                            |                       6. Amroha                             |
                                            |                       7. Auraiya                            |
                                            |                       8. Azamgarh                           | 
                                            |                       9. Baghpat                            | 
                                            |                      10. Bahraich                           |
                                            |                      11. Ballia                             | 
                                            |                      12. Balrampur                          |
                                            |                      13. Banda                              |
                                            |                      14. Barabanki                          |
                                            |                      15. Bareilly                           |
                                            |                      16. Basti                              |
                                            |                      17. Bhadohi                            |
                                            |                      18. Bijnor                             | 
                                            |                      19. Budaun                             |
                                            |                      20. Bulandshahr                        | 
                                            |                      21. Chandauli                          |
                                            |                      22. Chitrakoot                         |
                                            |                      23. Deoria                             |
                                            |                      24. Etah                               |
                                            |                      25. Etawah                             |
                                            |                      26. Ayodhya                            |
                                            |                      27. Farrukhabad                        |
                                            |                      28. Fatehpur                           |
                                            |                      29. Firozabad                          |
                                            |                      30. Gautam Buddha Nagar                |
                                            |                      31. Ghaziabad                          |
                                            |                      32. Ghazipur                           |
                                            |                      33. Gonda                              |
                                            |                      34. Gorakhpur                          |
                                            |                      35. Hamirpur                           |
                                            |                      36. Hapur                              |
                                            |                      37. Hardoi                             | 
                                            |                      38. Hathras                            | 
                                            |                      39. Jalaun                             |
                                            |                      40. Jaunpur                            |  
                                            |                      41. Jhansi                             |
                                            |                      42. Kannauj                            |
                                            |                      43. Kanpur Dehat                       |
                                            |                      44. Kanpur Nagar                       |
                                            |                      45. Kasganj                            |
                                            |                      46. Kaushambi                          |
                                            |                      47. Kheri                              |
                                            |                      48. Kushinagar                         |
                                            |                      49. Lalitpur                           |
                                            |                      50. Lucknow                            |
                                            |                      51. Maharajganj                        |
                                            |                      52. Mahoba                             |
                                            |                      53. Mainpuri                           |
                                            |                      54. Mathura                            |
                                            |                      55. Mau                                |
                                            |                      56. Meerut                             |
                                            |                      57. Mirzapur                           |
                                            |                      58. Moradabad                          |
                                            |                      59. Muzaffarnagar                      |
                                            |                      60. Pilibhit                           |
                                            |                      61. Pratapgarh                         |
                                            |                      62. Raebareli                          |
                                            |                      63. Rampur                             |
                                            |                      64. Saharanpur                         |
                                            |                      65. Sambhal                            |
                                            |                      66. Sant Kabir Nagar                   |
                                            |                      67. Shahjahanpur                       |
                                            |                      68. Shamli                             |
                                            |                      69. Shravasti                          |
                                            |                      70. Siddharthnagar                     |
                                            |                      71. Sitapur                            |
                                            |                      72. Sonbhadra                          |
                                            |                      73. Sultanpur                          |
                                            |                      74. Unnao                              |
                                            |                      75. Varanasi                           |
                                            ---------------------------------------------------------------

                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Agra'
                    break
                elif d == 2:
                    district = 'Aligarh'
                    break
                elif d == 3:
                    district = 'Prayagraj'
                    break
                elif d == 4:
                    district = 'Ambedkar Nagar'
                    break
                elif d == 5:
                    district = 'Amethi '
                    break
                elif d == 6:
                    district = 'Amroha '
                    break
                elif d == 7:
                    district = 'Auraiya'
                    break
                elif d == 8:
                    district = 'Azamgarh'
                    break
                elif d == 9:
                    district = 'Baghpat'
                    break
                elif d == 10:
                    district = 'Bahraich'
                    break
                elif d == 11:
                    district = 'Ballia'
                    break
                elif d == 12:
                    district = 'Balrampur'
                    break
                elif d == 13:
                    district = 'Banda'
                    break
                elif d == 14:
                    district = 'Barabanki'
                    break
                elif d == 15:
                    district = 'Bareilly'
                    break
                elif d == 16:
                    district = 'Basti'
                    break
                elif d == 17:
                    district = 'Bhadohi'
                    break
                elif d == 18:
                    district = 'Bijnor'
                    break
                elif d == 19:
                    district = 'Budaun'
                    break
                elif d == 20:
                    district = 'Bulandshahr'
                    break
                elif d == 21:
                    district = 'Chandauli'
                    break
                elif d == 22:
                    district = 'Chitrakoot'
                    break
                elif d == 23:
                    district = 'Deoria'
                    break
                elif d == 24:
                    district = 'Etah'
                    break
                elif d == 25:
                    district = 'Etawah'
                    break
                elif d == 26:
                    district = 'Ayodhya '
                    break
                elif d == 27:
                    district = 'Farrukhabad'
                    break
                elif d == 28:
                    district = 'Fatehpur'
                    break
                elif d == 29:
                    district = 'Firozabad'
                    break
                elif d == 30:
                    district = 'Gautam Buddha Nagar'
                    break
                elif d == 31:
                    district = 'Ghaziabad'
                    break
                elif d == 32:
                    district = 'Ghazipur'
                    break
                elif d == 33:
                    district = 'Gonda'
                    break
                elif d == 34:
                    district = 'Gorakhpur'
                    break
                elif d == 35:
                    district = 'Hamirpur'
                    break
                elif d == 36:
                    district = 'Hapur '
                    break
                elif d == 37:
                    district = 'Hardoi'
                    break
                elif d == 38:
                    district = 'Hathras '
                    break
                elif d == 38:
                    district = 'Jalaun'
                    break
                elif d == 39:
                    district = 'Jaunpur'
                    break
                elif d == 40:
                    district = 'Jhansi'
                    break
                elif d == 41:
                    district = 'Kannauj'
                    break
                elif d == 42:
                    district = 'Kanpur Dehat'
                    break
                elif d == 43:
                    district = 'Kanpur Nagar'
                    break
                elif d == 44:
                    district = 'Kasganj '
                    break
                elif d == 45:
                    district = 'Kaushambi'
                    break
                elif d == 46:
                    district = 'Kheri'
                    break
                elif d == 47:
                    district = 'Kushinagar'
                    break
                elif d == 48:
                    district = 'Lalitpur'
                    break
                elif d == 49:
                    district = 'Lucknow'
                    break
                elif d == 50:
                    district = 'Maharajganj'
                    break
                elif d == 51:
                    district = 'Mahoba'
                    break
                elif d == 52:
                    district = 'Mainpuri'
                    break
                elif d == 53:
                    district = 'Mathura'
                    break
                elif d == 54:
                    district = 'Mau'
                    break
                elif d == 55:
                    district = 'Meerut'
                    break
                elif d == 56:
                    district = 'Mirzapur'
                    break
                elif d == 57:
                    district = 'Moradabad'
                    break
                elif d == 58:
                    district = 'Muzaffarnagar'
                    break
                elif d == 59:
                    district = 'Pilibhit'
                    break
                elif d == 60:
                    district = 'Pratapgarh'
                    break
                elif d == 61:
                    district = 'Raebareli'
                    break
                elif d == 62:
                    district = 'Rampur'
                    break
                elif d == 63:
                    district = 'Saharanpur'
                    break
                elif d == 64:
                    district = 'Sambhal '
                    break
                elif d == 65:
                    district = 'Sant Kabir Nagar'
                    break
                elif d == 66:
                    district = 'Shahjahanpur'
                    break
                elif d == 67:
                    district = 'Shamli '
                    break
                elif d == 68:
                    district = 'Shravasti'
                    break
                elif d == 69:
                    district = 'Siddharthnagar'
                    break
                elif d == 70:
                    district = 'Sitapur'
                    break
                elif d == 71:
                    district = 'Sonbhadra'
                    break
                elif d == 72:
                    district = 'Sultanpur'
                    break
                elif d == 73:
                    district = 'Sultanpur'
                    break
                elif d == 74:
                    district = 'Unnao'
                    break
                elif d == 75:
                    district = 'Varanasi'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Uttarakhand":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Uttarakhand :              |
                                                |                       1. Almora                             |
                                                |                       2. Bageshwar                          |
                                                |                       3. Chamoli                            |
                                                |                       4. Champawat                          | 
                                                |                       5. Dehradun                           |
                                                |                       6. Haridwar                           |
                                                |                       7. Nainital                           |
                                                |                       8. Pauri                              | 
                                                |                       9. Pithoragarh                        | 
                                                |                      10. Rudraprayag                        |
                                                |                      11. Tehri                              | 
                                                |                      12. Udham Singh Nagar                  |
                                                |                      13. Uttarkashi                         |
                                                ---------------------------------------------------------------
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Almora'
                    break
                elif d == 2:
                    district = 'Bageshwar'
                    break
                elif d == 3:
                    district = 'Chamoli'
                    break
                elif d == 4:
                    district = 'Champawat'
                    break
                elif d == 5:
                    district = 'Dehradun'
                    break
                elif d == 6:
                    district = 'Haridwar'
                    break
                elif d == 7:
                    district = 'Nainital'
                    break
                elif d == 8:
                    district = 'Pauri'
                    break
                elif d == 9:
                    district = 'Pithoragarh'
                    break
                elif d == 10:
                    district = 'Rudraprayag'
                    break
                elif d == 11:
                    district = 'Tehri'
                    break
                elif d == 12:
                    district = 'Udham Singh Nagar'
                    break
                elif d == 13:
                    district = 'Uttarkashi'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "West Bengal":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in West Bengal :              |
                                                |                       1. Alipurduar                         |
                                                |                       2. Bankura                            |
                                                |                       3. Birbhum                            |
                                                |                       4. Cooch Behar                        | 
                                                |                       5. Dakshin Dinajpur                   |
                                                |                       6. Darjeeling                         |
                                                |                       7. Hooghly                            |
                                                |                       8. Howrah                             | 
                                                |                       9. Jalpaiguri                         | 
                                                |                      10. Jhargram                           |
                                                |                      11. Kalimpong                          | 
                                                |                      12. Kolkata                            |
                                                |                      13. Malda                              |
                                                |                      14. Murshidabad                        |
                                                |                      15. Nadia                              |
                                                |                      16. North 24 Parganas                  |
                                                |                      17. Paschim Bardhaman                  |
                                                |                      18. Paschim Medinipur                  | 
                                                |                      19. Purba Bardhaman                    |
                                                |                      20. Purba Medinipur                    |  
                                                |                      21. Purulia                            |
                                                |                      22. South 24 Parganas                  |
                                                |                      23. Uttar Dinajpur                     |
                                                ---------------------------------------------------------------
                        """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Alipurduar'
                    break
                elif d == 2:
                    district = 'Bankura'
                    break
                elif d == 3:
                    district = 'Birbhum'
                    break
                elif d == 4:
                    district = 'Cooch Behar'
                    break
                elif d == 5:
                    district = 'Dakshin Dinajpur'
                    break
                elif d == 6:
                    district = 'Darjeeling'
                    break
                elif d == 7:
                    district = 'Hooghly'
                    break
                elif d == 8:
                    district = 'Howrah'
                    break
                elif d == 9:
                    district = 'Jalpaiguri'
                    break
                elif d == 10:
                    district = 'Jhargram'
                    break
                elif d == 11:
                    district = 'Kalimpong'
                    break
                elif d == 12:
                    district = 'Kolkata'
                    break
                elif d == 13:
                    district = 'Malda'
                    break
                elif d == 14:
                    district = 'Murshidabad'
                    break
                elif d == 15:
                    district = 'Nadia'
                    break
                elif d == 16:
                    district = 'North 24 Parganas'
                    break
                elif d == 17:
                    district = 'Paschim Bardhaman'
                    break
                elif d == 18:
                    district = 'Paschim Medinipur'
                    break
                elif d == 19:
                    district = 'Purba Bardhaman'
                    break
                elif d == 20:
                    district = 'Purba Medinipur'
                    break
                elif d == 21:
                    district = 'Purulia'
                    break
                elif d == 22:
                    district = 'South 24 Parganas'
                    break
                elif d == 23:
                    district = 'Uttar Dinajpur'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Andaman & Nicobar":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Andaman & Nicobar :        |
                                                |                       1. Nicobar                            |
                                                |                       2. North Middle Andaman               |
                                                |                       3. South Andaman                      |
                                                ---------------------------------------------------------------
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Nicobar'
                    break
                elif d == 2:
                    district = 'North Middle Andaman'
                    break
                elif d == 3:
                    district = 'South Andaman'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Chandigarh":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Chandigarh :               |
                                                |                       1. Chandigarh                         |
                                                ---------------------------------------------------------------
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Chandigarh'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Dadra and Nagar Haveli and Daman and Diu":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Dadra and Nagar Haveli     |
                                                |          and Daman and Diu :                                |
                                                |                       1. Dadra and Nagar Haveli             |
                                                |                       2. Daman                              |
                                                |                       3. Diu                                |
                                                ---------------------------------------------------------------
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Dadra and Nagar Haveli'
                    break
                elif d == 2:
                    district = 'Daman'
                    break
                elif d == 3:
                    district = 'Diu'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Delhi":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Delhi :                    |
                                                |                       1. Central Delhi                      |
                                                |                       2. East Delhi                         |
                                                |                       3. New Delhi                          |
                                                |                       4. North Delhi                        | 
                                                |                       5. North East Delhi                   |
                                                |                       6. North West Delhi                   |
                                                |                       7. Shahdara                           |
                                                |                       8. South Delhi                        | 
                                                |                       9. South East Delhi                   | 
                                                |                      10. South West Delhi                   |
                                                |                      11. West Delhi                         | 
                                                ---------------------------------------------------------------
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Central Delhi'
                    break
                elif d == 2:
                    district = 'East Delhi'
                    break
                elif d == 3:
                    district = 'New Delhi'
                    break
                elif d == 4:
                    district = 'North Delhi'
                    break
                elif d == 5:
                    district = 'North East Delhi'
                    break
                elif d == 6:
                    district = 'North West Delhi'
                    break
                elif d == 7:
                    district = 'Shahdara'
                    break
                elif d == 8:
                    district = 'South Delhi'
                    break
                elif d == 9:
                    district = 'South East Delhi'
                    break
                elif d == 10:
                    district = 'South West Delhi'
                    break
                elif d == 11:
                    district = 'West Delhi'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Lakshadweep":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Lakshadweep :              |
                                                |                       1. Lakshadweep                        |
                                                ---------------------------------------------------------------
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Lakshadweep'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Ladakh":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Ladakh :                   |
                                                |                       1. Kargil                             |
                                                |                       2. Leh                                |
                                                ---------------------------------------------------------------
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Kargil'
                    break
                elif d == 2:
                    district = 'Leh'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        if st_ut == "Puducherry":
            print("""
                                                ---------------------------------------------------------------
                                                |          List of all District in Puducherry :               |
                                                |                       1. Karaikal                           |
                                                |                       2. Mahe                               |
                                                |                       3. Puducherry                         |
                                                |                       4. Yanam                              |
                                                ---------------------------------------------------------------
                    """)
            while True:
                d = int(input("\nEnter the district no. :"))
                if d == 1:
                    district = 'Karaikal'
                    break
                elif d == 2:
                    district = 'Mahe'
                    break
                elif d == 3:
                    district = 'Puducherry'
                    break
                elif d == 4:
                    district = 'Yanam'
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        r1 = ['Jammu & Kashmir', 'Ladakh', 'Himachal Pradesh', 'Punjab', 'Uttarakhand']
        r2 = ['Sikkim', 'Nagaland', 'Arunachal Pradesh', 'Manipur', 'Tripura', 'Mizoram', 'Meghalaya', 'Assam']
        r3 = ['Haryana', 'Chandigarh', 'Delhi', 'Rajasthan', 'Uttar Pradesh']
        r4 = ['Bihar', 'West Bengal', 'Jharkhand', 'Odisha']
        r5 = ['Madhya Pradesh', 'Chattisgrarh', 'Gujarat', 'Maharashtra', 'Dadra and Nagar Haveli and Daman and Diu']
        r6 = ['Andhra Pradesh', 'Telangana', 'Karnataka', 'Tamil Nadu', 'Kerala', 'Goa', 'Puducherry',
              'Andaman & Nicobar', 'Lakshadweep']

        region = None
        if st_ut in r1:
            region = "Western Himalayas Region"

        elif st_ut in r2:
            region = "Eastern Himalayas Region"

        elif st_ut in r3:
            region = "Western Plains Region"

        elif st_ut in r4:
            region = "Eastern Plains Region"

        elif st_ut in r5:
            region = "Central Region"

        elif st_ut in r6:
            region = "Southern Region"

        while True:
            tensil = input("\nEnter your Tensil Name :")
            if tensil.isalpha() is True:
                break
            else:
                print(
                    "\n" + " " * 30 + "---------------------------------------INVALID TENSIL NAME--------------------------------------")

        while True:
            block_locality = input("\nEnter your Block/Locality Name :")
            if block_locality == '' or block_locality == ' ':
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID BLOCK/LOCALITY NAME----------------------------------")
            else:
                break

        while True:
            pin_no = input("\nEnter the Pin No :")
            if pin_no.isnumeric() is True:
                break
            else:
                print(
                    "\n" + " " * 30 + "--------------------------------------INALID PIN NO.--------------------------------------------")

        while True:
            police_sta = input("\nEnter the Police Station :")
            if police_sta == ' ' or police_sta == '':
                print(
                    "\n" + " " * 30 + "---------------------------------INVALID POLICE STATION-----------------------------------------")
            else:
                break

        while True:
            post_office = input("\nEnter your Post Office :")
            if post_office == ' ' or post_office == '':
                print(
                    "\n" + " " * 30 + "---------------------------------- INVALID POST OFFICE------------------------------------------")
            else:
                break

        while True:
            tele_office = input("\nEnter your Telegram Office :")
            if tele_office == ' ' or tele_office == '':
                print(
                    "\n" + " " * 30 + "-------------------------------- INVALID TELEGRAM OFFICE----------------------------------------")
            else:
                break

        print("\nPress ENTER to continue the registration process...............................")
        print()
        k = input()

        time.sleep(2)

        print()
        print("DETAILS :")
        print()

        while True:
            print(" " * 47 + "-" * 62)
            print(" " * 47 + "|      Choice for the matrial status:                        |")
            print(" " * 47 + "|" + " " * 20 + "1. General Rally" + " " * 24 + "|")
            print(" " * 47 + "|" + " " * 20 + "2. Unit Head Quator (UHQ)" + " " * 15 + "|")
            print(" " * 47 + "-" * 62)
            print()
            cat = int(input("\nEnter your Choise :"))
            if cat == 1:
                category = "General Rally"
                break
            elif cat == 2:
                category = "Unit Head Quator (UHQ)"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        while True:
            s = input("\nAre you a sports man? (Y/N)\n")
            if s in 'Yy':
                sports = input("\nSpecify the sports :")
                break
            elif s in 'nN':
                sports = "NO"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        while True:
            nc = input("\nAre you in NCC? (Y/N)\n")
            if nc in 'Yy':
                ncc = "YES"
                break
            elif nc in 'nN':
                ncc = "NO"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        print("""
                                               ---------------------------------------------------------------------------
                                               |   Sl.no    |                    Special category                        |
                                               |------------|------------------------------------------------------------|
                                               |     1.     | Non Dispensation Category                                  |
                                               |------------|------------------------------------------------------------|
                                               |     2.     | Ladakhi                                                    |
                                               |------------|------------------------------------------------------------|
                                               |     3.     | Gorkha Nepalese and Indian Origin                          |
                                               |------------|------------------------------------------------------------|
                                               |     4.     | Settlers ( Andaman and Nicobar, Lakshadweep including      |
                                               |            | Minicoy )                                                  |
                                               |------------|------------------------------------------------------------|
                                               |     5.     | Locals of Andaman and Nicobar, Lakshadweep including       |
                                               |            | Minicoy                                                    |
                                               |------------|------------------------------------------------------------|
                                               |     6.     | Tribals of Recognized Tribal Areas                         |
                                               |------------|------------------------------------------------------------|
                                               |     7.     | Son of Army Personal                                       |
                                               |------------|------------------------------------------------------------|
                                               |     8.     | Arunachal and Sikkim Scouts only                           |
                                               ---------------------------------------------------------------------------

        """)
        while True:
            print("Do you belong to any of the mentioned Special Category?\n"
                  "Select any one from above.\n"
                  "If NO press n.\n"
                  "Choose your Option :")
            cho = input().strip()
            if cho == 'n' or cho == 'N':
                spe_category = "NO"
            if cho == '1':
                spe_category = "Non Dispensation Category"
                break
            elif cho == '2':
                spe_category = "Ladakhi"
                break
            elif cho == '3':
                spe_category = "Gorkha Nepalese and Indian Origin"
                break
            elif cho == '4':
                spe_category = "Settlers ( Andaman and Nicobar, Lakshadweep including Minicoy )"
                break
            elif cho == '5':
                spe_category = "Locals of Andaman and Nicobar, Lakshadweep including Minicoy"
                break
            elif cho == '6':
                spe_category = "Tribals of Recognized Tribal Areas"
                break
            elif cho == '7':
                spe_category = "Son of Army Personal"
                break
            elif cho == '8':
                spe_category = "Arunachal and Sikkim Scouts only"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        print("\nPress ENTER to continue the registration process...............................")
        print()
        j = input()

        time.sleep(2)

        print()
        print("EDUCATION DETAILS :")
        print()

        print("""
                                            ------------------------------------------------------------------
                                            |      Choose for Highest Qualification:                         |
                                            |                         1. 8th Pass                            |
                                            |                         2. 10th Pass                           |
                                            |                         3. 12th Pass                           |
                                            |                         4. Graduation                          |
                                            |                         5. Post Graduation                     |
                                            ------------------------------------------------------------------
        """)

        while True:
            h_q = int(input("\nEnter your choice :"))
            if h_q == 1:
                highest_qualification = "8th Pass"
                break
            elif h_q == 2:
                highest_qualification = "10th Pass"
                break
            elif h_q == 3:
                highest_qualification = "12th Pass"
                break
            elif h_q == 4:
                highest_qualification = "Graduation"
                break
            elif h_q == 5:
                highest_qualification = "Post Graduation"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        while True:
            qualification_course = input("\nEnter the qualifying course :")
            if qualification_course == '' or qualification_course == ' ':
                print(
                    "\n" + " " * 30 + "-------------------------------INVALID QUALIFICATION COURSE-------------------------------------")
            else:
                break

        print("""
                                       ------------------------------------------------------------------
                                       |           Choose for Board/Education University :              |
                                       |                      1. Central University                     |
                                       |                      2. State University                       |
                                       |                      3. Deemed University                      |
                                       |                      4. Private University                     |
                                       |                      5. CBSE                                   |
                                       |                      6. ICSE                                   |
                                       |                      7. Open School                            |
                                       |                      8. State Board                            |
                                       |                      9. Others                                 |
                                       ------------------------------------------------------------------
        """)

        while True:
            uni = int(input("\nEnter your Board/Education University :"))
            if uni in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        if uni == 1:
            university = "Central University"
        if uni == 2:
            university = "State University"
        if uni == 3:
            university = "Deemed University"
        if uni == 4:
            university = "Private University"
        if uni == 5:
            university = "CBSE"
        if uni == 6:
            university = "ICSE"
        if uni == 7:
            university = "Open School"
        if uni == 8:
            university = "State Board"
        if uni == 9:
            university = "Others"

        if uni in (1, 2, 3, 4, 9):
            while True:
                uni_boa_name = input("\nEnter the name of the university :").upper()
                if uni_boa_name == '' or uni_boa_name == ' ':
                    print(
                        "\n" + " " * 30 + "------------------------------INVALID UNIVERSITY/BOARD NAME-------------------------------------")
                else:
                    break

        if uni == 5:
            uni_boa_name = "CENTRAL BOARD OF SECONDARY EDUCATION"

        if uni == 6:
            uni_boa_name = "INDIAN CERTIFICATE OF SECONDARY EDUCATION"

        if uni in (7, 8, 9):
            print(" " * 15 + "-" * 126)
            print(
                " " * 15 + "|              Choice for Board :                                                                                            |")
            print(" " * 15 + "|" + " " * 20 + " 1. NORTHWEST ACCREDITATION COMMISSION(NWAC), USA" + " " * 55 + "|")
            print(" " * 15 + "|" + " " * 20 + " 2. NATIONAL INSTITUTE OF OPEN SCHOOLING, NEW DELHI" + " " * 53 + "|")
            print(
                " " * 15 + "|" + " " * 20 + " 3. COUNCIL FOR THE INDIAN SCHOOL CERTIFICATE EXAMINATIONS, NEW DELHI" + " " * 35 + "|")
            print(" " * 15 + "|" + " " * 20 + " 4. BOARD OF INTERMEDIATE EDUCATION, ANDHRA PRADESH" + " " * 53 + "|")
            print(" " * 15 + "|" + " " * 20 + " 5. BOARD OF SECONDARY EDUCATION, ANDHRA PRADESH" + " " * 56 + "|")
            print(" " * 15 + "|" + " " * 20 + " 6. A.P. OPEN SCHOOL SOCIETY, ANDHRA PRADESH" + " " * 60 + "|")
            print(" " * 15 + "|" + " " * 20 + " 7. ASSAM HIGHER SECONDARY EDUCATION COUNCIL, ASSAM" + " " * 53 + "|")
            print(" " * 15 + "|" + " " * 20 + " 8. BOARD OF SECONDARY EDUCATION, ASSAM" + " " * 65 + "|")
            print(" " * 15 + "|" + " " * 20 + " 9. BIHAR SCHOOL EXAMINATION BOARD, BIHAR" + " " * 63 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "10. BIHAR BOARD OF OPEN SCHOOLING AND EXAMINATION(BBOSE), BIHAR" + " " * 41 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "11. CHHATISGARH BOARD OF SECONDARY EDUCATION, CHHATISGARH" + " " * 47 + "|")
            print(" " * 15 + "|" + " " * 20 + "12. CHHATISGARH STATE OPEN SCHOOL, CHHATISGARH" + " " * 58 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "13. GOA BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, GOA" + " " * 42 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "14. GUJARAT SECONDARY AND HIGHER SECONDARY EDUCATION BOARD, GUJARAT" + " " * 37 + "|")
            print(" " * 15 + "|" + " " * 20 + "15. BOARD OF SCHOOL EDUCATION, HARYANA" + " " * 66 + "|")
            print(" " * 15 + "|" + " " * 20 + "16. H.P.BOARD OF SCHOOL EDUCATION, HIMACHAL PRADESH" + " " * 53 + "|")
            print(" " * 15 + "|" + " " * 20 + "17. THE J & K STATE BOARD OF SCHOOL EDUCATION, JAMMU" + " " * 52 + "|")
            print(" " * 15 + "|" + " " * 20 + "18. JHARKHAND ACADEMIC COUNCIL, RANCHI" + " " * 66 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "19. GOVT.OF KARNATAKA DEPT.OF PRE - UNIVERSITY EDUCATION, KARNATAKA" + " " * 37 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "20. KARNATAKA SECONDARY EDUCATION, EXAMINATION BOARD, KARNATAKA" + " " * 41 + "|")
            print(" " * 15 + "|" + " " * 20 + "21. KERALA BOARD OF PUBLIC EXAMINATION, KERALA" + " " * 58 + "|")
            print(" " * 15 + "|" + " " * 20 + "22. KERALA BOARD OF HIGHER SECONDARY EDUCATION, KERALA" + " " * 50 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "23. BOARD OF VOCATIONAL HIGHER SECONDARY EDUCATION, KERALA" + " " * 46 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "24. MAHARASHTRA STATE BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, MAHARASHTRA" + " " * 20 + "|")
            print(" " * 15 + "|" + " " * 20 + "25. BOARD OF SECONDARY EDUCATION, MADHYA PRADESH" + " " * 56 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "26. M.P.STATE OPEN SCHOOL EDUCATION BOARD, MADHYA PRADESH" + " " * 47 + "|")
            print(" " * 15 + "|" + " " * 20 + "27. BOARD OF SECONDARY EDUCATION, MANIPUR" + " " * 63 + "|")
            print(" " * 15 + "|" + " " * 20 + "28. COUNCIL OF HIGHER SECONDARY EDUCATION, MANIPUR" + " " * 54 + "|")
            print(" " * 15 + "|" + " " * 20 + "29. MEGHALAYA BOARD OF SCHOOL EDUCATION, MEGHALAYA" + " " * 54 + "|")
            print(" " * 15 + "|" + " " * 20 + "30. MIZORAM BOARD OF SCHOOL EDUCATION, MIZORAM" + " " * 58 + "|")
            print(" " * 15 + "|" + " " * 20 + "31. NAGALAND BOARD OF SCHOOL EDUCATION, NAGALAND" + " " * 56 + "|")
            print(" " * 15 + "|" + " " * 20 + "32. BOARD OF SECONDARY EDUCATION, ODISHA" + " " * 64 + "|")
            print(" " * 15 + "|" + " " * 20 + "33. COUNCIL OF HIGHER SECONDARY EDUCATION, ODISHA" + " " * 55 + "|")
            print(" " * 15 + "|" + " " * 20 + "34. PUNJAB SCHOOL EDUCATION BOARD, PUNJAB" + " " * 63 + "|")
            print(" " * 15 + "|" + " " * 20 + "35. BOARD OF SECONDARY EDUCATION, RAJASTHAN" + " " * 61 + "|")
            print(" " * 15 + "|" + " " * 20 + "36. RAJASTHAN STATE OPEN SCHOOL, RAJASTHAN" + " " * 62 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "37. STATE BOARD OF SCHOOL EXAMINATIONS(SEC.) & BOARD OF HIGHER SECONDARY, TAMIL NADU" + " " * 20 + "|")
            print(" " * 15 + "|" + " " * 20 + "38. BOARD OF SECONDARY EDUCATION, TELANGANA STATE" + " " * 55 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "39. TELANGANA STATE BOARD OF INTERMEDIATE EDUCATION, TELANGANA" + " " * 42 + "|")
            print(" " * 15 + "|" + " " * 20 + "40. TELANGANA OPEN SCHOOL SOCIETY, TELANGANA" + " " * 60 + "|")
            print(" " * 15 + "|" + " " * 20 + "41. TRIPURA BOARD OF SECONDARY EDUCATION, TRIPURA" + " " * 55 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "42. U.P.BOARD OF HIGH SCHOOL & INTERMEDIATE EDUCATION, UTTAR PRADESH" + " " * 36 + "|")
            print(" " * 15 + "|" + " " * 20 + "43. BOARD OF SCHOOL EDUCATION, UTTARAKHAND" + " " * 62 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "44. WEST BENGAL BOARD OF SECONDARY EDUCATION, WEST BENGAL" + " " * 47 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "45. WEST BENGAL COUNCIL OF HIGHER SECONDARY EDUCATION, WEST BENGAL" + " " * 38 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "46. THE WEST BENGAL COUNCIL OF RABINDRA OPEN SCHOOLING, WEST BENGAL" + " " * 37 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "47. WEST BENGAL STATE COUNCIL OF TECHNICAL & VOCATIONAL EDUCATION & SKILL DEVELOPMENT, WEST BENGAL" + " " * 6 + "|")
            print(" " * 15 + "|" + " " * 20 + "48. MAHARISHI PATANJALI SANSKRIT SANSTHAN, NEW DELHI" + " " * 52 + "|")
            print(" " * 15 + "|" + " " * 20 + "49. URDU EDUCATION  BOARD, NEW DELHI" + " " * 68 + "|")
            print(" " * 15 + "|" + " " * 20 + "50. BIHAR SANSKRIT SHIKSHA BOARD, BIHAR" + " " * 65 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "51. U.P.BOARD OF SEC.SANSKRIT EDUCATION SANSKRIT BHAWAN, UTTAR PRADESH" + " " * 34 + "|")
            print(" " * 15 + "|" + " " * 20 + "52. ASSAM SANSKRIT BOARD, ASSAM" + " " * 73 + "|")
            print(" " * 15 + "|" + " " * 20 + "53. JAMIA MILIA ISLAMIA, NEW DELHI" + " " * 70 + "|")
            print(" " * 15 + "|" + " " * 20 + "54. UTTRAKHAND SANSKRIT SHIKSHA PARISHAD, UTTRAKHAND" + " " * 52 + "|")
            print(" " * 15 + "|" + " " * 20 + "55. STATE MADRASSA EDUCATION BOARD, ASSAM" + " " * 63 + "|")
            print(" " * 15 + "|" + " " * 20 + "56. BIHAR STATE MADRASA EDUCATION BOARD, BIHAR" + " " * 58 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "57. WEST BENGAL BOARD OF MADRASAH EDUCATION, WEST BENGAL" + " " * 48 + "|")
            print(" " * 15 + "|" + " " * 20 + "58. CHHATTISGARH MADRASA BOARD, CHHATTISGARH" + " " * 60 + "|")
            print(" " * 15 + "|" + " " * 20 + "59. UTTARAKHAND MADRASA EDUCATION BOARD, UTTARAKHAND" + " " * 52 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "60. ALIGARH MUSLIM UNIVERSITY BOARD OF SECONDARY & SR.SECONDARY EDUCATION, UTTAR PARDESH" + " " * 16 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "61. INDIAN COUNCIL FOR HINDI & SANSKRIT EDUCATION, NEW DELHI" + " " * 44 + "|")
            print(" " * 15 + "|" + " " * 20 + "62. DAYALBAGH EDUCATIONAL INSTITUTE, AGRA" + " " * 63 + "|")
            print(" " * 15 + "|" + " " * 20 + "63. BANASTHALI VIDYAPITH P.O., RAJASTHAN" + " " * 64 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "64. BHUTAN COUNCIL FOR SCHOOL EXAMINATIONS & ASSESSMENT, BHUTAN" + " " * 41 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "65. CAMBRIDGE ASSESSMENT INTERNATIONAL EXAMINATIONS, UK" + " " * 49 + "|")
            print(" " * 15 + "|" + " " * 20 + "66. CHHATTISGARH SANSKRIT BOARD, RAIPUR" + " " * 65 + "|")
            print(" " * 15 + "|" + " " * 20 + "67. MAURITIUS EXAMINATION SYNDICATE, MAURITIUS" + " " * 58 + "|")
            print(" " * 15 + "|" + " " * 20 + "68. NATIONAL EXAMINATIONS BOARD, NEPAL" + " " * 66 + "|")
            print(" " * 15 + "|" + " " * 20 + "69. PEARSON EDEXCEL LTD., UK" + " " * 76 + "|")
            print(" " * 15 + "|" + " " * 20 + "70. INTERNATIONAL BACCALAUREATE, GENEVA" + " " * 65 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "71. SINGHANIA UNIVERSITY BOARD OF SECONDARY & SENIOR SECONDARY EDUCATION, RAJASTHAN" + " " * 21 + "|")
            print(" " * 15 + "-" * 126)

            while True:
                c1 = int(input("\nChoose the board :"))
                if c1 == 1:
                    uni_boa_name = "NORTHWEST ACCREDITATION COMMISSION(NWAC), USA"
                    break
                elif c1 == 2:
                    uni_boa_name = "NATIONAL INSTITUTE OF OPEN SCHOOLING, NEW DELHI"
                    break
                elif c1 == 3:
                    uni_boa_name = "COUNCIL FOR THE INDIAN SCHOOL CERTIFICATE EXAMINATIONS, NEW DELHI"
                    break
                elif c1 == 4:
                    uni_boa_name = "BOARD OF INTERMEDIATE EDUCATION, ANDHRA PRADESH"
                    break
                elif c1 == 5:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, ANDHRA PRADESH"
                    break
                elif c1 == 6:
                    uni_boa_name = "A.P. OPEN SCHOOL SOCIETY, ANDHRA PRADESH"
                    break
                elif c1 == 7:
                    uni_boa_name = "ASSAM HIGHER SECONDARY EDUCATION COUNCIL, ASSAM"
                    break
                elif c1 == 8:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, ASSAM"
                    break
                elif c1 == 9:
                    uni_boa_name = "BIHAR SCHOOL EXAMINATION BOARD, BIHAR"
                    break
                elif c1 == 10:
                    uni_boa_name = "BIHAR BOARD OF OPEN SCHOOLING AND EXAMINATION(BBOSE), BIHAR"
                    break
                elif c1 == 11:
                    uni_boa_name = "CHHATISGARH BOARD OF SECONDARY EDUCATION, CHHATISGARH"
                    break
                elif c1 == 12:
                    uni_boa_name = "CHHATISGARH STATE OPEN SCHOOL, CHHATISGARH"
                    break
                elif c1 == 13:
                    uni_boa_name = "GOA BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, GOA"
                    break
                elif c1 == 14:
                    uni_boa_name = "GUJARAT SECONDARY AND HIGHER SECONDARY EDUCATION BOARD, GUJARAT"
                    break
                elif c1 == 15:
                    uni_boa_name = "BOARD OF SCHOOL EDUCATION, HARYANA"
                    break
                elif c1 == 16:
                    uni_boa_name = "H.P.BOARD OF SCHOOL EDUCATION, HIMACHAL PRADESH"
                    break
                elif c1 == 17:
                    uni_boa_name = "THE J & K STATE BOARD OF SCHOOL EDUCATION, JAMMU"
                    break
                elif c1 == 18:
                    uni_boa_name = "JHARKHAND ACADEMIC COUNCIL, RANCHI"
                    break
                elif c1 == 19:
                    uni_boa_name = "GOVT.OF KARNATAKA DEPT.OF PRE - UNIVERSITY EDUCATION, KARNATAKA"
                    break
                elif c1 == 20:
                    uni_boa_name = "KARNATAKA SECONDARY EDUCATION, EXAMINATION BOARD, KARNATAKA"
                    break
                elif c1 == 21:
                    uni_boa_name = "KERALA BOARD OF PUBLIC EXAMINATION, KERALA"
                    break
                elif c1 == 22:
                    uni_boa_name = "KERALA BOARD OF HIGHER SECONDARY EDUCATION, KERALA"
                    break
                elif c1 == 23:
                    uni_boa_name = "BOARD OF VOCATIONAL HIGHER SECONDARY EDUCATION, KERALA"
                    break
                elif c1 == 24:
                    uni_boa_name = "MAHARASHTRA STATE BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, MAHARASHTRA"
                    break
                elif c1 == 25:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, MADHYA PRADESH"
                    break
                elif c1 == 26:
                    uni_boa_name = "M.P.STATE OPEN SCHOOL EDUCATION BOARD, MADHYA PRADESH"
                    break
                elif c1 == 27:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, MANIPUR"
                    break
                elif c1 == 28:
                    uni_boa_name = "COUNCIL OF HIGHER SECONDARY EDUCATION, MANIPUR"
                    break
                elif c1 == 29:
                    uni_boa_name = "MEGHALAYA BOARD OF SCHOOL EDUCATION, MEGHALAYA"
                    break
                elif c1 == 30:
                    uni_boa_name = "MIZORAM BOARD OF SCHOOL EDUCATION, MIZORAM"
                    break
                elif c1 == 31:
                    uni_boa_name = "NAGALAND BOARD OF SCHOOL EDUCATION, NAGALAND"
                    break
                elif c1 == 32:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, ODISHA"
                    break
                elif c1 == 33:
                    uni_boa_name = "COUNCIL OF HIGHER SECONDARY EDUCATION, ODISHA"
                    break
                elif c1 == 34:
                    uni_boa_name = "PUNJAB SCHOOL EDUCATION BOARD, PUNJAB"
                    break
                elif c1 == 35:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, RAJASTHAN"
                    break
                elif c1 == 36:
                    uni_boa_name = "RAJASTHAN STATE OPEN SCHOOL, RAJASTHAN"
                    break
                elif c1 == 37:
                    uni_boa_name = "STATE BOARD OF SCHOOL EXAMINATIONS(SEC.) & BOARD OF HIGHER SECONDARY, TAMIL NADU"
                    break
                elif c1 == 38:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, TELANGANA STATE"
                    break
                elif c1 == 39:
                    uni_boa_name = "TELANGANA STATE BOARD OF INTERMEDIATE EDUCATION, TELANGANA"
                    break
                elif c1 == 40:
                    uni_boa_name = "TELANGANA OPEN SCHOOL SOCIETY, TELANGANA"
                    break
                elif c1 == 41:
                    uni_boa_name = "TRIPURA BOARD OF SECONDARY EDUCATION, TRIPURA"
                    break
                elif c1 == 42:
                    uni_boa_name = "U.P.BOARD OF HIGH SCHOOL & INTERMEDIATE EDUCATION, UTTAR PRADESH"
                    break
                elif c1 == 43:
                    uni_boa_name = "BOARD OF SCHOOL EDUCATION, UTTARAKHAND"
                    break
                elif c1 == 44:
                    uni_boa_name = "WEST BENGAL BOARD OF SECONDARY EDUCATION, WEST BENGAL"
                    break
                elif c1 == 45:
                    uni_boa_name = "WEST BENGAL COUNCIL OF HIGHER SECONDARY EDUCATION, WEST BENGAL"
                    break
                elif c1 == 46:
                    uni_boa_name = "THE WEST BENGAL COUNCIL OF RABINDRA OPEN SCHOOLING, WEST BENGAL"
                    break
                elif c1 == 47:
                    uni_boa_name = "WEST BENGAL STATE COUNCIL OF TECHNICAL & VOCATIONAL EDUCATION & SKILL DEVELOPMENT, WEST BENGAL"
                    break
                elif c1 == 48:
                    uni_boa_name = "MAHARISHI PATANJALI SANSKRIT SANSTHAN, NEW DELHI"
                    break
                elif c1 == 49:
                    uni_boa_name = "URDU EDUCATION  BOARD, NEW DELHI"
                    break
                elif c1 == 50:
                    uni_boa_name = "BIHAR SANSKRIT SHIKSHA BOARD, BIHAR"
                    break
                elif c1 == 51:
                    uni_boa_name = "U.P.BOARD OF SEC.SANSKRIT EDUCATION SANSKRIT BHAWAN, UTTAR PRADESH"
                    break
                elif c1 == 52:
                    uni_boa_name = "ASSAM SANSKRIT BOARD, ASSAM"
                    break
                elif c1 == 53:
                    uni_boa_name = "JAMIA MILIA ISLAMIA, NEW DELHI"
                    break
                elif c1 == 54:
                    uni_boa_name = "UTTRAKHAND SANSKRIT SHIKSHA PARISHAD, UTTRAKHAND"
                    break
                elif c1 == 55:
                    uni_boa_name = "STATE MADRASSA EDUCATION BOARD, ASSAM"
                    break
                elif c1 == 56:
                    uni_boa_name = "BIHAR STATE MADRASA EDUCATION BOARD, BIHAR"
                    break
                elif c1 == 57:
                    uni_boa_name = "WEST BENGAL BOARD OF MADRASAH EDUCATION, WEST BENGAL"
                    break
                elif c1 == 58:
                    uni_boa_name = "CHHATTISGARH MADRASA BOARD, CHHATTISGARH"
                    break
                elif c1 == 59:
                    uni_boa_name = "UTTARAKHAND MADRASA EDUCATION BOARD, UTTARAKHAND"
                    break
                elif c1 == 60:
                    uni_boa_name = "ALIGARH MUSLIM UNIVERSITY BOARD OF SECONDARY & SR.SECONDARY EDUCATION, UTTAR PARDESH"
                    break
                elif c1 == 61:
                    uni_boa_name = "INDIAN COUNCIL FOR HINDI & SANSKRIT EDUCATION, NEW DELHI"
                    break
                elif c1 == 62:
                    uni_boa_name = "DAYALBAGH EDUCATIONAL INSTITUTE, AGRA"
                    break
                elif c1 == 63:
                    uni_boa_name = "BANASTHALI VIDYAPITH P.O., RAJASTHAN"
                    break
                elif c1 == 64:
                    uni_boa_name = "BHUTAN COUNCIL FOR SCHOOL EXAMINATIONS & ASSESSMENT, BHUTAN"
                    break
                elif c1 == 65:
                    uni_boa_name = "CAMBRIDGE ASSESSMENT INTERNATIONAL EXAMINATIONS, UK"
                    break
                elif c1 == 66:
                    uni_boa_name = "CHHATTISGARH SANSKRIT BOARD, RAIPUR"
                    break
                elif c1 == 67:
                    uni_boa_name = "MAURITIUS EXAMINATION SYNDICATE, MAURITIUS"
                    break
                elif c1 == 68:
                    uni_boa_name = "NATIONAL EXAMINATIONS BOARD, NEPAL"
                    break
                elif c1 == 69:
                    uni_boa_name = "PEARSON EDEXCEL LTD., UK"
                    break
                elif c1 == 70:
                    uni_boa_name = "INTERNATIONAL BACCALAUREATE, GENEVA"
                    break
                elif c1 == 71:
                    uni_boa_name = "SINGHANIA UNIVERSITY BOARD OF SECONDARY & SENIOR SECONDARY EDUCATION, RAJASTHAN"
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        while True:
            mat_name = input("\nEnter the name as given in Matriculation Certificate :")
            if mat_name.isalpha() is True and mat_name != '':
                break
            else:
                print(
                    "\n" + " " * 30 + "-----------------------------------------INVALID NAME-------------------------------------------")

        while True:
            today = date.today()
            p_year = int(input("\nEnter the year of passing :"))
            if p_year <= today.year and p_year != None:
                break
            else:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID YEAR OF PASSING--------------------------------------")
        pass_year = str(p_year)

        while True:
            roll_no = input("\nEnter the Roll No. :")
            if roll_no.isnumeric() is True and roll_no != '':
                break
            else:
                print(
                    "\n" + " " * 30 + "---------------------------------------INVALID ROLL NO.-----------------------------------------")

        while True:
            cert_no = input("\nEnter the Certificate No. :")
            if cert_no == '' or cert_no == ' ':
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID CERTIFICATE NO.--------------------------------------")
            else:
                break

        print()
        print("Press ENTER to finish the registration process.........................")
        print()

        exe_query = "INSERT INTO " \
                    "new_enrollment( Aadhar_No, Candidate_Name, Father_Name, Mother_Name, Date_Of_Birth, Candidate_Age, Gender, Nationality, Martial_Status, Email_Address, Mobile_No, Higher_Education, Matriculation_Board, Username, Password, House_No, Address, Village, City_Town, State_Name_UT_Name, District, Region, Tensil, Block_Locality, Pin_No, Police_Station, Post_Office, Telegram_Office, Category, Sport, NCC, Special_Category, Highest_Education, Qualifying_Course, Board_Education_University, Name_of_the_University_Board, Name_in_Matriculation_Certificate, Year_Of_Passing, Roll_No, Certificate_No)" \
                    "VALUES( '%s', '%s', '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' )" % (
                        aadhar, c_name, f_name, m_name, dob, c_age, gender, nationality, status, c_email, c_mobile,
                        higher_qualification, m_board, c_username, password, house_no, address, village, city_town,
                        st_ut,
                        district, region, tensil, block_locality, pin_no, police_sta, post_office, tele_office,
                        category,
                        sports, ncc, spe_category, highest_qualification, qualification_course, university,
                        uni_boa_name,
                        mat_name, pass_year, roll_no, cert_no)
        cursor.execute(exe_query)
        connect.commit()

        time.sleep(2)
        print(
            "\n" + " " * 30 + "-------------------------YOUR REGISTRATION HAS BEEN DONE SUCCESSFULLY---------------------------")
        print()
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            choose = int(input("Enter your option :"))

            if choose == 1:
                print("Are you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.main(self)
                    break

            elif choose == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    def check(self):
        print("=" * 150)
        print(" " * 41 + "*** For Checking Enrollment in Agnipath Yojana Entry Scheme ***")
        print("=" * 150 + "\n")
        print("""                 
                                              IMPORTANT INSTRUCTION TO FILL ONLINE APPLICATION FORM :

                                                       1. Read all the instruction for registration carefully and then proceed further.
                                                       2. Check your Job Eligibility for joining Indian Army as JCO/OR and then Register.
                                                       3. Fill in all your personal details strictly as given in your matriculation 
                                                          Certificates. (I.e. Your Name, DOB, Father Name & Educational Qualification.)
                                                       4. Candidate must ensure that Email Id and mobile No entered at the time of 
                                                          registration process are active and unique. Sharing/Usage of Email Id /Mobile no 
                                                          of friends is strictly prohibited.
                                                       5. Ensure all the field are filled in correctly and then click on enter.
                                                       6. Registration process is mandatory for all the candidates to apply online for 
                                                          various Entries.
                                                       7. By default your Email Id will also be your user name but candidate must select 
                                                          their own password (Not more than 10 Characters). All Candidates are advised to 
                                                          remember their user name and password.
                                                       8. Ensure all the detail you enter are correct.


                                              Press ENTER to continue for Checking the Eligibility.\n\n""")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back\n")
        print("=" * 150)
        print()

        while True:
            choose = input()

            if choose == '1':
                print("\nAre you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.main(self)
                    break

            else:
                break

        print()
        print("PERSONAL DATAILS :")
        print()

        while True:
            aadhar = input("\nEnter your aadhar no. :")
            if aadhar.isnumeric() is True and len(aadhar) == 12:
                break
            else:
                print(
                    "\n" + " " * 30 + "-------------------------------------INVALID AADHAR NO.-----------------------------------------")

        while True:
            c_name = input("\nEnter the candidate name :")
            if c_name.isalpha() is True and (c_name != '' or c_name != ' '):
                break
            else:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID CANDIDATE NAME---------------------------------------")

        while True:
            f_name = input("\nEnter your father name :")
            if f_name.isalpha() is True and (f_name != '' or f_name != ' '):
                break
            else:
                print(
                    "\n" + " " * 30 + "-------------------------------------INVALID FATHER NAME----------------------------------------")
        while True:
            m_name = input("\nEnter your mother name :")
            if m_name.isalpha() is True and (m_name != '' or m_name != ' '):
                break
            else:
                print(
                    "\n" + " " * 30 + "-------------------------------------INVALID MOTHER NAME----------------------------------------")

        while True:
            today = date.today()
            try:
                b_year = int(input("\nEnter the year of birth :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------INVALID YEAR OF BIRTH---------------------------------------")
            if b_year < today.year and b_year != None:
                break
            else:
                print(
                    "\n" + " " * 30 + "------------------------------------INVALID YEAR OF BIRTH---------------------------------------")
        while True:
            pos = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
            try:
                b_month = int(input("\nEnter the month of birth :"))
            except:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID MONTH OF BIRTH---------------------------------------")
            if b_month in pos and b_month != None:
                break
            else:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID MONTH OF BIRTH---------------------------------------")

        while True:
            try:
                b_day = int(input("\nEnter the day of birth :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------INVALID DAY OF BIRTH----------------------------------------")
            p1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                  27, 28, 29, 30, 31]
            p2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                  27, 28, 29, 30]
            p3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                  27, 28]
            p4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                  27, 28, 29]

            if b_month in (1, 3, 5, 7, 8, 10, 12):
                if b_day in p1:
                    break
                else:
                    print(
                        "\n" + " " * 30 + "------------------------------------INVALID DAY OF BIRTH----------------------------------------")
            elif b_month in (4, 6, 9, 11):
                if b_day in p2:
                    break
                else:
                    print(
                        "\n" + " " * 30 + "------------------------------------INVALID DAY OF BIRTH----------------------------------------")
            elif b_month == 2 and b_year % 4 == 0:
                if b_day in p4:
                    break
                else:
                    print(
                        "\n" + " " * 30 + "------------------------------------INVALID DAY OF BIRTH----------------------------------------")
            elif b_month == 2 and b_year % 4 != 0:
                if b_day in p3:
                    break
                else:
                    print(
                        "\n" + " " * 30 + "------------------------------------INVALID DAY OF BIRTH----------------------------------------")

        dob = date(b_year, b_month, b_day)

        c_age = agniipath.age(self, dob)

        while True:
            gendr = input("\nEnter your gender (M/F) :")
            if gendr in 'mM':
                gender = 'Male'
                break
            elif gendr in 'fF':
                gender = 'Female'
                break
            else:
                print(
                    "\n" + " " * 30 + "---------------------------------------INALID GENDER--------------------------------------------")

        while True:
            nationality = input("\nEnter your nationality :")
            if nationality.isalpha() is True and (nationality != '' or nationality != ' '):
                break
            else:
                print(
                    "\n" + " " * 30 + "-------------------------------------INALID NATIONALITY-----------------------------------------")

        while True:
            print()
            print(" " * 47 + "-" * 62)
            print(" " * 47 + "|      Choice for the matrial status:                        |")
            print(" " * 47 + "|" + " " * 60 + "|")
            print(" " * 47 + "|" + " " * 25 + "1. Divorcee" + " " * 24 + "|")
            print(" " * 47 + "|" + " " * 25 + "2. Married" + " " * 25 + "|")
            print(" " * 47 + "|" + " " * 25 + "3. Unmarried" + " " * 23 + "|")
            print(" " * 47 + "|" + " " * 25 + "4. Widower" + " " * 25 + "|")
            print(" " * 47 + "-" * 62)
            m_status = input("\nEnter your choose :")
            if m_status == 1:
                status = "Divorcee"
                break
            elif m_status == 2:
                status = "Married"
                break
            elif m_status == 3:
                status = "Unmarried"
                break
            elif m_status == 4:
                status = "Widower"
                break
            else:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID MATRIAL STATUS---------------------------------------")

        print("\nPress ENTER to continue the process...............................")
        print()
        i = input()

        time.sleep(2)

        print()
        print("CONTACT DETAILS :")
        print()

        while True:
            c_email = input("\nEnter your email address :")
            if c_email == " " or c_email == "":
                print(
                    "\n" + " " * 30 + "------------------------------------INVALID EMAIL ADDRESS---------------------------------------")
            else:
                break

        while True:
            c_mobile = input("\nEnter your mobile no. :")
            if c_mobile.isnumeric() == True and len(c_mobile) == 10 and c_mobile != "":
                break
            else:
                print(
                    "\n" + " " * 30 + "--------------------------------------INVALID PHONE NO.-----------------------------------------")

        print("\nPress ENTER to continue the process...............................")
        print()
        j = input()

        time.sleep(2)

        print()
        print("EDUCATION DETAILS :")
        print()

        while True:
            higher_qualification = input("\nEnter your hiqh school qualification (8th, 10th, 12th) :")
            if higher_qualification in ('8th', '10th', '12th'):
                break
            else:
                print(
                    "\n" + " " * 30 + "---------------------------------INVALID HIGHER QUALIFICATION-----------------------------------")

        print(" " * 15 + "-" * 126)
        print(
            " " * 15 + "|              Choice for Matriculation Board :                                                                              |")
        print(" " * 15 + "|" + " " * 20 + " 1. CENTRAL BOARD OF SECONDARY EDUCATION" + " " * 64 + "|")
        print(" " * 15 + "|" + " " * 20 + " 2. NATIONAL INSTITUTE OF OPEN SCHOOLING, NEW DELHI" + " " * 53 + "|")
        print(
            " " * 15 + "|" + " " * 20 + " 3. COUNCIL FOR THE INDIAN SCHOOL CERTIFICATE EXAMINATIONS, NEW DELHI" + " " * 35 + "|")
        print(" " * 15 + "|" + " " * 20 + " 4. BOARD OF INTERMEDIATE EDUCATION, ANDHRA PRADESH" + " " * 53 + "|")
        print(" " * 15 + "|" + " " * 20 + " 5. BOARD OF SECONDARY EDUCATION, ANDHRA PRADESH" + " " * 56 + "|")
        print(" " * 15 + "|" + " " * 20 + " 6. A.P. OPEN SCHOOL SOCIETY, ANDHRA PRADESH" + " " * 60 + "|")
        print(" " * 15 + "|" + " " * 20 + " 7. ASSAM HIGHER SECONDARY EDUCATION COUNCIL, ASSAM" + " " * 53 + "|")
        print(" " * 15 + "|" + " " * 20 + " 8. BOARD OF SECONDARY EDUCATION, ASSAM" + " " * 65 + "|")
        print(" " * 15 + "|" + " " * 20 + " 9. BIHAR SCHOOL EXAMINATION BOARD, BIHAR" + " " * 63 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "10. BIHAR BOARD OF OPEN SCHOOLING AND EXAMINATION(BBOSE), BIHAR" + " " * 41 + "|")
        print(" " * 15 + "|" + " " * 20 + "11. CHHATISGARH BOARD OF SECONDARY EDUCATION, CHHATISGARH" + " " * 47 + "|")
        print(" " * 15 + "|" + " " * 20 + "12. CHHATISGARH STATE OPEN SCHOOL, CHHATISGARH" + " " * 58 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "13. GOA BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, GOA" + " " * 42 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "14. GUJARAT SECONDARY AND HIGHER SECONDARY EDUCATION BOARD, GUJARAT" + " " * 37 + "|")
        print(" " * 15 + "|" + " " * 20 + "15. BOARD OF SCHOOL EDUCATION, HARYANA" + " " * 66 + "|")
        print(" " * 15 + "|" + " " * 20 + "16. H.P.BOARD OF SCHOOL EDUCATION, HIMACHAL PRADESH" + " " * 53 + "|")
        print(" " * 15 + "|" + " " * 20 + "17. THE J & K STATE BOARD OF SCHOOL EDUCATION, JAMMU" + " " * 52 + "|")
        print(" " * 15 + "|" + " " * 20 + "18. JHARKHAND ACADEMIC COUNCIL, RANCHI" + " " * 66 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "19. GOVT.OF KARNATAKA DEPT.OF PRE - UNIVERSITY EDUCATION, KARNATAKA" + " " * 37 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "20. KARNATAKA SECONDARY EDUCATION, EXAMINATION BOARD, KARNATAKA" + " " * 41 + "|")
        print(" " * 15 + "|" + " " * 20 + "21. KERALA BOARD OF PUBLIC EXAMINATION, KERALA" + " " * 58 + "|")
        print(" " * 15 + "|" + " " * 20 + "22. KERALA BOARD OF HIGHER SECONDARY EDUCATION, KERALA" + " " * 50 + "|")
        print(" " * 15 + "|" + " " * 20 + "23. BOARD OF VOCATIONAL HIGHER SECONDARY EDUCATION, KERALA" + " " * 46 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "24. MAHARASHTRA STATE BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, MAHARASHTRA" + " " * 20 + "|")
        print(" " * 15 + "|" + " " * 20 + "25. BOARD OF SECONDARY EDUCATION, MADHYA PRADESH" + " " * 56 + "|")
        print(" " * 15 + "|" + " " * 20 + "26. M.P.STATE OPEN SCHOOL EDUCATION BOARD, MADHYA PRADESH" + " " * 47 + "|")
        print(" " * 15 + "|" + " " * 20 + "27. BOARD OF SECONDARY EDUCATION, MANIPUR" + " " * 63 + "|")
        print(" " * 15 + "|" + " " * 20 + "28. COUNCIL OF HIGHER SECONDARY EDUCATION, MANIPUR" + " " * 54 + "|")
        print(" " * 15 + "|" + " " * 20 + "29. MEGHALAYA BOARD OF SCHOOL EDUCATION, MEGHALAYA" + " " * 54 + "|")
        print(" " * 15 + "|" + " " * 20 + "30. MIZORAM BOARD OF SCHOOL EDUCATION, MIZORAM" + " " * 58 + "|")
        print(" " * 15 + "|" + " " * 20 + "31. NAGALAND BOARD OF SCHOOL EDUCATION, NAGALAND" + " " * 56 + "|")
        print(" " * 15 + "|" + " " * 20 + "32. BOARD OF SECONDARY EDUCATION, ODISHA" + " " * 64 + "|")
        print(" " * 15 + "|" + " " * 20 + "33. COUNCIL OF HIGHER SECONDARY EDUCATION, ODISHA" + " " * 55 + "|")
        print(" " * 15 + "|" + " " * 20 + "34. PUNJAB SCHOOL EDUCATION BOARD, PUNJAB" + " " * 63 + "|")
        print(" " * 15 + "|" + " " * 20 + "35. BOARD OF SECONDARY EDUCATION, RAJASTHAN" + " " * 61 + "|")
        print(" " * 15 + "|" + " " * 20 + "36. RAJASTHAN STATE OPEN SCHOOL, RAJASTHAN" + " " * 62 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "37. STATE BOARD OF SCHOOL EXAMINATIONS(SEC.) & BOARD OF HIGHER SECONDARY, TAMIL NADU" + " " * 20 + "|")
        print(" " * 15 + "|" + " " * 20 + "38. BOARD OF SECONDARY EDUCATION, TELANGANA STATE" + " " * 55 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "39. TELANGANA STATE BOARD OF INTERMEDIATE EDUCATION, TELANGANA" + " " * 42 + "|")
        print(" " * 15 + "|" + " " * 20 + "40. TELANGANA OPEN SCHOOL SOCIETY, TELANGANA" + " " * 60 + "|")
        print(" " * 15 + "|" + " " * 20 + "41. TRIPURA BOARD OF SECONDARY EDUCATION, TRIPURA" + " " * 55 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "42. U.P.BOARD OF HIGH SCHOOL & INTERMEDIATE EDUCATION, UTTAR PRADESH" + " " * 36 + "|")
        print(" " * 15 + "|" + " " * 20 + "43. BOARD OF SCHOOL EDUCATION, UTTARAKHAND" + " " * 62 + "|")
        print(" " * 15 + "|" + " " * 20 + "44. WEST BENGAL BOARD OF SECONDARY EDUCATION, WEST BENGAL" + " " * 47 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "45. WEST BENGAL COUNCIL OF HIGHER SECONDARY EDUCATION, WEST BENGAL" + " " * 38 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "46. THE WEST BENGAL COUNCIL OF RABINDRA OPEN SCHOOLING, WEST BENGAL" + " " * 37 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "47. WEST BENGAL STATE COUNCIL OF TECHNICAL & VOCATIONAL EDUCATION & SKILL DEVELOPMENT, WEST BENGAL" + " " * 6 + "|")
        print(" " * 15 + "|" + " " * 20 + "48. MAHARISHI PATANJALI SANSKRIT SANSTHAN, NEW DELHI" + " " * 52 + "|")
        print(" " * 15 + "|" + " " * 20 + "49. URDU EDUCATION  BOARD, NEW DELHI" + " " * 68 + "|")
        print(" " * 15 + "|" + " " * 20 + "50. BIHAR SANSKRIT SHIKSHA BOARD, BIHAR" + " " * 65 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "51. U.P.BOARD OF SEC.SANSKRIT EDUCATION SANSKRIT BHAWAN, UTTAR PRADESH" + " " * 34 + "|")
        print(" " * 15 + "|" + " " * 20 + "52. ASSAM SANSKRIT BOARD, ASSAM" + " " * 73 + "|")
        print(" " * 15 + "|" + " " * 20 + "53. JAMIA MILIA ISLAMIA, NEW DELHI" + " " * 70 + "|")
        print(" " * 15 + "|" + " " * 20 + "54. UTTRAKHAND SANSKRIT SHIKSHA PARISHAD, UTTRAKHAND" + " " * 52 + "|")
        print(" " * 15 + "|" + " " * 20 + "55. STATE MADRASSA EDUCATION BOARD, ASSAM" + " " * 63 + "|")
        print(" " * 15 + "|" + " " * 20 + "56. BIHAR STATE MADRASA EDUCATION BOARD, BIHAR" + " " * 58 + "|")
        print(" " * 15 + "|" + " " * 20 + "57. WEST BENGAL BOARD OF MADRASAH EDUCATION, WEST BENGAL" + " " * 48 + "|")
        print(" " * 15 + "|" + " " * 20 + "58. CHHATTISGARH MADRASA BOARD, CHHATTISGARH" + " " * 60 + "|")
        print(" " * 15 + "|" + " " * 20 + "59. UTTARAKHAND MADRASA EDUCATION BOARD, UTTARAKHAND" + " " * 52 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "60. ALIGARH MUSLIM UNIVERSITY BOARD OF SECONDARY & SR.SECONDARY EDUCATION, UTTAR PARDESH" + " " * 16 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "61. INDIAN COUNCIL FOR HINDI & SANSKRIT EDUCATION, NEW DELHI" + " " * 44 + "|")
        print(" " * 15 + "|" + " " * 20 + "62. DAYALBAGH EDUCATIONAL INSTITUTE, AGRA" + " " * 63 + "|")
        print(" " * 15 + "|" + " " * 20 + "63. BANASTHALI VIDYAPITH P.O., RAJASTHAN" + " " * 64 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "64. BHUTAN COUNCIL FOR SCHOOL EXAMINATIONS & ASSESSMENT, BHUTAN" + " " * 41 + "|")
        print(" " * 15 + "|" + " " * 20 + "65. CAMBRIDGE ASSESSMENT INTERNATIONAL EXAMINATIONS, UK" + " " * 49 + "|")
        print(" " * 15 + "|" + " " * 20 + "66. CHHATTISGARH SANSKRIT BOARD, RAIPUR" + " " * 65 + "|")
        print(" " * 15 + "|" + " " * 20 + "67. MAURITIUS EXAMINATION SYNDICATE, MAURITIUS" + " " * 58 + "|")
        print(" " * 15 + "|" + " " * 20 + "68. NATIONAL EXAMINATIONS BOARD, NEPAL" + " " * 66 + "|")
        print(" " * 15 + "|" + " " * 20 + "69. PEARSON EDEXCEL LTD., UK" + " " * 76 + "|")
        print(" " * 15 + "|" + " " * 20 + "70. INTERNATIONAL BACCALAUREATE, GENEVA" + " " * 65 + "|")
        print(" " * 15 + "|" + " " * 20 + "71. NORTHWEST ACCREDITATION COMMISSION(NWAC), USA" + " " * 55 + "|")
        print(
            " " * 15 + "|" + " " * 20 + "72. SINGHANIA UNIVERSITY BOARD OF SECONDARY & SENIOR SECONDARY EDUCATION, RAJASTHAN" + " " * 21 + "|")
        print(" " * 15 + "-" * 126)

        while True:
            c = int(input("\nChoose the matriculation board :"))
            if c == 1:
                m_board = "CENTRAL BOARD OF SECONDARY EDUCATION"
                break
            elif c == 2:
                m_board = "NATIONAL INSTITUTE OF OPEN SCHOOLING, NEW DELHI"
                break
            elif c == 3:
                m_board = "COUNCIL FOR THE INDIAN SCHOOL CERTIFICATE EXAMINATIONS, NEW DELHI"
                break
            elif c == 4:
                m_board = "BOARD OF INTERMEDIATE EDUCATION, ANDHRA PRADESH"
                break
            elif c == 5:
                m_board = "BOARD OF SECONDARY EDUCATION, ANDHRA PRADESH"
                break
            elif c == 6:
                m_board = "A.P. OPEN SCHOOL SOCIETY, ANDHRA PRADESH"
                break
            elif c == 7:
                m_board = "ASSAM HIGHER SECONDARY EDUCATION COUNCIL, ASSAM"
                break
            elif c == 8:
                m_board = "BOARD OF SECONDARY EDUCATION, ASSAM"
                break
            elif c == 9:
                m_board = "BIHAR SCHOOL EXAMINATION BOARD, BIHAR"
                break
            elif c == 10:
                m_board = "BIHAR BOARD OF OPEN SCHOOLING AND EXAMINATION(BBOSE), BIHAR"
                break
            elif c == 11:
                m_board = "CHHATISGARH BOARD OF SECONDARY EDUCATION, CHHATISGARH"
                break
            elif c == 12:
                m_board = "CHHATISGARH STATE OPEN SCHOOL, CHHATISGARH"
                break
            elif c == 13:
                m_board = "GOA BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, GOA"
                break
            elif c == 14:
                m_board = "GUJARAT SECONDARY AND HIGHER SECONDARY EDUCATION BOARD, GUJARAT"
                break
            elif c == 15:
                m_board = "BOARD OF SCHOOL EDUCATION, HARYANA"
                break
            elif c == 16:
                m_board = "H.P.BOARD OF SCHOOL EDUCATION, HIMACHAL PRADESH"
                break
            elif c == 17:
                m_board = "THE J & K STATE BOARD OF SCHOOL EDUCATION, JAMMU"
                break
            elif c == 18:
                m_board = "JHARKHAND ACADEMIC COUNCIL, RANCHI"
                break
            elif c == 19:
                m_board = "GOVT.OF KARNATAKA DEPT.OF PRE - UNIVERSITY EDUCATION, KARNATAKA"
                break
            elif c == 20:
                m_board = "KARNATAKA SECONDARY EDUCATION, EXAMINATION BOARD, KARNATAKA"
                break
            elif c == 21:
                m_board = "KERALA BOARD OF PUBLIC EXAMINATION, KERALA"
                break
            elif c == 22:
                m_board = "KERALA BOARD OF HIGHER SECONDARY EDUCATION, KERALA"
                break
            elif c == 23:
                m_board = "BOARD OF VOCATIONAL HIGHER SECONDARY EDUCATION, KERALA"
                break
            elif c == 24:
                m_board = "MAHARASHTRA STATE BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, MAHARASHTRA"
                break
            elif c == 25:
                m_board = "BOARD OF SECONDARY EDUCATION, MADHYA PRADESH"
                break
            elif c == 26:
                m_board = "M.P.STATE OPEN SCHOOL EDUCATION BOARD, MADHYA PRADESH"
                break
            elif c == 27:
                m_board = "BOARD OF SECONDARY EDUCATION, MANIPUR"
                break
            elif c == 28:
                m_board = "COUNCIL OF HIGHER SECONDARY EDUCATION, MANIPUR"
                break
            elif c == 29:
                m_board = "MEGHALAYA BOARD OF SCHOOL EDUCATION, MEGHALAYA"
                break
            elif c == 30:
                m_board = "MIZORAM BOARD OF SCHOOL EDUCATION, MIZORAM"
                break
            elif c == 31:
                m_board = "NAGALAND BOARD OF SCHOOL EDUCATION, NAGALAND"
                break
            elif c == 32:
                m_board = "BOARD OF SECONDARY EDUCATION, ODISHA"
                break
            elif c == 33:
                m_board = "COUNCIL OF HIGHER SECONDARY EDUCATION, ODISHA"
                break
            elif c == 34:
                m_board = "PUNJAB SCHOOL EDUCATION BOARD, PUNJAB"
                break
            elif c == 35:
                m_board = "BOARD OF SECONDARY EDUCATION, RAJASTHAN"
                break
            elif c == 36:
                m_board = "RAJASTHAN STATE OPEN SCHOOL, RAJASTHAN"
                break
            elif c == 37:
                m_board = "STATE BOARD OF SCHOOL EXAMINATIONS(SEC.) & BOARD OF HIGHER SECONDARY, TAMIL NADU"
                break
            elif c == 38:
                m_board = "BOARD OF SECONDARY EDUCATION, TELANGANA STATE"
                break
            elif c == 39:
                m_board = "TELANGANA STATE BOARD OF INTERMEDIATE EDUCATION, TELANGANA"
                break
            elif c == 40:
                m_board = "TELANGANA OPEN SCHOOL SOCIETY, TELANGANA"
                break
            elif c == 41:
                m_board = "TRIPURA BOARD OF SECONDARY EDUCATION, TRIPURA"
                break
            elif c == 42:
                m_board = "U.P.BOARD OF HIGH SCHOOL & INTERMEDIATE EDUCATION, UTTAR PRADESH"
                break
            elif c == 43:
                m_board = "BOARD OF SCHOOL EDUCATION, UTTARAKHAND"
                break
            elif c == 44:
                m_board = "WEST BENGAL BOARD OF SECONDARY EDUCATION, WEST BENGAL"
                break
            elif c == 45:
                m_board = "WEST BENGAL COUNCIL OF HIGHER SECONDARY EDUCATION, WEST BENGAL"
                break
            elif c == 46:
                m_board = "THE WEST BENGAL COUNCIL OF RABINDRA OPEN SCHOOLING, WEST BENGAL"
                break
            elif c == 47:
                m_board = "WEST BENGAL STATE COUNCIL OF TECHNICAL & VOCATIONAL EDUCATION & SKILL DEVELOPMENT, WEST BENGAL"
                break
            elif c == 48:
                m_board = "MAHARISHI PATANJALI SANSKRIT SANSTHAN, NEW DELHI"
                break
            elif c == 49:
                m_board = "URDU EDUCATION  BOARD, NEW DELHI"
                break
            elif c == 50:
                m_board = "BIHAR SANSKRIT SHIKSHA BOARD, BIHAR"
                break
            elif c == 51:
                m_board = "U.P.BOARD OF SEC.SANSKRIT EDUCATION SANSKRIT BHAWAN, UTTAR PRADESH"
                break
            elif c == 52:
                m_board = "ASSAM SANSKRIT BOARD, ASSAM"
                break
            elif c == 53:
                m_board = "JAMIA MILIA ISLAMIA, NEW DELHI"
                break
            elif c == 54:
                m_board = "UTTRAKHAND SANSKRIT SHIKSHA PARISHAD, UTTRAKHAND"
                break
            elif c == 55:
                m_board = "STATE MADRASSA EDUCATION BOARD, ASSAM"
                break
            elif c == 56:
                m_board = "BIHAR STATE MADRASA EDUCATION BOARD, BIHAR"
                break
            elif c == 57:
                m_board = "WEST BENGAL BOARD OF MADRASAH EDUCATION, WEST BENGAL"
                break
            elif c == 58:
                m_board = "CHHATTISGARH MADRASA BOARD, CHHATTISGARH"
                break
            elif c == 59:
                m_board = "UTTARAKHAND MADRASA EDUCATION BOARD, UTTARAKHAND"
                break
            elif c == 60:
                m_board = "ALIGARH MUSLIM UNIVERSITY BOARD OF SECONDARY & SR.SECONDARY EDUCATION, UTTAR PARDESH"
                break
            elif c == 61:
                m_board = "INDIAN COUNCIL FOR HINDI & SANSKRIT EDUCATION, NEW DELHI"
                break
            elif c == 62:
                m_board = "DAYALBAGH EDUCATIONAL INSTITUTE, AGRA"
                break
            elif c == 63:
                m_board = "BANASTHALI VIDYAPITH P.O., RAJASTHAN"
                break
            elif c == 64:
                m_board = "BHUTAN COUNCIL FOR SCHOOL EXAMINATIONS & ASSESSMENT, BHUTAN"
                break
            elif c == 65:
                m_board = "CAMBRIDGE ASSESSMENT INTERNATIONAL EXAMINATIONS, UK"
                break
            elif c == 66:
                m_board = "CHHATTISGARH SANSKRIT BOARD, RAIPUR"
                break
            elif c == 67:
                m_board = "MAURITIUS EXAMINATION SYNDICATE, MAURITIUS"
                break
            elif c == 68:
                m_board = "NATIONAL EXAMINATIONS BOARD, NEPAL"
                break
            elif c == 69:
                m_board = "PEARSON EDEXCEL LTD., UK"
                break
            elif c == 70:
                m_board = "INTERNATIONAL BACCALAUREATE, GENEVA"
                break
            elif c == 71:
                m_board = "NORTHWEST ACCREDITATION COMMISSION(NWAC), USA"
                break
            elif c == 72:
                m_board = "SINGHANIA UNIVERSITY BOARD OF SECONDARY & SENIOR SECONDARY EDUCATION, RAJASTHAN"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        print("\nPress ENTER to continue the process...............................")
        print()
        k = input()

        time.sleep(2)

        print()
        print("COMMUNICATION INFORMATION :")
        print()

        print(
            """                         
                                         --------------------------------------------------------------------------
                                         |      Sl.no.      |               State/Union Territory Name            |
                                         |------------------|-----------------------------------------------------|
                                         |         1.       | Andhra Pradesh                                      |
                                         |         2.       | Arunachal Pradesh                                   |
                                         |         3.       | Assam                                               |
                                         |         4.       | Bihar                                               |
                                         |         5.       | Chattisgrarh                                        |
                                         |         6.       | Goa                                                 |
                                         |         7.       | Gujarat                                             |
                                         |         8.       | Haryana                                             |
                                         |         9.       | Himachal Pradesh                                    |
                                         |        10.       | Jammu & Kashmir                                     |
                                         |        11.       | Jharkhand                                           |
                                         |        12.       | Karnataka                                           |
                                         |        13.       | Kerala                                              |
                                         |        14.       | Madhya Pradesh                                      |
                                         |        15.       | Maharashtra                                         |
                                         |        16.       | Manipur                                             |
                                         |        17.       | Meghalaya                                           |
                                         |        18.       | Mizoram                                             |
                                         |        19.       | Nagaland                                            |
                                         |        20.       | Odisha                                              |
                                         |        21.       | Punjab                                              |
                                         |        22.       | Rajasthan                                           |
                                         |        23.       | Sikkim                                              |
                                         |        24.       | Tamil Nadu                                          |
                                         |        25.       | Telangana                                           |
                                         |        26.       | Tripura                                             |
                                         |        27.       | Uttar Pradesh                                       |
                                         |        28.       | Uttarakhand                                         |
                                         |        29.       | West Bengal                                         |
                                         |        30.       | Andaman & Nicobar                                   |
                                         |        31.       | Chandigarh                                          |
                                         |        32.       | Dadra and Nagar Haveli and Daman and Diu            |
                                         |        33.       | Delhi                                               |
                                         |        34.       | Lakshadweep                                         |
                                         |        35.       | Ladakh                                              |
                                         |        36.       | Puducherry                                          |
                                         --------------------------------------------------------------------------
            """)
        while True:
            s_u = int(input("\nChoose your State/Union Territory Name :"))
            if s_u == 1:
                st_ut = 'Andhra Pradesh'
                break
            elif s_u == 2:
                st_ut = 'Arunachal Pradesh'
                break
            elif s_u == 3:
                st_ut = 'Assam'
                break
            elif s_u == 4:
                st_ut = 'Bihar'
                break
            elif s_u == 5:
                st_ut = 'Chattisgrarh'
                break
            elif s_u == 6:
                st_ut = 'Goa'
                break
            elif s_u == 7:
                st_ut = 'Gujarat'
                break
            elif s_u == 8:
                st_ut = 'Haryana'
                break
            elif s_u == 9:
                st_ut = 'Himachal Pradesh'
                break
            elif s_u == 10:
                st_ut = 'Jammu & Kashmir'
                break
            elif s_u == 11:
                st_ut = 'Jharkhand'
                break
            elif s_u == 12:
                st_ut = 'Karnataka'
                break
            elif s_u == 13:
                st_ut = 'Kerala'
                break
            elif s_u == 14:
                st_ut = 'Madhya Pradesh'
                break
            elif s_u == 15:
                st_ut = 'Maharashtra'
                break
            elif s_u == 16:
                st_ut = 'Manipur'
                break
            elif s_u == 17:
                st_ut = 'Meghalaya'
                break
            elif s_u == 18:
                st_ut = 'Mizoram'
                break
            elif s_u == 19:
                st_ut = 'Nagaland'
                break
            elif s_u == 20:
                st_ut = 'Odisha'
                break
            elif s_u == 21:
                st_ut = 'Punjab'
                break
            elif s_u == 22:
                st_ut = 'Rajasthan'
                break
            elif s_u == 23:
                st_ut = 'Sikkim'
                break
            elif s_u == 24:
                st_ut = 'Tamil Nadu'
                break
            elif s_u == 25:
                st_ut = 'Telangana'
                break
            elif s_u == 26:
                st_ut = 'Tripura'
                break
            elif s_u == 27:
                st_ut = 'Uttar Pradesh'
                break
            elif s_u == 28:
                st_ut = 'Uttarakhand'
                break
            elif s_u == 29:
                st_ut = 'West Bengal'
                break
            elif s_u == 30:
                st_ut = 'Andaman & Nicobar'
                break
            elif s_u == 31:
                st_ut = 'Chandigarh'
                break
            elif s_u == 32:
                st_ut = 'Dadra and Nagar Haveli and Daman and Diu'
                break
            elif s_u == 33:
                st_ut = 'Delhi'
                break
            elif s_u == 34:
                st_ut = 'Lakshadweep'
                break
            elif s_u == 35:
                st_ut = 'Ladakh'
                break
            elif s_u == 36:
                st_ut = 'Puducherry'
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        r1 = ['Jammu & Kashmir', 'Ladakh', 'Himachal Pradesh', 'Punjab', 'Uttarakhand']
        r2 = ['Sikkim', 'Nagaland', 'Arunachal Pradesh', 'Manipur', 'Tripura', 'Mizoram', 'Meghalaya', 'Assam']
        r3 = ['Haryana', 'Chandigarh', 'Delhi', 'Rajasthan', 'Uttar Pradesh']
        r4 = ['Bihar', 'West Bengal', 'Jharkhand', 'Odisha']
        r5 = ['Madhya Pradesh', 'Chattisgrarh', 'Gujarat', 'Maharashtra', 'Dadra and Nagar Haveli and Daman and Diu']
        r6 = ['Andhra Pradesh', 'Telangana', 'Karnataka', 'Tamil Nadu', 'Kerala', 'Goa', 'Puducherry',
              'Andaman & Nicobar', 'Lakshadweep']

        region = None
        if st_ut in r1:
            region = "Western Himalayas Region"

        elif st_ut in r2:
            region = "Eastern Himalayas Region"

        elif st_ut in r3:
            region = "Western Plains Region"

        elif st_ut in r4:
            region = "Eastern Plains Region"

        elif st_ut in r5:
            region = "Central Region"

        elif st_ut in r6:
            region = "Southern Region"

        print("\nPress ENTER to continue the process...............................")
        print()
        k = input()

        time.sleep(2)

        print()
        print("DETAILS :")
        print()

        while True:
            print(" " * 47 + "-" * 62)
            print(" " * 47 + "|      Choice for the matrial status:                        |")
            print(" " * 47 + "|" + " " * 20 + "1. General Rally" + " " * 24 + "|")
            print(" " * 47 + "|" + " " * 20 + "2. Unit Head Quator (UHQ)" + " " * 15 + "|")
            print(" " * 47 + "-" * 62)
            print()
            cat = int(input("\nEnter your Choise :"))
            if cat == 1:
                category = "General Rally"
                break
            elif cat == 2:
                category = "Unit Head Quator (UHQ)"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        while True:
            s = input("\nAre you a sports man? (Y/N)\n")
            if s in 'Yy':
                sports = input("\nSpecify the sports :")
                break
            elif s in 'nN':
                sports = "NO"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        while True:
            nc = input("\nAre you in NCC? (Y/N)\n")
            if nc in 'Yy':
                ncc = "YES"
                break
            elif nc in 'nN':
                ncc = "NO"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        print("""
                                               ---------------------------------------------------------------------------
                                               |   Sl.no    |                    Special category                        |
                                               |------------|------------------------------------------------------------|
                                               |     1.     | Non Dispensation Category                                  |
                                               |------------|------------------------------------------------------------|
                                               |     2.     | Ladakhi                                                    |
                                               |------------|------------------------------------------------------------|
                                               |     3.     | Gorkha Nepalese and Indian Origin                          |
                                               |------------|------------------------------------------------------------|
                                               |     4.     | Settlers ( Andaman and Nicobar, Lakshadweep including      |
                                               |            | Minicoy )                                                  |
                                               |------------|------------------------------------------------------------|
                                               |     5.     | Locals of Andaman and Nicobar, Lakshadweep including       |
                                               |            | Minicoy                                                    |
                                               |------------|------------------------------------------------------------|
                                               |     6.     | Tribals of Recognized Tribal Areas                         |
                                               |------------|------------------------------------------------------------|
                                               |     7.     | Son of Army Personal                                       |
                                               |------------|------------------------------------------------------------|
                                               |     8.     | Arunachal and Sikkim Scouts only                           |
                                               ---------------------------------------------------------------------------

        """)
        while True:
            print("Do you belong to any of the mentioned Special Category?\n"
                  "Select any one from above.\n"
                  "If NO press n.\n"
                  "Choose your Option :")
            cho = input()
            if cho in 'nN':
                spe_category = "NO"
                break
            elif cho == '1':
                spe_category = "Non Dispensation Category"
                break
            elif cho == '2':
                spe_category = "Ladakhi"
                break
            elif cho == '3':
                spe_category = "Gorkha Nepalese and Indian Origin"
                break
            elif cho == '4':
                spe_category = "Settlers ( Andaman and Nicobar, Lakshadweep including Minicoy )"
                break
            elif cho == '5':
                spe_category = "Locals of Andaman and Nicobar, Lakshadweep including Minicoy"
                break
            elif cho == '6':
                spe_category = "Tribals of Recognized Tribal Areas"
                break
            elif cho == '7':
                spe_category = "Son of Army Personal"
                break
            elif cho == '8':
                spe_category = "Arunachal and Sikkim Scouts only"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        print("\nPress ENTER to continue the process...............................")
        print()
        j = input()

        time.sleep(2)

        print()
        print("EDUCATION DETAILS :")
        print()

        print("""
                                            ------------------------------------------------------------------
                                            |      Choose for Highest Qualification:                         |
                                            |                         1. 8th Pass                            |
                                            |                         2. 10th Pass                           |
                                            |                         3. 12th Pass                           |
                                            |                         4. Graduation                          |
                                            |                         5. Post Graduation                     |
                                            ------------------------------------------------------------------
        """)

        while True:
            h_q = int(input("\nEnter your choice :"))
            if h_q == 1:
                highest_qualification = "8th Pass"
                break
            elif h_q == 2:
                highest_qualification = "10th Pass"
                break
            elif h_q == 3:
                highest_qualification = "12th Pass"
                break
            elif h_q == 4:
                highest_qualification = "Graduation"
                break
            elif h_q == 5:
                highest_qualification = "Post Graduation"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        while True:
            qualification_course = input("\nEnter the qualifying course :")
            if qualification_course == '' or qualification_course == ' ':
                print(
                    "\n" + " " * 30 + "-------------------------------INVALID QUALIFICATION COURSE-------------------------------------")
            else:
                break

        print("""
                                       ------------------------------------------------------------------
                                       |           Choose for Board/Education University :              |
                                       |                      1. Central University                     |
                                       |                      2. State University                       |
                                       |                      3. Deemed University                      |
                                       |                      4. Private University                     |
                                       |                      5. CBSE                                   |
                                       |                      6. ICSE                                   |
                                       |                      7. Open School                            |
                                       |                      8. State Board                            |
                                       |                      9. Others                                 |
                                       ------------------------------------------------------------------
        """)

        while True:
            uni = int(input("\nEnter your Board/Education University :"))
            if uni in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        if uni == 1:
            university = "Central University"
        if uni == 2:
            university = "State University"
        if uni == 3:
            university = "Deemed University"
        if uni == 4:
            university = "Private University"
        if uni == 5:
            university = "CBSE"
        if uni == 6:
            university = "ICSE"
        if uni == 7:
            university = "Open School"
        if uni == 8:
            university = "State Board"
        if uni == 9:
            university = "Others"

        if uni in (1, 2, 3, 4, 9):
            while True:
                uni_boa_name = input("\nEnter the name of the university :").upper()
                if uni_boa_name == '' or uni_boa_name == ' ':
                    print(
                        "\n" + " " * 30 + "------------------------------INVALID UNIVERSITY/BOARD NAME-------------------------------------")
                else:
                    break

        if uni == 5:
            uni_boa_name = "CENTRAL BOARD OF SECONDARY EDUCATION"

        if uni == 6:
            uni_boa_name = "INDIAN CERTIFICATE OF SECONDARY EDUCATION"

        if uni in (7, 8, 9):
            print(" " * 15 + "-" * 126)
            print(
                " " * 15 + "|              Choice for Board :                                                                                            |")
            print(" " * 15 + "|" + " " * 20 + " 1. NORTHWEST ACCREDITATION COMMISSION(NWAC), USA" + " " * 55 + "|")
            print(" " * 15 + "|" + " " * 20 + " 2. NATIONAL INSTITUTE OF OPEN SCHOOLING, NEW DELHI" + " " * 53 + "|")
            print(
                " " * 15 + "|" + " " * 20 + " 3. COUNCIL FOR THE INDIAN SCHOOL CERTIFICATE EXAMINATIONS, NEW DELHI" + " " * 35 + "|")
            print(" " * 15 + "|" + " " * 20 + " 4. BOARD OF INTERMEDIATE EDUCATION, ANDHRA PRADESH" + " " * 53 + "|")
            print(" " * 15 + "|" + " " * 20 + " 5. BOARD OF SECONDARY EDUCATION, ANDHRA PRADESH" + " " * 56 + "|")
            print(" " * 15 + "|" + " " * 20 + " 6. A.P. OPEN SCHOOL SOCIETY, ANDHRA PRADESH" + " " * 60 + "|")
            print(" " * 15 + "|" + " " * 20 + " 7. ASSAM HIGHER SECONDARY EDUCATION COUNCIL, ASSAM" + " " * 53 + "|")
            print(" " * 15 + "|" + " " * 20 + " 8. BOARD OF SECONDARY EDUCATION, ASSAM" + " " * 65 + "|")
            print(" " * 15 + "|" + " " * 20 + " 9. BIHAR SCHOOL EXAMINATION BOARD, BIHAR" + " " * 63 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "10. BIHAR BOARD OF OPEN SCHOOLING AND EXAMINATION(BBOSE), BIHAR" + " " * 41 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "11. CHHATISGARH BOARD OF SECONDARY EDUCATION, CHHATISGARH" + " " * 47 + "|")
            print(" " * 15 + "|" + " " * 20 + "12. CHHATISGARH STATE OPEN SCHOOL, CHHATISGARH" + " " * 58 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "13. GOA BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, GOA" + " " * 42 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "14. GUJARAT SECONDARY AND HIGHER SECONDARY EDUCATION BOARD, GUJARAT" + " " * 37 + "|")
            print(" " * 15 + "|" + " " * 20 + "15. BOARD OF SCHOOL EDUCATION, HARYANA" + " " * 66 + "|")
            print(" " * 15 + "|" + " " * 20 + "16. H.P.BOARD OF SCHOOL EDUCATION, HIMACHAL PRADESH" + " " * 53 + "|")
            print(" " * 15 + "|" + " " * 20 + "17. THE J & K STATE BOARD OF SCHOOL EDUCATION, JAMMU" + " " * 52 + "|")
            print(" " * 15 + "|" + " " * 20 + "18. JHARKHAND ACADEMIC COUNCIL, RANCHI" + " " * 66 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "19. GOVT.OF KARNATAKA DEPT.OF PRE - UNIVERSITY EDUCATION, KARNATAKA" + " " * 37 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "20. KARNATAKA SECONDARY EDUCATION, EXAMINATION BOARD, KARNATAKA" + " " * 41 + "|")
            print(" " * 15 + "|" + " " * 20 + "21. KERALA BOARD OF PUBLIC EXAMINATION, KERALA" + " " * 58 + "|")
            print(" " * 15 + "|" + " " * 20 + "22. KERALA BOARD OF HIGHER SECONDARY EDUCATION, KERALA" + " " * 50 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "23. BOARD OF VOCATIONAL HIGHER SECONDARY EDUCATION, KERALA" + " " * 46 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "24. MAHARASHTRA STATE BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, MAHARASHTRA" + " " * 20 + "|")
            print(" " * 15 + "|" + " " * 20 + "25. BOARD OF SECONDARY EDUCATION, MADHYA PRADESH" + " " * 56 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "26. M.P.STATE OPEN SCHOOL EDUCATION BOARD, MADHYA PRADESH" + " " * 47 + "|")
            print(" " * 15 + "|" + " " * 20 + "27. BOARD OF SECONDARY EDUCATION, MANIPUR" + " " * 63 + "|")
            print(" " * 15 + "|" + " " * 20 + "28. COUNCIL OF HIGHER SECONDARY EDUCATION, MANIPUR" + " " * 54 + "|")
            print(" " * 15 + "|" + " " * 20 + "29. MEGHALAYA BOARD OF SCHOOL EDUCATION, MEGHALAYA" + " " * 54 + "|")
            print(" " * 15 + "|" + " " * 20 + "30. MIZORAM BOARD OF SCHOOL EDUCATION, MIZORAM" + " " * 58 + "|")
            print(" " * 15 + "|" + " " * 20 + "31. NAGALAND BOARD OF SCHOOL EDUCATION, NAGALAND" + " " * 56 + "|")
            print(" " * 15 + "|" + " " * 20 + "32. BOARD OF SECONDARY EDUCATION, ODISHA" + " " * 64 + "|")
            print(" " * 15 + "|" + " " * 20 + "33. COUNCIL OF HIGHER SECONDARY EDUCATION, ODISHA" + " " * 55 + "|")
            print(" " * 15 + "|" + " " * 20 + "34. PUNJAB SCHOOL EDUCATION BOARD, PUNJAB" + " " * 63 + "|")
            print(" " * 15 + "|" + " " * 20 + "35. BOARD OF SECONDARY EDUCATION, RAJASTHAN" + " " * 61 + "|")
            print(" " * 15 + "|" + " " * 20 + "36. RAJASTHAN STATE OPEN SCHOOL, RAJASTHAN" + " " * 62 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "37. STATE BOARD OF SCHOOL EXAMINATIONS(SEC.) & BOARD OF HIGHER SECONDARY, TAMIL NADU" + " " * 20 + "|")
            print(" " * 15 + "|" + " " * 20 + "38. BOARD OF SECONDARY EDUCATION, TELANGANA STATE" + " " * 55 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "39. TELANGANA STATE BOARD OF INTERMEDIATE EDUCATION, TELANGANA" + " " * 42 + "|")
            print(" " * 15 + "|" + " " * 20 + "40. TELANGANA OPEN SCHOOL SOCIETY, TELANGANA" + " " * 60 + "|")
            print(" " * 15 + "|" + " " * 20 + "41. TRIPURA BOARD OF SECONDARY EDUCATION, TRIPURA" + " " * 55 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "42. U.P.BOARD OF HIGH SCHOOL & INTERMEDIATE EDUCATION, UTTAR PRADESH" + " " * 36 + "|")
            print(" " * 15 + "|" + " " * 20 + "43. BOARD OF SCHOOL EDUCATION, UTTARAKHAND" + " " * 62 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "44. WEST BENGAL BOARD OF SECONDARY EDUCATION, WEST BENGAL" + " " * 47 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "45. WEST BENGAL COUNCIL OF HIGHER SECONDARY EDUCATION, WEST BENGAL" + " " * 38 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "46. THE WEST BENGAL COUNCIL OF RABINDRA OPEN SCHOOLING, WEST BENGAL" + " " * 37 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "47. WEST BENGAL STATE COUNCIL OF TECHNICAL & VOCATIONAL EDUCATION & SKILL DEVELOPMENT, WEST BENGAL" + " " * 6 + "|")
            print(" " * 15 + "|" + " " * 20 + "48. MAHARISHI PATANJALI SANSKRIT SANSTHAN, NEW DELHI" + " " * 52 + "|")
            print(" " * 15 + "|" + " " * 20 + "49. URDU EDUCATION  BOARD, NEW DELHI" + " " * 68 + "|")
            print(" " * 15 + "|" + " " * 20 + "50. BIHAR SANSKRIT SHIKSHA BOARD, BIHAR" + " " * 65 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "51. U.P.BOARD OF SEC.SANSKRIT EDUCATION SANSKRIT BHAWAN, UTTAR PRADESH" + " " * 34 + "|")
            print(" " * 15 + "|" + " " * 20 + "52. ASSAM SANSKRIT BOARD, ASSAM" + " " * 73 + "|")
            print(" " * 15 + "|" + " " * 20 + "53. JAMIA MILIA ISLAMIA, NEW DELHI" + " " * 70 + "|")
            print(" " * 15 + "|" + " " * 20 + "54. UTTRAKHAND SANSKRIT SHIKSHA PARISHAD, UTTRAKHAND" + " " * 52 + "|")
            print(" " * 15 + "|" + " " * 20 + "55. STATE MADRASSA EDUCATION BOARD, ASSAM" + " " * 63 + "|")
            print(" " * 15 + "|" + " " * 20 + "56. BIHAR STATE MADRASA EDUCATION BOARD, BIHAR" + " " * 58 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "57. WEST BENGAL BOARD OF MADRASAH EDUCATION, WEST BENGAL" + " " * 48 + "|")
            print(" " * 15 + "|" + " " * 20 + "58. CHHATTISGARH MADRASA BOARD, CHHATTISGARH" + " " * 60 + "|")
            print(" " * 15 + "|" + " " * 20 + "59. UTTARAKHAND MADRASA EDUCATION BOARD, UTTARAKHAND" + " " * 52 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "60. ALIGARH MUSLIM UNIVERSITY BOARD OF SECONDARY & SR.SECONDARY EDUCATION, UTTAR PARDESH" + " " * 16 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "61. INDIAN COUNCIL FOR HINDI & SANSKRIT EDUCATION, NEW DELHI" + " " * 44 + "|")
            print(" " * 15 + "|" + " " * 20 + "62. DAYALBAGH EDUCATIONAL INSTITUTE, AGRA" + " " * 63 + "|")
            print(" " * 15 + "|" + " " * 20 + "63. BANASTHALI VIDYAPITH P.O., RAJASTHAN" + " " * 64 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "64. BHUTAN COUNCIL FOR SCHOOL EXAMINATIONS & ASSESSMENT, BHUTAN" + " " * 41 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "65. CAMBRIDGE ASSESSMENT INTERNATIONAL EXAMINATIONS, UK" + " " * 49 + "|")
            print(" " * 15 + "|" + " " * 20 + "66. CHHATTISGARH SANSKRIT BOARD, RAIPUR" + " " * 65 + "|")
            print(" " * 15 + "|" + " " * 20 + "67. MAURITIUS EXAMINATION SYNDICATE, MAURITIUS" + " " * 58 + "|")
            print(" " * 15 + "|" + " " * 20 + "68. NATIONAL EXAMINATIONS BOARD, NEPAL" + " " * 66 + "|")
            print(" " * 15 + "|" + " " * 20 + "69. PEARSON EDEXCEL LTD., UK" + " " * 76 + "|")
            print(" " * 15 + "|" + " " * 20 + "70. INTERNATIONAL BACCALAUREATE, GENEVA" + " " * 65 + "|")
            print(
                " " * 15 + "|" + " " * 20 + "71. SINGHANIA UNIVERSITY BOARD OF SECONDARY & SENIOR SECONDARY EDUCATION, RAJASTHAN" + " " * 21 + "|")
            print(" " * 15 + "-" * 126)

            while True:
                c1 = int(input("\nChoose the board :"))
                if c1 == 1:
                    uni_boa_name = "NORTHWEST ACCREDITATION COMMISSION(NWAC), USA"
                    break
                elif c1 == 2:
                    uni_boa_name = "NATIONAL INSTITUTE OF OPEN SCHOOLING, NEW DELHI"
                    break
                elif c1 == 3:
                    uni_boa_name = "COUNCIL FOR THE INDIAN SCHOOL CERTIFICATE EXAMINATIONS, NEW DELHI"
                    break
                elif c1 == 4:
                    uni_boa_name = "BOARD OF INTERMEDIATE EDUCATION, ANDHRA PRADESH"
                    break
                elif c1 == 5:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, ANDHRA PRADESH"
                    break
                elif c1 == 6:
                    uni_boa_name = "A.P. OPEN SCHOOL SOCIETY, ANDHRA PRADESH"
                    break
                elif c1 == 7:
                    uni_boa_name = "ASSAM HIGHER SECONDARY EDUCATION COUNCIL, ASSAM"
                    break
                elif c1 == 8:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, ASSAM"
                    break
                elif c1 == 9:
                    uni_boa_name = "BIHAR SCHOOL EXAMINATION BOARD, BIHAR"
                    break
                elif c1 == 10:
                    uni_boa_name = "BIHAR BOARD OF OPEN SCHOOLING AND EXAMINATION(BBOSE), BIHAR"
                    break
                elif c1 == 11:
                    uni_boa_name = "CHHATISGARH BOARD OF SECONDARY EDUCATION, CHHATISGARH"
                    break
                elif c1 == 12:
                    uni_boa_name = "CHHATISGARH STATE OPEN SCHOOL, CHHATISGARH"
                    break
                elif c1 == 13:
                    uni_boa_name = "GOA BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, GOA"
                    break
                elif c1 == 14:
                    uni_boa_name = "GUJARAT SECONDARY AND HIGHER SECONDARY EDUCATION BOARD, GUJARAT"
                    break
                elif c1 == 15:
                    uni_boa_name = "BOARD OF SCHOOL EDUCATION, HARYANA"
                    break
                elif c1 == 16:
                    uni_boa_name = "H.P.BOARD OF SCHOOL EDUCATION, HIMACHAL PRADESH"
                    break
                elif c1 == 17:
                    uni_boa_name = "THE J & K STATE BOARD OF SCHOOL EDUCATION, JAMMU"
                    break
                elif c1 == 18:
                    uni_boa_name = "JHARKHAND ACADEMIC COUNCIL, RANCHI"
                    break
                elif c1 == 19:
                    uni_boa_name = "GOVT.OF KARNATAKA DEPT.OF PRE - UNIVERSITY EDUCATION, KARNATAKA"
                    break
                elif c1 == 20:
                    uni_boa_name = "KARNATAKA SECONDARY EDUCATION, EXAMINATION BOARD, KARNATAKA"
                    break
                elif c1 == 21:
                    uni_boa_name = "KERALA BOARD OF PUBLIC EXAMINATION, KERALA"
                    break
                elif c1 == 22:
                    uni_boa_name = "KERALA BOARD OF HIGHER SECONDARY EDUCATION, KERALA"
                    break
                elif c1 == 23:
                    uni_boa_name = "BOARD OF VOCATIONAL HIGHER SECONDARY EDUCATION, KERALA"
                    break
                elif c1 == 24:
                    uni_boa_name = "MAHARASHTRA STATE BOARD OF SECONDARY AND HIGHER SECONDARY EDUCATION, MAHARASHTRA"
                    break
                elif c1 == 25:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, MADHYA PRADESH"
                    break
                elif c1 == 26:
                    uni_boa_name = "M.P.STATE OPEN SCHOOL EDUCATION BOARD, MADHYA PRADESH"
                    break
                elif c1 == 27:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, MANIPUR"
                    break
                elif c1 == 28:
                    uni_boa_name = "COUNCIL OF HIGHER SECONDARY EDUCATION, MANIPUR"
                    break
                elif c1 == 29:
                    uni_boa_name = "MEGHALAYA BOARD OF SCHOOL EDUCATION, MEGHALAYA"
                    break
                elif c1 == 30:
                    uni_boa_name = "MIZORAM BOARD OF SCHOOL EDUCATION, MIZORAM"
                    break
                elif c1 == 31:
                    uni_boa_name = "NAGALAND BOARD OF SCHOOL EDUCATION, NAGALAND"
                    break
                elif c1 == 32:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, ODISHA"
                    break
                elif c1 == 33:
                    uni_boa_name = "COUNCIL OF HIGHER SECONDARY EDUCATION, ODISHA"
                    break
                elif c1 == 34:
                    uni_boa_name = "PUNJAB SCHOOL EDUCATION BOARD, PUNJAB"
                    break
                elif c1 == 35:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, RAJASTHAN"
                    break
                elif c1 == 36:
                    uni_boa_name = "RAJASTHAN STATE OPEN SCHOOL, RAJASTHAN"
                    break
                elif c1 == 37:
                    uni_boa_name = "STATE BOARD OF SCHOOL EXAMINATIONS(SEC.) & BOARD OF HIGHER SECONDARY, TAMIL NADU"
                    break
                elif c1 == 38:
                    uni_boa_name = "BOARD OF SECONDARY EDUCATION, TELANGANA STATE"
                    break
                elif c1 == 39:
                    uni_boa_name = "TELANGANA STATE BOARD OF INTERMEDIATE EDUCATION, TELANGANA"
                    break
                elif c1 == 40:
                    uni_boa_name = "TELANGANA OPEN SCHOOL SOCIETY, TELANGANA"
                    break
                elif c1 == 41:
                    uni_boa_name = "TRIPURA BOARD OF SECONDARY EDUCATION, TRIPURA"
                    break
                elif c1 == 42:
                    uni_boa_name = "U.P.BOARD OF HIGH SCHOOL & INTERMEDIATE EDUCATION, UTTAR PRADESH"
                    break
                elif c1 == 43:
                    uni_boa_name = "BOARD OF SCHOOL EDUCATION, UTTARAKHAND"
                    break
                elif c1 == 44:
                    uni_boa_name = "WEST BENGAL BOARD OF SECONDARY EDUCATION, WEST BENGAL"
                    break
                elif c1 == 45:
                    uni_boa_name = "WEST BENGAL COUNCIL OF HIGHER SECONDARY EDUCATION, WEST BENGAL"
                    break
                elif c1 == 46:
                    uni_boa_name = "THE WEST BENGAL COUNCIL OF RABINDRA OPEN SCHOOLING, WEST BENGAL"
                    break
                elif c1 == 47:
                    uni_boa_name = "WEST BENGAL STATE COUNCIL OF TECHNICAL & VOCATIONAL EDUCATION & SKILL DEVELOPMENT, WEST BENGAL"
                    break
                elif c1 == 48:
                    uni_boa_name = "MAHARISHI PATANJALI SANSKRIT SANSTHAN, NEW DELHI"
                    break
                elif c1 == 49:
                    uni_boa_name = "URDU EDUCATION  BOARD, NEW DELHI"
                    break
                elif c1 == 50:
                    uni_boa_name = "BIHAR SANSKRIT SHIKSHA BOARD, BIHAR"
                    break
                elif c1 == 51:
                    uni_boa_name = "U.P.BOARD OF SEC.SANSKRIT EDUCATION SANSKRIT BHAWAN, UTTAR PRADESH"
                    break
                elif c1 == 52:
                    uni_boa_name = "ASSAM SANSKRIT BOARD, ASSAM"
                    break
                elif c1 == 53:
                    uni_boa_name = "JAMIA MILIA ISLAMIA, NEW DELHI"
                    break
                elif c1 == 54:
                    uni_boa_name = "UTTRAKHAND SANSKRIT SHIKSHA PARISHAD, UTTRAKHAND"
                    break
                elif c1 == 55:
                    uni_boa_name = "STATE MADRASSA EDUCATION BOARD, ASSAM"
                    break
                elif c1 == 56:
                    uni_boa_name = "BIHAR STATE MADRASA EDUCATION BOARD, BIHAR"
                    break
                elif c1 == 57:
                    uni_boa_name = "WEST BENGAL BOARD OF MADRASAH EDUCATION, WEST BENGAL"
                    break
                elif c1 == 58:
                    uni_boa_name = "CHHATTISGARH MADRASA BOARD, CHHATTISGARH"
                    break
                elif c1 == 59:
                    uni_boa_name = "UTTARAKHAND MADRASA EDUCATION BOARD, UTTARAKHAND"
                    break
                elif c1 == 60:
                    uni_boa_name = "ALIGARH MUSLIM UNIVERSITY BOARD OF SECONDARY & SR.SECONDARY EDUCATION, UTTAR PARDESH"
                    break
                elif c1 == 61:
                    uni_boa_name = "INDIAN COUNCIL FOR HINDI & SANSKRIT EDUCATION, NEW DELHI"
                    break
                elif c1 == 62:
                    uni_boa_name = "DAYALBAGH EDUCATIONAL INSTITUTE, AGRA"
                    break
                elif c1 == 63:
                    uni_boa_name = "BANASTHALI VIDYAPITH P.O., RAJASTHAN"
                    break
                elif c1 == 64:
                    uni_boa_name = "BHUTAN COUNCIL FOR SCHOOL EXAMINATIONS & ASSESSMENT, BHUTAN"
                    break
                elif c1 == 65:
                    uni_boa_name = "CAMBRIDGE ASSESSMENT INTERNATIONAL EXAMINATIONS, UK"
                    break
                elif c1 == 66:
                    uni_boa_name = "CHHATTISGARH SANSKRIT BOARD, RAIPUR"
                    break
                elif c1 == 67:
                    uni_boa_name = "MAURITIUS EXAMINATION SYNDICATE, MAURITIUS"
                    break
                elif c1 == 68:
                    uni_boa_name = "NATIONAL EXAMINATIONS BOARD, NEPAL"
                    break
                elif c1 == 69:
                    uni_boa_name = "PEARSON EDEXCEL LTD., UK"
                    break
                elif c1 == 70:
                    uni_boa_name = "INTERNATIONAL BACCALAUREATE, GENEVA"
                    break
                elif c1 == 71:
                    uni_boa_name = "SINGHANIA UNIVERSITY BOARD OF SECONDARY & SENIOR SECONDARY EDUCATION, RAJASTHAN"
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

        while True:
            mat_name = input("\nEnter the name as given in Matriculation Certificate :")
            if mat_name.isalpha() is True and mat_name != '':
                break
            else:
                print(
                    "\n" + " " * 30 + "-----------------------------------------INVALID NAME-------------------------------------------")

        while True:
            today = date.today()
            p_year = int(input("\nEnter the year of passing :"))
            if p_year <= today.year and p_year != None:
                break
            else:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID YEAR OF PASSING--------------------------------------")
        pass_year = str(p_year)

        print("\nPress ENTER to continue the process...............................")
        print()
        j = input()

        time.sleep(2)

        print()
        print("PHYSICAL DETAILS :")
        print()

        while True:
            try:
                height = int(input("\nEnter your Height (in CM) :"))
                break
            except:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID ENTRY OF HEIGHT--------------------------------------")

        while True:
            try:
                chest = int(input("\nEnter your Chest Size (in CM) :"))
                break
            except:
                print(
                    "\n" + " " * 30 + "---------------------------------INVALID ENTRY OF CHEST SIZE------------------------------------")

        while True:
            try:
                weight = int(input("\nEnter your weight (in Kg) :"))
                break
            except:
                print(
                    "\n" + " " * 30 + "-----------------------------------INVALID ENTRY OF WEIGHT--------------------------------------")

        while True:
            p_cha = input("\nAre you physical challenged? (Y/N)")
            if p_cha in 'nN':
                phy_cha = "NO"
                break
            elif p_cha in 'yY':
                phy_cha = "YES"
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

        print()
        print("Press ENTER to see the result.........................")
        print()

        c = input()

        if 17 <= c_age <= 21:
            if spe_category == "Gorkha Nepalese and Indian Origin" and phy_cha == 'NO' and height >= 157 and chest >= 77 and weight >= 48:
                print(
                    "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
            if spe_category == "Settlers ( Andaman and Nicobar, Lakshadweep including Minicoy )" and phy_cha == 'NO' and height >= 165 and chest >= 77 and weight >= 50:
                print(
                    "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
            if spe_category == "Ladakhi" and phy_cha == 'NO' and height >= 157 and chest >= 77 and weight >= 50:
                print(
                    "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
            if spe_category == "Non Dispensation Category" and phy_cha == 'NO' and height >= 160 and chest >= 77 and weight >= 50:
                print(
                    "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
            if spe_category == "Locals of Andaman and Nicobar, Lakshadweep including Minicoy" and phy_cha == 'NO' and height >= 165 and chest >= 77 and weight >= 50:
                print(
                    "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
            if spe_category == "Tribals of Recognized Tribal Areas" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 48:
                print(
                    "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
            if spe_category == "Son of Army Personal" and phy_cha == 'NO' and height >= 173 and chest >= 77 and weight >= 50:
                print(
                    "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
            if spe_category == "Arunachal and Sikkim Scouts only" and phy_cha == 'NO' and height >= 170 and chest >= 77 and weight >= 50:
                print(
                    "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
            if spe_category == 'NO':
                if region == "Western Himalayas Region" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 48:
                    print(
                        "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
                if region == "Eastern Himalayas Region" and phy_cha == 'NO' and height >= 157 and chest >= 77 and weight >= 48:
                    print(
                        "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
                if region == "Western Plains Region" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 50:
                    print(
                        "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
                if region == "Eastern Plains Region" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 50:
                    print(
                        "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
                if region == "Central Region" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 50:
                    print(
                        "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
                if region == "Southern Region" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 50:
                    print(
                        "\n" + " " * 30 + "---------------------------------------YOU ARE ELIGIBLE-----------------------------------------")
                else:
                    print(
                        "\n" + " " * 30 + "-------------------------------------YOU ARE NOT ELIGIBLE---------------------------------------")
        else:
            print(
                "\n" + " " * 30 + "-------------------------------------YOU ARE NOT ELIGIBLE---------------------------------------")

        print()
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to Go Back")
        print(" " * 60 + "b. Enter 2 to Exit\n")
        print("=" * 150)

        while True:
            choose = int(input("Enter your option :"))

            if choose == 1:
                print("Are you sure to go back? (Y/N)")
                ch = input()
                if ch in "Yy":
                    agniipath.main(self)
                    break

            elif choose == 2:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # To search a registration entry
    def veiw_regis_profile(self):
        print(
            "=" * 150 + "\n" + " " * 41 + "*** View the Registrations of Agnipath  Yojana Entry Scheme ***\n" +
            "=" * 150 + "\n")
        while True:
            user = input("\nEnter the username of the registraion :")
            passwd = input("\nEnter the password of the registraion :")
            query = "SELECT Aadhar_No, Candidate_Name, Father_Name, Mother_Name, Date_Of_Birth, Candidate_Age, Gender, " \
                    "Nationality, Martial_Status, Email_Address, Mobile_No, Higher_Education, Matriculation_Board, Username," \
                    "Password, House_No, Address, Village, City_Town, State_Name_UT_Name, District, Region, Tensil, " \
                    "Block_Locality, Pin_No, Police_Station, Post_Office, Telegram_Office, Category, Sport, NCC, Special_Category, " \
                    "Highest_Education, Qualifying_Course, Board_Education_University, Name_of_the_University_Board, Name_in_Matriculation_Certificate, " \
                    "Year_Of_Passing, Roll_No, Certificate_No FROM new_enrollment WHERE Username = '%s' AND Password = '%s'" % (
                    user, passwd)

            cursor.execute(query)
            data = cursor.fetchone()

            if data is None:
                print(
                    "\n" + " " * 30 + "------------------------------------NO REGISTRATION WHERE FOUND---------------------------------")
                print()
                c = input("\nDo you want to search more? (Y/N)")
                if c in 'nN':
                    break
            else:
                print()
                print("The Information about the registered candidate are..........................")
                print()
                print()
                print(" " * 25 + "-" * 100)
                print()
                print(" " * 30 + "Aadhar_No                             :", data[0])
                print(" " * 30 + "Candidate_Name                        :", data[1])
                print(" " * 30 + "Father_Name                           :", data[2])
                print(" " * 30 + "Mother_Name                           :", data[3])
                print(" " * 30 + "Date_Of_Birth                         :", data[4])
                print(" " * 30 + "Candidate_Age                         :", data[5])
                print(" " * 30 + "Gender                                :", data[6])
                print(" " * 30 + "Nationality                           :", data[7])
                print(" " * 30 + "Martial_Status                        :", data[8])
                print(" " * 30 + "Email_Address                         :", data[9])
                print(" " * 30 + "Mobile_No                             :", data[10])
                print(" " * 30 + "Higher_Education                      :", data[11])
                print(" " * 30 + "Matriculation_Board                   :", data[12])
                print(" " * 30 + "Username                              :", data[13])
                print(" " * 30 + "Password                              :", data[14])
                print(" " * 30 + "House_No                              :", data[15])
                print(" " * 30 + "Address                               :", data[16])
                print(" " * 30 + "Village                               :", data[17])
                print(" " * 30 + "City_Town                             :", data[18])
                print(" " * 30 + "State_Name_UT_Name                    :", data[19])
                print(" " * 30 + "District                              :", data[20])
                print(" " * 30 + "Region                                :", data[21])
                print(" " * 30 + "Tensil                                :", data[22])
                print(" " * 30 + "Block_Locality                        :", data[23])
                print(" " * 30 + "Pin_No                                :", data[24])
                print(" " * 30 + "Police_Station                        :", data[25])
                print(" " * 30 + "Post_Office                           :", data[26])
                print(" " * 30 + "Telegram_Office                       :", data[27])
                print(" " * 30 + "Category                              :", data[28])
                print(" " * 30 + "Sport                                 :", data[29])
                print(" " * 30 + "NCC                                   :", data[30])
                print(" " * 30 + "Special_Category                      :", data[31])
                print(" " * 30 + "Highest_Education                     :", data[32])
                print(" " * 30 + "Qualifying_Course                     :", data[33])
                print(" " * 30 + "Board_Education_University            :", data[34])
                print(" " * 30 + "Name_of_the_University_Board          :", data[35])
                print(" " * 30 + "Name_in_Matriculation_Certificate     :", data[36])
                print(" " * 30 + "Year_Of_Passing                       :", data[37])
                print(" " * 30 + "Roll_No                               :", data[38])
                print(" " * 30 + "Certificate_No                        :", data[39])
                print()
                print(" " * 25 + "-" * 100)
                print()
                c = input("\nDo you want to search more? (Y/N)")
                if c in 'nN':
                    break
        print()
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to go back")
        print(" " * 60 + "b. Enter 2 to exit\n")
        print("=" * 150)
        print()
        while True:
            choose = int(input("Enter your choice :"))
            if choose == 1:
                ch = input("\nDo you like to go back? (Y/N)")
                if ch in 'Yy':
                    agniipath.main(self)
                    break
            elif choose == 2:
                agniipath.exit(self)
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # India Army welcome message
    def logo(self):
        print(
            """\n\n
  ------------------- ------------         -------- ------------------------ ------------------- --------------------- ------------         --------
  |                 | |           \        |      | |                      | |                 | |                   | |           \        |      |
  -------      ------ |     |\     \       |      | ----    ----------     | -------      ------ |     ---------     | |     |\     \       |      |
        |      |      |     | \     \      |      |    |    |        |     |       |      |      |     |       |     | |     | \     \      |      |
        |      |      |     |  \     \     |      |    |    |        |     |       |      |      |     |       |     | |     |  \     \     |      |
        |      |      |     |   \     \    |      |    |    |        |     |       |      |      |      -------      | |     |   \     \    |      |
        |      |      |     |    \     \   |      |    |    |        |     |       |      |      |                   | |     |    \     \   |      |
        |      |      |     |     \     \  |      |    |    |        |     |       |      |      |      -------      | |     |     \     \  |      |
        |      |      |     |      \     \ |      |    |    |        |     |       |      |      |      |     |      | |     |      \     \ |      |
  -------      ------ |     |       \     \|      | ----    ----------     | -------      ------ |      |     |      | |     |       \     \|      |
  |                 | |     |        \            | |                      | |                 | |      |     |      | |     |        \            |
  ------------------- -------         ------------- ------------------------ ------------------- --------     -------- -------         -------------

                                      ----------------- ------------------ ----------      ---------- ------        -------
                                      |               | |                | |         \    /         |  \    \      /     /
                                      |      ----     | |     ------     | |    |\    \  /    /|    |   \    \    /     /
                                      |      |  |     | |     |    |     | |    | \    \/    / |    |    \    \  /     /
                                      |      ----     | |     ------     | |    |  \        /  |    |     \    \/     /
                                      |               | |                | |    |   \      /   |    |      \         /
                                      |      ----     | |    |\    ------- |    |    ------    |    |       \       /
                                      |      |  |     | |    | \    \      |    |              |    |        |     |
                                      |      |  |     | |    |  \    \     |    |              |    |        |     |
                                      --------  ------- ------   ------    ------              ------        -------
            """)
        i = input()
        print(
            "\n" + "=" * 150 + "\n\n" + " " * 67 + "JOIN INDIAN ARMY\n" + " " * 65 + "-" * 21 + "\n" + " " * 65 +
            " GOVERNMENT OF INDIA\n\n" + "+" * 150 + "\n\n" + " " * 60 + "* Become an AGNIVEER\n" + " " * 60 +
            "* Join the Indian Army for 4 YEARS\n" + " " * 60 + "* Walk the AGNIPATH\n\n" + "=" * 150)
        enter = input("\nPress ENTER to begin......")
        print()

    def begin_test(self):
        print()
        print("\nPress ENTER to begin the test.....................")
        i = input()
        print()
        print("Please Wait loading the data.................\n\n")
        time.sleep(3)

        print("=" * 150 + "\n" + " " * 53 + "*** Test For Agnipath  Yojana Entry Scheme ***\n" + "=" * 150 + "\n")
        print(" " * 50 + "1. Enter the Candidate Result")
        print(" " * 50 + "2. See the Eligible candidate and end the section\n")
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 3 to go back")
        print(" " * 60 + "b. Enter 4 to exit\n")
        print("=" * 150)
        print()

        while True:
            try:
                choos = int(input("\nEnter your choice :"))
            except:
                print(
                    "\n" + " " * 30 + "------------------------------------------INVALID ENTRY-----------------------------------------")
            if choos == 1:
                agniipath.enter_test_result(self)
                break
            elif choos == 2:
                agniipath.eligible_candidate(self)
                break
            elif choos == 3:
                ch = input("\nDo you like to go back? (Y/N)")
                if ch in 'Yy':
                    agniipath.sub_main(self)
                    break
            elif choos == 4:
                agniipath.exit(self)
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    def eligible_candidate(self):
        print()
        print("Press ENTER to see all the eligible candidate for the Agnipath  Yojana Scheme........................")
        i = input()
        print()

        time.sleep(3)

        query = "SELECT * FROM new_enrollment WHERE Medical_Test = 'PASS' AND Physical_Test = 'PASS' AND Written_Test >= 40"

        cursor.execute(query)
        data = cursor.fetchall()

        if data == [] or data == ():
            print(
                "\n" + " " * 30 + "---------------------------------------NO ELIGIBLE CANDIDATE------------------------------------")
            print()
        else:
            print()
            print("All the candidate for the Agnipath  Yojana Scheme are..........................")
            print()
            print()
            r = 0
            for records in data:
                print(" " * 40 + "Candidate_Name                    :", records[4])
                print()
                r += 1
            print(' ' * 40 + 'Total no. of candidate are -------> ', r)
            connect.commit()
        print()
        print(
            "Press ENTER to copy the eligible candidate records to another table and delete the remaining records................")
        i = input()
        print()

        write_query = "INSERT INTO eligible_candidate SELECT * FROM new_enrollment WHERE Medical_Test = 'PASS' AND Physical_Test = 'PASS' AND Written_Test >= 40"
        drop_query = "DROP TABLE new_enrollment"

        cursor.execute(write_query)
        connect.commit()
        print()
        print("Records of the Eligible candidate has been successfully copied...........")

        cursor.execute(drop_query)
        connect.commit()
        print()
        print("Records of the remaining candidate has been successfully deleted............")

        print()
        print("Press ENTER to exit the Agnipath  Yojana Entry Scheme........................")
        i = input()
        agniipath.exit(self)

    def user(self):
        query8 = "SELECT username FROM admin_section"
        cursor.execute(query8)
        username = cursor.fetchone()
        user_name = list(username)
        return user_name

    def password(self):
        query8 = "SELECT password FROM admin_section"
        cursor.execute(query8)
        passwd = cursor.fetchone()
        password = list(passwd)
        return password

    # Forgot password
    def change_password(list):
        new_password_c = tuple(list)
        new_password = new_password_c[0]
        query10 = "UPDATE admin_section SET password = '%s'" % new_password
        cursor.execute(query10)
        connect.commit()
        print()
        print(
            "\n" + " " * 30 + "----------------------------------PASSWORD SUCCESSFULLY CHANGED---------------------------------")
        print()

    def forgot(self):
        print()
        while True:
            print("\nDo you remember your password? (Y/N)")
            c = input()
            if c in "Yy":
                agniipath.admin(self)
                break
            elif c in "Nn":
                while True:
                    user_name = agniipath.user(self=True)
                    user = input("\nEnter the user name : ")
                    if user == user_name[0]:
                        break
                    else:
                        print(
                            "\n" + " " * 30 + "---------------------------------PLEASE ENTER A VALID USERNAME----------------------------------")

                password = agniipath.password(self=True)
                new_password = input("\nEnter the new password :")
                if new_password == password[0]:
                    print(
                        "\n" + " " * 30 + "-------------------------------ITS THE ALREADY EXISTING PASSWORD--------------------------------")
                    while True:
                        ch = input("\nDo you like to change it? (Y/N)")
                        if ch in 'Nn':
                            agniipath.admin(self)
                            break
                        elif ch in 'Yy':
                            break
                        else:
                            print("\nOops!!!")
                            print("You have entered a wrong option......")
                            print("Please enter correctly.....\n")
                while True:
                    con_password = input("\nConfirm the password :")
                    if con_password == new_password:
                        break
                    else:
                        print(
                            "\n" + " " * 30 + "-----------------------------PLEASE ENTER THE PASSWORD CORRECTLY--------------------------------")
                # Changing the password
                password[0] = new_password
                agniipath.change_password(password)
                print("+" * 150 + "\n")
                agniipath.admin(self)
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Admin section
    def admin(self):
        while True:
            user_name = agniipath.user(self=True)
            user = input("\nEnter the user name : ")
            if user == user_name[0]:
                break
            else:
                print(
                    "\n" + " " * 30 + "---------------------------------PLEASE ENTER A VALID USERNAME----------------------------------")

        i = 0
        while i < 4:
            password = agniipath.password(self=True)
            passwd = input("\nEnter the password :")
            if passwd == password[0]:
                break
            else:
                print(
                    "\n" + " " * 30 + "-----------------------------PLEASE ENTER THE PASSWORD CORRECTLY--------------------------------")
                i += 1
        if i == 4:
            agniipath.forgot(self)

        print()
        print()
        print("Please wait loading the contents from the database.................................")
        print()
        print()
        time.sleep(8)
        agniipath.sub_main(self)

    def delete_regis(self):
        print(
            "=" * 150 + "\n" + " " * 40 + "*** Delete the Registrations of Agnipath  Yojana Entry Scheme ***\n" +
            "=" * 150 + "\n")
        while True:
            user = input("\nEnter the username of the registraion :")
            passwd = input("\nEnter the password of the registraion :")
            query = "DELETE FROM new_enrollment WHERE Username = '%s' AND Password = '%s'" % (user, passwd)
            cursor.execute(query)

            dec = cursor.rowcount

            if dec == 0:
                print(
                    "\n" + " " * 30 + "-----------------------NO REGISTRATION WITH SUCH USERNAME AND PASSWORD EXISTS-------------------")
                c = input("\nDo you want to delete more? (Y/N)")
                if c in 'nN':
                    break
            else:
                print(
                    "\n" + " " * 30 + "-----------------REGISTRATION WITH SUCH USERNAME AND PASSWORD DELETED SUCCESSFULLY--------------")
                c = input("\nDo you want to delete more? (Y/N)")
                if c in 'nN':
                    break
            print()
            print("+" * 150 + "\n")
            print(" " * 60 + "a. Enter 1 to go back")
            print(" " * 60 + "b. Enter 2 to exit\n")
            print("=" * 150)
            print()
            while True:
                choose = int(input("Enter your choice :"))
                if choose == 1:
                    ch = input("\nDo you like to go back? (Y/N)")
                    if ch in 'Yy':
                        agniipath.sub_main(self)
                        break
                elif choose == 2:
                    agniipath.exit(self)
                    break
                else:
                    print("\nOops!!!")
                    print("You have entered a wrong option......")
                    print("Please enter correctly.....\n")

    def sub_main(self):
        print("Welcome to Agnipath  Yojana Entry Scheme Admin section....................\n")
        print("Press ENTER to continue.................\n\n")
        inp = input()
        print("=" * 150 + "\n" + " " * 59 + "*** Agnipath  Yojana Entry Scheme ***\n" + "=" * 150 + "\n")
        print(" " * 50 + "1. View the current username and password of the admin section")
        print(" " * 50 + "2. Change the username of the admin section")
        print(" " * 50 + "3. Change the password of the admin section")
        print(" " * 50 + "4. View all the registrations")
        print(" " * 50 + "5. To search a entry from the registrations")
        print(" " * 50 + "6. To delete an entry from the registration")
        print(" " * 50 + "7. To sort out the list from the registration and begin the test\n")
        print("+" * 150 + "\n")
        print(" " * 50 + "a. Enter 8 to go back")
        print(" " * 50 + "b. Enter 9 to exit\n")
        print("=" * 150)
        print()
        while True:
            choose = int(input("Enter your choice :"))
            if choose == 1:
                agniipath.view(self)
                break
            elif choose == 2:
                agniipath.change_user_name(self)
                break
            elif choose == 3:
                agniipath.change_admin_password(self)
                break
            elif choose == 4:
                agniipath.view_all_entry(self)
                break
            elif choose == 5:
                agniipath.search_regis(self)
                break
            elif choose == 6:
                agniipath.delete_regis(self)
                break
            elif choose == 7:
                agniipath.begin_test(self)
                break
            elif choose == 8:
                while True:
                    ch = input("Do you like to go back? (Y/N)")
                    if ch in 'Nn':
                        agniipath.sub_main(self)
                        break
                    elif ch in 'Yy':
                        agniipath.main(self)
                        break
                    else:
                        print("\nOops!!!")
                        print("You have entered a wrong option......")
                        print("Please enter correctly.....\n")
            elif choose == 9:
                agniipath.exit(self)
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # To search a registration entry
    def search_regis(self):
        print(
            "=" * 150 + "\n" + " " * 40 + "*** Search the Registrations of Agnipath  Yojana Entry Scheme ***\n" +
            "=" * 150 + "\n")
        while True:
            user = input("\nEnter the username of the registraion :")
            passwd = input("\nEnter the password of the registraion :")
            query = "SELECT Aadhar_No, Candidate_Name, Father_Name, Mother_Name, Date_Of_Birth, Candidate_Age, Gender, " \
                    "Nationality, Martial_Status, Email_Address, Mobile_No, Higher_Education, Matriculation_Board, Username," \
                    "Password, House_No, Address, Village, City_Town, State_Name_UT_Name, District, Region, Tensil, " \
                    "Block_Locality, Pin_No, Police_Station, Post_Office, Telegram_Office, Category, Sport, NCC, Special_Category, " \
                    "Highest_Education, Qualifying_Course, Board_Education_University, Name_of_the_University_Board, Name_in_Matriculation_Certificate, " \
                    "Year_Of_Passing, Roll_No, Certificate_No FROM new_enrollment WHERE Username = '%s' AND Password = '%s'" % (
                        user, passwd)
            cursor.execute(query)
            data = cursor.fetchone()

            if data is None:
                print(
                    "\n" + " " * 30 + "------------------------------------NO REGISTRATION WHERE FOUND---------------------------------")
                print()
                c = input("\nDo you want to search more? (Y/N)")
                if c in 'nN':
                    break
            else:
                print()
                print("The Information about the registered candidate are..........................")
                print()
                print()
                print(" " * 25 + "-" * 100)
                print()
                print(" " * 30 + "Aadhar_No                             :", data[0])
                print(" " * 30 + "Candidate_Name                        :", data[1])
                print(" " * 30 + "Father_Name                           :", data[2])
                print(" " * 30 + "Mother_Name                           :", data[3])
                print(" " * 30 + "Date_Of_Birth                         :", data[4])
                print(" " * 30 + "Candidate_Age                         :", data[5])
                print(" " * 30 + "Gender                                :", data[6])
                print(" " * 30 + "Nationality                           :", data[7])
                print(" " * 30 + "Martial_Status                        :", data[8])
                print(" " * 30 + "Email_Address                         :", data[9])
                print(" " * 30 + "Mobile_No                             :", data[10])
                print(" " * 30 + "Higher_Education                      :", data[11])
                print(" " * 30 + "Matriculation_Board                   :", data[12])
                print(" " * 30 + "Username                              :", data[13])
                print(" " * 30 + "Password                              :", data[14])
                print(" " * 30 + "House_No                              :", data[15])
                print(" " * 30 + "Address                               :", data[16])
                print(" " * 30 + "Village                               :", data[17])
                print(" " * 30 + "City_Town                             :", data[18])
                print(" " * 30 + "State_Name_UT_Name                    :", data[19])
                print(" " * 30 + "District                              :", data[20])
                print(" " * 30 + "Region                                :", data[21])
                print(" " * 30 + "Tensil                                :", data[22])
                print(" " * 30 + "Block_Locality                        :", data[23])
                print(" " * 30 + "Pin_No                                :", data[24])
                print(" " * 30 + "Police_Station                        :", data[25])
                print(" " * 30 + "Post_Office                           :", data[26])
                print(" " * 30 + "Telegram_Office                       :", data[27])
                print(" " * 30 + "Category                              :", data[28])
                print(" " * 30 + "Sport                                 :", data[29])
                print(" " * 30 + "NCC                                   :", data[30])
                print(" " * 30 + "Special_Category                      :", data[31])
                print(" " * 30 + "Highest_Education                     :", data[32])
                print(" " * 30 + "Qualifying_Course                     :", data[33])
                print(" " * 30 + "Board_Education_University            :", data[34])
                print(" " * 30 + "Name_of_the_University_Board          :", data[35])
                print(" " * 30 + "Name_in_Matriculation_Certificate     :", data[36])
                print(" " * 30 + "Year_Of_Passing                       :", data[37])
                print(" " * 30 + "Roll_No                               :", data[38])
                print(" " * 30 + "Certificate_No                        :", data[39])
                print()
                print(" " * 25 + "-" * 100)
                print()
                c = input("\nDo you want to search more? (Y/N)")
                if c in 'nN':
                    break
        print()
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to go back")
        print(" " * 60 + "b. Enter 2 to exit\n")
        print("=" * 150)
        print()
        while True:
            choose = int(input("Enter your choice :"))
            if choose == 1:
                ch = input("\nDo you like to go back? (Y/N)")
                if ch in 'Yy':
                    agniipath.sub_main(self)
                    break
            elif choose == 2:
                agniipath.exit(self)
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    def view_all_entry(self):
        query = "SELECT Candidate_Name FROM new_enrollment"
        cursor.execute(query)
        data = cursor.fetchall()
        if data == [] or data == ():
            print(
                "\n" + " " * 30 + "------------------------------------NO REGISTRATION WHERE FOUND---------------------------------")
            print()
        else:
            print()
            print("All the registrations available in the database are..........................")
            print()
            print()
            r = 0
            for records in data:
                print(" " * 40 + "Candidate_Name                    :", records[0])
                print()
                r += 1
            print(' ' * 40 + 'Total no. of registrations are -------> ', r)
            connect.commit()
        print()
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to go back")
        print(" " * 60 + "b. Enter 2 to exit\n")
        print("=" * 150)
        print()
        while True:
            choose = int(input("Enter your choice :"))
            if choose == 1:
                ch = input("\nDo you like to go back? (Y/N)")
                if ch in 'Yy':
                    agniipath.sub_main(self)
                    break
            elif choose == 2:
                agniipath.exit(self)
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Information about the current username and password
    def view(self):
        print("=" * 150 + "\n" + " " * 55 + "*** The current username and password ***\n" + "=" * 150 + "\n")
        print()
        print(" " * 50 + "The username :", agniipath.user(self))
        print()
        print(" " * 50 + "The password :", agniipath.password(self))
        print()
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to go back")
        print(" " * 60 + "b. Enter 2 to exit\n")
        print("=" * 150)
        print()
        while True:
            choose = int(input("Enter your choice :"))
            if choose == 1:
                ch = input("Do you like to go back? (Y/N)")
                if ch in 'Yy':
                    agniipath.sub_main(self)
                    break
            elif choose == 2:
                agniipath.exit(self)
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    def change_user(list):
        new_user = list[0]
        query = "UPDATE admin_section SET username = '%s'" % new_user
        cursor.execute(query)
        connect.commit()
        print(
            "\n" + " " * 30 + "----------------------------------USERNAME SUCCESSFULLY CHANGED---------------------------------")

    # Change the username
    def change_user_name(self):
        while True:
            ch = input("\nDo you want to change the username? (Y/N)\n")
            if ch in 'Yy':
                new_user = input("\nEnter the new user name :")
                l_new_user = [new_user]
                extract_old_user = agniipath.user(self)
                o_s_n = extract_old_user[0]
                old_user = str(o_s_n)
                if new_user == old_user:
                    print(
                        "\n" + " " * 30 + "-------------------------------ITS THE ALREADY EXISTING USERNAME--------------------------------")
                    while True:
                        ch = input("Do you like to change it? (Y/N)")
                        if ch in 'Nn':
                            agniipath.sub_main(self)
                            break
                        elif ch in 'Yy':
                            break
                        else:
                            print("\nOops!!!")
                            print("You have entered a wrong option......")
                            print("Please enter correctly.....\n")
                while True:
                    con_user = input("\nConfirm the username :")
                    if con_user == new_user:
                        break
                    else:
                        print(
                            "\n" + " " * 30 + "-----------------------------PLEASE ENTER THE USERNAME CORRECTLY--------------------------------")
                # Changing the username
                agniipath.change_user(l_new_user)
                print()
                print("+" * 150 + "\n")
                print(" " * 60 + "a. Enter 1 to go back")
                print(" " * 60 + "b. Enter 2 to exit\n")
                print("+" * 150)
                print()
                while True:
                    choose = int(input("Enter your choice :"))
                    if choose == 1:
                        ch = input("\nDo you like to go back? (Y/N)")
                        if ch in 'Yy':
                            agniipath.sub_main(self)
                            break
                    elif choose == 2:
                        agniipath.exit(self)
                        break
                    else:
                        print("\nOops!!!")
                        print("You have entered a wrong option......")
                        print("Please enter correctly.....\n")
            if ch in 'Nn':
                agniipath.sub_main(self)
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # Change the password
    def change_admin_password(self):
        while True:
            ch = input("\nDo you want to change the password? (Y/N)\n")
            if ch in 'Yy':
                new_password = input("\nEnter the new password :")
                l_new_password = [new_password]
                extract_old_password = agniipath.password(self)
                o_p = extract_old_password[0]
                old_password = str(o_p)
                if new_password == old_password:
                    print(
                        "\n" + " " * 30 + "-------------------------------ITS THE ALREADY EXISTING PASSWORD--------------------------------")
                    while True:
                        ch = input("Do you like to change it? (Y/N)")
                        if ch in 'Nn':
                            agniipath.sub_main(self)
                            break
                        elif ch in 'Yy':
                            break
                        else:
                            print("\nOops!!!")
                            print("You have entered a wrong option......")
                            print("Please enter correctly.....\n")
                while True:
                    con_password = input("\nConfirm the username :")
                    if con_password == new_password:
                        break
                    else:
                        print(
                            "\n" + " " * 30 + "-----------------------------PLEASE ENTER THE PASSWORD CORRECTLY--------------------------------")
                # Changing the username
                agniipath.change_password(l_new_password)
                print()
                print("+" * 150 + "\n")
                print(" " * 60 + "a. Enter 1 to go back")
                print(" " * 60 + "b. Enter 2 to exit\n")
                print("+" * 150)
                print()
                while True:
                    choose = int(input("Enter your choice :"))
                    if choose == 1:
                        ch = input("\nDo you like to go back? (Y/N)")
                        if ch in 'Yy':
                            agniipath.sub_main(self)
                            break
                    elif choose == 2:
                        agniipath.exit(self)
                        break
                    else:
                        print("\nOops!!!")
                        print("You have entered a wrong option......")
                        print("Please enter correctly.....\n")
            if ch in 'Nn':
                agniipath.sub_main(self)
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    def enter_test_result(self):
        physical_test = None
        medical_test = None
        while True:
            print(
                "=" * 150 + "\n" + " " * 42 + "*** Entering the Result for Agnipath  Yojana Entry Scheme ***\n" +
                "=" * 150 + "\n")
            user = input("\nEnter the username of the registraion :")
            passwd = input("\nEnter the password of the registraion :")
            query = "SELECT *" \
                    "FROM new_enrollment WHERE Username = '%s' AND Password = '%s'" % (user, passwd)
            cursor.execute(query)
            data = cursor.fetchone()

            if data is None:
                print(
                    "\n" + " " * 30 + "-----------------------NO REGISTRATION WITH SUCH USERNAME AND PASSWORD EXISTS-------------------")
                c = input("\nDo you want to enter more result? (Y/N)")
                print()
                if c in 'nN':
                    print()
                    break

            else:
                print()
                print("The Information about the registered candidate are..........................")
                print()
                print(" " * 40 + "Candidate_Name    :", data[4])
                print(" " * 40 + "Father_Name       :", data[6])
                print(" " * 40 + "Mother_Name       :", data[7])
                print()
                print("Press ENTER to continue.....................")
                i = input()
                print()
                spe_category = data[31]
                region = data[1]
                c_age = data[9]

                while True:
                    medical = input("\nEnter the result of the Medical Test(P/F) :")
                    if medical.isalpha() == True and medical in 'pP':
                        medical_test = 'PASS'
                        break
                    elif medical.isalpha() == True and medical in 'fF':
                        medical_test = 'FAIL'
                        break
                    else:
                        print("\nOops!!!")
                        print("You have entered a wrong option......")
                        print("Please enter correctly.....\n")

                while True:
                    try:
                        written_test = int(input("\nEnter the marks for the written test :"))
                        break
                    except:
                        print(
                            "\n" + " " * 30 + "-----------------------------------INVALID ENTRY OF MARK---------------------------------------")

                print()
                print("PHYSICAL DETAILS :")
                print()

                while True:
                    try:
                        height = int(input("\nEnter your Height (in CM) :"))
                        break
                    except:
                        print(
                            "\n" + " " * 30 + "-----------------------------------INVALID ENTRY OF HEIGHT--------------------------------------")

                while True:
                    try:
                        chest = int(input("\nEnter your Chest Size (in CM) :"))
                        break
                    except:
                        print(
                            "\n" + " " * 30 + "---------------------------------INVALID ENTRY OF CHEST SIZE------------------------------------")

                while True:
                    try:
                        weight = int(input("\nEnter your weight (in Kg) :"))
                        break
                    except:
                        print(
                            "\n" + " " * 30 + "-----------------------------------INVALID ENTRY OF WEIGHT--------------------------------------")

                while True:
                    p_cha = input("\nAre you physical challenged? (Y/N)")
                    if p_cha in 'nN':
                        phy_cha = "NO"
                        break
                    elif p_cha in 'yY':
                        phy_cha = "YES"
                        break
                    else:
                        print("\nOops!!!")
                        print("You have entered a wrong option......")
                        print("Please enter correctly.....\n")

                if 17 <= c_age <= 21:
                    if spe_category == "Gorkha Nepalese and Indian Origin" and phy_cha == 'NO' and height >= 157 and chest >= 77 and weight >= 48:
                        physical_test = 'PASS'
                    if spe_category == "Settlers ( Andaman and Nicobar, Lakshadweep including Minicoy )" and phy_cha == 'NO' and height >= 165 and chest >= 77 and weight >= 50:
                        physical_test = 'PASS'
                    if spe_category == "Ladakhi" and phy_cha == 'NO' and height >= 157 and chest >= 77 and weight >= 50:
                        physical_test = 'PASS'
                    if spe_category == "Non Dispensation Category" and phy_cha == 'NO' and height >= 160 and chest >= 77 and weight >= 50:
                        physical_test = 'PASS'
                    if spe_category == "Locals of Andaman and Nicobar, Lakshadweep including Minicoy" and phy_cha == 'NO' and height >= 165 and chest >= 77 and weight >= 50:
                        physical_test = 'PASS'
                    if spe_category == "Tribals of Recognized Tribal Areas" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 48:
                        physical_test = 'PASS'
                    if spe_category == "Son of Army Personal" and phy_cha == 'NO' and height >= 173 and chest >= 77 and weight >= 50:
                        physical_test = 'PASS'
                    if spe_category == "Arunachal and Sikkim Scouts only" and phy_cha == 'NO' and height >= 170 and chest >= 77 and weight >= 50:
                        physical_test = 'PASS'
                    if spe_category == 'NO':
                        if region == "Western Himalayas Region" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 48:
                            physical_test = 'PASS'
                        if region == "Eastern Himalayas Region" and phy_cha == 'NO' and height >= 157 and chest >= 77 and weight >= 48:
                            physical_test = 'PASS'
                        if region == "Western Plains Region" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 50:
                            physical_test = 'PASS'
                        if region == "Eastern Plains Region" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 50:
                            physical_test = 'PASS'
                        if region == "Central Region" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 50:
                            physical_test = 'PASS'
                        if region == "Southern Region" and phy_cha == 'NO' and height >= 162 and chest >= 77 and weight >= 50:
                            physical_test = 'PASS'
                        else:
                            physical_test = 'FAIL'
                else:
                    physical_test = 'FAIL'

                print()
                print("Press ENTER to Save the Result..............................")
                j = input()

                query = "UPDATE new_enrollment SET Medical_Test = '%s', Physical_Test = '%s', Written_Test = %s WHERE Username = '%s' AND Password = '%s'" % (
                medical_test, physical_test, written_test, user, passwd)
                cursor.execute(query)
                connect.commit()
                print(
                    "\n" + " " * 30 + "------------------------------------RESULT SAVED SUCCESSFULLY-----------------------------------")
                print()

                c = input("\nDo you want to enter more result? (Y/N)")
                if c in 'nN':
                    break

        print()
        print("+" * 150 + "\n")
        print(" " * 60 + "a. Enter 1 to go back")
        print(" " * 60 + "b. Enter 2 to exit\n")
        print("=" * 150)
        print()
        while True:
            choose = int(input("Enter your choice :"))
            if choose == 1:
                ch = input("\nDo you like to go back? (Y/N)")
                if ch in 'Yy':
                    agniipath.begin_test(self)
                    break
            elif choose == 2:
                agniipath.exit(self)
                break
            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")

    # First main screen
    def main(self):
        while True:
            print("=" * 150 + "\n" + " " * 59 + "*** Agnipath  Yojana Entry Scheme ***\n" + "=" * 150 + "\n")
            print(" " * 65 + "1. New Enrollment")
            print(" " * 65 + "2. Admin Section")
            print(" " * 65 + "3. Checking for Eligibility")
            print(" " * 65 + "4. Search your registration")
            print(" " * 65 + "5. About Agniveer Enrolment")
            print(" " * 65 + "6. About the Indian Army")
            print(" " * 65 + "7. Life in Army")
            print(" " * 65 + "8. Exit\n")
            print("=" * 150)

            choose = int(input("\nEnter the option :"))

            if choose == 1:
                agniipath.new_enrollment(self)
                break

            elif choose == 2:
                agniipath.admin(self)
                break

            elif choose == 3:
                agniipath.check(self)
                break

            elif choose == 4:
                agniipath.veiw_regis_profile(self)
                break

            elif choose == 5:
                agniipath.about(self)
                break

            elif choose == 6:
                agniipath.india(self)
                break

            elif choose == 7:
                agniipath.life(self)
                break

            elif choose == 8:
                agniipath.exit(self)
                break

            else:
                print("\nOops!!!")
                print("You have entered a wrong option......")
                print("Please enter correctly.....\n")


agniipath.use_database(self=True)
agniipath.create_admin_user_passwd(self=True)
agniipath.create_table(self=True)
agniipath.logo(self=True)
agniipath.main(self=True)

# END OF THE PROJECT