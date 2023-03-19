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


total_space = 70000000
required_space = 30000000
unused_space = total_space - data['size']
minimum_delete_required = required_space - unused_space


def find_dir_to_delete(data, min_size, current_dir='root',smallest_dir={'size': required_space+1}):
    for k, v in data.items():
        if isinstance(v, dict):
            current_dir = k
            smallest_dir = find_dir_to_delete(v, min_size, current_dir, smallest_dir)
        else:
            # if k == 'size':
            #     if v >= min_size:
            #         if v < smallest_dir['size']:
            #             smallest_dir = {k:v, 'dir': current_dir}
            if (k == 'size') and (v >= min_size) and (v < smallest_dir['size']):
                smallest_dir = {k:v, 'dir': current_dir}
    return smallest_dir

# pprint(data)

ans = find_dir_to_delete(data, minimum_delete_required)
print(ans)


        

