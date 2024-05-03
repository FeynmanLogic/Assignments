def pass1_assembler(program):
    IC = []
    ST = []
    LT = []
    nonliterals = ['A','B','C','D','E','F','G','H','X','Y','Z','I','J','K']
    OT = ['ADD', 'SUB', 'MOV', 'MUL', 'DIV']
    op = {'ADD': '01', 'SUB': '02', 'MOV': '03', 'MUL': '04', 'DIV': '05'}
    location_counter = 0

    for line in program:
        tokens = line.split()
        mnemonic = tokens[0]

        if mnemonic in OT:
            opcode = op[mnemonic]
            operand1 = tokens[1]
            operand2 = tokens[2]
            
            if operand1 not in nonliterals:
                entry1 = next((entry for entry in LT if entry[0] == operand1), None)
                if entry1 is None:
                    LT.append((operand1, location_counter))
                    entry1 = (operand1, location_counter)
                operand1 = f"LT({entry1[1]})"
                entry2 = next((entry for entry in ST if entry[0] == operand2), None)
                if entry2 is None:
                    ST.append((operand2, location_counter))
                    entry2 = (operand2, location_counter)
                operand2 = f"ST({entry2[1]} )"                
            if operand2 not in nonliterals:
                entry2 = next((entry for entry in LT if entry[0] == operand2), None)
                if entry2 is None:
                    LT.append((operand2, location_counter))
                    entry2 = (operand2, location_counter)
                operand2 = f"LT({entry2[1]})"
                entry1 = next((entry for entry in ST if entry[0] == operand1), None)
                if entry1 is None:
                    ST.append((operand1, location_counter))
                    entry1 = (operand1, location_counter)
                operand1 = f"ST({entry1[1]})"

            else:
                entry1 = next((entry for entry in ST if entry[0] == operand1), None)
                if entry1 is None:
                    ST.append((operand1, location_counter))
                    entry1 = (operand1, location_counter)
                operand1 = f"ST({entry1[1]})"
                entry2 = next((entry for entry in ST if entry[0] == operand2), None)
                if entry2 is None:
                    ST.append((operand2, location_counter))
                    entry2 = (operand2, location_counter)
                operand2 = f"ST({entry2[1]})"
                
            IC.append((location_counter, f"OT({opcode})", operand1, operand2))
            location_counter += 1

        elif mnemonic == 'DC':
            operand = tokens[1]
            LT.append((operand, location_counter))
            location_counter += 1

    return IC, ST, LT, OT


def pass2_assembler(IC, ST, LT, OT):
    machine_code = []

    for line in IC:
        location_counter, opcode, operand1, operand2 = line
        opcode_binary = format(int(opcode.split('(')[1].split(')')[0]), '03b') 

        if operand1.startswith('LT'):
            operand1_index = int(operand1.split('(')[1].split(')')[0])
        else:
            operand1_index = int(operand1.split('(')[1].split(')')[0])

        if operand2.startswith('LT'):
            operand2_index = int(operand2.split('(')[1].split(')')[0])
        else:
            operand2_index = int(operand2.split('(')[1].split(')')[0])

        machine_code.append(f"{location_counter} {opcode_binary} {operand1_index:02d} {operand2_index:02d}")

    return machine_code


program = [
    'MOV A B',
    'ADD A 5',
    'SUB C D',
    'MOV X Y',
    'MUL Z 8',
    'DIV E 3',
    'MOV F G',
    'ADD H 10',
    'SUB I 2',
    'MOV J K'
]

IC, ST, LT, OT = pass1_assembler(program)

print("Intermediate Code:")
for line in IC:
    print(line)

print("\nSymbol Table:")
for index, (symbol, address) in enumerate(ST, start=1):
    print(index, ":", symbol, address)

print("\nLiteral Table:")
for literal, address in LT:
    print(literal, ":", address)
print("Machine Code is:")
mach=pass2_assembler(IC,ST,LT,OT)
for line in mach:
    print(line)
