// u/algo-xero
class Robot {
public:
    Robot(int width, int height) {
        this->width = width; 
        this->height = height;
    }
    
    void step(int num) {
        moved = true;
        int perim = 2 * (width - 1) + 2 * (height - 1);
        int distance = num % perim;
        // if the number of steps causes the robot to return to its
        // original position, then there's no need to simulate movement.
        // this TLEs otherwise.
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
    
    vector<int> getPos() {
        return { x, y };
    }
    
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

private:
    int direction = 1;
    int width = 0;
    int height = 0;
    int x = 0; 
    int y = 0;
    bool moved = false;

    void turn90Deg() {
        direction = (((direction - 1) % 4) + 4) % 4;
    }

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
};

/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */
