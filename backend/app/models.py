import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, PickleType, JSON
from . import app, db


# see the project here! https://github.com/katdob/SpookyZephyrWarehouse


class Customer(db.Model):
    __tablename__ = 'customers'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    full_name = Column(String(500), index=True, unique=False, nullable=False)
    contact_info = Column(
        JSON, 
        default={
            'phone_number': '',
            'street_address': '',
            'town/city': '',
            'state_code': '',
            'zip_code': ''
        },
        nullable=False)

    def __init__(self, full_name, contact_info_dict):
        self.full_name = full_name
        
        key_list = ['phone_number', 'street_address', 'town/city', 'state_code', 'zip_code']
        for key in contact_info_dict:
            if key not in key_list:
                print('You must include key/value for {}.'.format(key))
                return 'You must include key/value for {}.'.format(key)
            if contact_info_dict[key] == '':
                print('You must include key/value for {}.'.format(key))
                return 'You must include key/value for {}.'.format(key)
        self.contact_info = contact_info_dict

    def __repr__(self):
        return '<Customer {}, {}>'.format(self.id, self.full_name)


class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    ordered_on = Column(DateTime, default=datetime.date.today(), nullable=False)

    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.ordered_on = datetime.date.today()

    def __repr__(self):
        customer = Customer.query.filter_by(id=self.customer_id).first()
        return '<Order {} for customer {} with id {}, ordered on {}>'.format(
            self.id, customer.full_name, customer.id, self.ordered_on)


class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(500), index=True, nullable=False)
    description = Column(String(500), index=True, nullable=False)
    suppliers = Column(PickleType, nullable=True) # a list of supplier ids (int)

    def __init__(self, name, description):
        if description == '' or name == '':
            print('You must include a name: {} and description: {}'.format(name, description))
            # return 'You must include a name and description'
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Product {}, {} suppliers: {}>'.format(self.id, self.name, self.suppliers)


class Shipment(db.Model):
    __tablename__ = 'shipments'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    tracking_no = Column(String(500), index=True)
    products = Column(PickleType, nullable=True) # a list of product ids (int)

    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)

    def __init__(self, products):
        if not isinstance(products, list): 
            return 'Products must be a list.'
        self.products = products

    def __repr__(self):
        return '<Shipment {}, with tracking_no {}>'.format(self.id, self.tracking_no)


class Supplier(db.Model):
    __tablename__ = 'suppliers'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(500), index=True, nullable=False)
    contact_info = Column(
        JSON, 
        default={
            'contact_name': '',
            'phone_number': '',
            'street_address': '',
            'town/city': '',
            'state_code': '',
            'zip_code': ''
        },
        nullable=False)
    products = Column(PickleType, nullable=True) # a list of product ids (int)

    def __init__(self, name, contact_info_dict):
        self.name = name
        key_list = ['contact_name', 'phone_number', 'street_address', 'town/city', 'state_code', 'zip_code']
        for key in contact_info_dict:
            if key not in key_list:
                return 'You must include key/value for {}.'
            if contact_info_dict[key] == '':
                return 'You must include key/value for {}.'
        self.contact_info = contact_info_dict

    def __repr__(self):
        return '<Supplier {}, {}>'.format(self.id, self.name)
