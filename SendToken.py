import os

token = input("what is the address of the token you want to send?  ")

amount = input("how many tokens you want to send?  ")

recipient = input("What is the address you want to send " + amount + " tokens to?  ")

command =  'spl-token transfer --fund-recipient --allow-unfunded-recipient '+ token + " " + amount + " " + recipient

os.system(command)