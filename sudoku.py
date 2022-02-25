board=[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]

def print_board(b):
    col_length = len(b)
    row_length = len(b[0])
    for i in range(col_length+1):#rows
        if i % 3 == 0 :
            print('_'*26)
        
        for j in range(row_length+1):#columns
            
            if i < col_length:
                if j % 3 == 0:
                    print('|', end=' ')
                
                if j < row_length:
                    if b[i][j]==0:
                        print('☐', end= ' ')
                    else:
                        print(b[i][j],end=' ')
        print()
    
def find_empty_spaces(b):
    col_length = len(b)
    row_length = len(b[0])

    for i in range(col_length):
        for j in range( row_length):
            if b[i][j] == 0:
                return(i,j) #return tuple with row, column 
    return None

def is_valid(b, num, pos):#b is board, pos is position of number added, num is number added
    col_length = len(b)
    row_length = len(b[0])
    #check in row
    for j in range(row_length):
        #b[i][j] i is the row and j is the column. pos[0] is row and pos[1] is columns
        if b[ pos[0] ][j] == num and j != pos[1]:# reason for ! statement is we dont wanna check where we just inserted the number
            return False
    #check column
    for i in range(col_length):
        if b[i][pos[1]] == num and i != pos[0]:
            return False

    #check box
    box_X = pos[1]//3
    box_Y = pos[0]//3
    for i in range(box_Y*3, (box_Y + 1)*3):
        for j in range(box_X*3, (box_X + 1)*3 ):
            if b[i][j] == num and (i,j) != pos :
                return False

    return True

def solve(b):# solve recursively
    empty_spaces = find_empty_spaces(b)
    #if no empty spaces we can leave program. if there are we get the empty space and act upon it
    #base case
    if empty_spaces == None:
        return True
    else:
        row, column = empty_spaces

    for i in range(1,10):
        if is_valid(b,i,(row,column)):
            b[row][column] = i #if valid, adds element in empty space

            if solve(b): #RECURSION, calls board with new element added and keeps repeating  and if reaches empty spaces = 0 then solved
                return True #returns True to the previous solve function that called it
            
    #resets last element added if it reaches an unsolvable state
    b[row][column]=0
    return False# if no possible solutions are there returns false and  goes to previous state and tries to find a new value from where it left off
    '''
    PROCESS:
    1. finds all empty spaces in board. If board has no empty spaces we end the prog
    2. checks each pos adding 1 to 10, as soon as it finds one that satisfies sudoku conditions we go to 
    next empty space by calling solve() in solve(). This is recursion. We do this as depending on values we 
    get later we may reach an unsolvable state and need to come back a step to see if any other number satisfies
    if that also fails we come back one more step etc etc
    3. So basically we change a value. if it leads to a deadlock we reset it to 0 and go to previous state and change the previous value over and and over again
    4.solve(b):
        return True
    as it calls the function again with new board constantly if reaches base case all will return be like a bunch of dominos of Trues falling to place

    5. return False
    as if False goes back one recursion

    '''
            


    



print_board(board)
solve(board)
print('*'*100)
print_board(board)