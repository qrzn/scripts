import random
import re

# --- I. Grammar Rules (Initial State) ---
grammar_rules = {
    "expr": ["func_call", "bin_op", "literal"],
    "func_call": ["func_{name}({args})"],
    "bin_op": ["({left} {op} {right})"],
    "literal": ["const_{val}"],
    "name": ["add", "sub", "mul", "div"],
    "args": ["expr", "expr, expr"],
    "left": ["expr"],
    "right": ["expr"],
    "op": ["+", "-", "*", "/"],
    "val": ["1", "2", "3", "42"]
}

rule_usage = {k: 0 for k in grammar_rules}

# --- II. Recursive Expander ---
def expand(symbol, depth=0, max_depth=5):
    if depth > max_depth:
        return "∅"  # Collapse event
    rule = random.choice(grammar_rules.get(symbol, [symbol]))
    rule_usage[symbol] += 1
    result = re.sub(r'\{(\w+)\}', lambda m: expand(m.group(1), depth + 1, max_depth), rule)
    return result

# --- III. Mutation Routine ---
def mutate_rule(symbol):
    if symbol not in grammar_rules:
        return
    if random.random() < 0.3:  # 30% chance
        grammar_rules[symbol].append("func_void({args})")
        grammar_rules[symbol] = list(set(grammar_rules[symbol]))

# --- IV. Decay Routine ---
def decay_rules():
    for k in list(grammar_rules):
        if rule_usage[k] == 0 and len(grammar_rules[k]) > 1:
            grammar_rules[k].pop()
        rule_usage[k] = 0

# --- V. ASCII Tree Renderer ---
def draw_tree(symbol, depth=0, max_depth=5):
    if depth > max_depth:
        return "  " * depth + "∅"
    rule = random.choice(grammar_rules.get(symbol, [symbol]))
    output = "  " * depth + symbol + " → " + rule
    branches = re.findall(r'\{(\w+)\}', rule)
    for b in branches:
        output += "\n" + draw_tree(b, depth + 1, max_depth)
    return output

# --- VI. Drift Run Example ---
if __name__ == "__main__":
    random.seed(42)  # Determinism for demo
    print("--- Drift Expansion ---")
    print(expand("expr"))
    print("\n--- Syntax Forest ---")
    print(draw_tree("expr"))
    print("\n--- Drift Mutation Applied ---")
    for key in grammar_rules:
        mutate_rule(key)
    print("--- Syntax Forest Post-Mutation ---")
    print(draw_tree("expr"))
    decay_rules()
