def swap_case(s):
    ss = ''
    for character in s:
        if character.isalpha():
            if character.isupper():
                character = character.lower()
            else:
                character = character.upper()
        ss+=character
    return ss

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)