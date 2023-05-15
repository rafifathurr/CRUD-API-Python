from flask import Flask, request, jsonify, make_response
import pymysql

app = Flask(__name__)

mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "assets"
)

@app.route("/post_wallet", methods=["POST"])
def post_wallet():
    hasil = {"status": "failed"}
    query = "INSERT INTO wallets(name) values(%s)"
    try:
        name = request.form.get('name')
        value = (name)
        mycursor = mydb.cursor()
        mycursor.execute(query, value)
        mydb.commit()
        hasil = {"status": "success"}
    except Exception as e:
        print("ERROR : "+str(e))

    return jsonify(hasil)

@app.route("/get_data_wallet", methods=["POST"])
def get_data_wallet():
    query = "SELECT * FROM wallets"

    mycursor = mydb.cursor()
    mycursor.execute(query)
    row_headers = [x[0] for x in mycursor.description]
    data = mycursor.fetchall()
    json_data = []
    for result in data:
        json_data.append(dict(zip(row_headers, result)))
    mydb.commit()
    return make_response(jsonify(json_data), 200)

@app.route("/post_asset", methods=["POST"])
def post_asset():
    hasil = {"status": "failed"}
    query = "INSERT INTO assets(wallet_id, name, symbol, network, address, balance) values(%s, %s, %s, %s, %s, %s)"
    try:
        wallet_id = request.form.get('wallet_id')
        name = request.form.get('name')
        symbol = request.form.get('symbol')
        network = request.form.get('network')
        address = request.form.get('address')
        balance = request.form.get('balance')
        value = (wallet_id, name, symbol, network, address, balance)
        mycursor = mydb.cursor()
        mycursor.execute(query, value)
        mydb.commit()
        hasil = {"status": "success"}
    except Exception as e:
        print("ERROR : "+str(e))

    return jsonify(hasil)

@app.route("/get_data_asset", methods=["POST"])
def get_data_asset():
    query = """select assets.id as id_assets, wallets.name as wallet_name,
            assets.name, assets.symbol, assets.network, assets.address,
            assets.balance from assets
            join wallets on wallets.id = assets.wallet_id"""

    mycursor = mydb.cursor()
    mycursor.execute(query)
    row_headers = [x[0] for x in mycursor.description]
    data = mycursor.fetchall()
    json_data = []
    for result in data:
        json_data.append(dict(zip(row_headers, result)))
    mydb.commit()
    return make_response(jsonify(json_data), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="9898")
