class TuringMachine:
    def __init__(self, tape, blank, initial_state, final_state, transition):
        self.tape = list(tape)
        self.blank = blank
        self.head = 0
        self.current_state = initial_state
        self.final_state = final_state
        self.transition = transition

    def step(self):
        current_symbol = self.tape[self.head]
        if (self.current_state, current_symbol) in self.transition:
            new_state, new_symbol, direction = self.transition[(self.current_state, current_symbol)]
            self.tape[self.head] = new_symbol
            self.current_state = new_state
            if direction == 'R':
                self.head += 1
                if self.head == len(self.tape):
                    self.tape.append(self.blank)
            elif direction == 'L':
                self.head -= 1
                if self.head < 0:
                    self.tape.insert(0, self.blank)
                    self.head = 0
        else:
            self.current_state = 'REJECT'

    def run(self):
        while self.current_state not in self.final_state and self.current_state != 'REJECT':
            self.step()
        return self.current_state in self.final_state

transition = { ('q0', 'a'): ('q1', 'a', 'R'),
               ('q1', 'a'): ('REJECT', 'a', 'R'),
               ('q1', 'b'): ('q1', 'b', 'R'),
               ('q1', 'a'): ('q2', 'a', 'R'),
               ('q2', 'a'): ('REJECT', 'a', 'R'),
               ('q2', 'b'): ('q2', 'b', 'R'),
               ('q2', 'a'): ('q3', 'a', 'R'),
               ('q3', 'a'): ('REJECT', 'a', 'R'),
               ('q3', 'b'): ('REJECT', 'b', 'R'),
               ('q3', ' '): ('qaccept', ' ', 'R'), }

def main():
    tape = input("Enter the input tape : ")
    blank = ' '
    initial_state = 'q0'
    final_state = {'qaccept'}

    tm = TuringMachine(tape, blank, initial_state, final_state, transition)
    accepted = tm.run()

    print(f"The input string {'is' if accepted else 'is not'} accepted by the Turing machine.")

if __name__ == "__main__":
    main()