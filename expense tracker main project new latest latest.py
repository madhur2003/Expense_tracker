# EXPENSE TRACKER

#==========================================================#
                    #EXPENSE TRACKER#
#==========================================================#

import mysql.connector
mydb=mysql.connector.connect(host = "localhost",
                             user = "root",
                             passwd = "root",
                             db="test",
                             buffered = True)

mycursor1=mydb.cursor()
mycursor2=mydb.cursor()
mycursor3=mydb.cursor()
mycursor4=mydb.cursor()
mycursor5=mydb.cursor()

print("███████╗██╗░░██╗██████╗░███████╗███╗░░██╗░██████╗███████╗  ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░")
print("██╔════╝╚██╗██╔╝██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗")
print("█████╗░░░╚███╔╝░██████╔╝█████╗░░██╔██╗██║╚█████╗░█████╗░░  ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝")
print("██╔══╝░░░██╔██╗░██╔═══╝░██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░  ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗")
print("███████╗██╔╝╚██╗██║░░░░░███████╗██║░╚███║██████╔╝███████╗  ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║")
print("╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")

class expense_tracker():   
    
    def __init__(self):
        self.monthly_salary=0
        self.grocery=0
        self.vehicle_expense=0
        self.recreation=0
        self.utilities=0
        self.extras=0
    
    def check_module(self):
        print("============================================================================================")
        print("Welcome to the expense tracker")
        print("Press y for yes and n for no")
        print("Enter new details: ")
        print("y if yes and n if no")
        print("============================================================================================")
        self.check=input("Enter your choice:")
        if self.check=='y':
            print("1. Enter details of 1st 15 days table")
            print("2. Enter details of 2nd 15 days table")
            self.choice6=int(input("Enter your choice: "))
            if self.choice6==1:
                self.amount_spent_1st_15()
            elif self.choice6==2:
                self.amount_spent_2nd_15()
            else:
                print("Please enter valid input")
                self.check_module() 
        elif self.check=='n':
            print("Please enter valid input")
            self.main_menu()
    
    #create two tables 1st_15days and 2nd_15days
    #"create table 1st_15days(month varchar(15) primary key not null, monthly_income varchar(7), grocery varchar(7), recreation varchar(7), utilities varchar(7), extras varchar(7)
    #"create table 2nd_15days(month varchar(15) primary key not null, monthly_income varchar(7), grocery varchar(7), recreation varchar(7), utilities varchar(7), extras varchar(7)
   
    def amount_spent_1st_15(self):
        print("============================================================================================")
        print("Enter for 1st 15 days")
        print("Enter the amount spent on weekly basis:")
        print("The order is")
        print("1.Enter the month")
        print("2.monthly_income")
        print("3.grocery")
        print("4.vehicle_expense")
        print("5.recreations")
        print("Recreations include sports, movies, etc.")
        print("6.utilities")
        print("Utilities include bills paid for power, water, telephone, etc.")
        print("7.extras")
        print("Extras include food outside, parities, clothings, etc.")
        print("============================================================================================")
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            db="test")
        
        self.month=input("Enter the month:")
        self.monthly_salary=int(input("Enter monthly salary in AED:"))
        self.grocery=int(input("Enter money spent on grocery in 1st 15 days:"))
        self.vehicle_expense=int(input("Enter money spent on vehicle_expense in 1st 15 days"))
        self.recreation=int(input("Enter money spent on recreation in 1st 15 days:"))
        self.utilities=int(input("Enter money spent on utilties in 1st 15 days:"))
        self.extras=int(input("Enter money spent on extras in 1st 15 days:"))
        
        command = "insert into 1st_15days(month, monthly_income, grocery, vehicle_expense, recreation, utilities, extras) values(%s, %s, %s, %s, %s, %s, %s);"
        values=[self.month, self.monthly_salary, self.grocery, self.vehicle_expense, self.recreation, self.utilities, self.extras]
       
        mycursor1=mydb.cursor()
        mycursor1.execute(command, values)
        mydb.commit()  
        mycursor1.execute("select * from 1st_15days")
        print("Here is the amount you spent in 1st 15days")
        for i in mycursor1:
            print(i)
        print("============================================================================================")
        print("1. Enter details of 2nd 15 days table")
        print("2. Proceed to main menu")
        print("============================================================================================") 
        self.choice7=int(input("Enter your choice: "))
        if self.choice7==1:
             self.amount_spent_2nd_15()
        elif self.choice7==2:
            self.main_menu()
        else:
            print("Since you inputed invalid input, you will proceed to enter amount spent in 2nd 15 days")
            self.amount_spent_2nd_15()
        
    def amount_spent_2nd_15(self):
        print("============================================================================================")
        print("Enter for 2nd 15 days")
        print("Enter the amount spent on weekly basis:")
        print("The order is")
        print("1.monthly_income")
        print("2.grocery")
        print("3.vehicle_expense")
        print("4.recreations")
        print("Recreations include sports, movies, etc.")
        print("5.utilities")
        print("Utilities include bills paid for power, water, telephone, etc.")
        print("6.extras")
        print("Extras include food outside, parities, clothings, etc.")
        print("============================================================================================")
        self.month=input("Enter the month:")
        self.monthly_salary1=int(input("Enter monthly salary in AED:"))
        self.grocery1=int(input("Enter money spent on grocery in next 15 days:"))
        self.vehicle_expense1=int(input("Enter money spent on vehicle_expense in next 15 days:"))
        self.recreation1=int(input("Enter money spent on recreation in next 15 days:"))
        self.utilities1=int(input("Enter money spent on utilties in next 15 days:"))
        self.extras1=int(input("Enter money spent on extras in next 15 days:"))
        command = "insert into 2nd_15days(month, monthly_income, grocery, vehicle_expense, recreation, utilities, extras) values(%s, %s, %s, %s, %s, %s, %s);"
        values=[self.month, self.monthly_salary1, self.grocery1, self.vehicle_expense1, self.recreation1, self.utilities1, self.extras1]
        mycursor2.execute(command, values)
        mydb.commit()
        mycursor2.execute("select * from 2nd_15days;")
        print("Here is the amount you spent in next 15days")
        for j in mycursor2:
            print(j)
        self.main_menu()
        
    def main_menu(self):
        print("============================================================================================")
        print("Select your preferred option")
        print("1. Edit Enrollments")
        print("2. Display Details")
        print("3. Details of month were specified expense are maximum")
        print("4. Amount spent and saved")
        print("The information for 4th choice is about the information you have just entered")
        print("5. Delete information")
        print("6. Tips to save money")
        print("7. Input new values again")
        print("8. Exit")
        print("============================================================================================")
        self.choice=int(input("Enter the your preferred choice:"))
        if self.choice==1:
             self.edit_details()
        elif self.choice==2:
             self.display_details()
        elif self.choice==3:
             self.higher_prices()
        elif self.choice==4:
             self.amount_spent_saved()
        elif self.choice==5:
             self.delete_information()
        elif self.choice==6:
             self.saving_tips()
        elif self.choice==7:
            self.check_module()
        elif self.choice==8:
             self.exit_over()
        else:
            print("Please enter from the valid choices")
            self.main_menu()
            
    def edit_details(self):
        print("============================================================================================")
        print("███████╗██████╗░██╗████████╗  ██████╗░███████╗████████╗░█████╗░██╗██╗░░░░░░██████╗")
        print("██╔════╝██╔══██╗██║╚══██╔══╝  ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║██║░░░░░██╔════╝")
        print("█████╗░░██║░░██║██║░░░██║░░░  ██║░░██║█████╗░░░░░██║░░░███████║██║██║░░░░░╚█████╗░")
        print("██╔══╝░░██║░░██║██║░░░██║░░░  ██║░░██║██╔══╝░░░░░██║░░░██╔══██║██║██║░░░░░░╚═══██╗")
        print("███████╗██████╔╝██║░░░██║░░░  ██████╔╝███████╗░░░██║░░░██║░░██║██║███████╗██████╔╝")
        print("╚══════╝╚═════╝░╚═╝░░░╚═╝░░░  ╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚══════╝╚═════╝░")
        print("You may edit the desired details")
        print("1.Edit monthly_income")
        print("2.Edit grocery")
        print("3.Edit vehicle_expense")
        print("4.Edit recreations")
        print("Recreations include sports, movies, etc.")
        print("5.Edit utilities")
        print("Utilities include bills paid for power, water, telephone, etc.")
        print("6.Edit extras")
        print("Extras include food outside, parities, clothings, etc.")
        print("============================================================================================")
        self.edit_choice=int(input("Enter the field to be edited:"))
        print("Select the table where you want to make changes")
        print("1. 1st_15days, 2.2nd_15days, 3.Main_menu")
        self.option1=int(input("Enter your choice:"))
        if self.option1==1:
            self.edit_details_1st()
        elif self.option1==2:
            self.edit_details_2nd()
        elif self.option1==3:
            self.main_menu()
        else:
            print("Please enter from the valid choices")
            self.edit_details()
    
    def edit_details_1st(self):
        print("============================================================================================")
        print("Select the option which you want to edit")
        print("1. Edit monthly_income")
        print("2. Edit grocery")
        print("3. Edit vehicle_expense")
        print("4. Edit recreations")
        print("5. Edit utilities")
        print("6. Edit extras")
        print("7. Edit details of 2nd 15 days")
        print("8. Back to main_menu")
        print("============================================================================================")
        self.option2=int(input("Enter you choice:"))
       
        if self.option2==1:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month1=input("Enter the month for which the details have to be edited")
            self.monthly_income_1=int(input("Enter the new amount in AED:"))
            command = "update 1st_15days set monthly_income=%s where month=%s"
            values=[self.monthly_income_1, self.month1]
            mycursor3.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_1st()
            
        elif self.option2==2:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month1=input("Enter the month for which the details have to be edited")
            self.grocery_1=int(input("Enter the new amount in AED:"))
            command = "update 1st_15days set grocery=%s where month=%s"
            values=[self.grocery_1, self.month1]
            mycursor3.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_1st()
            
        elif self.option2==3:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month1=input("Enter the month for which the details have to be edited")
            self.vehicle_expense_1=int(input("Enter the new amount in AED:"))
            command = "update 1st_15days set vehicle_expense=%s where month=%s"
            values=[self.vehicle_expense_1, self.month1]
            mycursor3.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_1st()
            
        elif self.option2==4:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month1=input("Enter the month for which the details have to be edited")
            self.recreation_1=int(input("Enter the new amount in AED:"))
            command = "update 1st_15days set recreation=%s where month=%s"
            values=[self.recreation_1, self.month1]
            mycursor3.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_1st()
            
        elif self.option2==5:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month1=input("Enter the month for which the details have to be edited")
            self.utilities_1=int(input("Enter new amount in AED:"))
            command = "update 1st_15days set utilities=%s where month=%s"
            values=[self.utilities_1, self.month1]
            mycursor3.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_1st()
            
        elif self.option2==6:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month1=input("Enter the month for which the details have to be edited")
            self.extras_1=int(input("Enter the new amount in AED:"))
            command = "update 1st_15days set extras=%s where month=%s"
            values=[self.extras_1, self.month1]
            mycursor3.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_1st()
            
        elif self.option2==7:
            self.edit_details_2nd()
            
        elif self.option2==8:
            self.main_menu()
        else:
            print("Please enter from the valid choices")
            self.edit_details_1st()
        

    def edit_details_2nd(self):
        print("============================================================================================")
        print("Select the option which you want to edit")
        print("1. Edit monthly_income")
        print("2. Edit grocery")
        print("3. Edit vehicle_expense")
        print("4. Edit recreations")
        print("5. Edit utilities")
        print("6. Edit extras")
        print("7. Back to main_menu")
        self.option3=int(input("Enter you choice:"))
        print("============================================================================================")
       
        if self.option3==1:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month2=input("Enter the month for which the details have to be edited: ")
            self.monthly_income_2=int(input("Enter the new amount in AED: "))
            command = "update 1st_15days set monthly_income=%s where month=%s"
            values=[self.monthly_income_2, self.month2]
            mycursor4.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_2nd()
            
        elif self.option3==2:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month2=input("Enter the month for which the details have to be edited: ")
            self.grocery_1=int(input("Enter the new amount in AED: "))
            command = "update 1st_15days set grocery=%s where month=%s"
            values=[self.grocery_2, self.month2]
            mycursor4.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_2nd()
            
        elif self.option3==3:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month2=input("Enter the month for which the details have to be edited: ")
            self.vehicle_expense_2=int(input("Enter the new amount in AED: "))
            command = "update 1st_15days set vehicle_expense=%s where month=%s"
            values=[self.vehicle_expense_2, self.month2]
            mycursor4.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_2nd()
            
        elif self.option3==4:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month2=input("Enter the month for which the details have to be edited")
            self.recreation_2=int(input("Enter the new amount in AED:"))
            command = "update 1st_15days set recreation=%s where month=%s"
            values=[self.recreation_2, self.month2]
            mycursor4.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_2nd()
            
        elif self.option3==5:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month2=input("Enter the month for which the details have to be edited: ")
            self.utilities_2=int(input("Enter new amount in AED: "))
            command = "update 1st_15days set utilities=%s where month=%s"
            values=[self.utilities_2, self.month2]
            mycursor4.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_2nd()
            
        elif self.option3==6:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month2=input("Enter the month for which the details have to be edited: ")
            self.extras_2=int(input("Enter the new amount in AED: "))
            command = "update 1st_15days set extras=%s where month=%s"
            values=[self.extras_2, self.month2]
            mycursor3.execute(command, values)
            mydb.commit()
            print("Information successfully updated")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.edit_details_2nd()
            
        elif self.option3==7:
            self.main_menu()
        else:
            print("Please enter from the valid choices")
            self.edit_details_2nd()

    def display_details(self):
        print("============================================================================================")
        print("██████╗░███████╗████████╗░█████╗░██╗██╗░░░░░░██████╗")
        print("██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║██║░░░░░██╔════╝")
        print("██║░░██║█████╗░░░░░██║░░░███████║██║██║░░░░░╚█████╗░")
        print("██║░░██║██╔══╝░░░░░██║░░░██╔══██║██║██║░░░░░░╚═══██╗")
        print("██████╔╝███████╗░░░██║░░░██║░░██║██║███████╗██████╔╝")
        print("╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚══════╝╚═════╝░")
        print("Select your preferred option:")
        print("1. Details of 1st 15 days table")
        print("2. Details of 2nd 15 days table")
        print("3. Return to main_menu")
        self.choice4=int(input("Select your choice:"))
        print("============================================================================================")
        
        if self.choice4==1:

            self.month4=input("Enter month for which you would like to see the statics")
            command="select * from 1st_15days where month=%s"
            values=[self.month4]
            mycursor5.execute(command, values)
            mydb.commit()
            for a in mycursor5:
                print(a)
            self.display_details()

            
        elif self.choice4==2:
            self.month5=input("Enter month fro which you would like to see the statics")
            command="select * from 2nd_15days where month=%s"
            values=[self.month5]
            mycursor5.execute(command, values)
            mydb.commit()
            for b in mycursor5:
                print(b)
            self.display_details()

            
        elif self.choice4==3:
            self.main_menu()
            
        else:
            print("Please enter from the valid choices")
            self.display_details()
            

    def higher_prices(self):
        print("============================================================================================")
        print("██╗░░██╗██╗░██████╗░██╗░░██╗███████╗██████╗░  ██████╗░██████╗░██╗░█████╗░███████╗░██████╗")
        print("██║░░██║██║██╔════╝░██║░░██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔════╝")
        print("███████║██║██║░░██╗░███████║█████╗░░██████╔╝  ██████╔╝██████╔╝██║██║░░╚═╝█████╗░░╚█████╗░")
        print("██╔══██║██║██║░░╚██╗██╔══██║██╔══╝░░██╔══██╗  ██╔═══╝░██╔══██╗██║██║░░██╗██╔══╝░░░╚═══██╗")
        print("██║░░██║██║╚██████╔╝██║░░██║███████╗██║░░██║  ██║░░░░░██║░░██║██║╚█████╔╝███████╗██████╔╝")
        print("╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░╚════╝░╚══════╝╚═════╝░")
        print("1. Details of 1st 15 days table")
        print("2. Details of 2nd 15 days table")
        print("3. Return to main_menu")
        self.choice4=int(input("Enter your choice: "))
        print("============================================================================================")
        
        if self.choice4==1:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Select your desired option")
            print("1. grocery")
            print("2. vehicle_expense")
            print("3. recreations")
            print("4. utilities")
            print("5. extras")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.choice5=int(input("Enter you desired choice: "))
            
            if self.choice5==1:
                mycursor1.execute("select month from 1st_15days where grocery=(select max(grocery) from 1st_15days)")
                mydb.commit()
                for i in mycursor1:
                    print(i)
                self.higher_prices()
                    
            elif self.choice5==2:
                 mycursor2.execute("select month from 1st_15days where vehicle_expense=(select max(vehicle_expense) from 1st_15days)")
                 mydb.commit()
                 for i in mycursor2:
                    print(i)
                 self.higher_prices()
            
            elif self.choice5==3:
                 mycursor3.execute("select month from 1st_15days where recreation=(select max(recreation) from 1st_15days)")
                 mydb.commit()
                 for i in mycursor3:
                    print(i)
                 self.higher_prices()

            elif self.choice5==4:
                 mycursor4.execute("select month from 1st_15days where utilities=(select max(utilities) from 1st_15days)")
                 mydb.commit()
                 for i in mycursor4:
                    print(i)
                 self.higher_prices()
                    
            elif self.choice5==5:
                 mycursor5.execute("select month from 1st_15days where extras=(select max(extras) from 1st_15days)")
                 mydb.commit()
                 for i in mycursor5:
                    print(i)
                 self.higher_prices()
            
            else:
                print("Please enter valid choice")
                self.higher_prices()
                
        elif self.choice4==2:
            print("Select your desired option")
            print("1. grocery")
            print("2. vehicle_expense")
            print("3. recreations")
            print("4. utilities")
            print("5. extras")
            self.choice6=int(input("Enter you desired choice: "))
            
            if self.choice6==1:
                mycursor2.execute("select month from 2nd_15days where grocery=(select max(grocery) from 2nd_15days)")
                mydb.commit()
                for i in mycursor2:
                    print(i)
                self.higher_prices()
                    
            elif self.choice6==2:
                 mycursor2.execute("select month from 2nd_15days where vehicle_expense=(select max(vehicle_expense) from 2nd_15days)")
                 mydb.commit()
                 for i in mycursor2:
                    print(i)
                 self.higher_prices()
            
            elif self.choice6==3:
                 mycursor2.execute("select month from 2nd_15days where recreation=(select max(recreation) from 2nd_15days)")
                 mydb.commit()
                 for i in mycursor2:
                    print(i)
                 self.higher_prices()

            elif self.choice6==4:
                 mycursor2.execute("select month from 1st_15days where utilities=(select max(utilities) from 2nd_15days)")
                 mydb.commit()
                 for i in mycursor2:
                    print(i)
                 self.higher_prices()
                    
            elif self.choice6==5:
                 mycursor2.execute("select month from 2nd_15days where extras=(select max(extras) from 2nd_15days)")
                 mydb.commit()
                 for i in mycursor2:
                    print(i)
                 self.higher_prices()
            
            else:
                print("Please enter valid choice")
                self.higher_prices()
                
        elif self.choice4==3:
            self.main_menu()
                
        else:
             print("Please enter valid choice")
             self.higher_prices()

    def amount_spent_saved(self):
        print("============================================================================================")
        print("This is for the recently added details")
        print("1.Amount of money spent")
        print("2.Amount of money saved")
        print("3.Back to main_menu")
        self.choice5=int(input("Enter your choice:"))
        print("============================================================================================")
        
        if self.choice5==1:
            self.amount_spent()
        elif self.choice5==2:
            self.amount_saved()
        elif self.choice5==3:
            self.main_menu()
        else:
            print("Please enter from the valid choices")
            self.amount_spent_saved()
    
    def amount_spent(self):
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("This information is about the information you have just entered")
        a=self.grocery+self.vehicle_expense+self.recreation+self.extras+self.utilities+self.extras
        b=self.grocery1+self.vehicle_expense1+self.recreation1+self.extras1+self.utilities1+self.extras1
        print("Total amount of money spent in week one")
        print(a)
        print("Total amount of money spent in week two")
        print(b)
        print("Total amount of money spent")
        print(a+b)
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        self.amount_spent_saved()
     
    def amount_saved(self):
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("This information is about the information you have just entered")
        a1=self.grocery+self.vehicle_expense+self.recreation+self.extras+self.utilities+self.extras
        b1=self.grocery1+self.vehicle_expense1+self.recreation1+self.extras1+self.utilities1+self.extras1
        print("The amount saved is")
        print(self.monthly_salary-(a1+b1))
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        self.amount_spent_saved()
        
    def delete_information(self):
        print("██████╗░███████╗██╗░░░░░███████╗████████╗███████╗")
        print("██╔══██╗██╔════╝██║░░░░░██╔════╝╚══██╔══╝██╔════╝")
        print("██║░░██║█████╗░░██║░░░░░█████╗░░░░░██║░░░█████╗░░")
        print("██║░░██║██╔══╝░░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░")
        print("██████╔╝███████╗███████╗███████╗░░░██║░░░███████╗")
        print("╚═════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░╚══════╝")
        print("============================================================================================")
        print("Select your desired choice")
        print("1, From 1st_15days")
        print("2. From 2nd_15days")
        print("3. Go back to main_menu")
        print("============================================================================================")
        self.choice5=int(input("Enter you choice:"))
        
        if self.choice5==1:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month3=input("Enter month for which you would like to delete the details")
            command="delete from 1st_15days where month=%s"
            values=[self.month3]
            mycursor4.execute(command, values)
            mydb.commit()
            print("Information successfully deleted")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.delete_information()
         
        elif self.choice5==2:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.month4=input("Enter month for which you would like to delete the details")
            command="delete from 2nd_15days where month=%s"
            values=[self.month4]
            mycursor4.execute(command, values)
            mydb.commit()
            print("Information successfully deleted")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            self.delete_information()
         
        elif self.choice5==3:
            self.main_menu()
        
        else:
            print("Please enter from the valid choices")
            self.delete_information()
        
    def saving_tips(self):
        myfile=open("savingtips.txt" , 'r')
        s=myfile.read()
        print(s)
        myfile.close()
        self.main_menu()
    
    def exit_over(self):
        print("██████╗░██╗░░░██╗███████╗")
        print("██╔══██╗╚██╗░██╔╝██╔════╝")
        print("██████╦╝░╚████╔╝░█████╗░░")
        print("██╔══██╗░░╚██╔╝░░██╔══╝░░")
        print("██████╦╝░░░██║░░░███████╗")
        print("╚═════╝░░░░╚═╝░░░╚══════╝")
        print("============================================================================================")
        print("Thank you for using our app")
        print("We hope enjoyed using our app")
        print("To help us improve, please contact our developers")
        print("Have a nice day")
        print("============================================================================================")
        
e=expense_tracker()
e.check_module()
