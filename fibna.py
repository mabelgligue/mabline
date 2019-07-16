number = int(input("\n please Enter the range number:"))
first_value = 0
second_value = 1
for num in range (0,number):
       if(num <= 1):
                 next = num
       else:
         next = first_value + second_value
         first_value = second_value
         second_value = next
print(next)