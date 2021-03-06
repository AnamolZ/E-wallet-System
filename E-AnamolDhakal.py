import csv
import random
import datetime
import sys

DATA_BASE_FILE_PATH = "/home/anamol/Main_Project/data_base.csv"
TRANSACTION_HISTORY_FILE_PATH = "/home/anamol/Main_Project/transaction_history.csv"
ADMIN_FILE_PATH="/home/anamol/Main_Project/admin_data.csv"

date_time=datetime.datetime.now()
user_transaction_info_list=[]
store_user_credentials=[]
admin_info=[]
        
def main():
    def user_login_redirect():
        try:
            account_number,key_pass = input("Account Number:"),input("Password:")
            user_login(account_number,key_pass,open(DATA_BASE_FILE_PATH).readlines())
        except Exception as Error:
            print(Error)
            main()
            
    def main_transaction_handler():
        print("\nSEND MONEY")
        sender_account_number,sender_key_pass = input("Sender Account Number:"),input("Sender Account Password:")
        receiver_account_number,transfering_amount = input("Beneficiary Account Number:"),int(input("Amount:"))
        with open(DATA_BASE_FILE_PATH) as read_file:
            transaction_data = csv.reader(read_file)
            header = next(transaction_data)
            for per_transaction_data in transaction_data:
                user_transaction_info_list.append(per_transaction_data)
        for row in user_transaction_info_list:
            if sender_account_number in row:
                sender_total_amount = row[-1]
            if receiver_account_number in row:
                receiver_total_amount = row[-1]
        calculated_sender_amount = int(sender_total_amount)-int(transfering_amount)
        calculated_receiver_amount = int(receiver_total_amount)+int(transfering_amount)
        if  calculated_sender_amount > 500:
            with open(DATA_BASE_FILE_PATH) as read_file:
                read_sender_file = read_file.read()
                if sender_account_number in read_sender_file:
                    read_sender_file = read_sender_file.replace(str(sender_total_amount),str(calculated_sender_amount))
            with open(DATA_BASE_FILE_PATH,"w") as write_file:
                write_file.write(read_sender_file)
            with open(DATA_BASE_FILE_PATH) as read_file:
                read_file_receiver=read_file.read()
                if receiver_account_number in read_file_receiver:
                    read_file_receiver=read_file_receiver.replace(str(receiver_total_amount),str(calculated_receiver_amount))
            with open(DATA_BASE_FILE_PATH,"w") as write_file:
                write_file.write(read_file_receiver)
            with open(TRANSACTION_HISTORY_FILE_PATH,"w+") as write_file:
                write_file.write(str(transfering_amount) + " Transfered From " + str(sender_account_number) + " To "+str(receiver_account_number)+str(date_time))
            user_login_redirect()
        else:
            print("\nInsuffient Balance\n")
            main()
            
    def transaction_history():
        try:
            with open(TRANSACTION_HISTORY_FILE_PATH) as read_file:
                transaction_data = read_file.read()
                print(transaction_data,"\n","\nPress U To Go To User Login \nOR\nPress M To Go To Main\n")
                main_user_input=input()
                if main_user_input.isupper() == "U":    
                    user_login_redirect()
                elif main_user_input.isupper() == "M":
                    main()
        except Exception as Error:
            print("No Transaction Has Made Yet",Error,"\nRedirecting Back To Login\n")
            user_login_redirect()
    
    def user_login(account_number,key_pass,lines):
        try:
            with open(DATA_BASE_FILE_PATH) as read_file:
                lines = read_file.readlines()
                for line in lines:
                    if account_number in line and key_pass in line:
                        with open(DATA_BASE_FILE_PATH) as read_file:
                            bouncer_data = csv.reader(read_file)
                            header = next(bouncer_data)
                            for user_credentials in bouncer_data:
                                store_user_credentials.append(user_credentials)
                        for i in range(len(store_user_credentials)):
                            if account_number in store_user_credentials[i][5] and key_pass in store_user_credentials[i][4]:
                                print("\nLogin Sucessfully\n")
                                with open(DATA_BASE_FILE_PATH) as read_file:
                                    bouncer_data = csv.reader(read_file)
                                    header = next(bouncer_data)
                                    for info in bouncer_data:store_user_credentials.append(info)
                                for i in range(len(store_user_credentials)):
                                    if account_number in store_user_credentials[i] and key_pass in store_user_credentials[i]:
                                        print("Account Number:",(store_user_credentials[i])[5],"\nAmount:",(store_user_credentials[i])[6] ,"\nEmail Address:",(store_user_credentials[i])[3],"\nPhone Number:",(store_user_credentials[i])[2],"\n")
                                        phone_number = store_user_credentials[i][2]
                                        print("1. Load Money\n2. WithDraw Money\n3. Transaction\n4. Transaction History\n5. Go Back\n6. Quit")
                                        main_user_input = input("\nEnter:\n")
                                        if main_user_input=="1":load_money(account_number,phone_number)
                                        elif main_user_input=="2":withdraw_money(account_number,phone_number)
                                        elif main_user_input=="3":main_transaction_handler()
                                        elif main_user_input=="4":transaction_history()
                                        elif main_user_input=="5":main()
                                        elif main_user_input=="6":sys.exit("Thank You For Your Time")
                else:
                    print("\n\nPassword Wrong\n Back To Login Page..")
                    main()
        except Exception as Error:
            print(Error)
    
    def load_money(account_number,phone_number):
        transfering_amount = int(input("Enter Amount: "))
        with open(DATA_BASE_FILE_PATH) as read_file:
            transaction_data = csv.reader(read_file)
            header = next(transaction_data)
            for per_transaction_data in transaction_data:
                user_transaction_info_list.append(per_transaction_data)
        for row in user_transaction_info_list:
            if account_number in row and phone_number in row:
                sender_total_amount = row[-1]
        calculated_sender_amount = int(sender_total_amount)+int(transfering_amount)
        with open(DATA_BASE_FILE_PATH) as read_file:
            read_sender_file = read_file.read()
            if account_number in read_sender_file:
                read_sender_file = read_sender_file.replace(str(sender_total_amount),str(calculated_sender_amount))
        with open(DATA_BASE_FILE_PATH,"w") as write_file:
            write_file.write(read_sender_file)
    
    def withdraw_money(account_number,phone_number):
        transfering_amount = int(input("Enter Amount: "))
        with open(DATA_BASE_FILE_PATH) as read_file:
            transaction_data = csv.reader(read_file)
            header = next(transaction_data)
            for per_transaction_data in transaction_data:
                user_transaction_info_list.append(per_transaction_data)
        for row in user_transaction_info_list:
            if account_number in row and phone_number in row:
                sender_total_amount = row[-1]
        calculated_sender_amount = int(sender_total_amount)-int(transfering_amount)
        if  calculated_sender_amount > 500:
            with open(DATA_BASE_FILE_PATH) as read_file:
                read_sender_file = read_file.read()
                if account_number in read_sender_file:
                    read_sender_file = read_sender_file.replace(str(sender_total_amount),str(calculated_sender_amount))
            with open(DATA_BASE_FILE_PATH,"w") as write_file:
                write_file.write(read_sender_file)
        else:
            print("\nInsuffient Balance\n")
    
    def admin_login():
        def account_creation():
            acc_number=random.randint(152749224,965489336)
            fname,lname,ph_number = input("First Name: "),input("Last Name: "),input("Phone Number: ")
            email,password,amount = input("E-Mail Address: "),input("Set Password: "),input("Opening Amount: ")
            user_data = ("\n"+str(fname)+","+str(lname)+","+str(ph_number)+","+str(email)+","+str(password)+","+str(acc_number)+","+str(amount))
            try:
                with open(DATA_BASE_FILE_PATH,"a+") as append_file:append_file.write(user_data)
                print("\n.....Redirecting To Login Page.....\n")
                input("Press Any Key To Continue.")
                main()
            except Exception as Error:
                print(Error)
                admin_login()

        def admin_login_point():
            try:
                admin_id,admin_pass = input("\nAdmin ID:"),input("Admin Pass:")
                with open(ADMIN_FILE_PATH) as read_file:
                    admin_data = csv.reader(read_file)
                    header = next(admin_data)
                    for per_admin_info in admin_data:admin_info.append(per_admin_info)
                for row in admin_info:
                    if admin_id in row and admin_pass in row:
                        account_creation()
                    elif admin_id not in row and admin_pass not in row:
                        print("\n..Redirecting.. Back To Login...\n")
                        main()
            except Exception as Error:
                print(Error)
                admin_login()
        
        def transaction_history_view():
            try:
                admin_id,admin_pass = input("\nAdmin ID:"),input("Admin Pass:")
                with open(ADMIN_FILE_PATH) as file:
                    admin_data = csv.reader(file)
                    header = next(admin_data)
                    for per_admin_info in admin_data:
                        admin_info.append(per_admin_info)
                for row in admin_info:
                    try:
                        if admin_id in row and admin_pass in row:
                            with open(DATA_BASE_FILE_PATH) as file:
                                view_data = csv.reader(file)
                                header = next(view_data)
                                for per_csv_admin_data in view_data:
                                    print("\n",",".join(per_csv_admin_data),"\n")
                            admin_login()
                        elif admin_id not in row and admin_pass not in row:
                            print("\n..Redirecting.. Back To Login...\n")
                            main()
                    except Exception as Error:
                        print(Error)
                        admin_login()
            except Exception as Error:
                print(Error)
                admin_login()
        
        print("\n1. Create Account\n2. View Entire Server Data\n3. Back\n4. Quit")
        user_input = input("\nEnter:\n")
        if user_input == "1":admin_login_point()
        elif user_input == "2":transaction_history_view()
        elif user_input == "3":main()
        elif user_input == "4":sys.exit("Thank You For Your Time")
        else:
            print("\nFunctional Error!\n")
            admin_login()            
    
    print("\n1. User Login\n2. Admin Login\n3. Quit")
    user_input = input("\nEnter:")
    if user_input == "1":user_login_redirect()
    elif user_input == "2":admin_login()
    elif user_input == "3":exit("Thank You For Your Time")
    else:main()
main()
