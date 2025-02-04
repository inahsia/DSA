s=[1,2,1,3,4,5]
freq={} # we are making a  counter
for num in s:
  freq[num]=freq.get(num,0)+1
print(freq)

maxi=0
maxelement=None
mini=float('inf')
minelement=None
# dict is being used
for element,count in freq.items(): 
  if count>maxi:
    maxi=count
    maxelement=element
  if count<mini:
    mini=count
    minelement=element
print(minelement)
print(maxelement)

