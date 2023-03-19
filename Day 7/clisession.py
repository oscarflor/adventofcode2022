from collections import deque

class cliSession():
    def __init__(self, current_dir=deque()):
        self.current_dir = current_dir
    
    def is_command(self, data:str):
        if data.startswith('$'):
            return True
        return False

    def change_dir(self, new_dir:str):
        if new_dir.startswith('/'):
            # path is absolute
            self.current_dir = new_dir[1:].split('/')
        elif new_dir == '..':
            # go up one dir
            self.current_dir.pop()
        else:
            self.current_dir.append(new_dir)
        # print(f'dir CHANGE: {self.current_dir}')

    def pwd(self):
        return self.current_dir
    