import requests
import json

def main():
    base_url = "https://httpbin.org"
    
    # OPTIONS запрос
    print("\n" + "="*50)
    print("Выполнение OPTIONS запроса")
    print("="*50)
    try:
        response = requests.options(f"{base_url}/")
        print_response(response)
    except Exception as e:
        print(f"Ошибка при выполнении OPTIONS запроса: {e}")

    # GET запрос
    print("\n" + "="*50)
    print("Выполнение GET запроса")
    print("="*50)
    try:
        params = {"param1": "value1", "param2": "value2"}
        response = requests.get(f"{base_url}/get", params=params)
        print(f"Текст запроса: {response.url}")
        print_response(response)
    except Exception as e:
        print(f"Ошибка при выполнении GET запроса: {e}")

    # POST запрос
    print("\n" + "="*50)
    print("Выполнение POST запроса")
    print("="*50)
    try:
        data = {"key": "value", "number": 42}
        response = requests.post(f"{base_url}/post", json=data)
        print(f"Текст запроса (JSON): {json.dumps(data, indent=2)}")
        print_response(response)
    except Exception as e:
        print(f"Ошибка при выполнении POST запроса: {e}")

def print_response(response):
    print("\nКод ответа сервера:", response.status_code)
    
    print("\nЗаголовки ответа:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    
    print("\nТело ответа:")
    try:
        # Пытаемся отформатировать JSON
        json_response = response.json()
        print(json.dumps(json_response, indent=2, ensure_ascii=False))
    except ValueError:
        # Если не JSON, выводим как есть
        print(response.text)

if __name__ == "__main__":
    main()