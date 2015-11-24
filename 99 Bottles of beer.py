x = 99
while x > 0:
	if x == 2:
		print x,"bottles of beer on the wall",x,"bottles of beer! Take one down pass it around,",x-1,"bottle of beer on the wall!"
	elif x == 1:
		print x,"bottle of beer on the wall",x,"bottle of beer! Take one down pass it around, No more bottles of beer on the wall!"
	elif x != 1:
		print x,"bottles of beer on the wall",x,"bottles of beer! Take one down pass it around,", x-1,"bottles of beer on the wall!"
	print ""
	x -= 1
quit = raw_input("Press enter to quit")