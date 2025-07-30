''' Array Class '''
class Array:
    def __init__(self, size=None):
        if size is None:
            self.data = []
            self.size = None
        else:
            self.size = size
            self.data = [None] * size

    def get(self, index):
        return self.data[index]

    def insert(self, index, value):
        if self.size is None:
            self.data.append(value)
            return
        self.data[index] = value

    def __str__(self):
        return str(self.data)
    
    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        return None

    def __len__(self):
        return len(self.data)