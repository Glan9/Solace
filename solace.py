#!/usr/bin/env python3

import sys
import re
import operators

numRegex = '^-?\\d+(,-?\\d+)*'
stringRegex = '^"((\\"|[^"])*?)"'
charRegex = "^'([\s\S])"
arity1Suffixes = '<>EMNPS'
arity2Suffixes = '?'

"""
depth(o)

Returns the depth of object o. If o is an integer, its depth is 0.
Otherwise, the depth is the maximum level of nesting in the list o.
"""
def depth(o):
	if type(o) != list:
		return 0
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
def executeOp(op, stack):
	if len(stack) < op[0]: # Not enough arguments available
		sys.stderr.write("Error: Not enough arguments\n")
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
		stack += [results]
	if suffix == '?':
		cond = stack.pop() # Should we run block 1 or block 2?
		if cond != 0:
			stack += interpret(block, stack)  # Run first if cond is truthy
		else:  
			stack += interpret(block2, stack) # Run second if cond is falsy




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
			
			if code[0] == '{':
				code = code[1:]
				block2 = ''
				depth = 1
				while depth>0:
					if len(code) == 0:
						print("Error: Unclosed block")
						exit(1)

					block2 += code[0]
					if code[0] == '{':
						depth += 1
					elif code[0] == '}':
						depth -= 1
					code = code[1:]

				block2 = block2[:-1]
				
				if code[0] in arity2Suffixes:
					suffix = code[0]
					code = code[1:]
					executeBlock(block, suffix, stack, block2)
				else:
					suffix = code[0] if code[0] in arity1Suffixes else ''
					code = code[1:]
					executeBlock(block, '', stack)
					executeBlock(block2, suffix, stack)
			else:
				suffix = code[0] if code[0] in arity1Suffixes else ''
				code = code[1:]
				executeBlock(block, suffix, stack)
			
			continue
		elif code[0] in operators.ops:
			result = executeOp(operators.ops[code[0]], stack)
			if result != None:
				stack += [result]
		
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