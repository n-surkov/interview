# Собеседование на [аналитика в Яндекс.Такси](https://yandex.ru/jobs/vacancies/analytics/suppan_taxi)

Результатов того, насколько верными или неверными были ответы на задачи Яндекс не дал, но на собеседование позвал.

**Задание 1**

Для осуществления дистанционного контроля качества Яндекс.Такси необходимо организовать проверку 
фотографий автомобилей асессорами. По результатам проверки автомобиль признается либо подходящим для нашего 
сервиса (хорошим), либо неподходящим (плохим). Стоимость проверки одной фотографии асессором один рубль. 
В вашем распоряжении есть эксперт, который способен идеально отличать плохие автомобили от хороших, 
однако стоимость одной проверки экспертом пять рублей. Вы провели эксперимент, по результатам которого установили, 
что 20% всех автомобилей, поступающих на проверку, плохие, а также, что вероятности того, 
что асессор назовет хороший автомобиль хорошим, а плохой плохим, равны 85% и 90% соответственно. 
Какой алгоритм проведения проверок вы бы предложили в этом случае? Что еще можно было бы сделать, чтобы его улучшить?

Предложение по решению [здесь](./task1/submission.docx)

**Задание 2**

Дана таблица с колонками user_id, order_datetime, order_id. ([самодельный тестовый фаилик](./task2/table.db))
Напишите SQL-запрос, который считает недельный retention пользователей.

Предложение по решению [здесь](./task2/submission.ipynb)

**Задание 3**

На прошедшей неделе в рекламной сети параллельно размещалось два баннера Яндекс.Такси. 
Какой из баннеров показывать конкретному пользователю выбиралось случайно. 
Оба баннера были показаны один миллион раз. Первый получил 10 000 кликов и 440 установок, 
а второй — 11 500 кликов и 500 установок. Маркетолог просит у вас совета: какой баннер оставить, а какой отключить? 
Что вы ему ответите? Обоснуйте свой ответ.

Предложение по решению [здесь](./task3/submission.ipynb)

**Задание 4**

Имеется [набор данных](./task4/data.csv) со статусами водителей, по которому необходимо построить 
зависимость длительности поездки от эффективности. Приведите данные к удобному для анализа виду.

Предложение по решению [здесь](./task4/submission.ipynb)
