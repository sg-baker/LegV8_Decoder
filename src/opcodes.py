# This will contain the table with every commands unique opcode

# {Command : [type, opcode, *shamt]}
# * - shamt if it is an R type instruction


opcodes = {'B': ['B', '000101'],
           'FMULS': ['R', '00011110001', '000010'],
           'FDIVS': ['R', '00011110001', '000110'],
           'FCMPS': ['R', '00011110001', '001000'],
           'FADDS': ['R', '00011110001', '001010'],
           'FSUBS': ['R', '00011110001', '001110'],
           'FMULD': ['R', '00011110011', '000010'],
           'FDIVD': ['R', '00011110011', '000110'],
           'FCMPD': ['R', '00011110011', '001000'],
           'FADDD': ['R', '00011110011', '001010'],
           'FSUBD': ['R', '00011110011', '001110'],
           'STURB': ['D', '00111000000'],
           'LDURB': ['D', '00111000010'],
           'B.cond': ['CB', '01010100'],
           'STURH': ['D', '01111000000'],
           'LDURH': ['D', '01111000010'],
           'AND': ['R', '10001010000', '000000'],
           'ADD': ['R', '10001011000', '000000'],
           'ADDI': ['I', '1001000100'],
           'ANDI': ['I', '1001001000'],
           'BL': ['B', '100101'],
           'SDIV': ['R', '10011010110', '000010'],
           'UDIV': ['R', '10011010110', '000011'],
           'MUL': ['R', '10011011000', '011111'],
           'SMULH': ['R', '10011011010', '000000'],
           'UMULH': ['R', '10011011110', '000000'],
           'ORR': ['R', '10101010000', '000000'],
           'ADDS': ['R', '10101011000', '000000'],
           'ADDIS': ['I', '1011000100'],
           'ORRI': ['I', '1011001000'],
           'CBZ': ['CB', '10110100'],
           'CBNZ': ['CB', '10110101'],
           'STURW': ['D', '10111000000'],
           'LDURSW': ['D', '10111000100'],
           'STURS': ['R', '10111100000', '000000'],
           'LDURS': ['R', '10111100010', '000000'],
           'STXR': ['D', '11001000000'],
           'LDXR': ['D', '11001000010'],
           'EOR': ['R', '11001010000', '000000'],
           'SUB': ['R', '11001011000', '000000'],
           'SUBI': ['I', '1101000100'],
           'EORI': ['I', '1101001000'],
           'MOVZ': ['IM', '110100101'],
           'LSR': ['R', '11010011010', '000000'],
           'LSL': ['R', '11010011011', '000000'],
           'BR': ['R', '11010110000', '000000'],
           'ANDS': ['R', '11101010000', '000000'],
           'SUBS': ['R', '11101011000', '000000'],
           'SUBIS': ['I', '1111000100'],
           'ANDIS': ['I', '1111001000'],
           'MOVK': ['IM', '111100101'],
           'STUR': ['D', '11111000000'],
           'LDUR': ['D', '11111000010'],
           'STURD': ['R', '11111100000', '000000'],
           'LDURD': ['R', '11111100010', '000000']
           } 

# This is a function that converts binary values to their 2's complement

def twos_complement(binary_value):
    # Reverse binary value to work from LSB to MSB
    backwards_value = binary_value[::-1]
    complement = ''
        
    # Convert the binary value to 2's complement. Easiest way to do this
    # is to keep the first 1 that you come across, and then flip every bit
    # beyond that.

    # Flipping logic
    one_encountered = False
    for bit in backwards_value:
        if one_encountered == True:
            if bit == '1':
                complement += '0'
            else:
                complement += '1'
        else:
            if bit == '1':
                complement += '1'
                one_encountered = True
            else:
                complement += '0'
     
    # Returning new address
    return complement[::-1]