from flask import Flask, request, render_template
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv_file(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price'] = float(row['price'])
            row['id'] = int(row['id'])
            products.append(row)
    return products

def read_sqlite_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    conn.close()
    # Convert rows to a list of dictionaries
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None
    
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = read_sqlite_db()
    else:
        error = "Wrong source"
    
    if product_id:
        product_id = int(product_id)
        products = [p for p in products if p['id'] == product_id]
        if not products:
            error = "Product not found"
    
    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)

