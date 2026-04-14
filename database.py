import psycopg2

#eastablish connection to postgres
conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='1956',dbname='myduka')

#object for db operations
cur = conn.cursor()

cur.execute("select * from products")
products = cur.fetchall()
print(products)

cur.execute("select * from sales")
sales = cur.fetchall()
print(sales)

cur.execute("insert into products(name,buying_price,selling_price)values('laptop',50000,60000)")
conn.commit()

print(products)

#fetching products
def get_products():
    cur.execute('select * from products')
    products = cur.fetchall()
    return products

products_data = get_products()
print(products_data)

#fetching sales
def get_sales():
    cur.execute('select * from sales')
    sales = cur.fetchall()
    return sales

sales_data = get_sales()
print(sales_data)

# define the following functions : insert_sales(),insert_stock(),insert_users() 
# and use them to insert sales, stock and users respectively

def insert_sales(sale_details):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",(sale_details))
    conn.commit()

sale1 = (4,20)
sale2 = (5,40)
insert_sales(sale1)
insert_sales(sale2)

sales_data = get_sales()
print(sales_data)

def insert_stock(stock_details):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",(stock_details))
    conn.commit()


stock1 = (7,50)
stock2 = (8,25)

insert_stock(stock1)
insert_stock(stock2)


def insert_users(user_details):
    # CORRECT: string ends, then a comma, then the variable
    cur.execute("insert into users(username, password) values(%s, %s)", user_details)
    conn.commit()

user1 = ('admin', '1234')
user2 = ('cashier', 'pass123')

insert_users(user1)
insert_users(user2)

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
