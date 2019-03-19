#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 2:
    print 'Usage: `{} <folder where discs.csv lives>'.format(sys.argv[0])
    sys.exit(1)

template_path = '{}/template.kdenlivetitle'.format(sys.path[0])
folder_path = sys.argv[1]
csv_path = '{}/discs.csv'.format(folder_path)

print 'Using template from {}'.format(template_path)
print 'Reading discs from {}'.format(csv_path)
print 'Writing kdenlivetitle files to {}'.format(folder_path)
print ''

template_file = open(template_path)
csv_file = open(csv_path)

template = template_file.read()

line = csv_file.readline()[:-1]
i = 1

while line:

    try:
        brand, disc, plastic, speed, glide, turn, fade = line.split(',')
    except ValueError as e:
        print 'Error in line {}: {}\nLine was: >>{}<<'.format(i, e, line)
    
    result = template.format(brand=brand, disc=disc, plastic=plastic,
                             speed=speed, glide=glide, turn=turn, fade=fade)

    file_name = '{}/{} - {}.kdenlivetitle'.format(folder_path, brand, disc)
    result_file = open(file_name, 'w')
    result_file.write(result)
    result_file.close()

    print 'Generated {}'.format(file_name)

    line = csv_file.readline()[:-1]
    i = i + 1

print ''
print '{} files were generated'.format(i)








