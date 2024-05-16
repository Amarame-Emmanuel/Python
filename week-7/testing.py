import csv

with open("jt-ventures.csv") as doc:
    business = doc.read()
    
surname = input("Surname: ")
firstname = input("First name: ")
department = input("Department: ")

surname = surname.upper()

if ((surname in business ) and (department in business) and (firstname in business)):
    print("Welcome", surname,firstname )
    
    import pandas as pd
    df = pd.read_csv("jt-ventures.csv")
    print(df)
    
else:
    print ("No such employee exists")