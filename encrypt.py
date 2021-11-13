from Cipher.aux import *

def permute (a):
	def f(b):
		def g (c):
			return a[c]
		return "".join([g(0), g(5), g(10), g(7), g(4), g(9), g(14), g(19), g(11), g(8), g(13), g(18), g(2), g(15), g(12), g(17), g(1), g(6), g(3), g(16)])
	res = ""
	for d in split(a, 20):
		res += f(d)
	return res

def sub (a):
	a = split(a, 2)
	res = ""
	for b in a:
		res += (f2[int(b)])
	return res

def sum (a):
