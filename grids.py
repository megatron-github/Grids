"""
 *****************************************************************************
   FILE:        grids.py

   AUTHOR:      Truong Pham

   ASSIGNMENT:  Project 5: Grids

   DATE:        09/28/2018

   DESCRIPTION: The program is going to ask user to input a grid, a targeted
                number, and the direction. Then it is going to scan over this
                given squared grid of number and locate the targeted number 
                within the grid. When the target is found, this program is 
                going print out the locations of the target. The program is 
                also going to print a copy of the given grid with all the 
                targeted number turned into zero. Then, this program is going 
                to add all the numbers in the given direction from the 
                targeted number.
 *****************************************************************************
"""

from professors import input_data

# Complete these functions.  Don't change the headers (def line:
# function names and parameters) or the docstrings. The program is
# already designed to use these.

def locate_target(grid, target):
    """ Return a list of the locations (tuples) of target within grid. """
    
    # Location_list: list of all locations (tuples) of target within grid
    location_list = []

    # The for-loop compare the target to the all the numbers in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):

            # Append the locations (tuples) of the number in the grid if
            # the value of that number is equal to the value of target
            if grid[i][j] == target:
                location_list.append((i, j))
    return location_list

def is_in_bounds(grid, loc_tuple):
    """ Return True if loc_tuple is a legal position within grid.
        Return False otherwise. """

    # For convenience, get the grid size (all grids are square), and pull
    # apart the given loc_tuple.
    # Location of the number (tuple): (row_loc, col_loc)
    grid_size = len(grid)
    row_loc = loc_tuple[0]
    col_loc = loc_tuple[1]
    
    # Cite: Denzel Capella and Lucas Steele (Rigatoni)(Barusek)
    # Description: Stating that if (row_loc, col_loc) are smaller than zero
    # or bigger than grid_size, then (row_loc, col_loc) is outside of grid
    if row_loc < 0 or row_loc >= grid_size or \
       col_loc < 0 or col_loc >= grid_size:
        return False
    return True

def sum_all_neighbors(grid, location_list, direction):
    """ For each location in location_list, determine its neighbor in the 
        given direction, if it exists.  Return the sum of all such 
        neighbors. """

    # If you're smart, you make use of this:
    # Coordinate of all given direction
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

    neighbor_sum = 0

    # For-loops locate the neigbor of target and check if neighbor 
    # is in grid.
    for tple in location_list:

        # Location of the neighbor of target can be found by adding 
        # the target to the coordinate of the given direction.
        neigbor_row_loc = tple[0] + directions[direction][0]
        neigbor_col_loc = tple[1] + directions[direction][1]
        neigbor_loc_tuple = (neigbor_row_loc, neigbor_col_loc)

        # is_in_bounds check if the neighbor exists within the grid.
        if is_in_bounds(grid, neigbor_loc_tuple) is True:
            neighbor_sum += grid[neigbor_row_loc][neigbor_col_loc]
    return neighbor_sum

def print_zero_grid(grid, location_list):
    """ Prints the grid with each entry at the locations in location_list
        replaced by the digit 0. Does not actually modify grid.  
        The output should be in square form, each number in a row 
        followed by a space, and each row terminated with a newline. """
    
    # Source: Copying nested lists in Python
    # Cited: https://stackoverflow.com/
    # questions/2541865/copying-nested-lists-in-python
    # Make a copy of the given nested grid, and call it new_grid
    new_grid = [x[:] for x in grid]

    # For-loops gets the locations of target in the new grid
    # and turn that numbers at that locations to zero
    for i in range(len(new_grid)):
        for j in range(len(new_grid)):
            for tple in location_list: 
                if tple == (i, j):
                    new_grid[i][j] = 0

    # For-loop print out all the numbers in the grid without the bracket
    # and with the space at the end of the quotation marks
    for lst in new_grid:
        print(("{} "* len(new_grid)).format(*lst))

#######################################
#    DO NOT MODIFY BELOW THIS POINT   #
#######################################    

def main():
    """ The main function. """

    # Do not modify this function

    grid, target, direction = input_data()

    # Request a list of all locations of target in the given_grid:
    location_list = locate_target(grid, target)

    # Print the grid with each instance of target replaced by a zero:
    print_zero_grid(grid, location_list)

    # Print the location list
    for entry in location_list:
        print(entry)

    # Request the sum of neighbors of those locations in direction:
    neighbor_sum = sum_all_neighbors(grid, location_list, direction)
    print(neighbor_sum)

if __name__ == '__main__':
    main()