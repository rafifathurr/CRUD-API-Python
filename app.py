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
    query = """INSERT INTO wallets(name) 
            values(%s)"""

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
    query = """SELECT * 
            FROM wallets"""

    mycursor = mydb.cursor()
    mycursor.execute(query)
    row_headers = [x[0] for x in mycursor.description]
    data = mycursor.fetchall()
    json_data = []
    for result in data:
        json_data.append(dict(zip(row_headers, result)))
    mydb.commit()
    return make_response(jsonify(json_data), 200)

@app.route("/update_wallet", methods=["POST"])
def update_wallet():
    hasil = {"status": "failed"}
    query = """UPDATE wallets 
            SET name = %s 
            WHERE id = %s"""

    try:
        id = request.form.get('id')
        name = request.form.get('name')
        value = (name, id)
        mycursor = mydb.cursor()
        mycursor.execute(query, value)
        mydb.commit()
        hasil = {"status": "success"}
    except Exception as e:
        print("ERROR : "+str(e))

    return jsonify(hasil)

@app.route("/delete_wallet", methods=["POST"])
def delete_wallet():
    hasil = {"status": "failed"}
    query = """DELETE 
            FROM wallets 
            WHERE id = %s"""

    try:
        id = request.form.get('id')
        value = (id)
        mycursor = mydb.cursor()
        mycursor.execute(query, value)
        mydb.commit()
        hasil = {"status": "success"}
    except Exception as e:
        print("ERROR : "+str(e))

    return jsonify(hasil)

@app.route("/post_asset", methods=["POST"])
def post_asset():
    hasil = {"status": "failed"}
    query = """INSERT INTO assets(wallet_id, name, symbol, 
            network, address, balance) 
            values(%s, %s, %s, %s, %s, %s)"""

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
    query = """select 
            assets.id as id_assets, 
            wallets.name as wallet_name,
            assets.name, 
            assets.symbol, 
            assets.network, 
            assets.address,
            assets.balance 
            from assets
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

@app.route("/update_asset", methods=["POST"])
def update_asset():
    hasil = {"status": "failed"}
    query = """UPDATE assets 
            SET 
            wallet_id = %s ,
            name = %s ,
            symbol = %s ,
            network = %s ,
            address = %s ,
            balance = %s 
            WHERE id = %s"""
    try:
        id = request.form.get('id')
        wallet_id = request.form.get('wallet_id')
        name = request.form.get('name')
        symbol = request.form.get('symbol')
        network = request.form.get('network')
        address = request.form.get('address')
        balance = request.form.get('balance')
        value = (wallet_id, name, symbol, network, address, balance, id)
        mycursor = mydb.cursor()
        mycursor.execute(query, value)
        mydb.commit()
        hasil = {"status": "success"}
    except Exception as e:
        print("ERROR : "+str(e))

    return jsonify(hasil)

@app.route("/delete_asset", methods=["POST"])
def delete_asset():
    hasil = {"status": "failed"}
    query = """DELETE 
            FROM assets 
            WHERE id = %s"""
    try:
        id = request.form.get('id')
        value = (id)
        mycursor = mydb.cursor()
        mycursor.execute(query, value)
        mydb.commit()
        hasil = {"status": "success"}
    except Exception as e:
        print("ERROR : "+str(e))

    return jsonify(hasil)

@app.route("/post_transaction", methods=["POST"])
def post_transaction():
    hasil = {"status": "failed"}
    query = """INSERT INTO asset_transactions(src_wallet_id, src_asset_id, 
            dest_wallet_id, dest_asset_id, amount, gas_fee, total) 
            values(%s, %s, %s, %s, %s, %s, %s)"""

    try:
        src_wallet_id = request.form.get('src_wallet_id')
        src_asset_id = request.form.get('src_asset_id')
        dest_wallet_id = request.form.get('dest_wallet_id')
        dest_asset_id = request.form.get('dest_asset_id')
        amount = float(request.form.get('amount'))
        gas_fee = float(request.form.get('gas_fee'))
        total = amount+gas_fee
        value = (src_wallet_id, src_asset_id, dest_wallet_id, dest_asset_id, amount, gas_fee, total)
        mycursor = mydb.cursor()
        mycursor.execute(query, value)
        mydb.commit()
        hasil = {"status": "success"}
    except Exception as e:
        print("ERROR : "+str(e))

    return jsonify(hasil)

@app.route("/get_data_transaction", methods=["POST"])
def get_data_transaction():
    query = """select 
            src_w.name as source_wallet_name,
            src_a.name as source_asset_name,
            dest_w.name as destination_wallet_name,
            dest_a.name as destination_asset_name,
            at.amount,
            at.gas_fee,
            at.total
            from 
            asset_transactions as at
            join wallets src_w on src_w.id = at.src_wallet_id
            join wallets dest_w on dest_w.id = at.dest_wallet_id
            join assets src_a on src_a.id = at.src_asset_id
            join assets dest_a on dest_a.id = at.dest_asset_id
            """

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
