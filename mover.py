import json

with open('mover.json', 'r') as file:
    data = json.load(file)

for output, inputs in data.items():
    with open(output, 'w') as file:
        lines = []
        for inp in inputs:
            with open(inp, 'r') as inp_file:
                lines += inp_file.readlines()
                lines += '\n'
        print(lines)
        file.writelines(lines)
