class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest_index = 0
        self.storage = []

    def append(self, item):
        if len(self.storage) >= self.capacity:
            self.storage.pop(self.oldest_index)
            self.storage.insert(self.oldest_index, item)
            if self.oldest_index >= self.capacity - 1:
                self.oldest_index = 0
            else:
                self.oldest_index += 1
        else:
            self.storage.append(item)

    def get(self):
        return [x for x in self.storage if x is not None]
