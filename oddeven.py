
import multiprocessing

def compare(x):
    change = False
    if x[0] > x[1]:
        x[0], x[1] = x[1], x[0]
        change = True
    
    return (x, change)


def oddevensort(x):
    
    phase, flag = 0, 0    
    while (flag != 2):
        
        split = [[x[i], x[i+1]] for i in range(phase, len(x)-1, 2)]
        
        process_pool = multiprocessing.Pool(2)
        split_after_comparison = process_pool.map(compare, split)
        # close pool to prevent further tasks from execution
        process_pool.close()

        # temp is going to contain our final merged list
        temp = []
        if len(x)%2 == 0:
            if (phase == 1):
            
                temp.append(x[0])
                
                for i in split_after_comparison:
                   
                    temp += i[0]
                
                temp.append(x[-1])
            else:  
                for i in split_after_comparison:
                    temp += i[0]
        else:                  # x is odd in length
            if (phase == 1):   # odd phase
                temp.append(x[0])
                for i in split_after_comparison: # get back original list
                    temp += i[0]
            else:              # even phase
                for i in split_after_comparison: # get back original list
                    temp += i[0]
                temp.append(x[-1])
        
        x = temp
        phase = (phase + 1)%2
        if any([i[1] for i in split_after_comparison]):
            flag = 0
        else:
            flag += 1
    # done with the while loop i.e. list is sorted
    print "The sorted list", x
    return x
