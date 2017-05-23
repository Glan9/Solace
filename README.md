# Solace

A simple, stack-based language. Solace is still a work in progress and is very much incomplete.

The only data types in Solace are integers and lists of integers. Operators in general auto-vectorize over their arguments. That is, the operator is applied to every number in a list rather than on the list itself. Furthermore, pure integers are cast to 1-element lists whenever necessary.

### Hello, World! program:

    "Hello, World!"p

## Blocks

Blocks are code enclosed in `{` and `}`. Ordinarily, a block is simply run as if the braces weren't there. But if the block is followed by a valid suffix, it changes the way the block is run. For example, by using the `E` suffix, the block can be run on every element of a list. The following code would insert a space after every character in `Hello, World!`:

    "Hello, World!"{' :}Ep
