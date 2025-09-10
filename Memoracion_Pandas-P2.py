#!/usr/bin/env python
# coding: utf-8

# # Memoracion, Jancen Johan
# # 2ECEB
# # Programming Assignment 3
# **Problem 2**

#Syntax
import pandas as pd
cars = pd.read_csv('cars.csv')
cars.iloc[:5, ::2]
cars[0:1]
cars.loc[[23], ['Model', 'cyl']]
cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]

