#!/usr/bin/python3
import sys

def factorize(line):
    for i in range(line):
        if line % (i+2) == 0:
            print("{}={}*{}".format(line, line//(i+2), (i+2)))
            break

with open(sys.argv[1], "r") as file:
    newline = " "
    for readline in file:
        line_strip = int(readline.replace('\n', " "))
        factorize(line_strip)
