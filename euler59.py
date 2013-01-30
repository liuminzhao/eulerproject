__author__ = 'liuminzhao'

f = open('cipher1.txt', 'r')

text = [int(one) for one in f.read().split(',')]


f.close()