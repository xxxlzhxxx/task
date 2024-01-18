from flask import Flask, jsonify, request
from app import *


@app.route('/cart', methods=['GET'])
def get_cart():
    """Display all the items."""
    cart = session.get('cart', [])
    total = 0
    for item in cart:
        total += int(item['price'])
    return render_template('cart.html', cart=cart, total=total)




@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('index'))
