def prtlst(lst: list) -> list:
    return [i for i in lst if i is not None]


def hash_func(key: str) -> int:
    acc = 0
    for i in key:
        acc += ord(i)
    return acc


class hash_table_open_addr:
    def __init__(self) -> None:
        self.table = []

    def insert(self, key: str, value: int) -> None:
        hashed_key = hash_func(key)
        while hashed_key >= len(self.table):
            self.table.append(None)

        if self.table[hashed_key] is None:
            print(key, value, "1")
            self.table[hashed_key] = (key, value)
            return
        if self.table[hashed_key][0] == key:
            print(key, value, "2")
            self.table[hashed_key] = (key, value)
            return
        if self.table[hashed_key][0] != key:
            print(key, value, "3")
            i = 1
            while self.table[hashed_key + i] != None:
                i += 1
            self.table[hashed_key + i] = (key, value)

    def delete(self, key: str) -> None:
        hashed_key = hash_func(key)
        if hashed_key >= len(self.table) or self.table[hashed_key] is None:
            return

        i = 0
        while (
            self.table[hashed_key + i] is not None
            and self.table[hashed_key + i][0] != key
        ):
            i += 1
        self.table[hashed_key + i] = None

    def get(self, key: str) -> int:
        hashed_key = hash_func(key)
        if hashed_key >= len(self.table) or self.table[hashed_key] is None:
            return None

        i = 0
        while (
            self.table[hashed_key + i] is not None
            and self.table[hashed_key + i][0] != key
        ):
            i += 1

        if self.table[hashed_key + i] is None:
            return None

        return self.table[hashed_key + i][1]


class hash_table_linked_list:
    def __init__(self) -> None:
        self.table = []

    def insert(self, key: str, value: int) -> None:
        hashed_key = hash_func(key)
        # Каждый элемент таблицы - список из (key, value)
        while hashed_key >= len(self.table):
            self.table.append([])
        if len(self.table[hashed_key]) == 0:
            self.table[hashed_key].append((key, value))
            return
        if self.table[hashed_key][0][0] == key:
            self.table[hashed_key][0] = (key, value)
            return
        i = 1
        while i < len(self.table[hashed_key]) and self.table[hashed_key][i][0] != key:
            i += 1
        if i >= len(self.table[hashed_key]):
            self.table[hashed_key].append((key, value))
            return
        if self.table[hashed_key][i][0] == key:
            self.table[hashed_key][i] = (key, value)

    def delete(self, key: str) -> None:
        hashed_key = hash_func(key)
        if len(self.table) < hashed_key or len(self.table[hashed_key]) == 0:
            return
        i = 0
        while i < len(self.table[hashed_key]) and self.table[hashed_key][i][0] != key:
            i += 1
        if i >= len(self.table[hashed_key]):
            return
        if self.table[hashed_key][i][0] == key:
            del self.table[hashed_key][i]

    def get(self, key: str) -> int:
        hashed_key = hash_func(key)
        if hashed_key > len(self.table) or len(self.table[hashed_key]) == 0:
            return None
        i = 0
        while i < len(self.table[hashed_key]) and self.table[hashed_key][i][0] != key:
            i += 1
        if i >= len(self.table[hashed_key]):
            return None
        if self.table[hashed_key][i][0] == key:
            return self.table[hashed_key][i][1]
        


def test_linear():
    table = hash_table_open_addr()

    table.insert("мама", 123)
    table.insert("папа", 321)
    table.insert("амам", 122)
    print(*table.table)
    print(*prtlst(table.table))
    #table.delete('амам')
    print(*prtlst(table.table))
    table.delete("амам")
    print(*prtlst(table.table))

    print(table.get("папа"))
    print(table.get("амам"))
    print(table.get("мама"))
    # print(*table.table)


def test_lists():
    table = hash_table_linked_list()
    table.insert("мама", 123)
    table.insert("папа", 321)
    table.insert("амам", 122)
    print(*table.table)
    print(table.get('дфлыовдфылов'))
    table.delete("амам")
    table.delete("амам")
    table.delete("мама")
    #print(*table.table)



test_linear()