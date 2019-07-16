def get_fibonacci_series(terms):                                                
    a, b = 0, 1                                                                 
    while a < terms:                                                            
        print(a, end=' ')                                                       
        a, b = b, a+b                                                           
    print()                                                                     
                                                                                
if __name__ == "__main__":                                                      
    terms = float(input("Enter number of terms: "));                            
    get_fibonacci_series(terms) 