# BinClassify
![Image alt](https://res.cloudinary.com/tatemmedia/image/upload/v1641976135/logoBinClassify.jpg)
---
Binclassify is a library that makes it easy to classify into groups. The main idea of the library is to classify as many groups as possible using the minimum number of questions.The library can be useful when we need to divide users by interests.
I also apologize for my crooked English translation.
Author's website:
https://tatem.pythonanywhere.com/
---
For example, we need to divide users into 10 groups. And in order for us to do this, we just need to ask 4 questions. And for 300 groups there are only 9 questions.
The questions should be binary. For example: yes and no. We will be able to find out the number of questions using the method from our library. 
A good example is my soul color(RGB) detection test - Color Soul https://tatem.pythonanywhere.com/project/colorpeople/
#
#
# A simple example:
## Let's find out how many questions we need:
```python
# Import library
from BinClassify import BinClassify
# Creating a class
binclass = BinClassify()
"""
CoutQustion accepts the number of groups you want to get.
The number should be:
1. The whole
2. More than 1
If the transfer is successful, it returns the number of responses that you must pass to the Answer method.
"""
print(binclass.CoutQustion(10))
# Outputs: 4
```
#
#
Then suppose we conduct a survey on our website:
1) Do you have many friends?
1. Yes (save as 1)
2. No (save as 0)
2) Do you like busy places?
1. Yes (save as 1)
2. No (save as 0)
3) Do you see your friends often?
1. Yes (save as 1)
2. No (save as 0)
4) Are you popular with people?
1. Yes (save as 1)
2. No (save as 0)
#
#
## Classification by groups:
```python
from BinClassify import BinClassify

# Sample data from the above test
data = [1, 0, 1, 0]
binclass = BinClassify()
binclass.CoutQustion(10) # 4
"""
The Answer method. Accepts an array with the following criteria:
1. The length of the array must be equal to the number returned by the CoutQustion method.
2. Array elements must be binary (1 or 0).
"""
print(binclass.Answer(data))
# Outputs: 6
# This means that my answer puts me in group 6.
# Starts from 1.
# Let's try a few more times:
print(binclass.Answer([0, 0, 0, 0])) # 1 
print(binclass.Answer([1, 1, 1, 1])) # 10
print(binclass.Answer([1, 1, 1, 0])) # 9
```
## Find out how many groups can be divided into by the number of questions
```python
# Import library
from BinClassify import BinClassify
# Creating a class
binclass = BinClassify()
"""
CoutGroups accepts the number of questions. Returns an array with a range of the number of groups.
The first element is the minimum number of groups for such a number of questions, the second is the maximum.
The minimum transmitted number is 1.
"""
print(binclass.CoutGroups(4))
# Outputs: [9, 16]
```