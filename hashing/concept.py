s=[1,2,1,3,4,5]
freq={} # we are making a  counter
for num in s:
  freq[num]=freq.get(num,0)+1
print(freq)