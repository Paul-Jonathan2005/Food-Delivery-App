import config
from sqlalchemy import text

class FoodMenu:
    def __init__(self):
        self.engine=config.db_engine
        self.user_table=config.user_table
        self.menu_table=config.menu_table
        self.cart_table=config.cart_table
        self.menutype_table=config.menutype_table

    def add_item_type(self, item_type):
        insert_query = f"insert into {self.menutype_table} values ('{item_type}')"
        insert_query = text(insert_query)
        with self.engine.begin() as conn:
            conn.execute(insert_query)
        