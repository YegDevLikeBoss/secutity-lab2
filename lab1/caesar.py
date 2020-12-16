import sys

def shift(char: str, num: int) -> str:
    """Shift a charecter"""
    code = ord(char)
    a, A, z, Z = ord('a'), ord('A'), ord('z'), ord('Z')

    if code >= A and code <= Z:
        rv = code + (num%26)
        if rv > Z:
            rv -= 26
        return chr(rv)
    elif code >= a and code <= z:
        rv = code + (num%26)
        if rv > z:
            rv -= 26
        return chr(rv)
    else:
        return char

def chipher(sentence: str, key) -> str:
    try:
        key = int(key)
    except ValueError:
        key = str(key)
    if type(key) == type(0):
        return ''.join(map(shift, sentence, [key]*len(sentence)))
    else:
        return ''.join(map(shift, sentence, [ord(char)-97 for char in key.lower()]*((len(sentence)//len(key))+1)))

print(chipher(str(sys.argv[1]), sys.argv[2]))
