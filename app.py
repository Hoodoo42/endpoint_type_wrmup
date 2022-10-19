
from apihelpers import check_endpoint_info
import dbhelpers as dbh
from flask import Flask, request, make_response
import json

app = Flask(__name__)

@app.post('/api/restaurant')
def new_restaurant():
    is_valid = check_endpoint_info(request.json, ['name', 'address', 'phone', 'img'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL new_restaurant(?,?,?,?)', [request.json.get('name'), request.json.get('address'), request.json.get('phone'), request.json.get('img')])

    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('sorry, error'), 500)

@app.get('/api/restaurant')
def get_restaurants():
    results =dbh.run_statement('CALL get_restaurant')

    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('sorry, error', default=str), 500)        

@app.delete('/api/restaurant')
def delete_restaurant():
    is_valid = check_endpoint_info(request.json, ['id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL delete_restaurant(?)',[request.json.get('id')])

    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('Sorry, error', default=str), 500)    


# ITEM MENU

@app.get('/api/menu_item')
def get_items():
    results =dbh.run_statement('CALL get_item()')

    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('sorry, error', default=str), 500)

@app.post('/api/menu_item')
def new_item():

    is_valid = check_endpoint_info(request.json, ['r_id', 'name', 'description', 'price', 'img'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL new_item(?,?,?,?,?)', [request.json.get('r_id'), request.json.get('name'), request.json.get('description'), request.json.get('price'), request.json.get('img')])

    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('sorry, error'), 500)

@app.delete('/api/menu_item')
def delete_item():
    is_valid = check_endpoint_info(request.json, ['id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 200)

    results = dbh.run_statement('CALL delete_item(?)', [request.json.get('id')])

    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('Sorry, error', default=str), 500) 
            
app.run(debug=True)        