from flask import Flask
app = Flask(__name__)


@app.route('/coin_count/<int:amount>', methods=['GET'])
def coin_count(amount):
    '''returned from a given sum amount in the number of coins'''
    coins = [1, 4, 15, 20]
    remaining_amount = amount
    denomination = []
    counts = []

    # creating list of used coins and counts
    for coin in sorted(coins, reverse=True):
        num = remaining_amount / coin
        if num:
            denomination.append(coin)
            count_id = remaining_amount // coin
            counts.append(count_id)
            remaining_amount -= count_id * coin
            final_dict = {}
            dict_indx = 0
            for value in denomination:
                final_dict[value] = counts[dict_indx]
                dict_indx += 1

    # deleting zero value keys
    for key, value in list(final_dict.items()):
        if value == 0:
            del final_dict[key]
    return final_dict

if __name__ == '__main__':
    app.run(debug=True)