INSTRUCTIONS = {
    "PUSH": 0x01,
    "XOR":  0x02,
    "RET":  0xFF
}

def compile_input(raw_str: str) -> list:
    bytecode = []
    for ch in raw_str:
        bytecode.append(INSTRUCTIONS["PUSH"])
        bytecode.append(ord(ch))
    bytecode.append(INSTRUCTIONS["XOR"])
    bytecode.append(66)
    bytecode.append(INSTRUCTIONS["RET"])
    return bytecode

def interpret(bytecode: list) -> str:
    stack = []
    pc = 0
    while pc < len(bytecode):
        instr = bytecode[pc]
        pc += 1
        if instr == INSTRUCTIONS["PUSH"]:
            stack.append(bytecode[pc])
            pc += 1
        elif instr == INSTRUCTIONS["XOR"]:
            k = bytecode[pc]
            pc += 1
            stack = [b ^ k for b in stack]
        elif instr == INSTRUCTIONS["RET"]:
            return ''.join(f'{c:02x}' for c in stack)
        else:
            raise Exception(f"Unknown instruction {instr}")
    return ""
