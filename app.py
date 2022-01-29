import requests

"""
zipcode = "0231133"
# 変数にHTTPライブラリで、APIの情報を取得して代入する
response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}")

print(response)
print(response.text)
print(response.json())
print(type(response.json()))

add = response.json()
a1 = add['results'][0]['address1'] + add['results'][0]['address2'] + add['results'][0]['address3']
print(a1)
"""


def search_address(zipcode):
    url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    response = requests.get(url)
    results = response.json()['results']
    pref_name = results[0]['address1']
    city_name = results[0]['address2']
    town_name = results[0]['address3']
    address = f"{pref_name}{city_name}{town_name}"
    return address


def main():
    zipcode = "0231133"
    # zipcode = input("郵便番号<ハイフン無し7桁>は?")   # 郵便番号<ハイフン無し7桁>は?

    address = search_address(zipcode)

    print(address)


if __name__ == '__main__':
    main()
