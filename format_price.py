import argparse


def get_price():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='price to format')
    return parser.parse_args()


def print_error(error):
    print(error)


def format_price(price):
    try:
        price = float(price)
        price = '{:,.2f}'.format(price).replace(',', ' ')
    except (ValueError, TypeError):
        print_error('Invalid price value!')
        return None
    if price[0] == '-' or price == '0.00':
        print_error('Price must be greater then 0.00!')
        return None
    return price


if __name__ == '__main__':
    price = get_price().price
    price = format_price(price)
    print(price)
