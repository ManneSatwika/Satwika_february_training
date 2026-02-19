# Question 3: Smart Login System with Security Rules


correct_username = "admin"
correct_password = "1234"
account_active = True


username = input("Enter username: ")
password = input("Enter password: ")


if username == correct_username and password == correct_password:
    if account_active:
        print("Login Successful")
    else:
        print("Account Disabled")
else:
    print("Wrong Credentials")
