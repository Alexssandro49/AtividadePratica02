from abc import ABC, abstractmethod

class MotorVehicle(ABC):
    @abstractmethod
    def build(self):
        pass

class Car(MotorVehicle):
    def build(self):
        return "Carro construído."

class Motorcycle(MotorVehicle):
    def build(self):
        return "Moto construída."

class MotorVehicleFactory(ABC):
    @abstractmethod
    def create_motor_vehicle(self) -> MotorVehicle:
        pass

    def create(self) -> MotorVehicle:
        vehicle = self.create_motor_vehicle()
        return vehicle.build()


class CarFactory(MotorVehicleFactory):
    def create_motor_vehicle(self) -> MotorVehicle:
        return Car()

class MotorcycleFactory(MotorVehicleFactory):
    def create_motor_vehicle(self) -> MotorVehicle:
        return Motorcycle()


if __name__ == "__main__":
    car_factory = CarFactory()
    motorcycle_factory = MotorcycleFactory()

    print(car_factory.create())  
    print(motorcycle_factory.create())  