# Grids
An introduction to writing a program that employs multiple functions.

Grids are represented as a list of lists, such as: 

[[3, 4, 3, 9], [8, 6, 9, 1], [5, 9, 4, 3], [1, 8, 7, 2]]

but for these instructions we will print such a grid like so:

3 4 3 9
8 6 9 1
5 9 4 3
1 8 7 2.

All test inputs will be square, having the same number of rows as columns. The entries in the grid will all be integers from 1 to 9. We refer to the position of a grid entry as (row, column). Along with a grid, the input will include a target from 1 to 9 and a direction from 0 to 7. These directions correspond to the eight orthogonal and diagonal directions that point at the neighbors of a grid entry. We will use 0 for straight north, 1 for northeast, 2 for east, and so on, to 7 for northwest. For example, from the 5 in position (2, 0) we see 8 in direction 0, 6 in direction 1, etc. Because 5 is on the edge of the grid, there are no neighbors in directions 5 through 7.

As another example, we observe that the neighbor of the 7 in position (3, 2) in direction 6 is 8. The program should accept a square grid, a target, and a direction. The program should then output:

  • The same grid with every instance of the search number replaced with 0;
  • The position(s) of these 0s;
  • The sum of all grid entries that neighbored the targets in the given direction
