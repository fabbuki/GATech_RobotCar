# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']



def search(grid,init,goal,cost):

    init.append(0) #[0, 0, 0]
    blocked = [init[-2:]] #get coordinates of blocked spot

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                #add to blocked
                blocked.append([i,j])

    print blocked

    current_spot = init[-2:]
    g = 0

    #check 4 directions
    for direction in delta:
        spot = current_spot
        new_spot = [current_spot[0] + direction[0], current_spot[1] + direction[1]]
        print new_spot
        if ((new_spot[0] < 0) | (new_spot[0] > len(grid[0]))) | ((new_spot[1] < 0) | (new_spot[1] > len(grid))):
            #item is out of bounds; ignore it
            print "out of bounds"
            print new_spot
        else:
            if new_spot in blocked:
                print "skip" #if the new spot is in the blocked list, ignore it
                print new_spot
            else:
                print "we are in business"




    #pass in grid
    #pass in current element
    #pass in blocked off list
    #perform search (check if it is the GOAL)
    #generate search agents for each element with lowest g value

    path = [11, 4, 5]



    return path

#def searchAgent(start,)

search(grid, init, goal, cost)