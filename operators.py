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

ops = {
	'!': [
		1,
		1,
		lambda z: 1 if z==0 else 0
	],
	'#': [
		
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
	'<': [
		
	],
	'=': [
		
	],
	'>': [
		
	],
	'?': [
		
	],
	'@': [
		
	],
	'A': [
		
	],
	'B': [
		
	],
	'C': [
		
	],
	'D': [
		
	],
	'E': [
		
	],
	'F': [
		
	],
	'G': [
		
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
		1,
		0,
		lambda z: len([z] if type(z)==int else z)
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
		
	],
	'm': [
		
	],
	'n': [
		
	],
	'o': [
		
	],
	'p': [
		
	],
	'q': [
		1,
		0,
		lambda z: print(z)
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