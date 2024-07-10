class CFG:
    def __init__(self, terminals, nonterminals, start_symbol, productions):
        self.terminals = terminals
        self.nonterminals = nonterminals
        self.start_symbol = start_symbol
        self.productions = productions

class NPDA:
    def __init__(self, states, input_symbols, stack_symbols, transitions, start_state, start_stack_symbol, accept_states):
        self.states = states
        self.input_symbols = input_symbols
        self.stack_symbols = stack_symbols
        self.transitions = transitions
        self.start_state = start_state
        self.start_stack_symbol = start_stack_symbol
        self.accept_states = accept_states

def construct_npda_from_cfg(cfg):
    start_state = "0"
    middle_state = "1"
    accept_state = "-1"
    states = {start_state, middle_state, accept_state}
    input_symbols = set(cfg.terminals)
    stack_symbols = set(cfg.nonterminals + cfg.terminals)
    
    transitions = []
    
    def add_transition(from_state, input_symbol, stack_top, to_state, stack_operation):
        transitions.append((from_state, input_symbol, stack_top, to_state, stack_operation))
    add_transition(start_state, 'ε', None, middle_state, f"PUSH({cfg.start_symbol})")

    for lhs in cfg.productions:
        for rhs in cfg.productions[lhs]:
            if rhs == ['ε']:
                add_transition(middle_state, 'ε', lhs, middle_state, "POP")
            else:
                rhs_reversed = ''.join(rhs[::-1])
                add_transition(middle_state, 'ε', lhs, middle_state, f"PUSH({rhs_reversed})")
    
    for terminal in cfg.terminals:
        add_transition(middle_state, terminal, terminal, middle_state, "POP")
    
    add_transition(middle_state, 'ε', '$', accept_state, "ε")

    return NPDA(
        states=states,
        input_symbols=input_symbols,
        stack_symbols=stack_symbols,
        transitions=transitions,
        start_state=start_state,
        start_stack_symbol='$',
        accept_states={accept_state}
    )

# Example CFG
cfg = CFG(
    terminals=['a', 'b'],
    nonterminals=['S', 'A'],
    start_symbol='S',
    productions={
        'S': [['a', 'A', 'b']],
        'A': [['a', 'S', 'b'], ['ε']],
    }
)

npda = construct_npda_from_cfg(cfg)

print("NPDA Transitions:")
for transition in npda.transitions:
    print(f"{transition[0]}, {transition[1]}, {transition[2]}, {transition[3]}, {transition[4]}")
