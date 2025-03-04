Saga Pattern: E-commerce Checkout Workflow
Этот проект демонстрирует реализацию Saga Pattern для процесса оформления заказа (checkout) в интернет-магазине. Saga Pattern используется для управления распределёнными транзакциями, где каждый шаг может быть откатан в случае ошибки.

Описание
Процесс оформления заказа включает три шага:

Payment (Оплата): Обработка платежа через платёжный шлюз.

Inventory (Проверка наличия товара): Резервирование товара на складе.

Shipping (Доставка): Организация доставки товара.

Каждый шаг поддерживает две операции:

Do: Выполнение действия (например, оплата, резервирование товара, доставка).

Compensate: Откат действия в случае ошибки (например, возврат денег, возврат товара на склад, отмена доставки).

Если любой из шагов завершается ошибкой, все предыдущие шаги откатываются в обратном порядке.

Как работает
Saga Orchestrator управляет выполнением шагов: Payment → Inventory → Shipping.

Если шаг выполняется успешно, Orchestrator переходит к следующему.

Если шаг завершается ошибкой, Orchestrator запускает компенсацию всех выполненных шагов.

Пример вывода:

Payment: Processing payment...
Inventory: Reserving product...
Shipping: Scheduling delivery...
Shipping: Failed to schedule delivery.
Compensating...
Shipping: Canceling delivery...
Inventory: Releasing product...
Payment: Refunding payment...