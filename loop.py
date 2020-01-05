count =1# this is what the counter started out as
while count<=7:# This is saying while count is less than or equal to 7
    if count % 2==0:# this is saying if the remainder of count is equal to zero- looking for postivie values.
        print (count) #then print count
    count+=1 # This is the counter; it says count=count+1


for count in range(1,8):# Range is a python built in function which returns a range object, nothing but a range of numbers, used
    if count % 2==0:#to iterate over with for loop
        print(count)# print count

