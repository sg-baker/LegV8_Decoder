import opcodes as op

# Taking input
print("Please input a valid LegV8 assembly command.\n")
instruction = input()

# Parsing the instruction
command = instruction.split(' ', 1)[0]
instr_type = op.opcodes[command][0]

if instr_type == 'R':
    # Need to parse rm, shamt, rn, and rd
    
elif instr_type == 'I':
    # Need to parse immediate, rn, rd
elif instr_type == 'D':
    # Need to parse address, op, rn, and rt
elif instr_type == 'B':
    # Need to parse address
elif instr_type == 'CB':
    # Need to parse address and rt
elif instr_type == 'IM':
    # Need to parse immediate and rt
