#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 08:48:41 2018

@author: mm82089
"""
import numpy as np
import pandas as pd
import seaborn as sns

from itertools import combinations

# Example datasets
dat = pd.read_csv("~/Desktop/dat.csv", parse_dates=["date_created_customer",
                                                    "date_created_policy", 
                                                    "date_submitted_app"])
mtcars = pd.read_csv("~/Desktop/mtcars.csv")
titanic = pd.read_csv("~/Desktop/titanic.csv")

# Multivariate plots

def multivar_plot(df, target):
    
    # Store columns by type
    type_bool = df.select_dtypes(include=['bool'])
    type_num = df.select_dtypes(include=['float64'])
    type_discrete = df.select_dtypes(include=['int', 'category'])
    type_date = df.select_dtypes(include=['datetime'])
    
    type_unique = pd.DataFrame()
    type_const = pd.DataFrame()
    temp = pd.DataFrame()
    
    # Unique and constant data types
    for var in df:
        if dat[var].nunique() >= df.size * 0.9:
            type_unique.append(pd.DataFrame(var))
            
        elif dat[var].nunique() == 1:
            type_const.append(pd.DataFrame(var))
    
    # Plot hist and scatterplot of num vars
    if type_num.shape[1] != 0:
        comb = combinations(type_num.columns.values, 2)
        for i in list(comb):
            sns.jointplot(i[0], i[1], data=type_num, kind='reg');
        
    # Plot num var by date var: time series
    if type_date.shape[1] != 0 and type_discrete.shape[1] != 0:
        temp = type_date.join(pd.DataFrame(type_discrete))
        for date_var in type_date:
            for dis_var in type_discrete:
                sns.factorplot(date_var.year, data=temp, aspect=4.0, kind='count',
                               hue=dis_var)
        # Reset temp
        temp = pd.DataFrame()
    
    # Check conditions to segment by cat/int var (e.g. residual between segmented
    # num vars negative/positive?)
        
    
    # Plot num var segmented by binary var
    if type_num.shape[1] != 0 and type_bool.shape[1] != 0:
        temp = type_num.join(pd.DataFrame(type_bool))
        for num_var in type_num:
            for binary_var in type_bool:
                sns.kdeplot(temp[num_var][temp[binary_var]==temp[binary_var].values[0]],
                            label=np.array(set(temp[binary_var].values)), shade=True)
                sns.kdeplot(temp[num_var][temp[binary_var]==temp[binary_var].values[1]],
                            label=temp[binary_var].values, shade=True)
        
        # Reset temp
        temp = pd.DataFrame()
   
    # Plot two num vars segmented by cat var
    
     
    # Plot 
    
    

    
    
    