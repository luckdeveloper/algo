#!/usr/bin/python
# -*- coding: UTF-8 -*-
import turtle

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)


import sys
import traceback
def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:

        myTurtle = turtle.Turtle()
        myWin = turtle.Screen()
        drawSpiral(myTurtle, 100)
        myWin.exitonclick()
        
    except Exception, err:
        print err.message
        traceback.print_exc()


if __name__ == "__main__":
    main()
