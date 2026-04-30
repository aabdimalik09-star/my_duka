from flask import Flask , render_template,request,redirect,url_for,flash
from database import get_products,get_sales,get_stock,insert_products,insert_stock,insert_sales
from database import check_user_exists,create_user,get_users,available_stock
from flask_bcrypt import Bcrypt

#creating a Flask instance
app = Flask(__name__)

#bcrypt
bcrypt = Bcrypt(app)


app.secret_key = 'tyuqwiojhdskljdhsaklgggj'


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
        flash("Product Added Successfully",'success')
    return redirect(url_for('products'))


@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    if request.method == 'POST':
        product_id = request.form['pid']
        quantity = request.form['quantity']
        check_stock = available_stock(product_id)
    if check_stock < quantity:
        flash("insufficient stock,can not complete sale", 'danger')
        return redirect(url_for('sales'))
        new_sales = (product_id,quantity)
        insert_sales(new_sales)
        flash("Sales made successfully",'success')
    return redirect(url_for('sales'))



@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method == 'POST':
        product_id = request.form['p_id']
        stock_quantity = request.form['stock_quantity']
        new_stock = (product_id,stock_quantity,)
        insert_stock(new_stock)
        flash("Stock added successfully"'success')
    return redirect(url_for('stock'))




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            flash('User doesn\'t exist, please register','danger')
        else:
            if bcrypt.check_password_hash(existing_user[-1],password):
                flash('Login successful', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Password Incorrect', 'danger')

    return render_template('login.html')







@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone_number']
        password = request.form['password']
        
        if check_user_exists(email):
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            flash("User Already Exists", 'danger')
        else:
            create_user(full_name, email, phone, hashed_password)
            flash("User Registered Successfully", 'success')
            return redirect(url_for('login'))
            
    return render_template('register.html')














@app.route('/sales')
def sales():
    sales_data = get_sales()
    products_data = get_products()
    return render_template("sales.html",sales_data = sales_data,products_data = products_data)


@app.route('/stock')
def stock():
    stock_data = get_stock()
    products_data = get_products()
    return render_template("stock.html",stock_data = stock_data,products_data = products_data)


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")







# run your application
app.run(debug=True)