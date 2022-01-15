#questions interview FizzBuzz Game
# Complete the code below to go over the array numbers and check the numbers one by one and do the following
#
# If the number is divisible by 3, print "Fizz".
# If it's divisible by 5, print "Buzz".
# If it's divisible by 3 and 5, print "FizzBuzz".
# Otherwise just output the number.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for x in numbers:
    if(x%3 == 0 and x%5 == 0):
        print("Fizz")
    elif(x%5 == 0):
        print("Buzz")
    elif(x%3 == 0):
        print("FizzBuzz")
    else:
        print(x)







