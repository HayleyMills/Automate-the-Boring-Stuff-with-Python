##Say you have a list of lists where each value in the inner lists is a
## one-character string, like this:
##
##grid = [['.', '.', '.', '.', '.', '.'],
##        ['.', 'O', 'O', '.', '.', '.'],
##        ['O', 'O', 'O', 'O', '.', '.'],
##        ['O', 'O', 'O', 'O', 'O', '.'],
##        ['.', 'O', 'O', 'O', 'O', 'O'],
##        ['O', 'O', 'O', 'O', 'O', '.'],
##        ['O', 'O', 'O', 'O', '.', '.'],
##        ['.', 'O', 'O', '.', '.', '.'],
##        ['.', '.', '.', '.', '.', '.']]
##
##Think of grid[x][y] as being the character at the x- and y-coordinates of a
##“picture” drawn with text characters. The (0, 0) origin is in the upper-left
##corner, the x-coordinates increase going right, and the y-coordinates
##increase going down.
##
##Copy the previous grid value, and write code that uses it to print the image.
##
##..OO.OO..
##.OOOOOOO.
##.OOOOOOO.
##..OOOOO..
##...OOO...
##....O....

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


##print each item 0 in each of the lists, then print each 1 item in each of the
##lists

for i in range(len(grid[1])):
    for item in range(len(grid)):
        print(grid[item][i], end ='')
    print('\n', end='')








