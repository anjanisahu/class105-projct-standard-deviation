import csv
import math

with open("height-weight.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)
# pop means remove something and 0 means first line    
file_data.pop(0)
new_data=[]
   # print(file_data)
   # len means length 
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))
n=len(new_data)
total=0  
for x in new_data: 
    total += x
mean = total / n
print("Mean / Average is: " + str(mean))

# - and square the no.
square_list=[]
for number in new_data:
    a=int(number)-mean
    a=a**2
    square_list.append(a)


#find the sum
sum=0
for i in square_list:
    sum=sum+i


#now we divide

result=sum/(len(new_data)-1)

#taking square root

standard_deviation=math.sqrt(result)
print(standard_deviation)
