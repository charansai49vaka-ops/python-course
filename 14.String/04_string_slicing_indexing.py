# string slicing is used to print a particulare number of alphabets in string upto what we want
# we can able to write slicing as [0:0:0]
name="sai charan"
print(name[0:4])   #it will follows the rule of [r:n] = r,n-1
print(name[5:9])
print(name[0:8:1]) #There is no skipping in the alphabets 
print(name[0:9:2]) #here there is spacing of 1 digits like sai charan here s i c a a 
print(name[0:9:3])  #IT FOLLOWS THE RULUE OF [R:N-1:P]= p-1 
        # [r:n:p]

#in string slicing if we don't give the number it takes automatically as 0 and last index of string

name="king virat kholi"
print(name[0:])  #Here we can able to see it will print total as king virat kholi
#because python will automatically prints as total 
print(name[:5])  #here it will print king it takes as 0 as simple