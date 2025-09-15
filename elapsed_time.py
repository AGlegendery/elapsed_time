# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(AG_legend)s
"""

import time


def timer_start():
    '''
    

    Returns nothing and starts the time prosess 
    
    -------
    Warning!! 
    dont use this function without the timer_end() function

    '''
    global start
    start = time.time()
    
def timer_end():
    '''
    

    Returns nothing and end the time prosess
    -------
    None.

    '''
    global elapsed
    elapsed = time.time() - start
    
def elapsed_time():
    '''
    

    Returns the elapsed time of your entier progeram
    -------
    use this with out print 

    '''
    print(f"time elapsed: {elapsed:.2f} seconds")
    



    