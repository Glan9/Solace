"""
This file defines a dict containing all operators.
Each operator is a list of three components: [arity, vectorization, lambda]

arity:         How many arguments it accepts
vectorization: The vectorization behaviour
lambda:        The function to call to execute it

Vectorization:

The vectorization behaviour is deteremined by flags:

0 Does not vectorize
1 Normal vectorization
2 Vectorizes only over the first argument (only for dyads)
3 Vectorizes only over the second argument (only for dyads)

Lambdas for dyadic operators should accept x and y
Lambdas for monadic operators should accept z

"""

import sys

def flatten(z):
	if type(z) == int:
		return [z]
	result = []
	for sub in z:
		if type(sub)==int:
			result += [sub]
		else:
			result += flatten(sub)
	return result

def gcd(x, y):
	remainder = x%y
	while remainder != 0:
		x = y
		y = remainder
		remainder = x%y
	return y



ops = {
	'!': [
		1,
		1,
		lambda z: 1 if z==0 else 0
	],
	'#': [
		2,
		3,
		lambda x,y: x[y%len(x)]
	],
	'$': [
		
	],
	'%': [ # Modulus
		2,
		1,
		lambda x,y: x%y
	],
	'&': [ # Bitwise AND
		2,
		1,
		lambda x,y: x&y
	],
	'*': [
		2,
		1,
		lambda x,y: x*y
	],
	'+': [ # Addition
		2,
		1,
		lambda x,y: x+y
	],
	'-': [
		2,
		1,
		lambda x,y: x-y
	],
	'.': [
		1,
		1,
		lambda z: [i for i in range(z)]
	],
	'/': [
		2,
		1,
		lambda x,y: int(x/y)
	],
	':': [ # Concatenation
		2,
		0,
		lambda x,y: ([x] if type(x)==int else x)+([y] if type(y)==int else y)
	],
	';': [
		
	],
	'<': [ # Less than
		2,
		1,
		lambda x,y: 1 if x<y else 0
	],
	'=': [ # Equal
		2,
		1,
		lambda x,y: 1 if x==y else 0
	],
	'>': [ # Greater than
		2,
		1,
		lambda x,y: 1 if x>y else 0
	],
	'?': [ # Compare
		2,
		1,
		lambda x,y: -1 if x<y else (0 if x==y else 1)
	],
	'A': [
		
	],
	'B': [
		
	],
	'C': [
		
	],
	'D': [
		
	],
	'E': [ # Equivalent
		2,
		0,
		lambda x,y: 1 if x == y else 0
	],
	'F': [ # Flatten
		1,
		0,
		lambda z: flatten(z)
	],
	'G': [
		2,
		1,
		lambda x,y: gcd(x,y)
	],
	'H': [
		
	],
	'I': [
		
	],
	'J': [
		
	],
	'K': [
		
	],
	'L': [
		2,
		1,
		lambda x,y: x*y/gcd(x,y)
	],
	'M': [
		
	],
	'N': [
		
	],
	'O': [
		
	],
	'P': [
		
	],
	'Q': [
		
	],
	'R': [
		
	],
	'S': [
		1,
		0,
		lambda z: sorted(flatten(z))
	],
	'T': [
		
	],
	'U': [
		
	],
	'V': [
		
	],
	'W': [
		
	],
	'X': [
		2,
		1,
		lambda x,y: x**y
	],
	'Y': [
		
	],
	'Z': [
		
	],
	'[': [
		
	],
	'\\': [
		
	],
	']': [
		
	],
	'^': [ # Bitwise XOR
		2,
		1,
		lambda x,y: x^y
		
	],
	'_': [
		
	],
	'`': [
		
	],
	'a': [
		1,
		1,
		lambda z: -z if z<0 else z
	],
	'b': [
		
	],
	'c': [
		
	],
	'd': [
		
	],
	'e': [
		
	],
	'f': [
		
	],
	'g': [
		
	],
	'h': [
		
	],
	'i': [
		
	],
	'j': [
		
	],
	'k': [
		
	],
	'l': [
		1,
		0,
		lambda z: len([z] if type(z)==int else z)
	],
	'm': [
		
	],
	'n': [
		
	],
	'o': [
		
	],
	'p': [
		1,
		0,
		lambda z: sys.stdout.write(''.join([(chr(i) if i>=0 else '') for i in flatten(z)])) and None
	],
	'q': [
		1,
		0,
		lambda z: sys.stdout.write(str(z)) and None
	],
	'r': [
		
	],
	's': [
		
	],
	't': [
		
	],
	'u': [
		
	],
	'v': [
		
	],
	'w': [
		
	],
	'x': [
		2,
		3,
		lambda x,y: ([x] if type(x)==int else x)*y
	],
	'y': [
		
	],
	'z': [
		
	],
	'|': [ # Bitwise OR
		2,
		1,
		lambda x,y: x|y
		
	],
	'~': [ # Bitwise NOT
		1,
		1,
		lambda z: ~z
	]
}