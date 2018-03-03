

# Creates a list containing 8 lists, each of 8 items, all set to 0
w, h = 8, 8;
List_queens = []
List_heuristics = [0 for x in range(w)]
accumulated = 0 
# For the first time it doesn't need to take the mean

def get_min ():
    Value = min(List_heuristics) 
    Index = List_heuristics.index(Value)
    print (Value, Index)
    return Value, Index
    
def manhattan_distance(x_orig, y_orig, x_new, y_new): 
    return abs(x_orig-x_new) + abs(y_orig-y_new)    

def heuristic(col): 
    for x in range(w):
        sumH = 0
        #print("len" + str(len(List_queens)))
        for i in range(len(List_queens)):
            
            xy_old = List_queens[i]
            x_old = xy_old[0]
            y_old = xy_old[1]
            abs_X = abs(x_old - x)
            abs_Y = abs(y_old - col)
            sumH = manhattan_distance(x_old, y_old, i, col)  
            #print("sum H for x = " + str(x) + " = " + str(sumH))
            #print("x = " + str(x) + " // x_old = " + str(x_old) + " \\ sums= " + str(sumD_new) + "  " + str(sumD_old) + "  \\ minus = " + str(minusD_new) + "  " + str(minusD_old)) 
            if (x==x_old or (abs_X == abs_Y)):
                 List_heuristics[x] += 99999 
        sumH = sumH / len(List_queens)
        #print(List_heuristics)
        List_heuristics[x] += (sumH + accumulated)
    
def star_A(n_queens): 
    #aqui tambien hay que poner lo de backtracking
    global List_queens
    global List_heuristics
    global accumulated
    List_queens.append([0,0])
    print (List_queens)
    for i in range(1,n_queens): 
         heuristic(i)
         value, index = get_min()
         accumulated += value
         if (value >90000): 
             break
         List_queens.append([index,i]) 
         List_heuristics = [0, 0, 0, 0, 0, 0, 0, 0]
         print(List_queens) 
    

star_A(8)
