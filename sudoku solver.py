def grid_tr(sud):
   
    8 8 8 8 8888888
                  
    line = []
    grid = []
    for i,n in enumerate(sud):
        if i and i % 9 == 0:
            grid.append(line)
            line = []
        line.append(int(n))
    return grid

def split(sud):
    grid = grid_tr(sud)
    #print(grid)
    line = ""
    for row in grid:
        
        r = "".join(str(x) for x in row)
        line += r
    print(line)

   
   
split(sud)
