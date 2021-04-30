first=int(input("enter 1st number"))
second=int(input("enter 2nd number"))
third=int(input("enter 3rd number"))
if first>=second and first>=third:
    print(first,"first")
elif second>=first and second>=third:
    print(second,"second")
elif third>=first and third>=second:
    print(third,"third")
else:
    print("all are equal")
    