from flask import *
from app import *

@app.route('/admin', methods=['GET', 'POST'])
def manage_inventory():
    if request.method == 'POST':
        # 获取用户提交的表单数据
        name = request.form['name']
        price = int(request.form['price'])
        nums = int(request.form['quantity'])

        conn = sqlite3.connect('online_shop.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ITEMS  
            (name, price, nums) 
            VALUES 
            (?, ?, ?)
        """, (name, price, nums))
        
        conn.commit()
        #conn.close()
        return redirect(url_for('manage_inventory'))

    return render_template('admin.html')



