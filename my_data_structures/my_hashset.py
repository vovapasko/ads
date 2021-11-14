import math


class MyHashSet:

    def __init__(self):
        self.size = 20000
        self.array_extension = 10
        self.extension_coeff = 0.7
        self.container = [None] * self.size
        self.elements_counter = 0

    def add(self, key: int) -> None:
        if self.elements_counter > (self.extension_coeff * len(self.container)):
            # self.size += self.array_extension
            self.container = self.container + [None] * self.array_extension
        self.__add(key)

    def __add(self, key: int) -> None:
        value = self.__get(key)
        if value is not None:
            if isinstance(value, int):
                value = [value]
            value.append(key)
        else:
            self.container[self.__hash(key)] = key
            self.elements_counter += 1

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.container[self.__hash(key)] = None
            self.elements_counter -= 1

    def contains(self, key: int) -> bool:
        return self.__get(key) is not None

    def __get(self, key: int):
        value = self.container[self.__hash(key)]
        if isinstance(value, list):
            if key in value:
                return key
            return None
        if value != key:  # happened collision
            return None
        return value

    def __hash(self, key: int):
        return key % self.size


functions = ["contains", "remove", "add", "add", "contains", "remove", "contains", "contains", "add", "add", "add", "add", "remove", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "contains", "add", "contains", "add", "add", "contains", "add", "add", "remove", "add", "add", "add", "add", "add", "contains", "add", "add", "add", "remove", "contains", "add", "contains", "add", "add", "add", "add",
             "add", "contains", "remove", "remove", "add", "remove", "contains", "add", "remove", "add", "add", "add", "add", "contains", "contains", "add", "remove", "remove", "remove", "remove", "add", "add", "contains", "add", "add", "remove", "add", "add", "add", "add", "add", "add", "add", "add", "remove", "add", "remove", "remove", "add", "remove", "add", "remove", "add", "add", "add", "remove", "remove", "remove", "add", "contains", "add"]
values = [[72], [91], [48], [41], [96], [87], [48], [49], [84], [82], [24], [7], [56], [87], [81], [55], [19], [40], [68], [23], [80], [53], [76], [93], [95], [95], [67], [31], [80], [62], [73], [97], [33], [28], [62], [81], [57], [40], [11], [89], [28], [97], [86], [20], [5], [77], [52], [57], [88], [
    20], [48], [42], [86], [49], [62], [53], [43], [98], [32], [15], [42], [50], [19], [32], [67], [84], [60], [8], [85], [43], [59], [65], [40], [81], [55], [56], [54], [59], [78], [53], [0], [24], [7], [53], [33], [69], [86], [7], [1], [16], [58], [61], [34], [53], [84], [21], [58], [25], [45], [3]]
obj = MyHashSet()
rules = {
    "contains": obj.contains,
    "remove": obj.remove,
    "add": obj.add
}

results = []
index = 0
for (value, fun, exp) in zip(values, functions, expected):
    res = rules[fun](value[0])
    if res != exp:
        print("Here")
    results.append(res)
    index += 1
print(results)
