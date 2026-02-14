# these statements are used to not print the particular code without terminating the code by not printing the code which was givemn by User
# for example if user given numbers from 0 to 100
# i don't want to print number 18 then we use continue 
# when we are using these statements we have to write the print statements after the conditional statements

for i in range(0, 21):
    if(i==18):
        continue
    print(i)


for j in range(0,  100):
    if(j==97):
        continue
    print(j)


for i in range (0, 18):
    if i==5:
        continue
    print(i)

for j in range (0, 10):
    if j==4:
        continue
    print(j)