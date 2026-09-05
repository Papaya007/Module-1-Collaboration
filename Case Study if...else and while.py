# Name: Julian Paiz
# File Name: studentqualifications.py
# Description: This app accepts student names and GPAs and determines if each
# student qualifies for the Dean's List or Honor Roll.

while True:
    lastname = input("Enter student's last name:")

    if lastname == "ZZZ":
        break

    firstname = input("Enter student's first name:")
    gpa = float(input("Enter student's GPA:"))

    if gpa >= 3.5:
                print (firstname, lastname, "has made the Dean's List.")
    if gpa >= 3.25:
                print(firstname, lastname, "has made the Honor Roll.")
    
    



    
            
