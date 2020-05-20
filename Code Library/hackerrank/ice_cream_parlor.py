def findFlavors(cost, flavorsList):
    amount = 0
    for i in range(len(flavorsList)):
        j = i + 1
        if j >= len(flavorsList):
            j = 0
        while j != i:
            amount = flavorsList[i] + flavorsList[j]
            if amount == cost:
                return i + 1, j + 1
            else:
                j += 1
                if j >= len(flavorsList):
                    j = 0
                    
def main():
    numTestCases = int(input())
    out = []
    for i in range(numTestCases):
        cost = int(input())
        flavors = input()
        flavorsList = input().split()
        flavorsList = [int(i) for i in flavorsList]
        f1, f2 = findFlavors(cost, flavorsList)
        out.append([f1, f2])
    for item in out:
            print(item[0], item[1])

main()
