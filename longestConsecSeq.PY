# Leetcode 128

# Algorithm:
# Create a set of all the values in nums
# initialise longest to 0 to maintain the longest sequence count
# Iterate through nums and for each value n, check if n-1 exists in the set - this helps us identify if the number is a start of a sequence
# If n-1 does not exist, that means it is a start
# length of this sequence is set to 0
# while (n+length) exists in the set, increment the length of this sequence
# once the loop is over, you update longest by taking the maximum of longest and the length of this sequence
# finally, you return longest

#Code:
def longestConsecutive(nums: list[int]) -> int:
    numsSet = set(nums)
    longest = 0
    for n in nums:
        if (n-1) not in numsSet:
            length = 0
            while (n+length) in numsSet:
                length += 1
            longest = max(length, longest) 
    return longest

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))