from argparse import ArgumentParser
from tqdm import tqdm

def GetBasicOperation(op: str):
    if op == '+':
        return int.__add__
    if op == '-':
        return int.__sub__
    if op == '*':
        return int.__mul__
    if op == '/':
        return int.__floordiv__
    if op == '%':
        return int.__mod__
    raise(f"Operation {op} not recognized")

def ImportData(file_path: str) -> (dict, list):
    values = []
    operations = []
    start_nodes = set()
    end_nodes = set()
    leaves = set()

    with open(file_path, 'r') as data:
        lines = data.readlines()
        number_of_nodes = int(lines[0])
        total_number_of_lines = len(lines)

        #Populate initial node locations
        for i in range(number_of_nodes):
            values.append(int(lines[i+1]))

        #Populate operations array
        for j in range(number_of_nodes + 1, total_number_of_lines):
            op = tuple(lines[j].split(' '))
            start_nodes.add(op[0])
            end_nodes.add(op[1])
            operations.append((int(op[0]), int(op[1]), GetBasicOperation(op[2].strip())))

        #Find leaf nodes
        for n in end_nodes:
            if n not in start_nodes:
                leaves.add(n)

    return (values, operations, leaves)

def find_next(index, ops):
    next = []
    for elem in ops:
        if elem[0]==index:
            next.append((elem[1], elem[2]))
    return next

def iterate(iterations, vals, ops):
    count = 0
    max = -9999999999

    #to_test: index, actual_value
    to_test = [(0, vals[0])]

    pbar = tqdm(total=iterations, desc="Iterating...")
    while count < iterations:
        count += 1
        pbar.update(1)
        new_to_test = []
        for node_index, actual_value in to_test:
            next = find_next(node_index, ops)
            if len(next) == 0:
                #leaf
                if actual_value > max:
                    print(actual_value)
                    max = actual_value
            else:
                for next_index, op in next:
                    next_base_value = vals[next_index]
                    try:
                        new_to_test.append((next_index, op(actual_value, next_base_value)))
                    except:
                        continue
                    
        to_test = new_to_test
    pbar.close()

parser = ArgumentParser(description="Calculate max value across graph")
parser.add_argument("--input", "-i", action="store", help="The file containing the graph data. See the example file provided in Git repo for file structure.", required=True)
parser.add_argument("--iterations", "-I", action="store", type=int, help="Number of iterations to run through, should be a number.", required=True)
args = parser.parse_args()

vals, ops, leaves = ImportData(args.input)
iterate(args.iterations, vals, ops)