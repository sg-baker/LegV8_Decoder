from audioop import add
from email.headerregistry import Address
from pickletools import opcodes
from tkinter.tix import IMMEDIATE
import opcodes as op

# Output variables
machine_binary = ''
machine_hex = ''

# Taking input
print("Please input a valid LegV8 assembly command.\n")
instruction = input()

# Parsing the instruction
command = instruction.split(' ', 1)[0]
instr_type = op.opcodes[command][0]
opcode = op.opcodes[command][1]

if instr_type == 'R':
    # Parsing rm, rn, and rd
    instruction = instruction.split(' ', 1)[1]
    instruction = instruction.split(',')

    # Assiging rm, rn, and rd
    rm = instruction[2].lstrip(' X')
    rn = instruction[1].lstrip(' X')
    rd = instruction[0].lstrip('X')
    #print(rm,' ', rn,' ' ,rd)

    # Converting to binary
    rm = bin(int(rm)).lstrip('0b')
    rn = bin(int(rn)).lstrip('0b')
    rd = bin(int(rd)).lstrip('0b')
    #print(rm,' ', rn,' ' ,rd)

    # Adding leading zeros
    rm = '0' * (5 - len(rm)) + rm
    rn = '0' * (5 - len(rn)) + rn
    rd = '0' * (5 - len(rd)) + rd
    #print(rm,' ', rn,' ' ,rd)

    # Assiging shamt from 
    shamt = op.opcodes[command][2]

    # Putting full instruction together
    machine_binary = opcode + rm + shamt + rn + rd
    #print(machine_binary)


elif instr_type == 'I':
    # Parsing immediate, rn, rd
    instruction = instruction.split(' ', 1)[1]
    instruction = instruction.split(',')
    
    # Assiging immediate, rn, rd
    imm = instruction[2].lstrip(' #')
    rn = instruction[1].lstrip(' X')
    rd = instruction[0].lstrip('X')
    #print(rd, ' ', rn, ' ', imm)

    # Converting to binary
    imm = bin(int(imm)).lstrip('0b')
    rn = bin(int(rn)).lstrip('0b')
    rd = bin(int(rd)).lstrip('0b')
    #print(rd, ' ', rn, ' ', imm)


    # TODO: Make a use case for the immediate being negative

    # Adding leading zeros if needed
    imm = '0' * (12 - len(imm)) + imm
    rn = '0' * (5 - len(rn)) + rn 
    rd = '0' * (5 - len(rd)) + rd
    #print(rd, ' ', rn, ' ', imm)

    # Putting full instruction together
    machine_binary = opcode + imm + rn + rd
    #print(machine_binary)

elif instr_type == 'D':
    # Parsing address, rn, and rt
    instruction = instruction.split(' ', 1)[1]
    instruction = instruction.split(',')

    # Assigning op, address, rn, and rt
    two_bit_op = '00'
    address = instruction[2].lstrip(' #')
    address = address.rstrip(']')
    rn = instruction[1].lstrip(' [X')
    rt = instruction[0].lstrip('X')
    #print(two_bit_op, ' ', address, ' ', rn, ' ', rt)

    # TODO: Make a use case for the address being negative

    # Converting to binary
    address = bin(int(address)).lstrip('0b')
    rn = bin(int(rn)).lstrip('0b')
    rt = bin(int(rt)).lstrip('0b')
    #print(two_bit_op, ' ', address, ' ', rn, ' ', rt)

    # Adding leading zeros if needed
    address = '0' * (9 - len(address)) + address
    rn = '0' * (5 - len(rn)) + rn 
    rt = '0' * (5 - len(rt)) + rt
    #print(two_bit_op, ' ', address, ' ', rn, ' ', rt)

    # Putting full instruction together
    machine_binary = opcode + address + two_bit_op + rn + rt
    #print(machine_binary)  

elif instr_type == 'B':
    # Need to parse address
    address = instruction.split(' ')[1]
    #print(address)

    # TODO: Make a use case for the address being negative

    # Converting to binary
    address = bin(int(address)).lstrip('0b')
    #print(address)

    # Adding leading zeros
    address = '0' * (26 - len(address)) + address
    #print(address)

    # Putting full instruction together
    machine_binary = opcode + address
    #print(machine_binary)


elif instr_type == 'CB':
    # Need to parse address and rt
    instruction = instruction.split(' ', 1)[1]
    instruction = instruction.split(',')

    # Assigning address and rt
    address = instruction[1].lstrip(' ')
    rt = instruction[0].lstrip('X')
    #print(address, ' ', rt)
    # TODO: Make a use case for the address being negative

    # Converting to binary
    address = bin(int(address)).lstrip('0b')
    rt = bin(int(rt)).lstrip('0b')
    #print(address, ' ', rt)

    # Adding leading zeros
    address = '0' * (19 - len(address)) + address
    rt = '0' * (5 - len(rt)) + rt
    #print(address, ' ', rt)

    # Putting full instruction together
    machine_binary = opcode + address + rt
    #print(machine_binary)


elif instr_type == 'IM':
    # Need to parse immediate and rd
    instruction = instruction.split(' ', 1)[1]
    instruction = instruction.split(',')
    #print(instruction)

    # Assigning immediate and rd
    imm = instruction[1].lstrip(' ')
    rd = instruction[0].lstrip('X')
    #print(imm, ' ', rd)

    # TODO: Make a use case for the address being negative

    # Converting to binary
    imm = bin(int(imm)).lstrip('0b')
    rd = bin(int(rd)).lstrip('0b')
    #print(imm, ' ', rd)

    # Adding leading zeros
    imm = '0' * (16 - len(imm)) + imm
    rd = '0' * (5 - len(rd)) + rd
    #print(imm, ' ', rd)

    # Putting full instruction together
    machine_binary = opcode + imm + rd
    #print(machine_binary)


# Converting hex to binary
machine_hex = hex(int(machine_binary, 2))
machine_hex = machine_hex.lstrip('0x')
machine_hex = machine_hex.upper()

# Printing results
print('Machine Code:')
print('Binary: ', machine_binary)
print('Hex: ', machine_hex)
