import requests


def search_address(zipcode):
    if len(zipcode) != 7:
        return "郵便番号はハイフンなし7桁で入力してください。"

    url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    response = requests.get(url)

    results = response.json()['results']

    address = []
    for m in range(0, len(results)):
        pref_name = results[m]['address1']
        city_name = results[m]['address2']
        town_name = results[m]['address3']
        address.append(f"{pref_name}{city_name}{town_name}")

    return address
