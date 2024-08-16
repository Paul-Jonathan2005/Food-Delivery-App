from flask import Flask, request, jsonify
from food_menu import FoodMenu
import config

app = Flask(__name__)

menu = FoodMenu()

@app.route('/item-type', methods=['POST'])
def add_item_type():
    if request.is_json and  'item_type' in request.get_json():
        data = request.get_json()
        item_type = data['item_type']
        try:
            menu.add_item_type(item_type)
            return jsonify({"Status": 'Success'}), 200
        except Exception as e:
            return jsonify({"Status": "Failure"}), 400
    else:
        return jsonify({"Status": "incorrect payload"}), 400
    
@app.route('/item-to-menu', methods=['POST'])
def add_item_to_menu():
    if request.is_json and  'item_type' in request.get_json() and  'item_name' in request.get_json() and  'item_cost' in request.get_json():
        data = request.get_json()
        item_type = data['item_type']
        item_name = data['item_name']
        item_cost = data['item_cost']
        try:
            menu.add_item_to_menu(item_type, item_name, item_cost)
            return jsonify({"Status": 'Success'}), 200
        except Exception as e:
            return jsonify({"Status": "Failure"}), 400
    else:
        return jsonify({"Status": "incorrect payload"}), 400
    
@app.route('/item-to-cart', methods=['POST'])
def add_item_to_cart():
    if request.is_json and  'user_name' in request.get_json() and  'number_of_items' in request.get_json() and  'item_name' in request.get_json() and  'item_cost' in request.get_json():
        data = request.get_json()
        item_type = data['item_type']
        number_of_items = data['number_of_items']
        item_name = data['item_name']
        item_cost = data['item_cost']
        try:
            menu.add_item_to_cart(item_type, number_of_items, item_name, item_cost)
            return jsonify({"Status": 'Success'}), 200
        except Exception as e:
            return jsonify({"Status": "Failure"}), 400
    else:
        return jsonify({"Status": "incorrect payload"}), 400
    
@app.route('/user', methods=['POST'])
def add_user():
    if request.is_json and  'customer_name' in request.get_json() and  'phone_number' in request.get_json() and  'passcode' in request.get_json() and  'email' in request.get_json():
        data = request.get_json()
        customer_name = data['customer_name']
        phone_number = data['phone_number']
        passcode = data['passcode']
        email = data['email']
        try:
            menu.add_user(customer_name, phone_number, passcode, email)
            return jsonify({"Status": 'Success'}), 200
        except Exception as e:
            return jsonify({"Status": "Failure"}), 400 
    else:
        return jsonify({"Status": "incorrect payload"}), 400

@app.route('/all-item-in-menu', methods=['GET'])
def get_all_item_types():
    try :
        data = menu.get_all_item_types()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"Status": "incorrect payload"}), 400
    
@app.route('/all-item-in-menu/{item_type}', methods=['GET'])
def get_all_items_by_item_type(item_type):
    try :
        data = menu.get_all_items_by_item_type(item_type)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"Status": "incorrect payload"}), 400
    
@app.route('/all-item-in-menu/user/{user_name}', methods=['GET'])
def get_items_in_cart_by_user_name(user_name):
    try :
        data = menu.get_items_in_cart_by_user_name(user_name)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"Status": "Failure"}), 400

@app.route('/increase-item-count', methods=['PUT'])
def increase_item_count():
    if request.is_json and  'user_name' in request.get_json() and  'item_name' in request.get_json():
        data = request.get_json()
        user_name = data['user_name']
        item_name = data['item_name']
        try:
            menu.increase_item_count(user_name, item_name)
            return jsonify({"Status": 'Success'}), 200
        except Exception as e:
            return jsonify({"Status": "Failure"}), 400
    else:
        return jsonify({"Status": "incorrect payload"}), 400
    
@app.route('/decrease-item-count', methods=['PUT'])
def decrease_item_count():
    if request.is_json and  'user_name' in request.get_json() and  'item_name' in request.get_json():
        data = request.get_json()
        user_name = data['user_name']
        item_name = data['item_name']
        try:
            menu.decrease_item_count(user_name, item_name)
            return jsonify({"Status": 'Success'}), 200
        except Exception as e:
            return jsonify({"Status": "Failure"}), 400
    else:
        return jsonify({"Status": "incorrect payload"}), 400

@app.route('/item-to-cart/{user_name}/{item_name}', methods=['DELETE'])
def remove_item_from_cart(user_name, item_name):
    try :
        data = menu.remove_item_from_cart(user_name, item_name)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"Status": "Failure"}), 400
    
if __name__ == '__main__':
    app.run(host = config.app_host, port = config.app_port)

    
    
           