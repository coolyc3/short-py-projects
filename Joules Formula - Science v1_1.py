#Science Code For Class v1.1 by Yonaton Chriqui
num = raw_input("Type 1 for Heat. 2 for Temp. 3 for Specific Heat. 4 for Mass.")
num = int(num)
final = 0

def heat(x,y,z):
    final = x * y * z
    return final
def rest(x,y,z):
    final1 = y * z
    final = x / final1
    return final

if num == 1:
    ask = int(raw_input("Do you have Change in Tempurature. 1 for Yes. 2 for No."))
    if ask == 1:
        x = float(raw_input("Type your Change in Tempurature"))
    else:
        temp1 = float(raw_input("Type temp1 (temp1 > temp2)"))
        temp2 = float(raw_input("Type temp2"))
        x = temp1 - temp2
    y = float(raw_input("Type your Mass"))
    z = float(raw_input("Type your Specific Heat"))
    print heat(x,y,z)
elif num == 2:
    x = raw_input("Type your Heat")
    y = raw_input("Type your Specific Heat")
    z = raw_input("Type your Mass")
    print rest(x,y,z)
elif num == 3:
    x = raw_input("Type your Heat")
    y = raw_input("Type your Mass")
    ask = raw_input("Do you have Change in Tempurature. 1 for Yes. 2 for No.")
    ask = int(ask)
    if ask == 1:
        z = raw_input("Type your Change in Tempurature")
    else:
        temp1 = raw_input("Type temp1 (temp1 > temp2)")
        temp2 = raw_input("Type temp2")
        temp1 = int(temp1)
        temp2 = int(temp2)
        z = temp1 - temp2
    print rest(x,y,z)
elif num == 4:
    x = raw_input("Type your Heat")
    y = raw_input("Type your Specific Heat")
    ask = raw_input("Do you have Change in Tempurature. 1 for Yes. 2 for No.")
    ask = int(ask)
    if ask == 1:
        z = raw_input("Type your Change in Tempurature")
    else:
        temp1 = raw_input("Type temp1 (temp1 > temp2)")
        temp2 = raw_input("Type temp2")
        temp1 = int(temp1)
        temp2 = int(temp2)
        z = temp1 - temp2
    print rest(x,y,z)
quit = raw_input("Press enter to quit")
