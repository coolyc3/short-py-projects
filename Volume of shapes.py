#Shape Volume Program. V1.0 Made by Yonaton Chriqui
import math

choice = raw_input("Choose your shape: 1. Cube, 2. Rectangular Prism, 3. Cylinder, 4. Pyramid, 5. Cone, 6. Sphere:")
choice = float(choice)

def cube(a):
	z = a ** 3
	return z
def rect_prism(a,b,c):
	z = a * b * c
	return z
def cylinder(a,b):
	z = math.pi * a ** 2 * b
	return z
def pyramid(a,b,c):
	z = ((a * b) * c) / 3
	return z
def cone(a,b):
	z = (math.pi * a ** 2 * b) / 2
	return z
def sphere(a):
	z = (4 * math.pi * a ** 2) / 3
	return z

if choice == 1:
	a = float(raw_input("Side Length:"))
	print cube(a)
elif choice == 2:
	a = float(raw_input("Side 1 Length:"))
	b = float(raw_input("Side 2 Length:"))
	c = float(raw_input("Side 3 Length:"))
	print rect_prism(a,b,c)
elif choice == 3:
	a = float(raw_input("Raduis:"))
	b = float(raw_input("Height:"))
	print cylinder(a,b)
elif choice == 4:
	a = float(raw_input("Base Length 1:"))
	b = float(raw_input("Base Length 2:"))
	c = float(raw_input("Height:"))
	print pyramid(a,b,c)
quit = raw_input("Press enter to quit")