# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = input()
shoe_sizes = input()
N = input()
money_earned = 0
shoe_sizes = [int(n) for n in (shoe_sizes.split())]

for row in range(0, int(N)):
    desired = [int(n) for n in ((input()).split())]

    if int(desired[0]) in Counter(shoe_sizes).keys():
        money_earned += int(desired[1])
        shoe_sizes.remove(int(desired[0]))

print(money_earned)