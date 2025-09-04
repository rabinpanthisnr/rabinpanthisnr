username = "python"
password = "rules"
attempt = 0
while attempt < 5:
    inp_user_name = input("Enter your user name:")
    inp_user_pw = input("Enter your password name:")
    if (username == inp_user_name) and (password == inp_user_pw):
        print("Welcome!")
        break  # we can simply understand that (attempt=5)
    else:
        print("Invalid user and password!")

        attempt += 1
if attempt == 5:
    print("Access denied!")