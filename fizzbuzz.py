
import sys

print("Welcome to {}".format(sys.argv[0]))

while True:
    try:
        x = int(input("Please provide us with a top of the range value""\n"))
        break
    except ValueError:
        print("That wasn't an integer")

if x <= 0:
    usr_input = input("Please provide us with a POSITIVE integer""\n")
    x = int(usr_input)

if x <= 0:
    print("Exiting program")
    exit()

print ("Okay great, Fizz Buzz counting up to {}".format(x))

for n in range(1,x+1):
    if n % 3 == 0 and n % 5 ==0:
        print("fuzzbizz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)