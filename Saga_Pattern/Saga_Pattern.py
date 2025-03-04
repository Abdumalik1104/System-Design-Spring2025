# -*- coding: utf-8 -*-

class Payment:
    def do(self):
        """
        Выполняет оплату через платёжный шлюз.
        Возвращает True, если оплата успешна, иначе False.
        """
        print("Payment: Processing payment...")
        payment_success = self._call_payment_gateway()
        if not payment_success:
            print("Payment: Failed to process payment.")
            return False
        return True

    def compensate(self):
        """
        Откатывает оплату (возврат денег).
        """
        print("Payment: Refunding payment...")
        self._call_refund()

    def _call_payment_gateway(self):
        """
        Заглушка для имитации оплаты.
        """
        return True  # True = успех, False = ошибка

    def _call_refund(self):
        """
        Заглушка для имитации возврата денег.
        """
        print("Payment: Refund processed.")


class Inventory:
    def do(self):
        """
        Резервирует товар на складе.
        Возвращает True, если резервирование успешно, иначе False.
        """
        print("Inventory: Reserving product...")
        reservation_success = self._reserve_product()
        if not reservation_success:
            print("Inventory: Failed to reserve product.")
            return False
        return True

    def compensate(self):
        """
        Откатывает резервирование (возврат товара на склад).
        """
        print("Inventory: Releasing product...")
        self._release_product()

    def _reserve_product(self):
        """
        Заглушка для имитации резервирования товара.
        """
        return True  # True = успех, False = ошибка

    def _release_product(self):
        """
        Заглушка для имитации возврата товара.
        """
        print("Inventory: Product released.")


class Shipping:
    def do(self):
        """
        Организует доставку товара.
        Возвращает True, если доставка успешно запланирована, иначе False.
        """
        print("Shipping: Scheduling delivery...")
        delivery_success = self._schedule_delivery()
        if not delivery_success:
            print("Shipping: Failed to schedule delivery.")
            return False
        return True

    def compensate(self):
        """
        Откатывает доставку (отмена доставки).
        """
        print("Shipping: Canceling delivery...")
        self._cancel_delivery()

    def _schedule_delivery(self):
        """
        Заглушка для имитации доставки.
        """
        return False  # True = успех, False = ошибка (например, нет курьеров)

    def _cancel_delivery(self):
        """
        Заглушка для имитации отмены доставки.
        """
        print("Shipping: Delivery canceled.")


class SagaOrchestrator:
    def __init__(self):
        """
        Инициализирует Saga Orchestrator с шагами: Payment, Inventory, Shipping.
        """
        self.steps = [Payment(), Inventory(), Shipping()]
        self.completed_steps = []

    def run(self):
        """
        Выполняет шаги Saga. Если какой-то шаг fails, запускает компенсацию.
        """
        for step in self.steps:
            if step.do():
                self.completed_steps.append(step)
            else:
                self.compensate()
                break

    def compensate(self):
        """
        Выполняет компенсацию всех завершённых шагов в обратном порядке.
        """
        print("Compensating...")
        for step in reversed(self.completed_steps):
            step.compensate()


# Запуск Saga
if __name__ == "__main__":
    saga = SagaOrchestrator()
    saga.run()