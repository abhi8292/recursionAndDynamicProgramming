item = ["10", "68", "97", "9", "21", "12"]

def makeLarge(item):
    item.sort(reverse=True)
    return item


print(makeLarge(item))