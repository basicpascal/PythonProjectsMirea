numbers = [2, 1, 2, 5, 6, 3, 4, 5]
foundChains = []
a = numbers[0]
chain = []
for element in numbers:
    a -= element
    if a <= 0:
        chain.append(element)
    else:
        foundChains.append(chain)
        chain = [element]
    a = element
foundChains.append(chain)
maxLength = 0
maxLengthIndex = 0
for i in range(len(foundChains)):
    if maxLength < len(foundChains[i]):
        maxLength = len(foundChains[i])
        maxLengthIndex = i
print(*foundChains[maxLengthIndex])
