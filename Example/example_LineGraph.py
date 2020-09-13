#!/usr/bin/python3
#coding:utf-8

import sys
sys.path.append("..")
import csv
from Utils import Graph

def main():
    """
    Make data file (e.g. .csv) into list of x-axis, y-axis1, y-axis2, ...
    * Code it yourself in this region
    """
    with open('../Data/data1.csv', 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        nx = rows[0].index('x')
        ny1 = rows[0].index('y1')
        ny2 = rows[0].index('y2')
        ny3 = rows[0].index('y3')
        x = []
        y1 = []
        y2 = []
        y3 = []
        for row in rows[1:]:
            row = [float(r) for r in row]
            x.append(row[nx])
            y1.append(row[ny1])
            y2.append(row[ny2])
            y3.append(row[ny3])
    """
    Plot the data on a graph, and save this graph as .png
    arg1: [x-aixs1, x-axis2, ...] #Even if x-axis is only one, you must set the same number as that of y-axes
    arg2: [y-axis1, y-axis2, ...]
    arg3: x-axis label
    arg4: y-axis label
    arg5: Tag of "Setting.ini", which decide plot parameter #You can set plot parameters by using "Setting.ini"
    * Set arguments yourself
    """
    Graph.Plot([x] * 3, [y1, y2, y3], ['y1', 'y2', 'y3'], 'x', 'y', SettingTag = 'UserSetting1')

if __name__ == '__main__':
    main()