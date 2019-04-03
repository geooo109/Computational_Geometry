from point import *
from plane import *
import numpy as np
import matplotlib.pyplot as plt
def parse_input():
    points = []
    ch = raw_input("To autogenerate write ->AUTO<- else just type something: ")
    if ch != "AUTO":
        print("Give Points of the Plane in the form x,y to stop type ->quit<-: ")
        while True:
            in_str = raw_input()
            #sometimes i forget what i have to write :P
            if in_str == "quit" or in_str == "exit" or in_str == "stop":
                break
            in_str = in_str.split(",")
            points.append(Point(int(in_str[0]),int(in_str[1])))
    else:
        num_points = int(raw_input("Enter number of Points: "))
        points = np.array([Point(np.random.randint(0,400),np.random.randint(0,400)) for i in range(num_points)])
    return Plane(points)


def main():
    try:
        plane = parse_input()
    except:
        print("Error on input of the plane data points")
        return
    plane.print_plane()

if __name__ == "__main__":
    main()
