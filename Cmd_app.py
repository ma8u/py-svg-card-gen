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
from cmd import Cmd

class MyPrompt(Cmd):

    def do_info(self,args):

        print "     Available commands:"
        print " "
        print "     read_file {filename}  Read csv file and print item names."
        print "     count_file {filename} Read csv file and print items sum."
        print "     item_from {filename}  Read csv file, define line of source to be used and read item name."
        print "     sqr3 {filename}       Read csv file, define line of source to be used and create svg file."
        print "     sqr3_all {filename}   Read csv file, create svg files for every line."
        print "     sqr3m_all {filename}  Read csv file, create svg files for every line, text in the middle."
        print "     quit                  Quit this app"
        print " "

    def do_read_file(self,args):
        "Read csv file and print item names."

        num_lines = sum(1 for line in open(args))

        file=open(args)
        data=file.readlines()

        for line in range(0,num_lines-1):
            item=data[line].split()
            print item[9]

    def do_count_file(self,args):
        "Read csv file and print items sum."

        file=open(args)
        header=file.readline()
        data=file.readlines()
        num_lines = sum(1 for line in open(args))

        print "this file has ", num_lines, " items."

    def do_item_from(self,args):
        "Read csv file, define line of source to be used and read item name."

        file=open(args)
        header=file.readline()
        data=file.readlines()

        line=input("define line of source to be used:")
        item=data[line].split()
        print "selected number: ", line, " , item named: ",item[10]


    def do_sqr3(self,args):
        "Read csv file, define line of source to be used and svg filename."

        file=open(args)
        header=file.readline()
        data=file.readlines()

        line=input("define line of source to be used:")
        item=data[line].split()

        filename=raw_input("define filename (.svg):")
        dwg = svgwrite.Drawing(filename,(489,489))

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

    def do_sqr3_all(self,args):
        "Read source csv file, define line of source to be used and svg filename."

        file=open(args)

        data=file.readlines()
        num_lines = sum(1 for line in open(args))

        for line in range(0,num_lines-1):
            item=data[line].split()
            dwg = svgwrite.Drawing('sqr3_all_'+str(line)+'.svg',(489,489))

#template
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
            dwg.add(dwg.text(item[1], (180,30),font_family="fantasy", font_size='15',text_anchor='start', fill='black'))
            dwg.add(dwg.text(item[2], (340,30),font_family="fantasy", font_size='15',text_anchor='start', fill='black'))
            dwg.add(dwg.text(item[3], (20,190),font_family="fantasy", font_size='15',text_anchor='start', fill='black'))
            dwg.add(dwg.text(item[4], (180,190),font_family="fantasy", font_size='15',text_anchor='start', fill='black'))
            dwg.add(dwg.text(item[5], (340,190),font_family="fantasy", font_size='15',text_anchor='start', fill='black'))
            dwg.add(dwg.text(item[6], (20,350),font_family="fantasy", font_size='15',text_anchor='start', fill='black'))
            dwg.add(dwg.text(item[7], (180,350),font_family="fantasy", font_size='15',text_anchor='start', fill='black'))
            dwg.add(dwg.text(item[8], (340,350),font_family="fantasy", font_size='15',text_anchor='start', fill='black'))
            dwg.save()



    def do_sqr3m(self,args):
        "Read csv file, define line of source to be used and svg filename, text in the middle."

        file=open(args)
        header=file.readline()
        data=file.readlines()

        line=input("define line of source to be used:")
        item=data[line].split()

        filename=raw_input("define filename (.svg):")
        dwg = svgwrite.Drawing(filename,(489,489))

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


    def do_sqr3m_all(self,args):
        "Read source csv file, define line of source to be used and svg filename."

        file=open(args)

        data=file.readlines()
        num_lines = sum(1 for line in open(args))

        for line in range(0,num_lines-1):
            item=data[line].split()
            dwg = svgwrite.Drawing('sqr3m_all_'+str(line)+'.svg',(489,489))

#template
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

    def do_quit(self,args):
        "Quits the program."
        print "Quiting..."
        raise SystemExit

if __name__=='__main__':
    prompt=MyPrompt()
    prompt.prompt='>'
    prompt.cmdloop("""Welcome to the py-svg-card-eng prompt...

    Available commands:

    read_file {filename}  Read csv file and print item names.
    count_file {filename} Read csv file and print items sum.
    item_from {filename}  Read csv file, define line of source to be used and read item name.
    sqr3 {filename}       Read csv file, define line of source to be used and create svg file.
    sqr3m {filename}      Read csv file, define line of source to be used and create svg file, text in the middle.
    sqr3_all {filename}   Read csv file, create svg files for every line.
    sqr3m_all {filename}  Read csv file, create svg files for every line, text in the middle.
    quit                  Quit this app
    For a this list of commands print info, for the built-in version print help.
    """)
