from serach_address import search_address


def main():
    zipcode = "0231133"

    address = search_address(zipcode)

    assert "岩手県奥州市江刺広瀬" == address


if __name__ == '__main__':
    main()
