class FileSystem():
    def __init__(self, files_dict={'size': 0}):
        self.files_dict = files_dict

    def _nested_set(self, dic, keys, value):
        # print(f'nest_set {keys} {value}')
        if len(keys) == 1: # adding to root dir
            if isinstance(value, File):
                #  print(f'adding file {value.name} {value.size}')
                dic[value.name] = value.size
                dic['size'] += value.size
            else:
                dic[value] = {'size': 0}
            return 0
        
        # for nested keys
        # print(f'dic start {dic}')
        for key in keys[1:]:
            dic = dic[key]

        
        # print(f'setting key {keys[-1]} to {value}')
        if isinstance(value, File):
            # print(f'adding file {value.name} {value.size}')
            dic[value.name] = value.size
            dic['size'] += value.size
            # print('ADDING FILE')
            # print(keys)
            for count, key in enumerate(reversed(keys[1:]), 1):
                dic = self.files_dict
                # print(f'key - {key}')
                # print(keys[1:len(keys)-count])
                for key2 in keys[1:len(keys)-count]:
                    # print(f'k2 - {key2}')
                    dic = dic[key2]
                # print(f'updating key - {key}')
                dic['size'] += value.size
        else:
            # print(f'keys[-1] {keys[-1]} value {value}')
            # print(f'dic {dic}')
            dic[value] = {'size': 0}

    def mkdir(self, location, new_dir):
        # print(f'making dir {new_dir} at location {location}')
        self._nested_set(self.files_dict, location, new_dir)

    def add_file(self, location, new_file):
        self._nested_set(self.files_dict, location, new_file)

    def get_all(self):
        return self.files_dict

class File():
    def __init__(self, size, name):
        self.size = size
        self.name = name
    
    def get_size(self):
        return self.size
    
class Directory():
    def __init__(self, name, contents={}, size=0):
        self.size = size
        self.name = name
        self.contents = contents
    
    def get_size(self):
        return self.size