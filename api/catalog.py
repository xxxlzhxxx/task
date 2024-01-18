from flask import *
from app import *


@app.route('/', methods=['GET'])
def get_items():
    """Display all the items."""
    if 'cart' not in session or not session['cart']:
        print('initialize session')
        session['cart'] = []
    conn = sqlite3.connect('online_shop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    rows = cursor.fetchall()
    
    conn.close()
    products = []
    for item in rows:
        product = {}
        product['name'] = item[1]
        product['price'] = item[2]
        product['num'] = item[3]
        products.append(product)
    return render_template('catalog.html', products=products) 




@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form['id']
    product_name = request.form['name']
    price = request.form['price']

    product = {
        'id': product_id,
        'name': product_name,
        'price': price,
    }

    session['cart'].append(product)
    session.modified = True
    return redirect(url_for('get_items'))