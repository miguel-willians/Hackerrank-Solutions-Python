# Solution: / Solução:
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

maxValue = max(arr) 
aux = None

for num in arr:
    if num == maxValue:
        continue
    elif aux == None:
        aux = num
    elif num > aux:
        aux = num

print(aux)

# Another solution without preserving the list: / Outra solução sem preservar a lista:
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
  
arr = list(set(arr))
arr.remove(max(arr))
print(max(arr))
