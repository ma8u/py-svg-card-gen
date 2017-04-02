#!/usr/bin/python
#coding:utf-8
# Author:  ma8u
# Purpose: card generator
# Created: 24.03.2017
# Copyright (C) 2017, Mathios Psaltis
# License: MIT License

try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import svgwrite

class card():

    def __init__(self,data,data_row,filename):

        self.data=data
        self.data_row=data_row
        self.filename=filename

    def sqr3(self):
        "Read csv file, define line of source to be used and svg filename."

        file=open(self.data)
        header=file.readline()
        datax=file.readlines()

        item=datax[self.data_row].split()

        dwg = svgwrite.Drawing(self.filename,(489,489))

#first row cubes
        dwg.add(dwg.rect(insert=(10, 10), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(170, 10), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(330, 10), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))

#second row cubes
        dwg.add(dwg.rect(insert=(10, 170), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(170, 170), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(330, 170), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))

#third row cubes
        dwg.add(dwg.rect(insert=(10, 330), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(170, 330), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(330, 330), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))

#block of data from file
        dwg.add(dwg.text(item[0], (20,30),font_family="fantasy", font_size='15',text_anchor='start', fill='black'))
        dwg.add(dwg.text(item[1], (180,30),font_family="fantasy", font_size='15', fill='black'))
        dwg.add(dwg.text(item[2], (340,30),font_family="fantasy", font_size='15', fill='black'))
        dwg.add(dwg.text(item[3], (20,190),font_family="fantasy", font_size='15', fill='black'))
        dwg.add(dwg.text(item[4], (180,190),font_family="fantasy", font_size='15', fill='black'))
        dwg.add(dwg.text(item[5], (340,190),font_family="fantasy", font_size='15', fill='black'))
        dwg.add(dwg.text(item[6], (20,350),font_family="fantasy", font_size='15', fill='black'))
        dwg.add(dwg.text(item[7], (180,350),font_family="fantasy", font_size='15', fill='black'))
        dwg.add(dwg.text(item[8], (340,350),font_family="fantasy", font_size='15', fill='black'))
        dwg.save()




    def sqr3m(self):
        "Read csv file, define line of source to be used and svg filename, text in the middle."

        file=open(self.data)
        header=file.readline()
        datax=file.readlines()

        item=datax[self.data_row].split()

        dwg = svgwrite.Drawing(self.filename,(489,489))

#first row cubes
        dwg.add(dwg.rect(insert=(10, 10), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(170, 10), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(330, 10), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))

#second row cubes
        dwg.add(dwg.rect(insert=(10, 170), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(170, 170), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(330, 170), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))

#third row cubes
        dwg.add(dwg.rect(insert=(10, 330), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(170, 330), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))
        dwg.add(dwg.rect(insert=(330, 330), size=(150, 150),
                                fill='white', stroke='black', stroke_width=3))

#block of data from file
        dwg.add(dwg.text(item[0], (85,90),font_family="fantasy", font_size='25',text_anchor='middle', fill='black'))
        dwg.add(dwg.text(item[1], (245,90),font_family="fantasy", font_size='25',text_anchor='middle', fill='black'))
        dwg.add(dwg.text(item[2], (405,90),font_family="fantasy", font_size='25',text_anchor='middle', fill='black'))
        dwg.add(dwg.text(item[3], (85,250),font_family="fantasy", font_size='25',text_anchor='middle', fill='black'))
        dwg.add(dwg.text(item[4], (245,250),font_family="fantasy", font_size='25',text_anchor='middle', fill='black'))
        dwg.add(dwg.text(item[5], (405,250),font_family="fantasy", font_size='25',text_anchor='middle', fill='black'))
        dwg.add(dwg.text(item[6], (85,410),font_family="fantasy", font_size='25',text_anchor='middle', fill='black'))
        dwg.add(dwg.text(item[7], (245,410),font_family="fantasy", font_size='25',text_anchor='middle', fill='black'))
        dwg.add(dwg.text(item[8], (405,410),font_family="fantasy", font_size='25',text_anchor='middle', fill='black'))
        dwg.save()
