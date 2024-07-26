from abc import ABC, abstractmethod
# ABC (Abstract Base Class) - вспомогательный класс, который делает из обычного класса абстрактный посредством наследования от ABC.
# abstractmethod - декоратор, обозначающий, что данный метод является абстрактным

class Gun(ABC):
    """Абстрактное оружие, которое умеет стрелять"""
    
    @property
    @abstractmethod
    def title(self):
        pass
    
    @abstractmethod
    def shoot(self):
        class_name = self.title
        print('Shoot from {}'.format(class_name))

# Реализация сущностей оружия

class Pistol(Gun):
    """Пистолет"""

    @property
    def title(self):
        return 'Pistol'
        
    def shoot(self):
        super().shoot()

class Automat(Gun):
    """Автомат"""

    @property
    def title(self):
        return 'Automat'
        
    def shoot(self):
        super().shoot()

class MachineGun(Gun):
    """Пулемет"""

    @property
    def title(self):
        return 'MachineGun'
        
    def shoot(self):
        super().shoot()