def even(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    print(result)


#Test
even([1,2,3,4,5,6,7,8,9,10])
