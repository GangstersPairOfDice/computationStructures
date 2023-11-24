# note, this only works because of a correct encoding system with no bit overlaps

def decoder(msg, encodingSystem):

    decodingSystem = {v: k for k, v in encodingSystem.items()}
    encodedMessage = [decodingSystem.get(char, char) for char in msg]
    return ''.join(encodedMessage)

'''Example usage:
encodingSystem = {'A': '00', 'B': '01', 'C': '10', 'D': '11'}
result = decode("01001110", encodingSystem)

#thus result will be = 'BADC'
print(result)
'''
