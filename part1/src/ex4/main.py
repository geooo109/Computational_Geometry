from point import *
from plane import *
def parse_input():
    print("Give Points of the Plane in the form (x,y) to stop type ->quit<-:")
    points = []
    while True:
        in_str = raw_input()
    if in_str == "quit":
        break
    points.append(Point(int(in_str[0]),int(in_str[1])))
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
