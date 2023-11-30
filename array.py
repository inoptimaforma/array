total = 713
km = [0, 0, 0]
weight = [0, 0, 0]
for i in range(3):
    km[i] = int(input())
    weight[i] = int(input())
while sum(weight) != total:
    print("Not found")
    for i in range(3):
        km[i] = int(input())
        weight[i] = int(input())
print("Found")