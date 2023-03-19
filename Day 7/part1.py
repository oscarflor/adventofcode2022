from filesystem import FileSystem, File
from clisession import cliSession
from pprint import pprint
with open ('Day 7/input.txt') as input:
    data = input.readlines()

session = cliSession()
file_sys = FileSystem()
# print(f'current state: {file_sys.get_all()}')
for line in data:
    line = line.rstrip()
    # print(line)
    if session.is_command(line):
        line = line[2:].split(' ')
        command = line[0]
        command_args = None
        if len(line) > 1:
            command_args = line[1]
        if command == 'cd':
            session.change_dir(command_args)
            # print(session.pwd())
    else:
        # must be output from ls
        if line.startswith('dir'):
            dir_name = line.split(' ')[1]
            # print(f'mkdir {session.pwd()}, {dir_name}')
            file_sys.mkdir(session.pwd(), dir_name)
        else:
            file_size, file_name = line.split(' ')
            file_size = int(file_size)
            # print(f'add_file {session.pwd(), File(file_size, file_name).name}')
            file_sys.add_file(session.pwd(), File(file_size, file_name))

data = file_sys.get_all()

# gets sum of sizes of directories below a given threshold
def get_sum_below_threshold(data, threshold):
    total = 0
    for k, v in data.items():
        if isinstance(v, dict):
            total += get_sum_below_threshold(v, threshold)
        else:
            if k == 'size' and v <= threshold:
                # print(f'adding {v} to {total}')
                total += v
    return total

# pprint(data)

ans = get_sum_below_threshold(data, 100000)
print(ans)


        

