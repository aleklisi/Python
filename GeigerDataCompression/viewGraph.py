import csv

import matplotlib.pyplot as plt


def drawGraph(dayStart, dayEnd, startMonth, endMonth, year):
    for month in range(startMonth, endMonth+1):
        for day in range(dayStart, dayEnd+1):
            filename = 'dataAgg/agg{}_{}_{}.csv'.format(day, month, year)
            x = []
            y = []
            with open(filename, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=',')
                for row in plots:
                    x.append(int(row[0]))
                    y.append(int(row[1]))
            graphLabel = "Radiation level for {}.{}.{}".format(day, month, year)
            plt.plot(x, y, label=graphLabel)
        plt.xlabel('Hour')
    plt.ylabel('Radiation Level')
    plt.title('')
    plt.legend()
    plt.show()


drawGraph(12, 23, 4, 4, 2018)
