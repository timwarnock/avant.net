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
top16neg = 'ofsrdanluetmcwhi'
def num16alpha(num):
    chars = []
    toggle = 0
    while num > 0:
        num, d = divmod(num, 16)
        if toggle % 2 == 0:
          chars.append(top16pos[d])
        else:
          chars.append(top16neg[d])
        toggle += 1
    return ''.join(reversed(chars))


top16pos = 'etaoinshrdlcumwf'
def num16alpha(num):
    chars = []
    while num > 0:
        num, d = divmod(num, 16)
        chars.append(top16pos[d])
    return ''.join(reversed(chars))


def geta(n):
  return num16alpha(mixb(n,5))


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


