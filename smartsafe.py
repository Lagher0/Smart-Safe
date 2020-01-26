# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 13:13:03 2020

@author: Daniel-Jacques de Jonge, Adam Haigh, Laura Silaja
"""
import csv

        
def save_password():
    passw = input("Enter your new password: ")
    with open ("./passwords.csv", "w") as password:
        password = csv.writer(password, delimiter = ",")
        password.writerow([passw])
    checkPassword()
    
def checkPassword():
    with open ("./passwords.csv", "r") as csvFile:
        passw = csv.reader(csvFile, delimiter = ",")
        r=[]
        for f in passw:
          r=f  
          break
    x = 1
    print(r)
    while x == 1:
        if len(r) == 0:
            save_password()
        password = input("Enter Password: ")
        if password == r[0]:
            print("Correct")
        else:
            print("Incorrect")


checkPassword()