from app import app, db
from app.models import *

# seed with 5 customers

if Customer.query.filter_by(full_name='Kat Dob').first():
    pass
else:
    new_customer = Customer(
        full_name='Kat Dob',
        contact_info_dict=
            {
                'phone_number': '1111114444',
                'street_address': '123 four five six lane',
                'town/city': 'boston',
                'state_code': 'MA',
                'zip_code': '02115'
            }
    )
    db.session.add(new_customer)
    db.session.commit()

if Customer.query.filter_by(full_name='Clarence LaCroix').first():
    pass
else:
    new_customer = Customer(
        full_name='Clarence LaCroix',
        contact_info_dict=
            {
                'phone_number': '1111114444',
                'street_address': '123 Tangerine Street',
                'town/city': 'Sunnydale',
                'state_code': 'FL',
                'zip_code': '02115'
            }
    )
    db.session.add(new_customer)
    db.session.commit()

if Customer.query.filter_by(full_name='Frederick Gateau').first():
    pass
else:
    new_customer = Customer(
        full_name='Frederick Gateau',
        contact_info_dict=
            {
                'phone_number': '1111114444',
                'street_address': '123 Bakery Drive',
                'town/city': 'boston',
                'state_code': 'MA',
                'zip_code': '02115'
            }
    )
    db.session.add(new_customer)
    db.session.commit()

if Customer.query.filter_by(full_name='Lana Baytown').first():
    pass
else:
    new_customer = Customer(
        full_name='Lana Baytown',
        contact_info_dict=
            {
                'phone_number': '1111114444',
                'street_address': '123 Shell Avenue',
                'town/city': 'Portland',
                'state_code': 'ME',
                'zip_code': '02115'
            }
    )
    db.session.add(new_customer)
    db.session.commit()

if Customer.query.filter_by(full_name='Millie Turkeytown').first():
    pass
else:
    new_customer = Customer(
        full_name='Millie Turkeytown',
        contact_info_dict=
            {
                'phone_number': '1111114444',
                'street_address': '123 Pilgrim Lane',
                'town/city': 'New York',
                'state_code': 'NY',
                'zip_code': '02115'
            }
    )
    db.session.add(new_customer)
    db.session.commit()

print('\nCreated {} customers:\n{}'.format(Customer.query.count(), Customer.query.all()))

# seed with 3 suppliers
if Supplier.query.filter_by(name='HalloweenTown').first():
    pass
else:
    new_supplier = Supplier(
        name='HalloweenTown',
        contact_info_dict={
            'contact_name': 'Alex Smith',
            'phone_number': '0001110000',
            'street_address': '0 Uninhabitable Road',
            'town/city': 'Chicago',
            'state_code': 'IL',
            'zip_code': '83625'
        }
    )
    db.session.add(new_supplier)
    db.session.commit()

if Supplier.query.filter_by(name='Sleepy Hollow Inflatables').first():
    pass
else:
    new_supplier = Supplier(
        name='Sleepy Hollow Inflatables',
        contact_info_dict={
            'contact_name': 'Julia Ghoulton',
            'phone_number': '6667776666',
            'street_address': '666 Main Street',
            'town/city': 'Sleepy Hollow',
            'state_code': 'NY',
            'zip_code': '76304'
        }
    )
    db.session.add(new_supplier)
    db.session.commit()

if Supplier.query.filter_by(name='Haunted Labrynth House').first():
    pass
else:
    new_supplier = Supplier(
        name='Haunted Labrynth House',
        contact_info_dict={
            'contact_name': 'Gerald Cornfarmer',
            'phone_number': '1112223333',
            'street_address': '456 Crop Street',
            'town/city': 'Corntown',
            'state_code': 'VA',
            'zip_code': '21042'
        }
    )
    db.session.add(new_supplier)
    db.session.commit()

print('\nCreated {} suppliers: {}\n'.format(Supplier.query.count(), Supplier.query.all()))

# seed with 10 products

# seed with 5 orders

# seed with 10 shipments
