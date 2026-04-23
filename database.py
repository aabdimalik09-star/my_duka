import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="myduka",
        user="postgres",
        password="1956" # Use your actual psql password
    )
    return conn

def get_products():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM products;')
    products = cur.fetchall()
    cur.close()
    conn.close()
    return products

def get_sales():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, pid, quantity, created_at FROM sales;')
    sales = cur.fetchall()
    cur.close()
    conn.close()
    return sales

def get_stock():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, pid, stock_quantity, created_at FROM stock;')
    stock = cur.fetchall()
    cur.close()
    conn.close()
    return stock








# write sql queries to fetch the following data

def sales_per_product():
    cur.execute('''
        SELECT products.name, SUM(sales.quantity)
        AS total_sold
        FROM products
        JOIN sales ON products.id = sales.product_id
        GROUP BY products.name;
    ''')
    
    sales_product = cur.fetchall() 
    return sales_product



                
def sales_per_day():
    cur.execute('''
        SELECT s.created_at::DATE AS sale_date, SUM(p.selling_price * s.quantity)
        AS daily_sales
        FROM products p
        JOIN sales s ON p.id = s.pid
        GROUP BY sale_date;
    ''')
    
    sales_day = cur.fetchall()
    return sales_day


def profit_per_product():
    cur.execute('''
        SELECT p.name, SUM((p.selling_price - p.buying_price) * s.quantity) 
        AS total_profit
        FROM products p
        JOIN sales s ON p.id = s.pid
        GROUP BY p.name;
    ''')
    
    profit_prod = cur.fetchall()
    return profit_prod



def profit_per_day():
    cur.execute('''
        SELECT s.created_at::DATE AS sale_date, 
        SUM((p.selling_price - p.buying_price) * s.quantity) AS daily_profit
        FROM products p
        JOIN sales s ON p.id = s.pid
        GROUP BY sale_date;
    ''')
    
    profit_day = cur.fetchall()
    return profit_day
