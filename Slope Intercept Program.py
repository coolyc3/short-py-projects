ifslope = raw_input("Do you have a slope value?(y or n)")
if ifslope == "y":
    slope2 = raw_input("Type slope part one. (etc. -->1/x)")
    slope1 = raw_input("Type slope part two. (etc. y/1<--)")
    x1 = raw_input("Type x1")
    y1 = raw_input("Type y1")
    x1 = float(x1)
    y1 = float(y1)
    slope1 = float(slope1)
    slope2 = float(slope2)
elif ifslope == "n":
    x1 = raw_input("Type x1")
    y1 = raw_input("Type y1")
    x2 = raw_input("Type x2")
    y2 = raw_input("type y2")
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    slope1 = x2 - x1
    slope2 = y2 - y1
else:
	print "Thats not y or n. Try again."
slope = float(slope2/slope1)
print "Slope is ",slope2,"/",slope1
print "Slope as a decimal is",slope
step1 = float(slope * x1)
step2 = float(y1 + step1)
print "Final answer is: y =",slope2,"/",slope1,"x +",step2
quit = raw_input("Press enter to quit")