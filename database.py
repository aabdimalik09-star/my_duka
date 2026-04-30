import psycopg2

#establishing connection to Postgres
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='1956',dbname='myduka')

#object to perform db operations
cur = conn.cursor()

#fetching products
def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products


#fetching sales
def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


#fetching stock
def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock


def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data


def insert_products(products_details):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{products_details}")
    conn.commit()

products1 = ('milk',50,60)
insert_products(products1)



def insert_stock(stock_details):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",(stock_details))
    conn.commit()

def insert_sales(sales_details):
    cur.execute("insert into sales(pid, quantity) values (%s, %s)", sales_details)
    conn.commit()  



def get_users():
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return users

def create_user(full_name, email, phone, password):
    cur.execute("INSERT INTO users (full_name, email, phone_number, password) VALUES (%s, %s, %s, %s)", (full_name, email, phone, password))
    conn.commit()

def check_user_exists(email):
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    return user is not None



def available_stock(pid):
    cur.execute("select sum(stock_quantity)from stock where pid = %s",(pid,))
    total_stock = cur.fetchone()[0] or 0

    cur.execute("select sum(quantity)from sales where pid = %s",(pid,))
    total_sold = cur.fetchone()[0] or 0

    return total_stock - total_sold


check_stock = available_stock(58)
print(check_stock)








def sales_per_product():
    cur.execute('''
                select products.name as p_name , sum(quantity * selling_price) as total_sales 
                from sales join products on products.id = sales.pid group by p_name;
    ''')
    sales_product = cur.fetchall()
    return sales_product


def sales_per_day():
    cur.execute('''
        select date(sales.created_at) as day, (sales.quantity * products.selling_price) as 
        total_sales from products join sales on sales.pid = products.id group by day;
    ''')
    sales_day = cur.fetchall()
    return sales_day


def profit_per_product():
    cur.execute('''
        select products.name as p_name , sum((selling_price - buying_price) * quantity) as total_profit
        from sales join products on sales.pid = products.id group by p_name;
    ''')
    profit_product = cur.fetchall()
    return profit_product


def profit_per_day():
    cur.execute('''
        select date(sales.created_at) as day, sum((selling_price - buying_price) * quantity) as total_profit
        from sales join products on sales.pid = products.id group by day;
    ''')
    profit_day = cur.fetchall()
    return profit_day