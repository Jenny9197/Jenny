largeNum = -1
print('before', largeNum)
nums = [9,41,12,3,74,15]
for i in nums:
    if i > largeNum:
        largeNum = i
    print('largeNum: ', largeNum, 'currentNum :', i)
print('after', largeNum)