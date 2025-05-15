import pandas as pd

def flatten_orders(data):
    """Flatten nested customer orders."""
    rows = []
    for order in data:
        for item in order['items']:
            rows.append({
                'order_id': order['order_id'],
                'customer_id': order['customer']['id'],
                'customer_name': order['customer']['name'],
                'location': order['customer']['location'],
                'item_id': item['item_id'],
                'product': item['product'],
                'price': item['price'],
                'quantity': item['quantity'],
                'total_price': item['price'] * item['quantity'],
                'order_date': order['order_date'],
                'status': order['status']
            })
    return pd.DataFrame(rows)
