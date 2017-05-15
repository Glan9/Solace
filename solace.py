#!/usr/bin/env python3

import sys
import re

numRegex = '^-?\\d+(,-?\\d+)*'
stringRegex = '^"((\\"|[^"])*?)"'
charRegex = "^'([\s\S])"
arity1Suffixes = '*+<>EMOPR'
arity2Suffixes = '?'

"""
OPERATORS

Here we define a dict containing all operators, and a dict of all extended operators
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
Lambdas for niladic operators should accept no arguments

"""

def flatten(z): # For operator _
	if type(z) == int:
		return [z]
	result = []
	for sub in z:
		if type(sub)==int:
			result += [sub]
		else:
			result += flatten(sub)
	return result

def gcd(x, y): # For operator G
	remainder = x%y
	while remainder != 0:
		x = y
		y = remainder
		remainder = x%y
	return y

def find(x, y): # For operator f
	for i in range(len(x)):
		if x[i:i+len(y)] == y:
			return i
	return -1

def readByte(): # For operator k
	byte = sys.stdin.read(1)
	return -1 if len(byte)==0 else ord(byte)

def readLine(): # For operator j
	line = sys.stdin.readline()
	if line[-1] == '\n':
		return line[:-1]
	else:
		return line
	
def primeFactors(n): # For operator F
    factors = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            factors.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       factors.append(n)
    return factors

operators = {
	'!': [ # Logical NOT
		1,
		1,
		lambda z: 1 if z==0 else 0
	],
	'#': [ # Index
		2,
		3,
		lambda x,y: 0 if len(x)==0 else ([x] if type(x)==int else x)[y%len([x] if type(x)==int else x)]
	],
	'$': [ # Copy
		1,
		0,
		lambda z: [z, z]
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
	'(': [ # Slice before
		2,
		3,
		lambda x,y: x[:y]
	],
	')': [ # Slice after
		2,
		3,
		lambda x,y: x[y:]
	],
	'*': [ # Multiplication
		2,
		1,
		lambda x,y: x*y
	],
	'+': [ # Addition
		2,
		1,
		lambda x,y: x+y
	],
	'-': [ # Subtraction
		2,
		1,
		lambda x,y: x-y
	],
	'.': [ # Range
		1,
		1,
		lambda z: [i for i in range(z)]
	],
	'/': [ # Division
		2,
		1,
		lambda x,y: x//y
	],
	':': [ # Concatenation
		2,
		0,
		lambda x,y: ([x] if type(x)==int else x)+([y] if type(y)==int else y)
	],
	';': [ # Wrap
		1,
		0,
		lambda z: [z]
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
	'C': [ # Cartesian product
		2,
		0,
		lambda x,y: [[i, j] for i in x for j in y]
	],
	'D': [
		
	],
	'E': [ # Equivalent
		2,
		0,
		lambda x,y: 1 if x == y else 0
	],
	'F': [ # Prime factors
		1,
		1,
		lambda z: primeFactors(z)
	],
	'G': [ # GCD
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
	'L': [ # LCM
		2,
		1,
		lambda x,y: x*y//gcd(x,y)
	],
	'M': [ # Minimum
		2,
		1,
		lambda x,y: x if x>y else y
	],
	'N': [ # Maximum
		2,
		1,
		lambda x,y: x if x<y else y
	],
	'O': [ # Sort
		1,
		0,
		lambda z: sorted(flatten(z))
	],
	'P': [
		
	],
	'Q': [ # Deduplicate
		
	],
	'R': [ # Reverse
		1,
		0,
		lambda z: ([z] if type(z)==int else z)[::-1]
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
	'X': [ # Exponentiation
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
	'_': [ # Flatten
		1,
		0,
		lambda z: flatten(z)
	],
	'`': [
		
	],
	'a': [ # Absolute value
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
	'f': [ # Find
		2,
		0,
		lambda x,y: find([x] if type(x)==int else x, [y] if type(y)==int else y)
	],
	'g': [
		
	],
	'h': [
		
	],
	'i': [ # Read line + eval
		0,
		0,
		lambda: interpret(readLine(), [])
	],
	'j': [ # Read line
		0,
		0,
		lambda: [ord(c) for c in readLine()]
	],
	'k': [ # Read byte
		0,
		0,
		lambda: readByte()
	],
	'l': [ # Length
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
	'p': [ # Print as string
		1,
		0,
		lambda z: print(''.join([(chr(i) if i>=0 else '') for i in flatten(z)]))
	],
	'q': [ # Print as list
		1,
		0,
		lambda z: print(str(z))
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
	'x': [ # Repititon
		2,
		3,
		lambda x,y: ([x] if type(x)==int else x)*y
	],
	'y': [ # Sign
		1,
		1,
		lambda z: -1 if z<0 else (1 if z>0 else 0)
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

extOperators = {
	'(': [ # Rotate left
		2,
		3,
		lambda x,y: x[y:]+x[:y]
	],
	')': [ # Rotate right
		2,
		3,
		lambda x,y: x[-y:]+x[:-y]
	],
	'<': [ # Bitshift left
		2,
		1,
		lambda x,y: x << y
	],
	'>': [ # Bitshift right
		2,
		1,
		lambda x,y: x >> y
	],
	'j': [ # Read all input
		0,
		0,
		lambda: [ord(c) for c in sys.stdin.read()]
	]
}


"""
depth(o)

Returns the depth of object o. If o is an integer, its depth is 0.
Otherwise, the depth is the maximum level of nesting in the list o.
"""
def depth(o):
	if type(o) != list:
		return 0
	elif len(o) == 0:
		return 1
	else:
		return 1+max(depth(x) for x in o)


"""
applyDyad(op, x, y)

Given an operator and two arguments, execute it performing the correct vectorization.
Return the result.
"""
def applyDyad(op, x, y):
	if op[1] == 0:
		return op[2](x, y)
	elif op[1] == 1:
		if depth(x) == 0 and depth(y) == 0:
			return op[2](x, y)
		elif depth(x) == depth(y):
			num = min(len(x), len(y))
			return [applyDyad(op, x[i], y[i]) for i in range(num)] + x[num:] + y[num:]
		elif depth(x) < depth(y):
			return [applyDyad(op, x, i) for i in y]
		elif depth(x) > depth(y):
			return [applyDyad(op, i, y) for i in x]
	elif op[1] == 2:
		if depth(x) == 0:
			return op[2](x, y)
		else:
			return [applyDyad(op, i, y) for i in x]
	elif op[1] == 3:
		if depth(y) == 0:
			return op[2](x, y)
		else:
			return [applyDyad(op, x, i) for i in y]


"""
applyMonad(op, z)

Given an operator and one argument, execute it performing the correct vectorization.
Return the result.
"""
def applyMonad(op, z):
	if op[1] == 0:
		return op[2](z)
	else:
		if depth(z) == 0:
			return op[2](z)
		else:
			return [applyMonad(op, i) for i in z]


"""
executeOp(op)

Given an operator, execute it. Errors if not enough elements on the stack.
Return the result.
"""
def executeOp(op, stack, char):
	if len(stack) < op[0]: # Not enough arguments available
		sys.stderr.write("Error on operator '"+char+"': Not enough arguments\n")
		exit(1)
	else:
		if op[0] == 0: # It's a nilad
			return op[2]()
		if op[0] == 1: # It's a monad
			z = stack.pop()
			return applyMonad(op, z)
		if op[0] == 2: # It's a dyad
			y = stack.pop()
			x = stack.pop()
			return applyDyad(op, x, y)

"""
executeBlock(block, suffix, stack, block2='')

Given a block and its suffix, and the current stack, execute the block.
block2 is an optional argument for arity 2 suffixes.
"""
def executeBlock(block, suffix, stack, block2=''):
	if suffix == '':
		stack += interpret(block, stack)
	if suffix == 'E': # Each
		z = stack.pop()
		results = []
		for item in ([z] if type(z)==int else z):
			results += interpret(block, [item])
		stack.append(results)
	if suffix == '?': # Conditional
		cond = stack.pop() # Should we run block 1 or block 2?
		if (type(cond)==int and cond != 0) or (type(cond)==list and len(cond) != 0):
			interpret(block, stack)  # Run first if cond is truthy
		else:  
			interpret(block2, stack) # Run second if cond is falsy
	if suffix == 'R': # Reduce
		z = stack.pop()
		if len(z)==0:
			stack.append(z)
		else:
			stack.append(z[0])
			z = z[1:]
			for item in z:
				stack.append(item)
				interpret(block, stack)
	if suffix == '+': # Accumulate
		z = stack.pop()
		result = []
		for i in range(len(z)):
			result.append(z[:i+1])
			executeBlock(block, 'R', result)
		stack.append(result)





"""
interpret(code, stack)

Interprets the Solace code in the string code. The initial stack is passed an argument.
Returns the final stack at the end of the code.

"""
def interpret(code, stack):
	while len(code) > 0:

		if re.match(numRegex, code) != None:
			nums = [int(s) for s in re.match(numRegex, code).group(0).split(',')]
			stack += [nums] if len(nums)>1 else nums
			code = re.sub(numRegex,'',code)
			continue
		elif re.match(stringRegex, code) != None:
			stack += [[ord(c) for c in re.match(stringRegex, code).group(1)]]
			code = re.sub(stringRegex,'',code)
			continue
		elif re.match(charRegex, code) != None:
			stack += [ord(re.match(charRegex, code).group(1))]
			code = re.sub(charRegex,'',code)
			continue
		elif code[0] == '{':
			blocks = [] # The blocks appearing all directly in a row

			# Search for a series of consecutive blocks
			while len(code) > 0 and code[0] == '{':
				code = code[1:]
				block = ''
				depth = 1
				while depth>0:
					if len(code) == 0:
						print("Error: Unclosed block")
						exit(1)

					block += code[0]
					if code[0] == '{':
						depth += 1
					elif code[0] == '}':
						depth -= 1
					code = code[1:]

				block = block[:-1]
				blocks += [block]
			
			# After finding them...

			if len(code) == 0:
				# If there's no suffix
				for b in blocks:
					executeBlock(b, '', stack)
			elif code[0] in arity1Suffixes:
				# If there's an arity 1 suffix
				suffix = code[0]
				code = code[1:]
				for b in blocks[:-1]:
					executeBlock(b, '', stack)
				executeBlock(blocks[-1], suffix, stack)
			elif code[0] in arity2Suffixes:
				if len(blocks) >= 2:
					# If there's an arity 2 suffix and at least 2 blocks
					suffix = code[0]
					code = code[1:]
					for b in blocks[:-2]:
						executeBlock(b, '', stack)
					executeBlock(blocks[-2], suffix, stack, block[-1])
				else:
					# If there's an arity 2 suffix but not 2 blocks
					for b in blocks:
						executeBlock(b, '', stack)
			else:
				# Just in case
				for b in blocks:
					executeBlock(b, '', stack)
			
			continue
		elif code[0] == '@':
			if len(code) > 1:
				if code[1] in extOperators:
					result = executeOp(extOperators[code[1]], stack, code[:2])
					if result != None:
						stack.append(result)
					code = code[2:]
					continue
				else:
					print("Error: Undefined extended operator @"+code[1])
					break
			else:
				print("Error: Unfinished extended operator")
				break
		elif code[0] in operators:
			result = executeOp(operators[code[0]], stack, code[0])
			if result != None:
				if code[0] in "$i": # Some operators push mutliple values to the stack.
					stack += result
				else:
					stack.append(result)
			code = code[1:]
			continue

		code = code[1:]

	return stack




# Running the program

code = ''

if len(sys.argv) > 1:
	source = open(sys.argv[1], 'r')
	code = source.read()
else:
	sys.stderr.write("Error: No source file specified.\n")
	exit(1)

interpret(code, []) # Run the code starting with an empty stack

