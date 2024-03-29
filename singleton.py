# singleton.py

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# main.py

from singleton import Singleton

if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()
    
    print(singleton1 is singleton2)  # Output: True
