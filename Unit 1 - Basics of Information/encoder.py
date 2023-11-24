# note, this only works because of a correct encoding system with no bit overlaps

def encode(msg, encodeSystem):

    encodedMessage = [encodingSystem.get(char, char) for char in msg]
    return ''.join(encodedMessage)

'''Example usage:
encodingSystem = {'A': '00', 'B': '01', 'C': '10', 'D': '11'}
result = encode("BADC", encodingSystem)

#thus result will be = 01001110
print(result)
'''
