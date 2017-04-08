# Py-svg-card-gen Project
A python kit that automates the process of generating card-type graphics in svg format based on svgwrite.

## Getting Started
Py-svg-card-gen is a kit for reading csv files and creating card-type graphics on predifined templates. There are two version included, a Cmd type App that has a prompt and can be used to test your settings and a class type script that can be used in your own scripts.

## Cmd_app.py

Launch a prompt that has the following commands:

##### read_file {filename}
_Read csv file and print last item from lines_
##### count_file {filename}
_Read csv file and count items and print sum_
##### item_from {filename}
_Read csv file, define line of source to be used and print last item_


##### sqr3 {filename}        
_Read csv file, define line of source to be used and create type one square 3x3 svg card_
##### sqr3m {filename}       
_Read csv file, define line of source to be used and create type two square 3x3 svg card (text in the middle)_
##### sqr3_all {filename}    
_Read csv file, create type one svg cards for every line_
##### sqr3m_all {filename}   
_Read csv file, create type two svg cards for every line, text in the middle_
##### quit                   
_Quit this app_
##### info                   
_For this list of commands_
##### help                   
_build-in Cmd help_

## Script.py

A script that has a class named card that gets 3 arguments:

#### card(data,data_row,filename)

__data__ 
_(csv file to read)_
__data_row__
_(line of csv file to read)_
__filename__
_(svg file output card)_

and has 2 methods:

#### sqr3(self)
_create type one svg cards from data_row_

#### sqr3m(self)
_create type two svg cards from data_row_

## Prerequisites
This Project needs Python 2.x and svgwrite installed.
