# 1. Provide the sum of the following variables

num10 = 10
string8 = '8'
one = 1

num10 + int(string8) + one

# 2. Write a loop that will print only numbers divisible by 3 between 20 - 100
for i in range(20, 100):
  if i % 3 == 0:
    print(i)

# 3. Find the class average given the following test scores

scores = [88, 84, 100, 92, 70, 76, 76, 84, 86, 98]
sum(scores) / len(scores)
