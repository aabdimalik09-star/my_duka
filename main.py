from flask import Flask , render_template,request,redirect,url_for
from database import get_products,get_sales,get_stock,insert_products,insert_stock,insert_sales

#creating a Flask instance
app = Flask(__name__)

# http://127.0.0.1:5000/ - url
@app.route('/') #decorator function
def home():#view function
    return  render_template('index.html')


# http://127.0.0.1:5000/products
@app.route('/products')
def products():
    products_data = get_products()
    return render_template("products.html",products_data = products_data)


@app.route('/add_product',methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']
        new_products = (product_name,buying_price,selling_price)
        insert_products(new_products)
        print("Product Added Successfully")
    return redirect(url_for('products'))


@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    if request.method == 'POST':
        product_id = request.form['p_id']
        quantity = request.form['quantity']
        created_at = request.form['created_at']
        new_sales = (product_id,quantity,created_at)
        insert_sales(new_sale)
        print("Sales made successfully")
    return redirect(url_for('sales'))



@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method == 'POST':
        product_id = request.form['p_id']
        stock_quantity = request.form['s_quantity']
        Time = request.form['Time']
        new_stock = (product_id,stock_quantity,Time)
        insert_stock(new_stock)
        print("Stock added successfully")
    return redirect(url_for('stock'))








@app.route('/sales')
def sales():
    sales_data = get_sales()
    return render_template("sales.html",sales_data = sales_data)


@app.route('/stock')
def stock():
    stock_data = get_stock()
    return render_template("stock.html",stock_data = stock_data)


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


# run your application
app.run(debug=True)