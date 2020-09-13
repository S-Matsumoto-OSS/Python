"""
=======================================================
Project Name : Python
File Name : Graph.py
Encoding : UTF-8
Creation Date : 2020/9/13

Operation Confirmation by Python 3.8.2

Copyright (c) 2020 Shogo Matsumoto. All rights reserved.
=======================================================
"""
#coding:utf-8

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import os
import numpy as np
import configparser 

from .sub_package import Check

def Plot(XList, YList,\
    LabelList, XLabel = 'X', YLabel = 'Y',\
    SettingTag = 'DEFAULT', OutFileName = 'plot.png', 
    SettingFile = '../SettingFile/Setting.ini'):
        """
        Plot Parameter
        """
        Inifile = configparser.ConfigParser()
        Inifile.read(SettingFile, encoding = 'utf-8')
        SAVE_DIR  = Check.isstr(Inifile.get(SettingTag, 'SAVE_DIR'), return_str = True)
        FONT_SIZE = Check.isnum(Inifile.get(SettingTag, 'GRAPH_FONT_SIZE1'), return_float = True)
        MARKER = Check.isstrlist(Inifile.get(SettingTag, 'MARKER'), return_list = True)
        LINE_STYLE = Check.isstrlist(Inifile.get(SettingTag, 'LINE_STYLE'), return_list = True)
        LINE_WIDTH = Inifile.get(SettingTag, 'LINE_WIDTH')
        XLABEL_INT = Inifile.get(SettingTag, 'XLABEL_INT')
        YLABEL_INT = Inifile.get(SettingTag, 'YLABEL_INT')
        XLIM = Inifile.get(SettingTag, 'XLIM')
        YLIM = Inifile.get(SettingTag, 'YLIM')
        XTICK = Inifile.get(SettingTag, 'XTICK')
        YTICK = Inifile.get(SettingTag, 'YTICK')
        XLOG = Inifile.get(SettingTag, 'XLOG')
        YLOG = Inifile.get(SettingTag, 'YLOG')
        Num_DataLabel = len(YList)
        Val_MinXelement =  min([min(X) for X in XList])
        Val_MaxXelement =  max([max(X) for X in XList])
        Val_MinYelement =  min([min(Y) for Y in YList])
        Val_MaxYelement =  max([max(Y) for Y in YList])
        """
        Matplotlib Axes Plot
        """
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        for i in range(Num_DataLabel):
            ax.plot(XList[i], YList[i],
            label = LabelList[i],
            marker = MARKER[i],
            linestyle = LINE_STYLE[i],
            linewidth = LINE_WIDTH)
        ax.set_xlabel(XLabel, fontsize = FONT_SIZE)
        ax.set_ylabel(YLabel, fontsize = FONT_SIZE)
        legend = ax.legend(bbox_to_anchor = (0, 1, 1.05, 0.12), fontsize = FONT_SIZE, ncol = 3)
        if Check.isnum(XLABEL_INT): ax.get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))
        if Check.isnum(YLABEL_INT): ax.get_yaxis().set_major_locator(ticker.MaxNLocator(integer=True))
        if Check.isnumlist(XLIM): ax.set_xlim(Check.isnumlist(XLIM, return_list = True))
        if Check.isnumlist(YLIM): ax.set_ylim(Check.isnumlist(YLIM, return_list = True))
        if Check.isnum(XTICK): ax.set_xticks(np.arange(Val_MinXelement, Val_MaxXelement + 1, Check.isnum(XTICK, return_float = True)))
        if Check.isnum(YTICK): ax.set_yticks(np.arange(Val_MinYelement, Val_MaxYelement + 1, Check.isnum(YTICK, return_float = True)))
        if Check.istrue(XLOG): ax.set_xscale('log')
        if Check.istrue(YLOG): ax.set_yscale('log')
        plt.savefig(os.path.join(SAVE_DIR, OutFileName), bbox_extra_artists = (legend,), bbox_inches = "tight")