#class Restaurant(object):# 1st  we have to make a class, which is Restaurant.
   #bankrupt = False#2nd we have to assign class a property, which is called "bankrupt"- Which is currently false. Remember is is under the class statement!
    #def open_branch(self):#3rd we assign it a function open_branch which can only occur if "bankrupt" is false.
       #if not self.bankrupt:
           # print("branch opened")
x=Restaurant()#now x is a Restaurant which has a property bankrupt and a function open_branch. Now, we can access the property bankrupt by typing x.bankrupt.
#the above command is the same as: Restaurant().bankrupt

#Now you can see that self refers to the bound variable or object- see line three. In this case it was x because we had assisgned the Restaurant class to x,
# where as in the second one ( Below) case it was referred to Restaurant ().

x=Restaurant()# in this case x=Restaurant, but before
x.bankrupt
False

y=Resaurant()
y.bankrupt = True
y.bankrupt
True

x.bankrupt
False

#the second code and the one below are the same

class Restaurant(object)#1st we have to make the class- our class is Restaurant.
    bankrupt = False#2nd we have to assign class a property- which is currently False
    def open_branch(this)#3rd we have to assisgn it a function
        if not this.bankrupt:
            print("branch opened")










#The first argument of every class method, including init, is always referring to the current instance of the class.By convention, this argument is always
#names self!In the init method , self refers to the mewly created object; in other class methods, it referes to the instance whise method was called.



