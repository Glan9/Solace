# Operators

Below are all the operators in Solace. Blank rows have not been implemented yet.

Operators will vectorize for integer arguments, but not for list arguments.

Arity is the number of arguments the operator takes. For simplicity, in this list: 

- monads pop *z*
- dyads pop *y*, then pop *x*

Symbol | Arity | Result
--- | --- | ---
`!` | 1 | 1 if *z* is 0, else push 0.
`#` | 2 | The *y*<sup>th</sup> element of *x* (modular).
`$` | 1 | Push *z* twice. (copy)
`%` | 2 | *x* modulo *y*.
`&` | 2 | *x* bitwise AND *y*.
`(` | 2 | Slice *x* before index *y* (modular).
`)` | 2 | Slice *x* after index *y* (modular).
`*` | 2 | *x* times *y*.
`+` | 2 | *x* plus *y.
`-` | 2 | *x* minus *y*.
`.` | 1 | The range from 0 up to *z*-1
`/` | 2 | *x* integer divided by *y*.
`:` | 2 | *x* concatenated with *y*.
`;` | 1 | [*x*] (*x* wrapped in an array).
`<` | 2 | 1 if *x* is less than *y*, else 0.
`=` | 2 | 1 if *x* equals *y*, else 0.
`>` | 2 | 1 if *x* is greater than *y*, else 0.
`?` | 2 | -1 if *x* is less than *y*, 0 if they are equal, or 1 if *x* is greater than *y*.
`A` | | 
`B` | | 
`C` | 2 | Cartesian product of *x* and *y*.
`D` | 1 | Discard *z*.
`E` | 2 | 1 if *x* and *y* are equivalent (the same list), else 0.
`F` | 1 | The prime factors of *z*. For numbers less than 2, pushes the same number in a list.
`G` | 2 | Greatest common divisor of *x* and *y*.
`H` | | 
`I` | | 
`J` | | 
`K` | | 
`L` | 2 | Least common multiple of *x* and *y*.
`M` | 2 | *x* or *y*, whichever is greater.
`N` | 2 | *x* or *y*, whichever is lesser.
`O` | 1 | Flatten and sort *z*.
`P` | | 
`Q` | | 
`R` | 1 | Reverse *z*.
`S` | | 
`T` | | 
`U` | | 
`V` | | 
`W` | | 
`X` | 2 | *x* to the power *y*.
`Y` | | 
`Z` | | 
`[` | | 
`\` | | 
`]` | | 
`^` | 2 | *x* bitwise XOR *y*.
`_` | 1 | Flatten *z*.
`` ` `` | | 
`a` | 1 | Absolute value of *z*.
`b` | | 
`c` | | 
`d` | | 
`e` | | 
`f` | 2 | Find the index of *y* as a sublist of *x*.
`g` | | 
`h` | | 
`i` | 0 | Read and eval a line of input.
`j` | 0 | Read a line of input and push a list of its code points.
`k` | 0 | Read one character of input and push its code point.
`l` | 1 | The length of *z*.
`m` | | 
`n` | | 
`o` | | 
`p` | 1 | Flatten and print *z* as Unicode characters.
`q` | 1 | Push a string representation of *z* (as a list).
`r` | | 
`s` | 1 | Push *y*, then push *x* (swap).
`t` | | 
`u` | | 
`v` | | 
`w` | | 
`x` | 2 | Repeat *x*'s elements *y* times.
`y` | 1 | Sign of *z*. i.e., -1 if *z* is negative, 0 if its 0, 1 if its positive.
`z` | | 
`\|` | 2 | *x* bitwise OR *y*.
`~` | 1 | Bitwise negation of *z*

## Extended Operators

Symbol | Arity | Result
--- | --- | ---
@( | 2 | Rotate *x* *y* elements left.
@) | 2 | Rotate *x* *y* elements right.
@< | 2 | Bitshift *x* left by *y*.
@> | 2 | Bitshift *x* right by *y*.
@T | 0 | Push the time as an array: [year, month, day, hour, minute, second, millisecond]
@j | 0 | Read all input and push it as an array of code points.
@t | 0 | Push the milliseconds passed since the Unix epoch (since 00:00:00 January 1, 1970).


