password = input("enter password: ")
if len(password) < 8:
    print("weak password")
else:
    print("strong password")