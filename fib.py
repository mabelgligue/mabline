
def Fibonacci( pos ):
        #check for the terminating condition
        if pos <= 1 :
                #Return the value for position 1, here it is 0
                return 0
        if pos == 2:
                #return the value for position 2, here it is 1
                return 1

        #perform some operation with the arguments
        #Calculate the (n-1)th number by calling the function itself
        n_1 = Fibonacci( pos-1 )
        #calculation  the (n-2)th number by calling the function itself again
        n_2 = Fibonacci( pos-2 )
        #calculate the fibo number
        n = n_1 + n_2
        #return the fibo number
        return n

nth_fibo = Fibonacci( 5 ) 

print (nth_fibo)
