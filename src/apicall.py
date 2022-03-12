import requests

url = ''


def parse_json():
    try:
        response = requests.get(url)
        if response.ok:
            return response
    except requests.exceptions.RequestException as e:
        print(e)
        return {}
