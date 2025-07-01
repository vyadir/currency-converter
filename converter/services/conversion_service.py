# converter/services/conversion_service.py
class ConversionService:
    def __init__(self, exchange_provider):
        self.provider = exchange_provider

    def convert(self, amount_cop):
        usd = round(amount_cop * self.provider.get_rate("COP", "USD"), 2)
        crc = round(amount_cop * self.provider.get_rate("COP", "CRC"), 2)
        return {"USD": usd, "CRC": crc}
