from flask import Flask
app = Flask(__name__)
from script import coin_count

@app.route('/coin_count/<int:amount>', methods=['GET'])
def coin (amount):
    return coin_count(amount)

if __name__ == '__main__':
    app.run(debug=True)