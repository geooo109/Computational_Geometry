from triangle import *

'''
 Reads 3 points and constructs the triangle
'''
def parse_input():
	try :
		print "All input points must be in the form (x,y)"
		in_str = input("Enter Point1(x1,y1):")
		pt1 = Point(int(in_str[0]),int(in_str[1]))
		in_str = input("Enter Point2(x2,y2):")
		pt2 = Point(int(in_str[0]),int(in_str[1]))
		in_str = input("Enter Point2(x3,y3):")
		pt3 = Point(int(in_str[0]),int(in_str[1]))
	except :
		print("Error on Parsing the points of the triangle")
	return Triangle(pt1, pt2, pt3)


def main():
	try:
		trian = parse_input()
	except:
  		print("Error on creating an Object Triangle") 
	trian.print_triangle()


if __name__ == "__main__":
	main()