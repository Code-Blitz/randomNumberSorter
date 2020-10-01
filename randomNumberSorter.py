#Imports
import sys
import random

#bubbleSort algorithm
def bubbleSort(list1):
    n = len(list1)

    for i in range(n):

        for j in range(0, n-i-1):
            if list1[j] > list1[j+1]:

                list1[j], list1[j+1] = list1[j+1], list1[j]
                randomNumber = random.randint(0, 100000)
                randomNu = random.randint(0, 10)

                if randomNumber == 0:
                    if (randomNu == 2 or randomNu == 4):
                        print("Thinking...")
                    else:
                        print("Working...")
    

listOfNumbers = []
originalList = []
rangeOfNumbers = int(input('Enter the amount of numbers you want to generate: '))

for i in range(rangeOfNumbers):
    randomNumber = random.randint(0, rangeOfNumbers)

    listOfNumbers.append(randomNumber)
    originalList.append(randomNumber)

print('Random number generation complete...')
bubbleSort(listOfNumbers)

print('Original list of ' + str(rangeOfNumbers) + ' random numbers: ' + str(originalList))
print('Sorted list: ' + str(listOfNumbers))