from flask import Flask, jsonify, request

app = Flask(__name__)
cars = [
    {
        'name': 'Swift',
        'owner': "Vansh",
        'color': "white",
        "price": "30000",
    },
    {
        'name': 'Hyundai',
        'owner': "Thanisha",
        'color': "blue",
        "price": "50000",
    },
    {
        'name': 'Maruti Suzuki',
        'owner': "Janhavi",
        'color': "black",
        "price": "30010",
    },
    {
        'name': 'Toyota',
        'owner': "Pratham",
        'color': "pink",
        "price": "31000",
    },
    {
        'name': 'Honda',
        'owner': "Deepak",
        'color': "purple",
        "price": "30000",
    },
]


@app.route('/')
def home():
    return "Hello to Api"


@app.route('/cars')
def get_all_store_name():
    return jsonify({'cars': cars})


@app.route('/owner/<string:name>')
def get_store_name(name):
    for store in cars:
        if (store['name'] == name):
            return jsonify({'owner': store['owner']})
    return jsonify({'message': 'store not found'})


@app.route('/new_customer', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_owner = {
        'name': request_data['name'],
        'owner': request_data['owner'],
        'color': request_data['color'],
        'price': request_data['price']
    }
    cars.append(new_owner)
    return jsonify(new_owner)


@app.route('/delete/<int:index>', methods=['DELETE'])
def delete_name(index):
    cars.pop(index)
    return jsonify('successfully deleted')


app.run(port=5000)
