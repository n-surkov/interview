# Решение задачек с [Яндекс.Интервью](https://contest.yandex.ru/contest/8458/enter)

## Задача 1.

Даны две строки строчных латинских символов: строка J и строка S. Символы, входящие в строку J, — «драгоценности», входящие в строку S — «камни». Нужно определить, какое количество символов из S одновременно являются «драгоценностями». Проще говоря, нужно проверить, какое количество символов из S входит в J.

Это разминочная задача, к которой мы размещаем готовые решения. Она очень простая и нужна для того, чтобы вы могли познакомиться с нашей автоматической системой проверки решений. Ввод и вывод осуществляется через файлы, либо через стандартные потоки ввода-вывода, как вам удобнее. 

**Пример**

|Ввод|Вывод|
|--|--|
|ab <br/> aabbccd|4|

## Задача 2.

Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.

Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.

**Пример**

|Ввод|Вывод|
|--|--|
|5 <br/> 1 <br/> 0 <br/> 1 <br/> 0 <br/> 1|1|

## Задача 3.

Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.

Желательно получить решение, которое не считывает входной файл целиком в память, т.е., использует лишь константный объем памяти в процессе работы.

**Пример**

|Ввод|Вывод|
|--|--|
|5 <br/> 2 <br/> 4 <br/> 8 <br/> 8 <br/> 8|2 <br/> 4 <br/> 8|

## Задача 4.

Дано целое число $n$. Требуется вывести все правильные скобочные последовательности длины $2 \cdot n$, упорядоченные лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).

В задаче используются только круглые скобки.

Желательно получить решение, которое работает за время, пропорциональное общему количеству правильных скобочных последовательностей в ответе, и при этом использует объём памяти, пропорциональный $n$.

**Пример**

|Ввод|Вывод|
|--|--|
|3|((())) <br/> (()()) <br/> (())() <br/> ()(()) <br/> ()()()|

## Задача 5.

Даны две строки, состоящие из строчных латинских букв. Требуется определить, являются ли эти строки анаграммами, т. е. отличаются ли они только порядком следования символов. 

**Пример**

|Ввод|Вывод|
|--|--|
|qiu <br/> iuq|1|

## Задача 6.

Даны $k$ отсортированных в порядке неубывания массивов неотрицательных целых чисел, каждое из которых не превосходит 100. Требуется построить результат их слияния: отсортированный в порядке неубывания массив, содержащий все элементы исходных $k$ массивов.

Длина каждого массива не превосходит $10 \cdot k$.

Постарайтесь, чтобы решение работало за время $k \cdot log(k) \cdot n$, если считать, что входные массивы имеют длину $n$.

**Пример**

|Ввод|Вывод|
|--|--|
|4 <br/> 6 2 26 64 88 96 96 <br/> 4 8 20 65 86 <br/> 7 1 4 16 42 58 61 69 <br/> 1 84|1 2 4 8 16 20 26 42 58 61 64 65 69 84 86 88 96 96|
