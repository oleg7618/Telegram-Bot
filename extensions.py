import json
import requests
from config import exchanges

class APIException(Exception):
    pass

class Converter:
        @staticmethod
        def get_price(base, sym, amount):
                try:
                        base_key = exchanges[base.lower()]
                except KeyError:
                        raise APIException(f"Валюта {base} не найдена!")

                try:
                        sym_key = exchanges[sym.lower()]
                except KeyError:
                        raise APIException(f"Валюта {sym} не найдена!")

                if base_key == sym_key:
                        raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

                try:
                        amount = float(amount)
                except ValueError:
                        raise APIException(f'Не удалось обработать количество {amount}!')

                url = (f"https://api.apilayer.com/currency_data/convert?to={base_key}&from={sym_key}&amount={amount}")

                payload = {}
                headers = {
                "apikey": "CzGoh12752wGYgGjOuPhz41jAhtdyPX8"
                }

                response = requests.request("GET", url, headers=headers, data=payload)
                result = json.loads(response.content)
                message = f"Цена {amount} {sym_key} в {base_key}: {result.get('result')}"
                return message
