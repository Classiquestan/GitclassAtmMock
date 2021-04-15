#register
#- first name, last name, password, email
#-generate user id and account number


#login
#-account number and password

#bank operations

#Initializing the system
import random

database = {
    8044720745: ['Stanley', 'Chima', 'Stanniss@yahoo.com', 'pass12', 900]
}


def init():
    print('Welcome to Bank PHP')

    have_account = int(input('Do you have account with us: 1 (yes) 2 (no) \n'))

    if (have_account == 1):
        login()


    elif (have_account == 2):
        register()

    else:
        print('You have selected invalid option')
        init()


def login():
    print('******** Login to your account ********')

    user_account_number = int(input('enter your account number\n'))
    user_password = input('enter your password \n')

    for account_number, user_details in database.items():
        if account_number == user_account_number:
            if user_details[3] == user_password:
                bank_operation(user_details)
    else:
        print('Invalid login details')

    return user_details


def register():
    print('****** Register ********')

    email = input('what is your email address? \n')
    first_name = input('what is your first name? \n')
    last_name = input('what is your last name? \n')
    password = input('create a password for yourself \n')

    account_number = generate_account_number()

    database[account_number] = [first_name, last_name, email, password, 0]

    print('Your account has been created')
    print('Your account number is: %d' % account_number)
    print('Keep it safe')

    login()

    return database


def bank_operation(user_details):
    print("Welcome %s %s" % (user_details[0], user_details[1]))

    selected_option = int(input('What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n'))

    if (selected_option == 1):

        deposit_operation(user_details)
    elif (selected_option == 2):

        withdrawal_operation(user_details)
    elif (selected_option == 3):

        logout()
    elif (selected_option == 4):

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user_details)


def deposit_operation(user_details):
    print("Deposit Operations")

    get_current_balance(user_details)

    print('This is your current balance')

    deposit_amount = int(input('How much do you want to deposit: \n'))

    updated_balance = user_details[4] + deposit_amount

    print(updated_balance, ':This is your updated balance')

    your_response = int(input('Do you want to perform another operation? (1) Yes (2) No \n'))

    if your_response == 1:
        login()

    elif your_response == 2:
        print('Thank you for banking with us')

        init()


def withdrawal_operation(user_details):
    print("*****Withdrawal Channel****")

    get_current_balance(user_details)

    deduct_amount = int(input('How much do you want to withdraw? \n'))

    current_balance = user_details[4] - deduct_amount

    if user_details[4] < deduct_amount:
        print('You have exceeded your withdrawal limit')

    elif user_details[4] >= deduct_amount:
        print(current_balance, ':This is your current balance')

    your_response = int(input('Do you want to perform another operation? (1) Yes (2) No \n'))

    if your_response == 1:
        login()
        
    elif your_response == 2:
        print('Thank you for banking with us')

        init()



def generate_account_number():
    # print('Generating Account Number')
    return random.randrange(1111111111, 9999999999)


def get_current_balance(user_details):
    return user_details[4]



def logout():
    login()


init()


