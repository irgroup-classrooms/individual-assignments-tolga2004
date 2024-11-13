import re
from collections import Counter

def main():
    # Read the CSV file with the product orders
    with open('./csv/orders.csv') as f_in:
        text = f_in.read()

    # Define the regular expression to extract all order numbers
    regex = r'\d+'

    # Match the regex with the text
    orders = re.findall(regex, text)

    # Print the results
    print(orders)

    # Erweiterung: Extrahiere alle Bestellnummern
    order_numbers = re.findall(r'Order\s#(\d+)', text)
    print("Order numbers:", order_numbers)

    # Erweiterung: Extrahiere alle Produktnamen
    product_names = re.findall(r'Product:\s([A-Za-z\s]+)', text)
    print("Product names:", product_names)

    # Erweiterung: Extrahiere alle Preise
    prices = re.findall(r'Price:\s\$(\d+\.\d{2})', text)
    print("Prices:", prices)

    # Erweiterung: Extrahiere alle Bestelldaten
    dates = re.findall(r'Date:\s(\d{4}-\d{2}-\d{2})', text)
    print("Order dates:", dates)

    # Erweiterung: Finde alle Bestellungen für Produkte, die über $500 kosten
    prices_over_500 = [(product, price) for product, price in zip(product_names, prices) if float(price) > 500]
    print("Products priced over $500:", prices_over_500)

    # Erweiterung: Ändere das Datumsformat in DD/MM/YYYY
    formatted_dates = [re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', date) for date in dates]
    print("Formatted dates (DD/MM/YYYY):", formatted_dates)

    # Erweiterung: Extrahiere Produktnamen mit mehr als 6 Zeichen
    long_product_names = [name for name in product_names if len(name) > 6]
    print("Product names with more than 6 characters:", long_product_names)

    # Erweiterung: Zähle die Vorkommen jedes Produkts
    product_count = Counter(product_names)
    print("Product count:", product_count)

    # Erweiterung: Extrahiere Bestellungen mit Preisen, die auf .99 enden
    prices_ending_in_99 = [(product, price) for product, price in zip(product_names, prices) if price.endswith('.99')]
    print("Products with prices ending in .99:", prices_ending_in_99)

    # Erweiterung: Finde das günstigste Produkt
    cheapest_product_price = min(prices, key=float)
    cheapest_product = product_names[prices.index(cheapest_product_price)]
    print("Cheapest product:", cheapest_product, "with price $", cheapest_product_price)

if __name__ == '__main__':
    main()
