# Solace

A simple, stack-based language. Solace is still a work in progress and is very much incomplete.

The only data types in Solace are integers and lists of integers. Operators in general auto-vectorize over their arguments. That is, the operator is applied to every number in a list rather than on the list itself. Furthermore, pure integers are cast to 1-element lists whenever necessary.

## Basic syntax

Since Solace uses a stack to store values, operators are used with postfix notation. Operators pop their operands off the stack, and push the result to the stack.

For a full list of operators, [see here](https://github.com/splcurran/Solace/blob/master/Operators.md).

### Literals

There are a few ways to write literals in Solace. The most basic way is a simple number literal, e.g. `123`. This pushes the integer 123.

Lists can be created in two ways. One is a comma-separated list of numbers, e.g. `12,34,56,78`, which pushes `[12, 34, 56, 78]`. The other way is to write a string literal. Enclosing any characters between two `"`s will push a list of those characters code points.

It is also possible to use a single quote `'` followed by any character, which pushes that character's code point.

### Hello, World! program:

    "Hello, World!"p

## Blocks

Blocks are code enclosed in `{` and `}`. Ordinarily, a block is simply run as if the braces weren't there. But if the block is followed by a valid suffix, it changes the way the block is run. For example, by using the `E` suffix, the block can be run on every element of a list. The following code would insert a space after every character in `Hello, World!`:

    "Hello, World!"{' :}Ep
