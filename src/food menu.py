import config

class FoodMenu:
    def __init__(self):
        self.engine=config.db_engine
        self.user_table=config.user_table
        self.menu_table=config.menu_table
        self.cart_table=config.cart_table
        self.menutype_table=config.menutype_table

    
        