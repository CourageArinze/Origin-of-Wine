# TO check if a wine is part of the dataset
import origin

print("Enter the constituent of the wine you want to verify in the list")
new_wine=[]
print("the len ->",len(origin.df_ind))
for x in origin.df_ind:
    print('Enter value for',x,end='')
    cons = float(input(': '))
    new_wine.append(cons)

print(new_wine)
w_tuple=0
count=0
for each in origin.independent:
    w_tuple = w_tuple + 1
    for e in each: #range(0,len(each)):
        if (e == new_wine[count]):
            count = count + 1
    if count != 13:
        count=0
    if count == 13:
        break

print(count, len(each))

for d in range(len(origin.dependent)):
    label = origin.dependent[w_tuple]

if count == len(each):
    print('The wine has the class label',label)
else:
    print('The wine is not present in the dataset')
