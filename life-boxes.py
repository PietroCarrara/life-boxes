#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 pietro <pietro@the-arch>
#
# Distributed under terms of the MIT license.

"""
Draws a box foreach week of a life
Boxes in black are the ones you've used
"""

from PIL import Image

# How many weeks do we have in a year? (I don't think anyone wants to change it)
WEEKS_IN_YEAR = 52

# A box is a square, so only one number is needed
BOX_SIZE = 20
# Gaps
BOX_GAPS = 8

# Your age in weeks
TOTAL_AGE = 959

# How many years do you expect to live
TOTAL_TIME_YEARS = 85

# How many years to display in a single row?
YEARS_PER_ROW = 2

# Calculating total rows we will display
TOTAL_ROWS = TOTAL_TIME_YEARS // YEARS_PER_ROW
if (TOTAL_TIME_YEARS % YEARS_PER_ROW > 0):
    TOTAL_ROWS += 1

# Main canvas
main = Image.new("RGB", (WEEKS_IN_YEAR * YEARS_PER_ROW * BOX_SIZE, TOTAL_ROWS * BOX_SIZE))
# Make it white
main.paste( (128,128,128), [0,0,main.size[0],main.size[1]])

# White and black square
wsq = Image.new("RGB", (BOX_SIZE - BOX_GAPS, BOX_SIZE - BOX_GAPS))
wsq.paste( (255, 255, 255), [0,0,wsq.size[0],wsq.size[1]])

bsq = Image.new("RGB", (BOX_SIZE - BOX_GAPS, BOX_SIZE - BOX_GAPS))

# We begin using black squares
curr = bsq

x = 0
y = 0
for i in range(TOTAL_TIME_YEARS * WEEKS_IN_YEAR):

    # If we got past our age, white it up
    if (i >= TOTAL_AGE):
        curr = wsq

    main.paste(curr, (x * BOX_SIZE + BOX_GAPS // 2, y * BOX_SIZE + BOX_GAPS // 2))

    x += 1

    # If we got to the end of the line, go down a level
    if (x >= WEEKS_IN_YEAR * YEARS_PER_ROW):
        x = 0
        y += 1

main.save("out.png")
