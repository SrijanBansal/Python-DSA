num = [1,4,2,5,1,2,4,5,3,6,7,2,1]

freq = {}

for i in range(0,len(num)):
    freq[num[i]] = freq.get(num[i],0) + 1
print(freq)
