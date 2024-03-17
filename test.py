print("Hello World!")

print(123456789 * 9876543211)




friends = ['a','b','c']
for friend in  friends:
    print("Hi, " + friend)

values = [3,6,9]
sum =0
length=0
for value in values:
    sum += value
    length += 1
print("Total sum: " + str(sum) + " - Average: " + str(str(sum/length)))


import glob
print(glob.glob("c:\Intel/*"))



y = 3
z = 0
while y < 5:
    print("Not there yet, y=" + str(y))
    y += 1
    z += 1
    print("Y is: " + str(y))
print("z= " + str(z))

for x in range(12):
    print(str(x), end= "|")
