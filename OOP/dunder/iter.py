class DataCollection:
    def __init__(self, data: list):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    collection = DataCollection(data)
    for item in collection:
        print(item)