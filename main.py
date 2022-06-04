from dataPlotter import *
import pandas as pd

catalog = "data/"
dataFile = 'outNormaliseData.csv'

videoNum = 10 #Номер видео
snapshotTime = 5 #Начальная секунда
intervalTime = 1 #Сколько секунд от начала

peopleNum = 1 #С какого человека
peopleCount = 5 #Сколько человек

dop = 80 #Интервал

preProd(snapshotTime, intervalTime, catalog,peopleNum, videoNum, peopleCount, dop)

df = pd.read_csv('outNormaliseData.csv')
df.plot(x="X", y="Y", kind="scatter")
plt.axis([0, 1920, 0, 1080])
plt.show()