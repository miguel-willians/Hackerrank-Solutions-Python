def swap_case(s):
  # Solution: / Solução:
    swapped = ''.join(letter.upper() if letter.islower() else letter.lower() for letter in s)
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
