
import sys  # This is built into python
import csv  # Also built in to pyhthon
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree


def FindBottomLeft(TrainingData):

    BottomLeftOutput = []
    for BoardState in TrainingData:
        if BoardState[0] == 1:
            BottomLeftOutput.append(1)
        elif BoardState[0] == 2:
            BottomLeftOutput.append(2)
        else:
            BottomLeftOutput.append(0)

    return BottomLeftOutput

def FindMiddleColumn(TrainingData):

    MiddleColumnOutput = []
    Player1Counter = 0
    Player2Counter = 0;
    for BoardState in TrainingData:
        for Position in BoardState[18:24]:
            if Position == 1:
                Player1Counter += 1
            elif Position == 2:
                Player2Counter += 1
        if Player1Counter > Player2Counter:
            MiddleColumnOutput.append(1)
        elif Player1Counter < Player2Counter:
            MiddleColumnOutput.append(2)
        else:
            MiddleColumnOutput.append(0)
        Player1Counter = Player2Counter = 0

    return MiddleColumnOutput

def FindBottomMiddle(TrainingData):

    BottomMiddleOutput = []
    for BoardState in TrainingData:
        if BoardState[18] == 1:
            BottomMiddleOutput.append(1)
        elif BoardState[18] == 2:
            BottomMiddleOutput.append(2)
        else:
            BottomMiddleOutput.append(0)

    return BottomMiddleOutput

# def FindMiddleMatrix(TrainingData):
#
#     MiddleMatrixOutput = []
#     Player1Counter = 0
#     Player2Counter = 0;
#     for BoardState in TrainingData:
#         for Position in range(BoardState[13:29]):
#             if Position != 4 or 5 or 10 or 11:
#                 if BoardState[13 + Position] == 1:
#                     Player1Counter += 1
#                 elif BoardState[13 + Position] == 2:
#                     Player2Counter += 1
#         if Player1Counter > Player2Counter:
#             MiddleMatrixOutput.append(1)
#         elif Player1Counter < Player2Counter:
#             MiddleMatrixOutput.append(2)
#         else:
#             MiddleMatrixOutput.append(0)
#         print(Player1Counter)
#         print(Player2Counter)
#         return MiddleMatrixOutput



if __name__ == "__main__":

    # The *.csv files
    first_input_csv = sys.argv[2]
    second_output_csv = sys.argv[3]  # Same here

    # Now we want to open the *.csv file.
    #inputcsv = open(first_input_csv, 'r')  # This is means we are openning a file and then editing it.
    #TrainingCSV = csv.reader(inputcsv)  # Now we can read the file that was opened by python
    TrainingSet = pd.read_csv(first_input_csv, header=0)
    a = FindMiddleMatrix(TrainingSet.values)
    print("alalala")
    print(a)













    # Here are some changes we are going to make/create
    changes = [
        ['1 dozen', '12'],
        ['1 banana', '13'],
        ['1 dollar', 'elephant', 'heffalump'],
    ]

    """
    Now we will write the changes to the output file.

    First, we need to take in the string that is the 
    filename and create a filepath out of it.

    """

    # Now, if the rejectme.csv file is being viewed in the GUI
    # before the script runs, you will get write permission errors.

    # Creating the path
    outfilepath = "./" + str(second_output_csv)
    # Opening the file at the path.
    outfile = open(outfilepath, 'w')
    # Then we create an object to write data with.
    writer = csv.writer(outfile, delimiter=',')
    # Now we do the writing
    for row in changes:
        writer.writerow(row)
    """
    Now you have read in and written to a *.csv file
    the way the graders will.

    """
