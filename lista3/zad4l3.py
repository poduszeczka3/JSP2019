# L
str1 = ""
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==6) and (col>0 and col<5)):
            str1 = str1+"*"
        else:
            str1 = str1 + " "
    str1 = str1+"\n"

#print(str1)

# A
str2 = ""
for row in range(7):
    for col in range(13):
        if ((col==0 or col==12) and row==6) or ((col==1 or col==11) and row==5) or ((col==2 or col==10) and row==4):
            str2 = str2+"*"
        elif ((col==4 or col==8) and row==2) or ((col==5 or col==7) and row==1) or (col==6 and row==0):
            str2 = str2+"*"
        elif ((col==3 or col==4 or col==5 or col==6 or col==7 or col==8 or col==9) and row==3):
            str2 = str2+"*"        
        else:
            str2 = str2 + " "
    str2 = str2+"\n"

#print(str2)

# R
str3 = ""
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0) and (col>0 and col<4)) or ((row==3) and (col>0 and col<4)):
            str3 = str3+"*"
        elif col==4 and (row==1 or row==2):
            str3 = str3+"*"
        elif (col==2 and row==4) or (col==3 and row==5) or (col==4 and row==6):
            str3 = str3+"*"        
        else:
            str3 = str3 + " "
    str3 = str3+"\n"

#print(str3)

print("*           *        **** ")
print("*          * *       *   *")
print("*         *   *      *   *")
print("*        * * * *     **** ")
print("*       *       *    * *  ")
print("*      *         *   *  * ")
print("***** *           *  *   *")