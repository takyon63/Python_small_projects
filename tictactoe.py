# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:10:21 2018

@author: takyon
TicTacToe game
"""
theBoard={'top-L': ' ', 'top-M': ' ','top-R': ' ',
          'mid-L': ' ', 'mid-M': ' ','mid-R': ' ',
          'low-L': ' ', 'low-M': ' ','low-R': ' ' }

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)


    
