coins = [5, 6, 1, 1, 2, 3, 43]
coins.sort()
#create a minimum change variable
minimum_change = 0
#loop through coins
for coin in coins:
    if coin > minimum_change + 1:
        break
    minimum_change += coin
print(minimum_change + 1)
