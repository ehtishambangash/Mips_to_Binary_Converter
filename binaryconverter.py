instructions = {"ADD": "0000", "SLL": "0001", "SLR": "0010", "MUL": "1010", "MFLO": "1011", "MFHI": "1100",
                "OR": "0011", "AND": "0100", "ADDI": "0101", "LI": "0110", "LW": "0111", "SW": "1000", "J": "1001",
                "BEQZ": "1010", "BEQ": "1011", "MOVE": "1100"}

registers = {"T0": "000", "T1": "001", "T2": "010", "T3": "011", "T4": "100", "T5": "101", "T6": "110", "T7": "111"}

def Calculate():
    opcode_input = input("Enter the name of your command:").upper()
    opcode = ""
    instruction = ""
    for i in instructions:
        if opcode_input == i:
            opcode = opcode + instructions[i]
            instruction = instruction + opcode + "_"

    if opcode_input in ["ADDI", "LI", "LW", "SW"]:
        I_Rd_input = input("Enter Rd:").upper()
        I_Rs_input = input("Enter Rs:").upper()
        D_constant = int(input("Enter the Constant in decimal:"))
        constant = "{0:06b}".format(D_constant)
        for i in registers:
            if I_Rd_input == i:
                instruction = instruction + registers[i] + "_"
        for i in registers:
            if I_Rs_input == i:
                instruction = instruction + registers[i] + "_"
        instruction = instruction + constant
    elif opcode_input in ["J", "BEQZ", "BEQ"]:
        D_address = int(input("Enter the Address in decimal:"))
        address = "{0:09b}".format(D_address)
        instruction = instruction + address
        instruction = instruction + "000"
    elif opcode_input in ["ADD", "SLL", "SLR", "MUL", "MFLO", "MFHI", "OR", "AND", "MOVE"]:
        R_Rd_input = input("Enter Rd:").upper()
        R_Rs_input = input("Enter Rs:").upper()
        R_Rt_input = input("Enter Rt:").upper()
        D_shift = int(input("Enter the Shift in decimal:"))
        shift = "{0:03b}".format(D_shift)
        for i in registers:
            if R_Rd_input == i:
                instruction = instruction + registers[i] + "_"
        for i in registers:
            if R_Rs_input == i:
                instruction = instruction + registers[i] + "_"
        for i in registers:
            if R_Rt_input == i:
                instruction = instruction + registers[i] + "_"
        instruction = instruction + shift

    print(instruction)
    Calculate()
Calculate()