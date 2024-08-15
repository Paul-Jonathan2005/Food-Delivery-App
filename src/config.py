from sqlalchemy import create_engine

db_name='Food Delivery'
db_host='localhost'
db_port=5432
db_user='postgres'
db_pass='jona@2005'
menu_table='menu'
user_table='user_details'
cart_table='cart'
menutype_table='menu_types'

db_engine=create_engine(f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')
