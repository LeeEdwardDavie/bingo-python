#!/usr/bin/env python3

import tkinter as tk
import random as rand

#https://stackoverflow.com/questions/16115378/tkinter-example-code-for-multiple-windows-why-wont-buttons-load-correctly

DrawList = []

def makeDrawList ():
  global DrawList
  numbers = list(range(1,91))
  rand.shuffle(numbers)
  print(len(numbers))
  DrawList = numbers
  print(len(DrawList))

def draw():
  global DrawList
  if len(DrawList) > 0:
    value = DrawList.pop()
  else:
    value = "All Numbers Drawn"
  return value

def stringBuilder(value):
  string = str(rhyme(value)) + ' - number ' + str(value)
  return string

def rhyme (value):
  bingoDict = {
  1: "Kelly's Eye",
  2: "One Little Duck",
  3: "Cup of Tea",
  4: "Knock at the Door",
  5: "Man Alive",
  6: "Tom Mix...Up to his tricks",
  7: "Lucky",
  8: "Garden Gate",
  9: "Doctor's Orders",
  10: "Boris' Den",
  11: "Legs 11",
  12: "One Dozen",
  13: "Unlucky for Some",
  14: "Valentines Day",
  15: "Young and Keen",
  16: "Sweet 16",
  17: "Dancing Queen",
  18: "Coming of Age",
  19: "Goodbye Teens",
  20: "One Score",
  21: "Blackjack",
  22: "Two Little Ducks",
  23: "Three and Me",
  24: "Two Dozen",
  25: "Duck and Dive",
  26: "Pick and Mix",
  27: "Gateway to Heaven",
  28: "Over Weight",
  29: "Rise and Shine",
  30: "Dirty Gertie",
  31: "Get Up and Run",
  32: "Buckle My Shoe",
  33: "Dirt Knee",
  34: "Ask for More",
  35: "Jump and Jive",
  36: "Three Dozen",
  37: "More than 11",
  38: "Christmas Cake",
  39: "Steps",
  40: "Naughty 40",
  41: "Time for Fun",
  42: "Winnie the Pooh",
  43: "Down on Your Knees",
  44: "Droopy Drawers",
  45: "Halfway There",
  46: "Up to Tricks",
  47: "Four and Seven",
  48: "Four Dozen",
  49: "PC",
  50: "Half a Century",
  51: "Tweak of the Thumb",
  52: "Danny La Rue",
  53: "Stuck in the Tree",
  54: "Clean the Floor",
  55: "Snakes Alive",
  56: "Was She Worth it",
  57: "Heinz Varieties",
  58: "Make them Wait",
  59: "Brighton Line",
  60: "Five Dozen",
  61: "Bakers Bun",
  62: "Turn the Screw",
  63: "Tickle Me",
  64: "Red Raw",
  65: "Old Age Pension",
  66: "Clickety Click",
  67: "Made in Heaven",
  68: "Saving Grace",
  69: "Either Way Up",
  70: "Three Score and 10",
  71: "Bang on the Drum",
  72: "Six Dozen",
  73: "Queen B",
  74: "Candy Store",
  75: "Strive and Strive",
  76: "Trombones",
  77: "Sunset Strip",
  78: "Heavens Gate",
  79: "One More Time",
  80: "Eight and Blank",
  81: "Stop and Run",
  82: "Straight On Through",
  83: "Time for Tea",
  84: "Seven Dozen",
  85: "Staying Alive",
  86: "Between the Sticks",
  87: "Torquay in Devon",
  88: "Two Fat Ladies",
  89: "Nearly There",
  90: "Top of the Shop",
  }
  return bingoDict[value]

def GUI():
  def clicked():
    value = draw()
    lbl.configure(text=value)
    if isinstance(value, int):
      print(stringBuilder(value))
  window = tk.Tk()
  window.title("Brilliant Bingo")
  lbl = tk.Label(window, text="Good Luck", font=("Arial Bold", 150))
  lbl.grid(column=5, row=0)
  window.geometry('1024x768')
  btn = tk.Button(window, text="Draw", command=clicked)
  btn.grid(column=1, row=2)
  window.mainloop()

def bingo ():
  makeDrawList()
  GUI()

bingo()
