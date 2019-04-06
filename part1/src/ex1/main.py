from triangle import *

'''
 Reads 3 points and constructs the triangle
'''
def parse_input():
    print("All input points must be in the form (x,y)")
    in_str = input("Enter Point1(x1,y1):")
    pt1 = Point(int(in_str[0]),int(in_str[1]))
    in_str = input("Enter Point2(x2,y2):")
    pt2 = Point(int(in_str[0]),int(in_str[1]))
    in_str = input("Enter Point2(x3,y3):")
    pt3 = Point(int(in_str[0]),int(in_str[1]))
    if pt1.can_construct_triangle(pt2, pt3) == False:
        return None
    return Triangle(pt1, pt2, pt3)


def main():
    try:
        poss_trian = parse_input()
    except:
        print("Error on creating an Object Triangle")
    if poss_trian is None:
        print ("Input points could not construct a Triagnle")
        return
    poss_trian.print_triangle()
    pt0 = Point(0,0)
    if poss_trian.check_pt_triangle(pt0) == True:
        print ("Triangle contains (0,0)")
    else:
        print ("Triangle dosen't contain (0,0)")
    ch = raw_input("Do you want to Plot the Triangle and the (0,0) point? type (yes) or (not): ")
    poss_trian.display_triangle_and_test_point(pt0)


if __name__ == "__main__":
    main()
