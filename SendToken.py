import os
import csv

def Choice():
    print("How many tokens do you want to send? \nFor 1 token press: 1 \nFor many tokens press: 2")
    branch = input("Please enter 1 or 2:  ")
    if branch == "1":
        One()
    elif branch == "2":
        Many()
    else:
        Choice()

def One():
    token = input("what is the address of the token you want to send?  ")
    amount = input("how many tokens you want to send to each recipient?  ")
    recipient = input("What is the address you want to send " + amount + " tokens to?  ")
    Send(token, amount, recipient)
    
def Send(token, amount, recipient):
    command =  'spl-token transfer --fund-recipient --allow-unfunded-recipient '+ token + " " + amount + " " + recipient
    os.system(command)

def Many():
    token = input("what is the address of the token you want to send?  ")
    amount = input("how many tokens you want to send to each recipient?  ")
    spot = input("Please enter the exact filepath to the CSV file containing the address you wish to send to \n")
    with open(spot, "r+") as file_r:
        file_reader = csv.reader(file_r)
        for row in file_reader:
            recipient = row[0]
            Send(token, amount, recipient)

Choice()