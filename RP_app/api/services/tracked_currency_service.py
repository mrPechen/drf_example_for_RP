from RP_app.api.repositories.tracked_currency_repository import TrackedCurrencyRepository


class TrackedCurrencyService:
    def __init__(self):
        self.repository = TrackedCurrencyRepository()

    """
    Добавление отслеживаемых объектов.
    """

    def add_tracked_currency(self, email: str, currency_id: int, threshold: float):
        result = self.repository.add_tracked_currency(email=email, currency_id=currency_id, threshold=threshold)
        return result

    """
    Удаление отслеживаемых объектов.
    """

    def delete_tracked_currency(self, email: str, currency_id: int):
        return self.repository.delete_tracked_currency(email=email, currency_id=currency_id)

    """
    Изменение отслеживаемых значений объектов.
    """

    def change_tracked_currency_threshold(self, email: str, currency_id: int, threshold: float):
        return self.change_tracked_currency_threshold(email=email, currency_id=currency_id, threshold=threshold)

    """
    Получение отслеживаемых объектов.
    """

    def get_tracked_currency(self, email: str, parameter: None | str = None):
        if parameter == 'value':
            return self.repository.get_asc_tracked_currency(email=email)
        if parameter == '-value':
            return self.repository.get_desc_tracked_currency(email=email)
        return self.repository.get_tracked_currency(email=email)
