
# Game: Start with a variable x = 0. Using only three operations, subtract 2, multiply by 3 and add 5 , try and make any
# number (n) in as few moves as possible.

# This script contains an algorithm to accomplish this working in O(log(n)) time.
# It works by either subtracting 2 or adding 5 (to create a new number divisible by 3) then dividing by 3. Repeating
# this process until our number is one of the base cases creates a route to our original number n.


# Returns a list of operations required to generate the number x and an indicator showing the base case.
# Indicators:
# -1: Indicates a simple case 0 <= x <= 11
#  0, 3, 6, 12: Indicates a base case of 0, 3, 6 12, respectively
def reduce(x):

    l = []

    # Simple cases (0 - 11):
    if x == 0:
        return [], -1
    elif x == 1:
        return [5, 2, 2], -1
    elif x == 2:
        return [2, 3, 5, 5, 2], -1
    elif x == 3:
        return [5, 2], -1
    elif x == 4:
        return [2, 3, 5, 5], -1
    elif x == 5:
        return [5], -1
    elif x == 6:
        return [2, 2, 5, 5], -1
    elif x == 7:
        return [2, 5, 3, 2], -1
    elif x == 8:
        return [5, 5, 2], -1
    elif x == 9:
        return [5, 2, 3], -1
    elif x == 10:
        return [5, 5], -1
    elif x == 11:
        return [5, 3, 2, 2], -1

    while True:
        m = x % 3

        # If x % 3 == 1, add 2 to make it divisible by 3
        if m == 1:
            x = x + 2
            l.insert(0, 2)
        # If x %3 == 2, subtract 5 to make it divisible by 3
        elif m == 2:
            x = x - 5
            l.insert(0, 5)

        # At this point x is divisible by 3

        # If x is either 0, 3, 6 or 12 we can stop early as these numbers are our base cases
        if x == 0:
            return l, 0
        elif x == 3:
            t = [5, 2]
            t.extend(l)
            return t, 3
        elif x == 6:
            t = [5, 5, 2, 2]
            t.extend(l)
            return t, 6
        elif x == 12:
            t = [2, 5, 3, 2, 5]
            t.extend(l)
            return t, 12

        # Divide the number by 3
        x = x / 3
        l.insert(0, 3)


# Take the list, and apply all the operations to generate a number
def build(l: list):
    x = 0
    for op in l:
        if op == 2:
            x = x - 2
        elif op == 3:
            x = x * 3
        elif op == 5:
            x = x + 5
        else:
            print("Invalid op + " + str(op))

    return x


for i in range(10000):
    print(str(i))
    l, ind = reduce(i)
    print("    " + str(l.__len__()) + " " + str(l) + " " + str(ind))
    if build(l) != i:
        print("assertion failed " + str(l) + " " + str(i))
        exit()
