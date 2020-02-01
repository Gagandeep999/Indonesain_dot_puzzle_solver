'''
Takes a board as a parameter and has node class in it, each node is initialized with the board.
Creates a root node with initial config and calls check_final_state(board)
Creates children nodes puts them in a stack, and until the level max_d provided in the assignment
then makes a call to the check_final_state() to check.
Nodes need to keep track of parents.
Think about the output files; what kind of useful info to display.
'''