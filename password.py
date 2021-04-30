password=input("enter the number")
if len(password)<6:
    print("it is too long it must be in between 6 to 12 character")
elif len(password)>12:
    print("it is too long charactor it must be in between 6 to 12")
elif len(password)>=6 or (password)<12:
    print("passwork okk")