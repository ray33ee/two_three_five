# two_three_five
A O(log(n)) solution to the 'two three five' game

# two three five game

Starting with the number 0 and only using operations subtract 2, multiply by 3 and add 5, make a given number `n` in as few steps as possible. For example, the number 30 can be made as (+5, +5, *3)

# Our solution

A simple and O(log(n)) solution used here works by working backwards from the number `n`, making the number divisible by 3 then dividing by 3 until one of several base cases is achieved.

Since we work in reverse from `n`, we perform the inverse (add 2, subtract 5 and divide by 3). If the number is 1 (mod 3) then we add 2, and if the number is 2 (mod 3) then we subtract 5.

# Example [5, 2, 3, 3, 5]

Take the number 32. Starting with 32, we subtract 5 (since 32 is 2 (mod 3)) giving 27. Since 27 is not a base case, we divide by 3 to get 9. 9 is divisible by 3, so we can divide by 3 to get 3. Since 3 is our base case, we stop there. Since a base case of 3 is made by (+5, -2) we have the operations

[-5, +2, *3, *3, +5]
