#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 17:12:17 2021

@author: abhishek
"""
import pyautogui as x

x.click()
x.click('search.png')
x.move(100,100)
x.doubleClick("search.png")


currentMouseX, currentMouseY = x.position()


#Search using 
search_cor=(537,156)

x.click(search_cor)
x.write('React', interval=0.25)
x.press('enter')


jobs=(477,226)
x.click(jobs)