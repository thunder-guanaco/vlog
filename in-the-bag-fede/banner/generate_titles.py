#!/usr/bin/python
# -*- coding: utf-8 -*-

template = open('template.kdenlivetitle').read()
csv_file = open('discs.csv')
line = csv_file.readline()[:-1]

while line:

    splitted_line = line.split(',')
    
    brand   = splitted_line[0]
    disc    = splitted_line[1]
    plastic = splitted_line[2]
    speed   = splitted_line[3]
    glide   = splitted_line[4]
    turn    = splitted_line[5]
    fade    = splitted_line[6]
    
    # import pdb; pdb.set_trace()
    
    result = template.format(brand=brand, disc=disc, plastic=plastic,
                             speed=speed, glide=glide, turn=turn, fade=fade)

    result_file = open('{} - {}.kdenlivetitle'.format(brand, disc), 'w')
    result_file.write(result)
    result_file.close()

    line = csv_file.readline()[:-1]








