#!/usr/bin/python3


def number():
  n=float(input('Please enter a number: '))
  return n

def sum(x,y):
  return x+y

def sub(x,y):
  return x-y

def times(x,y):
  return(x*y)

def div(x,y):
  return x/y

def arthimetic():
  x=number()
  y=number()
  print( sum(x,y))
  print( sub(x,y))
  print(times(x,y))
  print(div(x,y))
