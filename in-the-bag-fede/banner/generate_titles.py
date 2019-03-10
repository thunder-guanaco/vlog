#!/usr/bin/python
# -*- coding: utf-8 -*-

template = open('template.kdenlivetitle').read()
csv_file = open('discs.csv')
line = csv_file.readline()[:-1]

while line:

    splitted_line = line.split(',')
    
    amount  = splitted_line[0]
    brand   = splitted_line[1]
    disc    = splitted_line[2]
    plastic = splitted_line[3]
    speed   = splitted_line[4]
    glide   = splitted_line[5]
    turn    = splitted_line[6]
    fade    = splitted_line[7]
    
    # import pdb; pdb.set_trace()
    
    result = template.format(amount=amount, brand=brand, disc=disc,
                             plastic=plastic, speed=speed, glide=glide,
                             turn=turn, fade=fade)

    result_file = open('{} - {}.kdenlivetitle'.format(brand, disc), 'w')
    result_file.write(result)
    result_file.close()

    line = csv_file.readline()[:-1]








