# Игры разума (Python)

«Brain Games» — это набор из пяти консольных игр для тренировки устного счёта и логики.
Каждая игра задаёт три вопроса подряд. Чтобы победить, нужно ответить правильно на все три;
при первой же ошибке игра завершается и показывает правильный ответ.

В проект входят:

- **brain-even** — проверка числа на чётность;
- **brain-calc** — вычисление значения арифметического выражения (`+`, `-`, `*`);
- **brain-gcd** — поиск наибольшего общего делителя двух чисел;
- **brain-progression** — поиск пропущенного числа в арифметической прогрессии;
- **brain-prime** — проверка, является ли число простым.

## Стек

- Python

## Установка

Требуется Python 3.10+ и пакетный менеджер uv

```bash
# 1. Клонируйте репозиторий
git clone git@github.com:<ваш-логин>/<ваш-репозиторий>.git
cd <ваш-репозиторий>

# 2. Установите зависимости
make install

# 3. Соберите и установите пакет в систему
make build
make package-install
```
# 4. Демонстрация процксса сборки и установки
[![asciicast](https://asciinema.org/a/o6EKDFSAxlMvpcKY.svg)](https://asciinema.org/a/o6EKDFSAxlMvpcKY)

## Использование
После установки любую игру можно запустить по имени: 
`brain-even`,
 `brain-calc`,
 `brain-gcd`,
 `brain-progression`,
 `brain-prime`.
---

## Демонстрация игр

#Игра "Проверка на чётность" - brain-even
[![asciicast](https://asciinema.org/a/kyxRvyN3pVRTqjGp.svg)](https://asciinema.org/a/kyxRvyN3pVRTqjGp)

#Игра "Калькулятор" - brain-calc
[![asciicast](https://asciinema.org/a/Un8SXY56sVOBAdAH.svg)](https://asciinema.org/a/Un8SXY56sVOBAdAH)

#Игра «НОД» - brain-gcd
[![asciicast](https://asciinema.org/a/y3NO1cmH4md7UhYh.svg)](https://asciinema.org/a/y3NO1cmH4md7UhYh)

#Игра "Арифметическая прогрессия" - brain-progression
[![asciicast](https://asciinema.org/a/0ovn2tp2s4BlGZBG.svg)](https://asciinema.org/a/0ovn2tp2s4BlGZBG)

#Игра «Простое ли число?» - brain-prime
[![asciicast](https://asciinema.org/a/XmvKTNDN863U1KBE.svg)](https://asciinema.org/a/XmvKTNDN863U1KBE)

