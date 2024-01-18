from flask import *
from app import *

@app.route('/checkout', methods=['GET'])
def checkout():
    cart = session.get('cart', {})
    # total_price = calculate_total_price(cart)
    return render_template('checkout.html')


@app.route('/process_check', methods=['POST'])
def process_checkout():
    session.pop('cart', None)
    return redirect(url_for('get_items'))


def calculate_total_price(cart):
    total_price = 0
    for product_id, item in cart.items():
        quantity = item['quantity']
        price = item['price']
        total_price += quantity * price
    return total_price

