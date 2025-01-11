def maximumsum(nums,k):
  sums=0
  maxi=0
  n=len(nums)
  sums=sum(nums[:k])
  for i in range(k,n):
    sums+=nums[i]-nums[i-k]
    maxi=max(maxi,sums)
  print(maxi)
nums=[1, 4, 2, 10, 23, 3, 1, 0, 20]
k=4
maximumsum(nums,k)