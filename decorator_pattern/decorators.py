from components import Gun, Pistol

class SilencerDecorator(Gun):
    """Декоратор глушителя"""

class LightingDecorator(Gun):
    """Декоратор для фонарика"""

# Конкретные декораторы

class AllGunSilencerDecorator(SilencerDecorator):
    @property
    def title(self):
        return self._gun.title
        
    def __init__(self, gun: Gun):
        self._gun = gun   
        
    def shoot(self):
        print('Надеваем глушитель...')
        self._gun.shoot()
        print('Снимаем глушитель...')

class PistolSilencerDecorator(SilencerDecorator):
    @property
    def title():
        return self._pistol.title
        
    def __init__(self, pistol: Pistol):
        self._pistol = pistol
        
    def shoot(self):
        print('Надеваем специальный глушитель для пистолетов...')
        self._pistol.shoot()
        print('Снимаем специальный глушитель для пистолетов...')