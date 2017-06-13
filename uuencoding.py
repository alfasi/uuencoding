def bytes_to_uuencoding(array, mode, filename):
    result = 'begin ' + str(mode) + ' ' + filename + '\n'

    remaining_bytes = len(array)

    while remaining_bytes > 0:
        # Handle line (45 characters)
        if remaining_bytes >= 45:
            line = array[len(array) - remaining_bytes : 
                         len(array) - remaining_bytes + 45]
        else:
            line = array[len(array) - remaining_bytes :]
            
            # 0 padding
            if len(line) % 3 == 1:
                line += str(chr(0)) + str(chr(0))
            elif len(line) % 3 == 2:
                line += str(chr(0))

        remaining_bytes -= len(line)

        formatted_line = ''

        for i in range(0, len(line), 3):
            letter_group = chr(32 + (ord(line[i]) >> 2))
            letter_group += chr(32 + (((ord(line[i]) & 0b00000011) << 4) | (ord(line[i+1]) >> 4)))
            letter_group += chr(32 + (((ord(line[i+1]) & 0b00001111) << 2) |
                                ord(line[i+2]) >> 6))
            letter_group += chr(32 + (ord(line[i+2]) & 0b00111111 ))

            formatted_line += letter_group

        result += str(chr(32 + len(line))) + formatted_line + '\n'

    result += '`\nend\n'

    return result


def main():
    mode = 644
    filename = 'filename.txt'
    raw = input("Enter text:")

    uuenc = bytes_to_uuencoding(raw, mode, filename)

    print(uuenc)

if __name__ == '__main__': 
    main()

