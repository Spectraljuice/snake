'''
Created on Jan 23, 2018

@author: student
'''
import random
rawData= ""
print("Hello, welcome to the Dice Roller. Please input the dice roll in 1d6 format,where 1 = number of dice and 6 = the number of faces")
rawData = input(":")
dataList = rawData.split("d")
dice = int(dataList[0])
sides = int(dataList[1])
while dice>0:
    results = []
    results.append(random.randint(1,sides))
    dice = dice - 1


print(results)
