# Blocks

Blocks are code enclosed in `{` and `}`. By adding a suffix to the block, you can change the way in which the block is executed. If a block has no suffix, it is simply executed as-is.

Some suffixes in the following list describe the block being run "on" values. This means that the values are placed in a new stack, the block is executed, and the final stack is concatenated to the original stack.

Block syntax is `{<code>}<suffix>`, e.g. `{' :}E`. The suffix must be immediately following the `}` or it won't be interpreted as such. Some suffixes require two blocks, in this case the blocks must also be directly adjacent.

## Suffixes

Symbol | Name | # blocks | Effect
--- | --- | --- | ---
`+` | Accumulate | 1 | Pop *z*. Map each element of *z* to the result of reducing all elements of *z* before and including it (see suffix `R`). Push the resulting array.
`>` | Maximum | 1 | Pop *z*. For each element of *z*, execute the block on it and pop a value. Push the element of *z* which gave the largest value.
`<` | Minimum | 1 | Pop *z*. For each element of *z*, execute the block on it and pop a value. Push the element of *z* which gave the lowest value.
`?` | Conditional | 2 | Pop *z*. If *z* is non-zero or non-empty, execute the first block. Otherwise, execute the second block.
`D` | Discard | 1 | Pop *z*. For each element of *z*, execute the block on it and pop a value. If the value is non-zero or non-empty, discard that element from *z*. Push the new *z*.
`E` | Each (map) |  1 | Pop *z*, then execute the block on each element of it (at depth 1). Push the results in an array.
`F` | Filter | 1 | Pop *z*. For each element of *z*, execute the block on it and pop a value. If the value is zero or empty, discard that element from *z*. Push the new *z*.
`O` | Sort | 1 | Pop *z*. For each element of *z*, execute the block on it and pop a value. Sort *z* by the value popped for each element, in increasing order. Push the new *z*.
`P` | Pairwise | 1 | Pop *z*. For each pair of elements in *z*, execute the block on those two elements. Push the results in an array.
`R` | reduce | 1 | Pop *z*. If z is empty, simply push it again. Otherwise, push the first element of *z*, then for each other element of *z*, push it and execute the block.
`U` | Until loop | 2 | Run the first block, then pop a value. If it's zero or empty, execute the second block, then repeat.
`W` | While loop | 2 | Run the first block, then pop a value. If it's non-zero or non-empty, execute the second block, then repeat.



