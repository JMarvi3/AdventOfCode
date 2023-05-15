from collections import defaultdict


class Intcode_VM:
    DONE, WAITING = -1, 0
    memory = outputs = inputs = input_idx = pc = rb = None

    @staticmethod
    def decode_instruction(inst):
        codes = [inst % 100]
        inst //= 100
        for _ in range(3):
            codes.append(inst % 10)
            inst //= 10
        return codes

    def process_mode(self, param, mode):
        if mode == 0:
            return self.memory[param]
        elif mode == 1:
            return param
        elif mode == 2:
            return self.memory[param + self.rb]

    def __init__(self, program, inputs=[]):
        if isinstance(program, str):
            program = map(int, program.split(','))
        self.program = defaultdict(int)
        for i, data in enumerate(program):
            self.program[i] = data
        self.reset(inputs)

    def reset(self, inputs=[]):
        self.memory = self.program.copy()
        self.outputs = []
        self.inputs = inputs
        self.input_idx = 0
        self.pc = 0
        self.rb = 0

    def run(self, inputs=[]):
        pc = self.pc
        memory = self.memory
        self.inputs.extend(inputs)
        while True:
            if pc >= len(memory):
                pass
            op, mode1, mode2, mode3 = Intcode_VM.decode_instruction(memory[pc])
            if op == 1:
                src1, src2, dest = memory[pc+1], memory[pc+2], memory[pc+3]
                src1, src2 = self.process_mode(src1, mode1), self.process_mode(src2, mode2)
                if mode3 == 2:
                    dest += self.rb
                memory[dest] = src1 + src2
                pc += 4
            elif op == 2:
                src1, src2, dest = memory[pc+1], memory[pc+2], memory[pc+3]
                src1, src2 = self.process_mode(src1, mode1), self.process_mode(src2, mode2)
                if mode3 == 2:
                    dest += self.rb
                memory[dest] = src1 * src2
                pc += 4
            elif op == 3:
                if self.input_idx == len(self.inputs):
                    self.inputs = []
                    self.input_idx = 0
                    self.pc = pc
                    outputs = self.outputs
                    self.outputs = []
                    return Intcode_VM.WAITING, outputs
                dest = memory[pc + 1]
                if mode1 == 2:
                    dest += self.rb
                memory[dest] = self.inputs[self.input_idx]
                self.input_idx += 1
                pc += 2
            elif op == 4:
                src = self.process_mode(memory[pc + 1], mode1)
                self.outputs.append(src)
                pc += 2
            elif op == 5:
                src, dest = self.process_mode(memory[pc + 1], mode1), self.process_mode(memory[pc + 2], mode2)
                if src != 0:
                    pc = dest
                else:
                    pc += 3
            elif op == 6:
                src, dest = self.process_mode(memory[pc + 1], mode1), self.process_mode(memory[pc + 2], mode2)
                if src == 0:
                    pc = dest
                else:
                    pc += 3
            elif op == 7:
                src1, src2, dest = memory[pc+1], memory[pc+2], memory[pc+3]
                src1, src2 = self.process_mode(src1, mode1), self.process_mode(src2, mode2)
                if mode3 == 2:
                    dest += self.rb
                memory[dest] = 1 if src1 < src2 else 0
                pc += 4
            elif op == 8:
                src1, src2, dest = memory[pc+1], memory[pc+2], memory[pc+3]
                src1, src2 = self.process_mode(src1, mode1), self.process_mode(src2, mode2)
                if mode3 == 2:
                    dest += self.rb
                memory[dest] = 1 if src1 == src2 else 0
                pc += 4
            elif op == 9:
                self.rb += self.process_mode(memory[pc+1], mode1)
                pc += 2
            elif op == 99:
                self.pc = pc
                return Intcode_VM.DONE, self.outputs
