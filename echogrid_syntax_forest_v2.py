import random
import re
import json
from graphviz import Digraph

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
node_log = []
collapse_events = []

# --- II. Recursive Expander with Logging and Collapse Detection ---
def expand(symbol, depth=0, max_depth=5):
    if depth > max_depth:
        collapse_events.append({"symbol": symbol, "depth": depth})
        return "∅"
    rule = random.choice(grammar_rules.get(symbol, [symbol]))
    rule_usage[symbol] += 1
    node_entry = {"symbol": symbol, "rule": rule, "depth": depth}
    node_log.append(node_entry)
    result = re.sub(r'\{(\w+)\}', lambda m: expand(m.group(1), depth + 1, max_depth), rule)
    return result

# --- III. Mutation Routine ---
def mutate_rule(symbol):
    if symbol not in grammar_rules:
        return
    if random.random() < 0.3:
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

# --- VI. Export JSON and Entropy Metrics ---
def export_state_json(filename="syntax_forest.json"):
    state = {
        "nodes": node_log,
        "collapses": collapse_events,
        "rules": grammar_rules
    }
    with open(filename, "w") as f:
        json.dump(state, f, indent=2)

def compute_entropy():
    total = sum(len(v) for v in grammar_rules.values())
    symbols = len(grammar_rules)
    avg = total / symbols if symbols else 0
    return {"total_variants": total, "symbol_count": symbols, "avg_variants_per_symbol": avg}

# --- VII. Symbolic Overlay Mapping via Graphviz ---
def generate_svg(symbol="expr", max_depth=5, filename="syntax_forest.svg"):
    dot = Digraph()

    def recurse(node, depth=0, parent=None):
        if depth > max_depth:
            cid = f"collapse_{depth}_{random.randint(1000,9999)}"
            dot.node(cid, "∅", shape="diamond", color="red")
            if parent:
                dot.edge(parent, cid)
            return

        rule = random.choice(grammar_rules.get(node, [node]))
        nid = f"{node}_{depth}_{random.randint(1000,9999)}"
        dot.node(nid, f"{node}\n→ {rule}")
        if parent:
            dot.edge(parent, nid)
        for child in re.findall(r"\{(\w+)\}", rule):
            recurse(child, depth + 1, nid)

    recurse(symbol)
    dot.render(filename, format="svg", cleanup=True)

# --- VIII. Drift Run Example ---
if __name__ == "__main__":
    random.seed(42)
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
    print("\n--- Entropy Metrics ---")
    print(compute_entropy())
    export_state_json()
    generate_svg()
