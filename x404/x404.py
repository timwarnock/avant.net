#!/usr/bin/env python
''' Usage: x404.py command [options]

    Where command includes:
    add [url] * e.g., add http://www.anattatechnologies.com/
    get [key] * e.g., get esza (returns the matching url)
    del [key] * e.g., del esza (removes the matching entry)
    list      * lists all entries

'''
import os
import sys
import math
import sqlite3


def add_url(url):
  conn = sqlite3.connect("URLs.db")
  curs = conn.cursor()
  curs.execute("select count(rowid) from URLS")
  numrows = curs.fetchall()[0][0]
  short_url = getalpha(numrows)
  curs.execute("insert into URLS(short_url, long_url) values(?,?)",(short_url,url))
  conn.commit()
  conn.close()
  return short_url



def revb(n):
  min_digits = 1 + int(math.log(n,16))
  bit_size = 4 * min_digits
  bin_number = bin(n)
  reverse_number = bin_number[-1:1:-1]
  reverse_number = reverse_number + (bit_size - len(reverse_number))*'0'
  return int(reverse_number,2)


def mixb(n):
   min_digits = 1 + int(math.log(n,16))
   bit_size = 4 * min_digits
   bin_number = bin(n)
   reverse_number = bin_number[-1:1:-1]
   reverse_number = reverse_number + (bit_size - len(reverse_number))*'0'
   if reverse_number[0:2] == '00':
     reverse_number = '1' + reverse_number + '0'
   return int(reverse_number,2)


top16pos = 'etaoinshrdlcumwf'
def num16alpha(num):
    chars = []
    while num > 0:
        num, d = divmod(num, 16)
        chars.append(top16pos[d])
    return ''.join(reversed(chars))


def getalpha(n):
  return num16alpha(mixb(n))


'''
is there a collision? where is first collision?
Let's find out :)
'''

def getaC(rmax):
  c = {}
  for i in range(1,rmax):
    min_digits = 1 + int(math.log(i,16))
    bit_size = 4 * min_digits
    def geta(n):
      return num16alpha(mixb(n))
    ''' ok '''
    print i, geta(i), "min_digits", min_digits, "bit_size", bit_size
    if geta(i) in c:
      print "COLLISION AT", geta(i), i, "=",c[geta(i)]
      break
    else:
      c[geta(i)] = i





if __name__ == '__main__':
  ''' optparse? '''
  if len(sys.argv) > 2 and sys.argv[1] == "add":
    short_url = add_url(sys.argv[2])
    while os.path.exists("../%s" % (short_url)):
      print >> sys.stderr, "%s already exists and won't cause a 404" % (short_url)
      short_url = add_url(sys.argv[2])
    print "SUCCESS\nhttp://avant.net/%s" % (short_url)
      




