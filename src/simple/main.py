from src.simple.helpers.sentrySDK import sentry_sdk
from loguru import logger


def run_ex1():
    try:
        # Ваш код, который может вызывать ошибку
        devision_by_zero = 1 / 0
    except Exception as e:
        sentry_sdk.capture_message(str(e))


def run_ex2():
    try:
        # Ваш код, который может вызывать ошибку
        devision_by_zero = 1 / 0
    except Exception as e:
        sentry_sdk.capture_message(str(e))
        logger.error(str(e))


def run_ex3():
    sentry_sdk.capture_message(message="Отправили данные", level="info")
    logger.info("Отправили данные")
    logger.success("Успешно отправили данные")


def run_ex4():
    with sentry_sdk.configure_scope() as scope:
        # Добавление дополнительных данных в scope
        scope.set_extra("user_id", 123)

        data = {
            'user_id': 123,
            'text': 'Отправили данные'
        }
        scope.set_extra("news_data", data)

        # Отправка сообщения
        sentry_sdk.capture_message("Отправили данные", level="info")


if __name__ == "__main__":
    run_ex1()  # Текущий пример показывает как именно обрабатывать ошибку и логировать ее в
    run_ex2()  # Тоже самое, что и первый пример только еще добавляем консольное логирование, через loguru
    run_ex3()  # Логируем сообщение обычного типа
    run_ex4()  # Логирование с дополнительными параметрами
