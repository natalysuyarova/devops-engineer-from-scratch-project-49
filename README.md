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
<script src="https://asciinema.org/a/o6EKDFSAxlMvpcKY.js" id="asciicast-o6EKDFSAxlMvpcKY" async="true"></script>

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

<script src="https://asciinema.org/a/kyxRvyN3pVRTqjGp.js" id="asciicast-kyxRvyN3pVRTqjGp" async="true"></script>

#Игра "Калькулятор" - brain-calc
<script src="https://asciinema.org/a/Un8SXY56sVOBAdAH.js" id="asciicast-Un8SXY56sVOBAdAH" async="true"></script>

#Игра «НОД» - brain-gcd
<script src="https://asciinema.org/a/y3NO1cmH4md7UhYh.js" id="asciicast-y3NO1cmH4md7UhYh" async="true"></script>

#Игра "Арифметическая прогрессия" - brain-progression
<script src="https://asciinema.org/a/0ovn2tp2s4BlGZBG.js" id="asciicast-0ovn2tp2s4BlGZBG" async="true"></script>

#Игра «Простое ли число?» - brain-prime
<script src="https://asciinema.org/a/XmvKTNDN863U1KBE.js" id="asciicast-XmvKTNDN863U1KBE" async="true"></script>
