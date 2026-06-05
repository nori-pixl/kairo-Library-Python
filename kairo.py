import re
import os

def _val(x):
    if isinstance(x, str) and x.isdigit(): return int(x)
    return x.value if hasattr(x, 'value') else int(bool(x))

class Node:
    def __init__(self, value=0, name=""):
        self.value = _val(value)
        self.name = name
    def __repr__(self):
        return f"{self.name} => {self.value}" if self.name else str(self.value)

def inname(name, value=0): return Node(value, name=name)
def outname(name, node):    return Node(_val(node), name=name)

def NOT(a):     return Node(not _val(a))
def AND(*args): return Node(all(_val(x) for x in args))
def OR(*args):  return Node(any(_val(x) for x in args))
def XOR(*args): return Node(sum(_val(x) for x in args) % 2 == 1)
def NAND(*args):return Node(not all(_val(x) for x in args))
def NOR(*args): return Node(not any(_val(x) for x in args))
def XNOR(*args):return Node(sum(_val(x) for x in args) % 2 == 0)

class KairoEngine:
    def __init__(self):
        self.variables = {}
        self.outputs = []

    def run_file(self, file_path, function_name="index"):
        if not os.path.exists(file_path):
            print(f"Error: '{file_path}' not found.")
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()

        func_pattern = rf"def\s+{function_name}\s*\(\s*\):(.*?(?=def\s|\Z))"
        match_func = re.search(func_pattern, code, re.DOTALL)
        if not match_func:
            print(f"Error: Function '{function_name}' not found.")
            return

        self._parse_lines(match_func.group(1).splitlines())
        
        print(f"--- {file_path} ---")
        for node in self.outputs:
            print(node)

    def _parse_lines(self, lines):
        current_module = globals()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line or line.startswith("#"):
                i += 1
                continue

            for_match = re.match(r"for\s+(\w+)\s+in\s+range\(\s*(\d+)\s*\)\s*:", line)
            if for_match:
                loop_var, count_str = for_match.groups()
                count = int(count_str)
                
                loop_lines = []
                i += 1
                while i < len(lines) and (not lines[i].strip() or lines[i].startswith(" ") or lines[i].startswith("\t")):
                    loop_lines.append(lines[i])
                    i += 1
                
                for val in range(count):
                    processed_lines = []
                    for l in loop_lines:
                        replaced = l
                        calc_matches = re.findall(rf"\[\s*{loop_var}\s*([\+\-])\s*(\d+)\s*\]", replaced)
                        for op, num in calc_matches:
                            offset = int(num) if op == '+' else -int(num)
                            replaced = replaced.replace(f"[{loop_var}{op}{num}]", str(val + offset))
                        replaced = replaced.replace(f"[{loop_var}]", str(val))
                        replaced = replaced.replace(f"{{{loop_var}}}", str(val))
                        processed_lines.append(replaced)
                    self._parse_lines(processed_lines)
                continue

            assignment_match = re.match(r"(\w+)\s*=\s*(?:kr\.)?([A-Za-z_]\w*)\((.*)\)", line)
            if assignment_match:
                var_name, func_name, args_str = assignment_match.groups()
                
                if func_name in current_module:
                    func_obj = current_module[func_name]
                else:
                    i += 1
                    continue

                args_raw = [arg.strip() for arg in args_str.split(",")]
                actual_args = []
                for arg in args_raw:
                    if not arg: continue
                    str_match = re.match(r"[\"']([^\n\"']*)[\"']", arg)
                    if str_match:
                        actual_args.append(str_match.group(1))
                    elif arg.isdigit():
                        actual_args.append(int(arg))
                    elif arg in self.variables:
                        actual_args.append(self.variables[arg])
                    else:
                        actual_args.append(0)

                result_node = func_obj(*actual_args)
                self.variables[var_name] = result_node

                if func_name == "outname":
                    self.outputs.append(result_node)

            i += 1

def run_file(file_path, function_name="index"):
    engine = KairoEngine()
    engine.run_file(file_path, function_name)
