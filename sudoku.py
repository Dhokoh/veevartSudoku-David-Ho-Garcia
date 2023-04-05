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

def addNumbersHorizontal(string):
    for i in range(len(string)):
        if (string[i] == '0'):
            newNumber = str(randint(1,9))
            string2List = list(string)
            string2List[i] = newNumber
            replaceRow = "".join(string2List)
            string = replaceRow
    return string



def sudoku(numbersMatrix):
    horizontalSet = set()
    verticalSet = set()
    set3x3 = set()
    for i in range(len(numbersMatrix)):
        for j in range(len(numbersMatrix[i])):
            horizontalSet.add(numbersMatrix[i][j])
            print(horizontalSet)
            if (numbersMatrix[i][j] == '0'):
                numbersMatrix[i] = addNumbersHorizontal(numbersMatrix[i])
                            


            

    print(numbersMatrix)



sudoku(testMatrix)
text = "abscezo"
checkRepeated(text)

print(checkRepeated(text))
