# lc 874 - walking robot simulation

here i attempt to explain my approach to solving lc problem 874.

## solution details

- problem: https://leetcode.com/problems/walking-robot-simulation
- language: cpp
- difficulty: medium
- solved: yes

## let's understand the problem

going through the problem statement, there are a few key words that stand out. firstly, we know there are two classes of commands, namely (i) rotation and (ii) movement commands.

rotation commands are identified by -1 for a right 90 deg turn, and -2 for a left 90 deg turn.

movement commands are positive numbers from 1 to 9 inclusively. interestingly, you're forbidden from moving 0 units.

once we understand this, it's easy to see that there are effectively just four directions to keep track of: north, east, south, and west.

all cool, so we can imagine the problem space as an XY plane, where the robot initially starts at the origin, facing north. we are told that some coordinates contain obstacles, so the robot must halt on encountering any one of them.

finally, it is possible for an obstacle to exist in the origin (0, 0), in which case the robot must move in any other direction.

the problem asks us to return the largest euclidean distance traveled by the robot, this just means to calculate the sum of the square of the largest valid x and y coordinates.

## approach

my approach is fairly straight forward, we'll simulate the robot's movement in this 2D space. we'll start by determining the class of command to execute (rotation/movement). for rotation commands, we must update the direction state accordingly (0, 1, 2, 3) for N, E, S, W respectively. for movement commands, we will simulate moving in the current direction until we encounter an obstacle.

once we've simulated travel, calculating the euclidean distance is a matter of squaring both x and y coordinates then comparing their sum with a previously saved maximum.

i outline this process below:

- store obstacle coordinates in a set data structure, since we'll constantly check for obstacles, this operation needs to be fast. 
- initialize and keep track of four major state variables: x, y, direction (dir), and max distance (res).
- for direction commands (-1 and -2) encode direction using increment for right, decrement for left, take the modulo base 4 of this answer, accounting for negative correction.
- for movement commands, create two new pieces of state (nx, ny) to simulate movement along this direction, 'unit' number of times.
- if this movement encounters an obstacle, abandon it, and continue with the next command.
- otherwise, update the x and y state coordinates.
- compute the euclidean distance, then compare it against the largest distance seen so far.

## conclusion

i try to stay language agnostic as much as possible, these steps should be easily reproducible in python, java or a similar programming language. you may find my c++ implementation attached.

solution by [u/algo-xero](https://leetcode.com/u/algo-xero)
