#Solution: / Solução:
def happiness():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    set_A = set(map(int, input().split()))
    set_B = set(map(int, input().split()))

    counter = 0
    
    for number in arr:
        if number in set_A:
            counter += 1
        elif number in set_B:
            counter -= 1
        
    print(counter)
    
happiness()
