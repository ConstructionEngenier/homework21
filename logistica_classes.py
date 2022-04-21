from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        is_found = False
        if self.get_free_space() >= count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
            if not is_found:
                self.items[name] = count
            print("Товар добавлен")
        else:
            if self.get_free_space() != 0:
                print(f"Товар не может быть добавлен, так как есть место только на {self.get_free_space()} товаров")
            else:
                print(f"Товар не может быть добавлен, так как место закончилось")

    def remove(self, name, count):
        is_found = False
        for key in self.items.keys():
            if name == key:
                is_found = True
                if self.items[key] - count >= 0:
                    self.items[key] = self.items[key] - count
                else:
                    print(f"Такого количества {name} нет на складе")
        if not is_found:
            print(f"Товар {name} не найден")

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.items = {}
        self.capacity = 20
        self._limit = limit

    @property
    def get_items_limit(self):
        return self._limit

    def add(self, name, count):
        if self.get_unique_items_count() <= self._limit:
            super().add(name, count)
        else:
            print("Товар не может быть добавлен")


class Request:
    def __init__(self, str):
        lst = self.get_data(str)

        self.from_ = lst[4]
        self.amount = int(lst[1])
        self.product = lst[2]
        self.to = lst[6]

    def get_data(self, str):
        return str.split(" ")

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"

