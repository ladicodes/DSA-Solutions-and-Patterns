# lc 2069 - walking robot simulation ii

here i attempt to explain my solution to lc problem 2069.

## solution details

- problem: https://leetcode.com/problems/walking-robot-simulation-ii/
- language: cpp
- difficulty: medium
- solved: yes

## understanding the problem

> before reading the problem statement, i realized that this would be another instance of what i normally refer to as "design" problems, my least favourite kind of problems on leetcode. if you've solved "lru cache" or "design twitter", you know what i'm talking about.

so right off the bat, we're given a resizable 2D grid space, whose dimensions are specified by the **width** and **height** parameters in the class constructor.

we are also told that the robot begins at coordinates **(0, 0)** facing eastwards, and will receive commands for operations which involve printing its current position (getPos), printing its current direction (getDir), and movement.

looking at this, the problem is quite different from the first variant of walking robot simulation, in the sense that we're initially facing a different direction, and there are no obstacles to watch out for.

the problem asks us to "redirect" the robot if at any point it leaves the boundary of the grid. redirection here means the robot must rotate counter clockwise, so if the robot is facing east, it must rotate towards the north.

the objective of this problem is to simulate the robot's movement while accurately preserving its directions and distance to be travelled.

i should note that there's an important optimization problem which will help us avoid redundant movement calculations on larger number of steps, as you'll soon see.

## approach

we have to be a bit careful with this problem, so we'll first of all model the robot problem using six state variables:

1. direction: the current direction the robot is facing (0: NORTH, 1: EAST, 2: SOUTH, 3: WEST).
2. width: this is the maximum horizontal distance traversable by the robot. in order words, the width of the grid.
3. height: this is the height of the grid, the maximum traversable vertical distance.
4. x: this is the robot's current x coordinate.
5. y: this is the robot's present y coordinate.
6. moved: this is a boolean variable which tracks whether the robot actually moved (this will be useful later on).

now that our state variables are set, let's start by tackling the sub problems incrementally, starting from the easiest ones.

### class instantiation

this here sets our width and height variables whenever the judge creates a new Robot instance.

```cpp
class Robot {
public:
    Robot(int width, int height) {
        this->width = width; 
        this->height = height;
    }
};
```

### get position

this method returns the current x and y coordinates when called.

```cpp
vector<int> getPos() {
    return { x, y };
}
```

### get direction

now, ignoring the if condition for now, the method returns the current direction from our encoded direction values (0 - 3).

the if check with **moved** simply corrects the direction after we apply our optimization trick in the **step** method. it essentially says "if the robot is at the origin and it's current direction is east, while having moved, then our correct direction must be south".

```cpp
string getDir() {
    // notice that if we've moved but return to the orign, the
    // robot must be facing southwards now if we were originally
    // facing east.
    if (moved && x == 0 && y == 0 && direction == 1)
        return "South";

    string direction_str;
    switch (direction) {
        case 0:
            direction_str = "North";
            break;
        case 1:
            direction_str = "East";
            break;
        case 2:
            direction_str = "South";
            break;
        case 3:
            direction_str = "West";
            break;
    }
    return direction_str;
}
```

### helper methods

before we tackle the **step** method, i decided to separate movements along the four directions and rotation into their own little methods.

again, i apply the negative modulo correction trick from the first variant of the problem. since we're turning counter clockwise, we have to subtract one from the current direction.

```cpp
void turn90Deg() {
    direction = (((direction - 1) % 4) + 4) % 4;
}
```
moving east is a matter of calculating the "overshoot" from adding the movement distance to the current x coordinate.

if the new x position is larger than our grid's width, then we have to turn 90 degrees, then compute the "remaining" distance to be travelled.

i then update the x coordinate accordingly and return the new distance to the calling method, which is **step**.

```cpp
int moveEast(int distance) {
    int new_x = x + distance;
    int new_dist = 0;
    if (new_x >= width) {
        new_dist = new_x - (width - 1);
        new_x = width - 1;
        turn90Deg();
    }
    x = new_x;
    return new_dist;
}
```

similarly for northwards movement, we calculate the new y coordinate, then compute the remaining distance to cover if we overshoot our grid height. we also turn 90 degrees when this happens.

```cpp
int moveNorth(int distance) {
    int new_y = y + distance;
    int new_dist = 0;
    if (new_y >= height) {
        new_dist = new_y - (height - 1);
        new_y = height - 1;
        turn90Deg();
    }
    y = new_y;
    return new_dist;
}
```

overshooting west is a bit different since our new_x coorindate would be negative, so our "remainder" in this case would be the absolute value of the new_x coordinate.

```cpp
int moveWest(int distance) {
    int new_x = x - distance;
    int new_dist = 0;
    if (new_x < 0) {
        new_dist = abs(new_x);
        new_x = 0;
        turn90Deg();
    }
    x = new_x;
    return new_dist;
}
```

the same reasoning applies to moving south here.

```cpp
int moveSouth(int distance) {
    int new_y = y - distance;
    int new_dist = 0;
    if (new_y < 0) {
        new_dist = abs(new_y);
        new_y = 0;
        turn90Deg();
    }
    y = new_y;
    return new_dist;
}
```

### step

finally, we rotation and movement logic together in the step method.

```cpp
void step(int num) {
    moved = true;
    int perim = 2 * (width - 1) + 2 * (height - 1);
    int distance = num % perim;
    // if the number of steps causes the robot to return 
    // to its original position, then there's no need to
    // simulate movement. this would TLE otherwise.
    while (distance) {
        switch (direction) {
            case 0:
                distance = moveNorth(distance);
                break;
            case 1:
                distance = moveEast(distance);
                break;
            case 2:
                distance = moveSouth(distance);
                break;
            case 3:
                distance = moveWest(distance);
                break;
        }
    }
}
```

the trick here is that, if moving any **num** number of times modulo the grid's perimeter is zero, then the robot effectively returns to the same position. it would be pointless to simulate movement when we know that the robot ends up right where it started (after going round the grid).

## conclusion

time complexity: O(1) for the step calls, which happens at most four times.

space complexity: O(1) since memory usage doesn't grow with input size.

this simulation problem leans a bit more into the harder mediums, you have to be careful to watch out for off-by-one errors that can leave you pulling your hair out late at night.

once again, you can find my solution code in c++ attached. i hope you enjoyed this one!

solution by [u/algo-xero](https://leetcode.com/u/algo-xero)
