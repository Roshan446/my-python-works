from abc import ABC, abstractmethod

class Car(ABC):
   @abstractmethod
   def __init__(self, name, brand, model):
      pass
   @abstractmethod
   def start(self):
      pass
   @abstractmethod
   def stop(self):
      pass
   @abstractmethod
   def accelerate():
      pass

class Baleno(Car):
   def __init__(self, name, brand, model):
      self.name = name
      self.brand = brand
      self.model = model
   def start(self):
      print("car is starting")
   def stop(self):
      print("car is stoping")
   def accelerate(self):
      print("car is accellerating")

ch = Baleno("baleno", "tata", "2013")
ch.start()
ch.stop()
ch.accelerate()

print(ch)