#============================================ Numbers from 1-150 ==================================================

for num in range (0,151,1):
    print(num)

#============================================ Multiples of Five ==================================================

for numfive in range (5,1000,5):
    print(numfive)

#============================================ Counting the Dojo Way ==================================================

for nums in range (1,100,1):
    if nums % 10 == 0:
        print("Coding Dojo")
    elif nums % 5 == 0:
        print("Coding")
    else:
        print(nums)

#============================================ Whoa. That Sucher's Huge ==================================================

sum = 0

for numsimp in range (1,500000,2):
    sum = sum + numsimp

print(sum)


#============================================ Countdown by Fours ==================================================
limit = 2018

while limit >=0:
    print(limit)
    limit = limit - 4

#============================================ Flexible Counter ==================================================

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum,highNum,mult):
    print(i+1)

