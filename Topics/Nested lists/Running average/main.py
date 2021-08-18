digits = input()
list_ = [int(x) for x in digits]
moving_average = []
count = 0
while count < (len(list_)-1):
    ai = (list_[count] + list_[count+1])/2
    moving_average.append(ai)
    count = count + 1
print(moving_average)
