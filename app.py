from serach_address import search_address

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


def main():
    # zipcode = "0231133"
    zipcode = input("郵便番号<ハイフン無し7桁>は?")  # 郵便番号<ハイフン無し7桁>は?

    address = search_address(zipcode)

    print(address)


if __name__ == '__main__':
    main()
