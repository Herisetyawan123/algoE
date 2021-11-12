data = [3,4,1,5,2]

# iterasi
# 3,4,1,5,2     => 3,1,4,2,5
# iterasi 2
# 3,1,4,2,5     => 1,3,2,4,5
# itetasi 3    
# 1,3,2,4,5     => 1,2,3,4,5
# iterasi 4
# 1,2,3,4,5
# iterasi 5
# 1,2,3,4,5
for i in range(len(data)-1,-1, -1):
    for j in range(i):
        if(data[j] > data[j+1]):
            data[j], data[j+1] = data[j+1], data[j]
print(data)