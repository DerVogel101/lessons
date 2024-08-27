from functools import wraps
import pickle


def exportable(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        self = result.self

        def export():
            return pickle.dumps(self)
        result.export = export
        return result
    return wrapper


@exportable
class MyClass:
    instances = 0

    def __init__(self, name: str, age: int, name_nobody_should_know: str):
        MyClass.instances += 1
        self.name = name
        self.age = age
        self.__name_nobody_should_know = name_nobody_should_know

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"MyClass('{self.name}', {self.age}, '{self.__name_nobody_should_know}')"

    def _get_hidden_name(self):
        return self.__name_nobody_should_know


if __name__ == "__main__":
    my_instance = MyClass("Alice", 25, "Alicija")
    print(my_instance)
    print(my_instance._get_hidden_name())
    print(repr(my_instance))
    print(my_instance.export())