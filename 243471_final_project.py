
print('Welcome to Thennek Bank Plc')
account_number = input('Enter Your account number: ')
pin_number = input('Enter Your pin: ')
account_balance = 20000

#Creation of different users for testing .. This took me 15minutes
user_1 = ['3113562522', '31135', 'John', 'Doe']
user_2 = ['1234567890', '12345', 'Dough', 'Ebube']
user_3 = ['0123450123', '09876', 'User', 'Heuristics']

#Verification process for the pin and account number (This took an hour and 10minutes)
entries_counter = 0
while entries_counter < 2:
  if account_number == user_1[0] and pin_number == user_1[1]:
    break
  elif account_number == user_2[0] and pin_number == user_2[1]:
    break
  elif account_number == user_3[0] and pin_number == user_3[1]:
    break
  else:
    print('Incorrect Details\nAccount Number must be 10\nPassowrd must be 5')
    account_number = input('Enter Your account number: ')
    pin_number = input('Enter Your pin: ')
    entries_counter += 1

if entries_counter == 2:
  print('You have exhausted your trials \n Try again later with the correct details')
else:
  #The working of the menu section
  print('')
  print('Main Menu \n 1-View my balance \n 2-Withdraw Cash \n 3-Deposit Funds \n 4-Exit')
  main_menu_choice = int(input('Enter a choice: '))

  #let's create a function for withdrawing cash (This took about 2hours 30minutes)
  def withdraw_cash():
    print('Withdrawal Menu: \n 1 - 1000 \n 2 - 2000 \n 3 - 5000 \n 4 - 10000 \n 5 - 20000 \n 6 - Cancel transaction')
    cash_withdrawal_choice = int(input('Enter a choice: '))
    global account_balance

    if cash_withdrawal_choice == 1:
      option_1 = 1000
      if account_balance < option_1:
        print('Insufficient Balance')
        withdraw_cash()
      else:
        account_balance = account_balance - option_1
        print(str(option_1) + ' successfully withdrawn')
        print('Your balance is ' + str(account_balance))
        print('Would you like to withdraw again? \n 1 - Yes \n 2 - No')
        second_withdrawal_choice = int(input('Enter a choice: '))
        if second_withdrawal_choice == 1:
          withdraw_cash()
        else: 
          print('Thank You for banking with us')
    elif cash_withdrawal_choice == 2:
      option_2 = 2000
      if account_balance < option_2:
        print('Insufficient Balance')
        withdraw_cash()   
      else:
        account_balance = account_balance - option_2
        print(str(option_2) + ' successfully withdrawn')
        print('Your balance is ' + str(account_balance))
        print('Would you like to withdraw again? \n 1 - Yes \n 2 - No')
        second_withdrawal_choice = int(input('Enter a choice: '))
        if second_withdrawal_choice == 1:
          withdraw_cash()
        else: 
          print('Thank You for banking with us')
    elif cash_withdrawal_choice == 3:
      option_3 = 5000
      if account_balance < option_3:
        print('Insufficient Balance')
        withdraw_cash()    
      else:
        account_balance = account_balance - option_3
        print(str(option_3) + ' successfully withdrawn')
        print('Your balance is ' + str(account_balance))
        print('Would you like to withdraw again? \n 1 - Yes \n 2 - No')
        second_withdrawal_choice = int(input('Enter a choice: '))
        if second_withdrawal_choice == 1:
          withdraw_cash()
        else: 
          print('Thank You for banking with us')
    elif cash_withdrawal_choice == 4:
      option_4 = 10000
      if account_balance < option_4:
        print('Insufficient Balance')
        withdraw_cash()    
      else:
        account_balance = account_balance - option_4
        print(str(option_4) + ' successfully withdrawn')
        print('Your balance is ' + str(account_balance))
        print('Would you like to withdraw again? \n 1 - Yes \n 2 - No')
        second_withdrawal_choice = int(input('Enter a choice: '))
        if second_withdrawal_choice == 1:
          withdraw_cash()
        else: 
          print('Thank You for banking with us')
    elif cash_withdrawal_choice == 5:
      option_5 = 20000
      if account_balance < option_5:
        print('Insufficient Balance')
        withdraw_cash()
      else:
        account_balance = account_balance - option_5
        print(str(option_5) + ' successfully withdrawn')
        print('Your balance is ' + str(account_balance))
        print('Would you like to withdraw again? \n 1 - Yes \n 2 - No')
        second_withdrawal_choice = int(input('Enter a choice: '))
        if second_withdrawal_choice == 1:
          withdraw_cash()
        else: 
          print('Thank You for banking with us')
    elif cash_withdrawal_choice == 6:
      print('Withdrawal Transaction Terminated \nNo amount is deducted')
      print('Your balance is ' + str(account_balance))
    else: 
      print('Your choice is not in the range of options')
      withdraw_cash()
  #end of withdrawing cash function

  #Let's write a function for depositing funds (This part took me about 20 minutes)
  def depositing_funds():
    print('How to deposit: \n 1: Enter the amount you wish to deposit \n 2: Enter 0 to terminate the process')
    deposit_choice = int(input('Enter a choice: '))
    global account_balance

    if deposit_choice > 0:
      account_balance = account_balance + deposit_choice
      print('You have deposited ' + str(deposit_choice) + ' Naira')
      print('Your account balance is ' + str(account_balance) + ' Naira')
    elif deposit_choice == 0:
      print('Deposit Transaction Terminated')


  #The code controlling the menu options using the functions above for the corresponding choice.
  #This took about 25-30 minutes
  if main_menu_choice == 1:
    print('Your account balance is' + ' #' + str(account_balance))
  elif main_menu_choice == 2:
    withdraw_cash()
  elif main_menu_choice == 3:
    depositing_funds()
  elif main_menu_choice == 4:
    print(' \n Transaction cancelled \n Thank You for banking with Thennek Bank Plc')
  else:
    print('Not within the range of options 1-4')
  


  

  




  

