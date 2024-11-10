"""
Date: October 2024
Description: An order management system for an e-commerce platform to process
1. customer orders
2. track inventory
3. generate sales reports
"""
_orders = []
MINIMUM = 5

_product_info = {
    "Laptop": {"price": 1000, "stock": 10},
    "Smartphone": {"price": 500, "stock": 20},
    "Headphones": {"price": 100, "stock": 50}
}

def display_products():
    for product, details in _product_info.items():
        print(f"Product: {product}, Price: £{details['price']: 0.2f}, Stock: {details['stock']}")


def check_stock_levels():
    for product, details in _product_info.items():
        #if _product_info[product]['stock'] < MINIMUM:
        if details['stock'] < MINIMUM:
            print(f"Alert: the stock levels are low for {product}")
        else:
            print(f"Stock levels are fine")


def process_order(product_name, quantity):
    if product_name in _product_info:
        if _product_info[product_name]["stock"] >= quantity:
            _product_info[product_name]["stock"] -= quantity
            order_details = {"product": product_name, "quantity": quantity,
                             "total": quantity * _product_info[product_name]["price"]}
            _orders.append(order_details)
            print(f"Order processed: {quantity}  {product_name}")
        else:
            print("Insufficient stock!")
    else:
        print("Product not found!")

def sales_report():
    print("Sales report:")
    for order in _orders:
        print(f"Product: {order['product']} Quantity: {order['quantity']} "
              f"Total: {order['total']:0.2f}")
    for product, details in _product_info.items():
        print(f"Product: {product}, Price: £{details['price']: 0.2f}, Stock: {details['stock']}")

def main():
    while True:
        choice = int(input("Product / Stock Management System\n"
                           "1. Display all stock\n"
                           "2. Check if stock levels are low\n"
                           "3. Process an order\n"
                           "4. Generate a sales report\n"
                           "5. Exit\n"))
        match choice:
            case 1:
                display_products()
            case 2:
                check_stock_levels()
            case 3:
                product_name = input("Please enter a product name to place an order: ")
                quantity = int(input("Please enter the quantity you would like to purchase? "))
                process_order(product_name, quantity)
            case 4:
                sales_report()
            case 5:
                break
            case _:
                print("Incorrect choice entered")


if __name__ == '__main__':
    main()
