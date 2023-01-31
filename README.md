## Hexlet tests and linter status:
[![Actions Status](https://github.com/Vlad-i-mir70/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/Vlad-i-mir70/python-project-49/actions)
<a href="https://codeclimate.com/github/Vlad-i-mir70/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/4beb700ac7eb4b5276a3/maintainability" /></a>

## **Пакет с игрой  "Игры Разума".**


Состоит из пяти игр:
### Проверка на четность

Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число чётное, или no — если нечётное.

[Пример установки и игры](https://asciinema.org/a/vlDnH9g4Y79shIQ9WNpAGT1uv)

### Калькулятор

Суть игры в следующем: пользователю показывается случайное математическое выражение, например 35 + 16, которое нужно вычислить и записать правильный ответ.

[Пример установки и игры](https://asciinema.org/a/oU86oxwsoDE3RdA5LsRWaCYId)

### Наибольший общий делитель (НОД)

Суть игры в следующем: пользователю показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.

[Пример установки и игры](https://asciinema.org/a/lm8qZNIo2KNJKMzUX2pIJUbNx)

### Арифметическая прогрессия

Показываем игроку ряд чисел, образующий арифметическую прогрессию, заменив любое из чисел двумя точками. Игрок должен определить это число.

[Пример установки и игры](https://asciinema.org/a/dbOGsNdaL2SaeFOK8cEHX4I2j)

### Простое ли число?

Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число простое, или no — если нет.

[Пример установки и игры](https://asciinema.org/a/NY5iiPpQoU2MBjvcbOn0KhpTT)


 ## Установка и запуск игры


Новая установка:

  1  Установите Python 3.10 и выше
Команда для Ubuntu или Ubuntu on Windows (WSL)

```sudo apt update
sudo apt install python3
```

Команда для macOS

Если не установлен Homebrew необходимо установить его с сайта https://brew.sh. Следуйте инструкциям по установке до "Next steps" и добавьте Homebrew в ваш PATH.

```# https://brew.sh/index_ru.html
brew install python
```
  2 Удостоверьтесь, что у вас установлен свежий pip, вызвав `python3 -m pip --version`. Потребуется версия 19 и выше. При необходимости обновите pip командой `python3 -m pip install --upgrade --user pip`.

  3 Склонируйте репозиторий c игрой локально.

`git clone https://github.com/Vlad-i-mir70/python-project-49.git` 

  4 Или установите игру прямо из репозитория 

`python3 -m pip install --user git+https://github.com/Vlad-i-mir70/python-project-49.git`

  5. Игры запускаются следующим командами
 ``` brain-even         #  Проверка на четность
     brain-calc         #  Калькулятор 
     brain-gcd          #  Наибольший общий делитель (НОД)
     brain-progression  #  Арифметическая прогрессия
     brain-prime        #  Простое ли число
``` 
