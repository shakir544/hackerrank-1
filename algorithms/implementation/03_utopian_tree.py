"""
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after NN growth cycles?

Input Format

The first line contains an integer, TT, the number of test cases.
TT subsequent lines each contain an integer, NN, denoting the number of cycles for that test case.

Constraints
1≤T≤101≤T≤10
0≤N≤600≤N≤60
Output Format

For each test case, print the height of the Utopian Tree after NN cycles. Each height must be printed on a new line.

Sample Input

3
0
1
4
Sample Output

1
2
7
Explanation

There are 3 test cases.

In the first case (N=0N=0), the initial height (H=1H=1) of the tree remains unchanged.

In the second case (N=1N=1), the tree doubles in height and is 22 meters tall after the spring cycle.

In the third case (N=4N=4), the tree doubles its height in spring (H=2H=2), then grows a meter in summer (H=3H=3), then doubles after the next spring (H=6H=6), and grows another meter after summer (H=7H=7). Thus, at the end of 4 cycles, its height is 77 meters.
"""

import sys

def cal_height_after_n_cycles(n):
    height = 1
    if n == 1:
        return height*2
    for cycle in range(1, n+1):
        if cycle%2 == 0:
            height = height+1
        else:
            height = height*2
    return height

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    height = cal_height_after_n_cycles(n=n)
    print height
