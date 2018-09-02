#!/usr/bin/python     
import sys    
import time    
from Quartz.CoreGraphics import *      
from threading import Timer
from datetime import datetime


def _mouseEvent(type, posx, posy):    
    theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)    
    CGEventPost(kCGHIDEventTap, theEvent)    
        
def mouseMove(posx, posy):    
    _mouseEvent(kCGEventMouseMoved, posx, posy)    
        
def mouseClickDown(posx, posy):    
    _mouseEvent(kCGEventLeftMouseDown, posx, posy)    
        
def mouseClickUp(posx, posy):    
    _mouseEvent(kCGEventLeftMouseUp, posx, posy)    
        
def mouseDrag(posx, posy):    
    _mouseEvent(kCGEventLeftMouseDragged, posx, posy)    
        
def mouseClick(posx, posy):    
    '''''''perform a left click'''    
    _mouseEvent(kCGEventLeftMouseDown, posx, posy)    
    _mouseEvent(kCGEventLeftMouseUp, posx, posy)    
        
def mouseRightClick(posx, posy):    
    theEvent = CGEventCreateMouseEvent(None, kCGEventRightMouseDown, (posx,posy), kCGMouseButtonRight)    
    CGEventPost(kCGHIDEventTap, theEvent)    
    theEvent2 = CGEventCreateMouseEvent(None, kCGEventRightMouseUp, (posx,posy), kCGMouseButtonRight)    
    CGEventPost(kCGHIDEventTap, theEvent2)    
    
def mouseDoubleClick(posx, posy):    
    '''''''perfrom a double left click'''    
    theEvent = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, (posx,posy), kCGMouseButtonLeft);      
    CGEventPost(kCGHIDEventTap, theEvent);      
    CGEventSetType(theEvent, kCGEventLeftMouseUp);      
    CGEventPost(kCGHIDEventTap, theEvent);     
    CGEventSetIntegerValueField(theEvent, kCGMouseEventClickState, 2);       
    CGEventSetType(theEvent, kCGEventLeftMouseDown);      
    CGEventPost(kCGHIDEventTap, theEvent);      
    CGEventSetType(theEvent, kCGEventLeftMouseUp);     
    CGEventPost(kCGHIDEventTap, theEvent);    
    
    
    
if __name__ == '__main__':    
    ourEvent = CGEventCreate(None);    
    currentpos=CGEventGetLocation(ourEvent); # Save current mouse position     
    time.sleep(1);    
    mouseMove(200,200);
    mouseMove(300,300);
    mouseMove(1100,375);
    
