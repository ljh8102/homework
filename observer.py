# observer.py

class Observer:
    def update(self, message):
        pass

# subject.py

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# main.py

from observer import Observer, Subject

class ConcreteObserver(Observer):
    def update(self, message):
        print("Received message:", message)

class ConcreteSubject(Subject):
    def send_message(self, message):
        print("Sending message:", message)
        self.notify(message)

if __name__ == "__main__":
    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()
    
    subject = ConcreteSubject()
    subject.attach(observer1)
    subject.attach(observer2)
    
    subject.send_message("Hello observers!")
