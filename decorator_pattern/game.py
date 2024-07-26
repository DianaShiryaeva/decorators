"""
    Цель: разработка шутера!
    Описание: в игре есть различные виды оружия: пистолеты, автоматы, пулемёты и т.д. Для оружия характерны различные приспособления, например, фонарики, глушители и т.д.
    Задача: реализовать гибкую, удобную и поддерживаемую архитектуру использования различных приспособлений для оружия.
"""
import components
import decorators

# создание оружия
pistol = components.Pistol()
automat = components.Automat()
machineGun = components.MachineGun()

# создание оружия с глушителем
silencer_pistol = decorators.AllGunSilencerDecorator(pistol)
silencer_automat = decorators.AllGunSilencerDecorator(automat)
silencer_machineGun = decorators.AllGunSilencerDecorator(machineGun)

# создание пистолета со специальным глушителем для пистолетов
silencer_spec_pistol = decorators.PistolSilencerDecorator(pistol)

# стрельба из оружия
for gun in [pistol, automat, machineGun, silencer_pistol, silencer_automat, silencer_machineGun, silencer_spec_pistol]:
    gun.shoot()
    print('='*5)