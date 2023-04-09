from random import *
from string import *

testMatrix = [
    "5 3 0 0 7 0 0 0 0", 
    "6 0 0 1 9 5 0 0 0", 
    "0 9 8 0 0 0 0 6 0", 
    "8 0 0 0 6 0 0 0 3", 
    "4 0 0 8 0 3 0 0 1", 
    "7 0 0 0 2 0 0 0 6", 
    "0 6 0 0 0 0 2 8 0", 
    "0 0 0 4 1 9 0 0 5", 
    "0 0 0 0 8 0 0 7 9"
    ]

def checkRepeated(string): ##Funcion que busca caracteres repetidos en un String
    alreadySeen = set()
    for i in range(len(string)):
        if string[i] in alreadySeen:
            return True
        alreadySeen.add(string[i])
    return False

# def passSudoku(sudoku): ##Funcion para revisar el Sudoku si ha quedado resuelto o no. 
#     for i in range(len(sudoku)):
#         if (checkRepeated(sudoku[i])):
#             return False
#     return True

def addNumbers(string):
    numbersPool = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for i in numbersPool:
        for j in range(len(string)):
            if (i not in string and string[j] == '0'):
                string2List = list(string)
                string2List[j] = i
                replaceRow = "".join(string2List)
                string = replaceRow
    return string


def sudoku(numbersMatrix):
    print (numbersMatrix)

    for i in range(len(numbersMatrix)):
        for j in range(len(numbersMatrix[i])):
            if (numbersMatrix[i][j] == '0'):
                numbersMatrix[i] = addNumbers(numbersMatrix[i])
                        
    print(numbersMatrix)



sudoku(testMatrix)
text = "abscezo"
checkRepeated(text)

print(checkRepeated(text))
