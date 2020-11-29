import pytz
import datetime
from . import app
from .models import *
from flask import jsonify


@app.route('/')
@app.route('/index')
def index():
    return jsonify('Hello, World!')


@app.route('/orders')
def get_orders():
    return_orders = {}
    for o in Order.query.all():
        return_orders[o.id] = {}
        customer = Customer.query.filter_by(id=o.customer_id).first()
        return_orders[o.id]['customer'] = customer.full_name
        return_orders[o.id]['ordered_on'] = o.ordered_on
        shipments = {}
        for s in Shipment.query.all():
            if s.order_id == o.id:
                shipments[s.id] = {}
                shipments[s.id]['tracking_no'] = s.tracking_no
                supplier_name = Supplier.query.filter_by(id=s.supplier_id).first().name 
                shipments[s.id]['supplier'] = supplier_name
                products = []
                for p in s.products:
                    pro = Product.query.filter_by(id=p).first()
                    products.append(pro.name)
                shipments[s.id]['products'] = products
        return_orders[o.id]['shipments'] = shipments
    return jsonify(return_orders)


@app.route('/products')
def get_products():
    return_products = {}
    for p in Product.query.all():
        return_products[p.id] = {}
        return_products[p.id]['name'] = p.name
        return_products[p.id]['description'] = p.description
        suppliers_list = []
        for s in p.suppliers:
            sup = Supplier.query.filter_by(id=s).first()
            suppliers_list.append(sup.name)
        return_products[p.id]['suppliers_list'] = suppliers_list
    return jsonify(return_products)