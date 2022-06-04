import matplotlib.pyplot as plt
from statistics import mean
import csv


def parceData(filename):
    xData = []
    yData = []
    fileI = open(filename, "r")
    lines = fileI.readlines()
    for line in lines:
        xData.append(int(line.split('(')[1][:-2].split(',')[0]))
        yData.append(int(line.split('(')[1][:-2].split(',')[1]))
    fileI.close()
    return [xData, yData]


def cutOneVideo(obj, sec, interval):
    frames = sec * 20
    slice_object = slice(frames, frames + int(interval * 20))
    result = obj[slice_object]
    return result


def plotter(snapshotTime, intervalTime, catalog, peopleNum, videoNum, peopleCount):
    xData = []
    yData = []
    color = ['r*', 'g^', 'bo', 'y*', 'm^', 'ro', 'b*', 'r^', 'go']
    for i in range(peopleCount):
        xData.append(cutOneVideo(parceData(catalog + str(videoNum) + "_" +
                                           str(peopleNum + i) + ".txt")[0], snapshotTime, intervalTime))
        yData.append(cutOneVideo(parceData(catalog + str(videoNum) + "_" +
                                           str(peopleNum + i) + ".txt")[1], snapshotTime, intervalTime))


    return [xData, yData]


def preProd(snapshotTime, intervalTime, catalog, peopleNum, videoNum, peopleCount, dop):
    xyData = plotter(snapshotTime, intervalTime, catalog,
                     peopleNum, videoNum, peopleCount)

    print(xyData)

    a = 0
    for item in xyData[0]:
        for items in item:
            a += items
    avgX = (a / (len(xyData[0]) * len(item)))
    avgX = int(round(avgX))

    a = 0
    for item in xyData[1]:
        for items in item:
            a += items
    avgY = (a / (len(xyData[1]) * len(item)))
    avgY = int(round(avgY))

    print(avgX, avgY)

    for index, item in enumerate(xyData[0]):
        for index_, item_ in enumerate(xyData[0][index]):
            print(index_, item_)
            if (item_ > (avgX + dop)) or (item_ < (avgX - dop)):
                xyData[0][index][index_] = 0
                xyData[1][index][index_] = 0

    for index, item in enumerate(xyData[1]):
        for index_, item_ in enumerate(xyData[1][index]):
            print(index_, item_)
            if (item_ > (avgY + dop)) or (item_ < (avgY - dop)):
                xyData[0][index][index_] = 0
                xyData[1][index][index_] = 0

    print(xyData[0])
    print(xyData[1])

    fileWriter(xyData)


def fileWriter(data):
    with open("outNormaliseData.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["X", "Y"])
        for index, item in enumerate(data[0]):
            for index_, item_ in enumerate(data[0][index]):
                if item_ != 0:
                    file_writer.writerow([data[0][index][index_], data[1][index][index_]])


def plotshow():
    plt.axis([0, 1920, 0, 1080])
    plt.show()
