# -*- coding: utf-8 -*-

"""Main module."""
import re

class LEDTester:
    
    lights = None
    
    def __init__(self, N):
        self.lights = [[False]*N for _ in range(N)]
        
    def apply(self, led_cmd):
        on_pat = re.compile(".*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        off_pat = re.compile(".*(turn off)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        switch_pat = re.compile(".*(switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        on = on_pat.match(led_cmd)
        off = off_pat.match(led_cmd)
        switch = switch_pat.match(led_cmd)
        
        if on:
            point1_x = on.group(2)
            print(point1_x)
            point1_y = on.group(3)
            print(point1_y)
            point2_x = on.group(4)
            print(point2_x)
            point2_y = on.group(5)
            print(point2_y)
            
            for i in range(int(point1_x), int(point2_x)+1):
                for j in range(int(point1_y), int(point2_y)+1):
                    self.lights[i][j] = True
            
        elif off:
            point1_x = off.group(2)
            print(point1_x)
            point1_y = off.group(3)
            print(point1_y)
            point2_x = off.group(4)
            print(point2_x)
            point2_y = off.group(5)
            print(point2_y)
            
            for i in range(int(point1_x), int(point2_x)+1):
                for j in range(int(point1_y), int(point2_y)+1):
                    self.lights[i][j] = False
        elif switch:
            point1_x = switch.group(2)
            print(point1_x)
            point1_y = switch.group(3)
            print(point1_y)
            point2_x = switch.group(4)
            print(point2_x)
            point2_y = switch.group(5)
            print(point2_y)
            
            for i in range(int(point1_x), int(point2_x)+1):
                for j in range(int(point1_y), int(point2_y)+1):
                    if self.lights[i][j] == True:
                        self.lights[i][j] = False
                    else:
                        self.lights[i][j] = True
    
    def count(self):
        count = 0
        numrows = len(self.lights)
        numcols = len(self.lights[0])
        
        for i in range(0, numrows):
                for j in range(0, numcols):
                    if self.lights[i][j] == True:
                        count += 1
        return count