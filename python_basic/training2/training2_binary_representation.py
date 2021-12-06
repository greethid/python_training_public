# Write program that displays number of bits set in itself
# (means: calculating number of bits '1' in binary representation of that program)
# and displaying its binary representation.

with open('training2_binary_representation.py', 'rb') as text:
    print(text)

    all_file = text.read()

    all_file_char = [char for char in all_file]
    all_file_byte = bytearray(all_file)

    sum_1 = 0

    for byte in all_file_byte:
        sum_1 += bin(byte).count("1")

    # all_file_bin = toBinary(all_file)
    print(sum_1)
    print(all_file_char)
    # print(all_file)
    #gawel
