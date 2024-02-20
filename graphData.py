import matplotlib.pyplot as plt
import numpy as np



def readFile(vrorvbias = 0, fileName = "langmuirtestdata.lvm"):
    fileIn = open(fileName, "r")
    voltage = []
    vbias = []
    test = 0

    for line in fileIn:
        line = line.strip()
        line = line.split("	")
        if float(line[1]) < 10:
            voltage.append(line[vrorvbias])

    fileIn.close()
    return(voltage)

# creates a .txt file to list shows that match user genre
def writeFile(userGenre, showList):
    fileOut = open(userGenre + ".txt", "w")
    for item in showList:
        print(item, file=fileOut)
    fileOut.close()

# prints messages to user and creates .txt file
def main():
    xpoints = np.array(readFile(1))
    ypoints = np.array(readFile(0))

    plt.plot(xpoints, ypoints, 'o')
    plt.show()
main()