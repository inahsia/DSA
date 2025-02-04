s='aihanisingh'
freq=[0]*128 # ascii values
for word in s:
  freq[ord(word)]+=1
print(freq[ord('h')])
  