sc="my name is sai charan i am from ongole i have completed my intermediate at nri junior college ongole"
sum=0
vowels=['a','e','i','o','u']
for char in sc.lower():
    if(char in vowels):
        sum += 1
print(f"There is {sum} many number of vowels")        