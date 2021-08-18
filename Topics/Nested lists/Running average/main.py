"""Read a string with digits from the input and convert each number of the string to an integer. For your newly created list, calculate the running average according to the following formula:

Ai=xi+xi+12,
where xi and xi+1 are elements of the original list, Ai is the element of the moving average. For instance, if your string is 123, an average of 1 and 2 will be 1.5, and an average of 2 and 3 will be 2.5.

Print the result. Notice that this list will have one less item."""
digits = input()
list_ = [int(x) for x in digits]
moving_average = []
count = 0
while count < (len(list_) - 1):
    ai = (list_[count] + list_[count + 1]) / 2
    moving_average.append(ai)
    count = count + 1
print(moving_average)
