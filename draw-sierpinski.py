#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import turtle
#-----------------------------
#class Point:                 
#    def __init__(self, x, y):
#        self.x = x           
#        self.y = y           
#    def setPos(self, x, y):  
#        self.x = x           
#        self.y = y           
#    def getPos(self, x, y):  
#        return [x, y]        
#    def getX(self, x):       
#        return self.x        
#    def getY(sefl, y):       
#        return self.y        
#    def setX(self, newX):    
#        self.x = newX        
#    def setY(self, newY):    
#        self.y = newY        
#-----------------------------
    
def getMid(point1, point2):
        midX = (point1[0]+ point2[0])/2
        midY = (point1[1]+ point2[1])/2
        return [midX, midY]

def drawTriangle(myTurtle, points, drawcolor):
    myTurtle.pencolor(drawcolor)
    myTurtle.setpos(points[0])
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])

def drawSierpinski(myTurtle, points, degree):
    colormap = ['blue', 'red', 'orange', 'yellow', 'green', 'white']
    colorindex = degree % len(colormap)
    drawTriangle(myTurtle, points, colormap[colorindex])
    if degree > 0:
        points1 = [points[0], getMid(points[0], points[1]), getMid(points[0], points[2])]
        points2 = [points[1], getMid(points[0], points[1]), getMid(points[1], points[2])]
        points3 = [points[2], getMid(points[2], points[1]), getMid(points[0], points[2])]
        drawSierpinski(myTurtle, points1, degree-1)
        drawSierpinski(myTurtle, points2, degree-1)
        drawSierpinski(myTurtle, points3, degree-1)		

import sys
import traceback
def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        myTurtle = turtle.Turtle()
        myWin = turtle.Screen()
        myPoints=[[-100, -50],[0,100], [100,-50]]
        drawSierpinski(myTurtle, myPoints, 4)
        myWin.exitonclick()

    except Exception, err:
        print err.message
        traceback.print_exc()


if __name__ == "__main__":
    main()
