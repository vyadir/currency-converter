import requests

class ExchangeRateProvider:
    BASE_URL = "https://open.er-api.com/v6/latest/"

    def get_rate(self, from_currency, to_currency):
        try:
            response = requests.get(f"{self.BASE_URL}{from_currency}")
            response.raise_for_status()
            data = response.json()
            rate = data["rates"].get(to_currency)
            if rate is None:
                raise ValueError(f"Tasa {to_currency} no disponible")
            return float(rate)
        except Exception as e:
            print(f"Error al obtener tasa {from_currency} → {to_currency}: {e}")
            return 0.0