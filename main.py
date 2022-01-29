
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

    xs = [x]

    # Simple cases (0 - 11):
    if x == 0:
        return [], xs
    elif x == 1:
        return [5, 2, 2], xs
    elif x == 2:
        return [2, 3, 5, 5, 2], xs
    elif x == 3:
        return [5, 2], xs
    elif x == 4:
        return [2, 3, 5, 5], xs
    elif x == 5:
        return [5], xs
    elif x == 6:
        return [2, 2, 5, 5], xs
    elif x == 7:
        return [2, 5, 3, 2], xs
    elif x == 8:
        return [5, 5, 2], xs
    elif x == 9:
        return [5, 2, 3], xs
    elif x == 10:
        return [5, 5], xs
    elif x == 11:
        return [5, 3, 2, 2], xs

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

        xs.append(x)

        # At this point x is divisible by 3

        # If x is either 0, 3, 6 or 12 we can stop early as these numbers are our base cases
        if x == 0:
            return l, xs
        elif x == 3:
            t = [5, 2]
            t.extend(l)
            return t, xs
        elif x == 6:
            t = [5, 5, 2, 2]
            t.extend(l)
            return t, xs
        elif x == 12:
            t = [2, 5, 3, 2, 5]
            t.extend(l)
            return t, xs
        elif x == 39:
            t = [5, 3, 2, 3]
            t.extend(l)
            return t, xs

        # Divide the number by 3
        x = x / 3
        l.insert(0, 3)

        xs.append(x)


# Take the list, and apply all the operations to generate a number
def build(lu: list):
    x = 0
    for op in lu:
        if op == 2:
            x = x - 2
        elif op == 3:
            x = x * 3
        elif op == 5:
            x = x + 5
        else:
            print("Invalid op + " + str(op))

    return x


# One layer in a breadth first search
def bfs(numb, d: dict):

    copy = d.copy()

    for x in copy:
        if x - 2 != 0 and x - 2 > -10 and x - 2 not in d:
            d[x - 2] = (x, 2)
        if x - 2 == numb:
            return d, True

        if x * 3 != 0 and x * 3 not in d:
            d[x * 3] = (x, 3)
        if x * 3 == numb:
            return d, True

        if x + 5 != 0 and x + 5 not in d:
            d[x + 5] = (x, 5)
        if x + 5 == numb:
            return d, True

    return d, False


# Keep iterating over layers in a breadth first search until we are finished
def find(nu):
    di = {0:0}
    f = False
    while not f:
        di, f = bfs(nu, di)

    return trace(di, nu)


# Given a completed search map, retrace the steps used to generate the number
def trace(trace_map, num):

    x = num
    ops = []
    while x != 0:
        e = trace_map[x]
        x = e[0]
        ops.insert(0, e[1])

    return ops


for i in range(10001):
    print(str(i))
    l, ind = reduce(i)
    print("    " + str(l.__len__()) + " " + str(l) + " " + str(ind))
    if build(l) != i:
        print("assertion failed " + str(l) + " " + str(i))
        exit()


n = 1000000

m = find(n)

print(m)

print(reduce(n))

print(build(m))