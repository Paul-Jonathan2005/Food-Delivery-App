import config
from sqlalchemy import text

class FoodMenu:
    def __init__(self):
        self.engine=config.db_engine
        self.user_table=config.user_table
        self.menu_table=config.menu_table
        self.cart_table=config.cart_table
        self.menutype_table=config.menutype_table

    def execute_query(self, query):
        query = text(query)
        with self.engine.begin() as conn:
            conn.execute(query)

    def execute_get_query(self, query):
        query = text(query)
        with self.engine.begin() as conn:
             result = conn.execute(query)
        return result

    def add_item_type(self, item_type):
        insert_query = f"insert into {self.menutype_table} values ('{item_type}')"
        self.execute_query(insert_query)

    def add_item_to_menu(self, item_type, item_name, item_cost):
        insert_query = f"insert into {self.menu_table} values ('{item_type}', '{item_name}', '{item_cost}')"
        self.execute_query(insert_query)

    def add_item_to_cart(self, user_name, number_of_items, item_name, item_cost):
        insert_query = f"insert into {self.cart_table} values ('{user_name}', '{number_of_items}', '{item_name}', '{item_cost}')"
        self.execute_query(insert_query)

    def add_user(self, customer_name, phone_number, passcode, email):
        insert_query = f"insert into {self.user_table} values ('{customer_name}', '{phone_number}', '{passcode}', '{email}')"
        self.execute_query(insert_query)
    
    def get_all_item_types(self):
        get_query = f"select * from {self.menutype_table}"
        all_item_types = self.execute_get_query(get_query)
        all_item_types = [x[0] for x in all_item_types]
        return {'item_types': all_item_types}
    
    def get_all_items_by_item_type(self, item_type):
        get_query = f"select item_name, item_cost from {self.menu_table} where item_type = '{item_type}'"
        all_items_by_item_type = self.execute_get_query(get_query)
        all_items_by_item_type = [{'item_name':name,'item_cost':cost} for name,cost in all_items_by_item_type]
        return {'items': all_items_by_item_type}
    
    def get_items_in_cart_by_user_name(self, user_name):
        get_query = f"select item_name, number_of_items, item_cost from {self.cart_table} where user_name = '{user_name}'"
        get_items_in_cart_by_user_name = self.execute_get_query(get_query)
        get_items_in_cart_by_user_name = [{'item_name':name, 'no_of_items':number_of_items, 'item_cost':cost} for name,number_of_items,cost in get_items_in_cart_by_user_name]
        return {'cart_items': get_items_in_cart_by_user_name}
    
    def increase_item_count(self, user_name, item_name):
        update_query = f"update {self.cart_table} set number_of_items = number_of_items+1 where user_name='{user_name}' and item_name = '{item_name}'"
        self.execute_query(update_query)
    
    def decrease_item_count(self, user_name, item_name):
        get_query = f"select number_of_items from {self.cart_table} where user_name = '{user_name}' and item_name = '{item_name}'"
        item_count = self.execute_get_query(get_query).fetchone()[0]
        if item_count>1:
            update_query = f"update {self.cart_table} set number_of_items = number_of_items-1 where user_name='{user_name}' and item_name = '{item_name}'"
            self.execute_query(update_query)

    def remove_item_from_cart(self, user_name, item_name):
        delete_query = f"delete from {self.cart_table} where user_name = '{user_name}' and item_name = '{item_name}'"
        self.execute_query(delete_query)