# Py-svg-card-gen Project
A python kit that automates the process of generating card-type graphics in svg format based on svgwrite.

## Getting Started
Py-svg-card-gen is a kit for reading csv files and creating card-type graphics on predifined templates. There are two version included, a Cmd type App that has a prompt and can be used to test your settings and a class type script that can be used in your own scripts.

## Cmd_app.py

Launch a prompt that has the following commands:

read_file {filename}  Read csv file and print last item.
count_file {filename} Read csv file and count items and print sum.
item_from {filename}  Read csv file, define line of source to be used and print last item.
sqr3 {filename}       Read csv file, define line of source to be used and create type one square 3x3 svg card.
sqr3m {filename}      Read csv file, define line of source to be used and create type two square 3x3 svg card (text in the middle).
sqr3_all {filename}   Read csv file, create type one svg cards for every line.
sqr3m_all {filename}  Read csv file, create type two svg cards for every line, text in the middle.
quit                  Quit this app.
info                  For this list of commands.
help                  build-in Cmd help version.

## Script.py

A script that has a class named card that gets 3 arguments:

card(data,data_row,filename)

data          csv file to read.
data_row      line of csv file to read.
filename      svg output card.

and has 2 methods:

sqr3(self)    create type one svg cards for every line.
sqr3m(self)   create type two svg cards for every line.

## Prerequisites
This Project needs Python 2.x and svgwrite installed.
