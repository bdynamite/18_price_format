import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='price to format')
    return parser.parse_args()


def format_price(price_str):
    try:
        float_price = float(price_str)
        price = '{:,.2f}'.format(float_price).replace(',', ' ')
    except (ValueError, TypeError):
        raise ValueError('Given value cannot be converted into a number')
    if price[0] == '-' or price == '0.00':
        raise ValueError('Price must be greater then 0.00!')
    return price


if __name__ == '__main__':
    options = get_args()
    print(format_price(options.price))
