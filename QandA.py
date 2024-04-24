Easy:
23165 
max_digit: 6 
min_digit: 1 
 
Solution:
word = input()
l = list(word)
l = list(map(int, l))
print("max_digit", max(l))
print("min_digit", min(l))
 
Medium:
string1: "malyalam"
string2: "lyamaaml"
(anagram --):
    1. both strings should be of same length 
    2. all characters present in string-1 should be present in string-2 
 
Input:  
string1: "abcd"
string2: "pabc"
 
Output:
Both strings are anagrams to each other
Both strings are not anagrams to each other
 
 
Solution:
word1 = input()
word2 = input()
 
word1 = sorted(word1)
word2 = sorted(word2)
if word1 == word2:
    print("Anagrams")
else:
    print("Not a anagrams")
 
 












class Bike:
    def __init__(self, speed, brand, wheelsCount):
        self.speed = speed 
        self.brand = brand
        self.wheelsCount = 12
 
    def helperFunction(self):
        print("One")
        print("Two")
 
    def printWheels(self):
        print("Wheels count is:", self.wheelsCount)
        self.helperFunction()
 
    def printBrandName(self):
        self.printWheels()
        print("Brand name is:", self.brand)
 
    def printSpeed(self):
        self.printWheels()
        print("Sorry, I am not going to print speed")
        self.printBrandName()
 
bike1 = Bike(90, "R-1 5", 2)
bike2 = Bike(115, "GT", 2)
bike3 = Bike(65, "Pulsar", 4)
print(bike2.brand)
bike2.printBrandName()
bike3.printSpeed()
bike1.printWheels()














1. Write a python program to accept list of integers
    and print the total sum of odd elements within 
    the list 
 
solution:
nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele % 2 == 1:
        result = result + ele 
print(result)
 
2. Write a python program to accept a list of 
    integers and print the total count of numbers 
    which are divisible by 5 
 
solution:    
nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele % 5 == 0:
        result = result + 1 
print(result)
 
 
3. Write a python program to accept a list of
    integers and print total count of negative
    numbers in the list 
 
nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele < 0:
        result = result + 1 
print(result)
 
 
4. Write a python program to accept a list of 
    integers and print the average of these 
    numbers 
 
nums = list(map(int, input().split()))
#temp = sum(nums)
sumOfElements = 0 
for ele in nums:
    sumOfElements = sumOfElements + ele 
print(sumOfElements // len(nums))
 
 
 
5. Write a python program to accept a list of
    integers and print sum of 2nd greatest 
     element and 2nd smallest element from list
 
n=int(input()) 
nums = list(map(int, input().split()))
result = 0 
nums = sorted(nums)
result = nums[1] + nums[n - 2]
print(result)
 










1. Write a python program to accept a string and 
    print alternate characters starting 
    from first character
 
solution:
    word = input()
    n = len(word)
    # n = 8
    # 0 1 2 3 4 5 
    for index in range(0, n, 2):
        print(word[index], end = " ")
 
 
 
2. Write a python program to accept a string and
    print only consonants in the given left to right order
 
solution:
    word = input()
    vowels = "aeiou"
 
    for ch in word:
        if ch not in vowels:
            print(ch)
 
 
3. Write a python program to accept a string and 
    print whether it is a palindrome or not
 
    # malayalam
    # program 
 
solution:
    word = input()
    reverseWord = word[::-1]
    if word == reverseWord:
        print("Palindrome")
    else:
        print("Not a palindrome")
 
 
 
 
4. Write a python program to accept string print number 
    of upper-case characters and number of lower-case
    characters and number of special characters in given string.
 
 # abcDEF@#def 
 no.of upper-case characters: 3
 no.of lower-case characters: 6
 no.of special characters: 2 
 
 solution:
     word = input()
     upperCount, lowerCount, specialCount = 0, 0, 0
     for ch in word:
         # some logic 
         if ch.isalpha():
             if ch.islower():
                 lowerCount += 1 
             else:
                 upperCount += 1 
         else:
             specialCount += 1 
 
     print("no.of upper-case characters", upperCount)
     print("no.of lower-case characters", lowerCount)
     print("no.of special characters", specialCount)
 
 
 
 
 
 
 
5. Write a python program to accept string and print 
    total number of "ab" substring present in given string
 
# freabsdabsdaab 
# 3
 
 
solution
word = input()
result = 0 
n = len(word)
# n = 8
 
for index in range(n - 1):
    if word[index] == 'a' and word[index + 1] == 'b':
        result += 1 
 
print(result)

















