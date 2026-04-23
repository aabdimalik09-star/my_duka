from flask import Flask, render_template
from database import get_products, get_sales, get_stock

# CREATING A FLASK INSTANCE
app = Flask(__name__)


@app.route('/')# decorator function
def home():#view function
    return render_template('index.html')


#http://127.0.0.1:5000/products
@app.route('/products')
def products():
    products_data = get_products()
    return render_template('products.html',products = products_data)


@app.route('/sales')
def sales():
    sales_data = get_sales()
    return render_template('sales.html',sales = sales_data)


@app.route('/stock')
def stock():
    stock_data = get_stock()
    return render_template('stock.html',stock = stock_data)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')







app.run()




