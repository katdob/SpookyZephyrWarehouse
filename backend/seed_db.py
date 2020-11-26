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

print('\n\nCreated {} customers:\n'.format(Customer.query.count()))
for c in Customer.query.all():
    print(c)
kat = Customer.query.all()[0]
clarence = Customer.query.all()[1]
fred = kat = Customer.query.all()[2]
lana = Customer.query.all()[3]
millie = Customer.query.all()[4]


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

print('\n\nCreated {} suppliers:\n'.format(Supplier.query.count()))
for s in Supplier.query.all():
    print(s)
halloweentown = Customer.query.all()[0]
sleepyhollow = Customer.query.all()[1]
hauntedlabrynth = Customer.query.all()[2]


# seed with 10 products

# https://www.gemmy.com/black-cat/
if Product.query.filter_by(name='Black Cat').first():
    pass
else:
    new_product = Product(
        name='Black Cat',
        description='Frighten your guests with this creepy Airblown inflatable character. \
            The black cat is prepared to pounce into any Halloween scene.'
    )
    new_product.suppliers = [hauntedlabrynth.id]
    db.session.add(new_product)
    db.session.commit()

# https://www.homedepot.com/p/Warner-9-5-ft-Pre-Lit-Beetlejuice-Sandworm-Animated-Airblown-Inflatable-224336/308475547
if Product.query.filter_by(name='Beetlejuice Sandworm').first():
    pass
else:
    new_product = Product(
        name='Beetlejuice Sandworm',
        description='Easily add a spooky touch to your Halloween décor \
            with this 9.5 ft. Pre-Lit Inflatable Animated Beetlejuice \
            Sandworm WB Airblown. Each scene self-inflates for a quick and \
            easy setup. All stakes and tethers are included for added security. \
            Animated: tongue moves from side to side.'
    )
    new_product.suppliers = [sleepyhollow.id]
    db.session.add(new_product)
    db.session.commit()

# https://www.gemmy.com/animated-audrey-from-little-shop-of-horrors/
if Product.query.filter_by(name='Little Shop of Horrors Audrey').first():
    pass
else:
    new_product = Product(
        name='Little Shop of Horrors Audrey',
        description='Amaze your guests with this animated giant \
        Airblown inflatable featuring Audrey from Little Shop of \
        Horrors! Audrey comes to life in this amazing Halloween scene \
        and her tongue moves from side to side.'
    )
    new_product.suppliers = [halloweentown.id]
    db.session.add(new_product)
    db.session.commit()

# https://www.gemmy.com/animated-globe-fire-ice-dragon/
if Product.query.filter_by(name='Dragon with Globe').first():
    pass
else:
    new_product = Product(
        name='Dragon with Globe',
        description='Decorate your yard with this incredible \
        Projection Airblown® Globe. It creates a spooky \
        Halloween light show with realistic, flickering flames.'
    )
    new_product.suppliers = [sleepyhollow.id]
    db.session.add(new_product)
    db.session.commit()

# https://www.gemmy.com/zero-in-doghouse/
if Product.query.filter_by(name='Zero with Doghouse').first():
    pass
else:
    new_product = Product(
        name='Zero with Doghouse',
        description='Greet your guests and neighbors with the \
        familiar face of this Airblown® inflatable character. \
        Zero from The Nightmare Before Christmas stands with his \
        doghouse in this fun Halloween scene.'
    )
    new_product.suppliers = [hauntedlabrynth.id, halloweentown.id, sleepyhollow.id]
    db.session.add(new_product)
    db.session.commit()

# https://www.gemmy.com/projection-fire-ice-two-headed-dragon/
if Product.query.filter_by(name='Two Headed Dragon').first():
    pass
else:
    new_product = Product(
        name='Two Headed Dragon',
        description='Double trouble awaits you this season \
        with the Animated Inflatable 2-Headed Dragon. Featuring \
        an incredible fire-and-ice and flaming mouth lighting \
        effect, this 2-headed creature will frighten visitors and \
        trick-or-treaters near and far. Stands over 7-1/2 ft. tall.'
    )
    new_product.suppliers = [halloweentown.id, hauntedlabrynth.id]
    db.session.add(new_product)
    db.session.commit()

# https://www.gemmy.com/haunted-castle-archway/
if Product.query.filter_by(name='Haunted Castle Archway').first():
    pass
else:
    new_product = Product(
        name='Haunted Castle Archway',
        description='Double trouble awaits you this season with \
        the Animated Inflatable 2-Headed Dragon. Featuring an \
        incredible fire-and-ice and flaming mouth lighting effect, \
        this 2-headed creature will frighten visitors and \
        trick-or-treaters near and far.'
    )
    new_product.suppliers = [hauntedlabrynth.id]
    db.session.add(new_product)
    db.session.commit()

# https://www.gemmy.com/green-and-black-spider/
if Product.query.filter_by(name='Green and Black Spider').first():
    pass
else:
    new_product = Product(
        name='Green and Black Spider',
        description='Light up the night with this giant Airblown \
        Inflatable character. The spider projects psychedelic spirals \
        of green light from its body.'
    )
    new_product.suppliers = [sleepyhollow.id, hauntedlabrynth.id]
    db.session.add(new_product)
    db.session.commit()

# https://www.gemmy.com/tree-with-ligthing-pumpkins/
if Product.query.filter_by(name='Tree with Pumpkins').first():
    pass
else:
    new_product = Product(
        name='Tree with Pumpkins',
        description='Frighten your guests with this amazing \
        inflatable scene. The terrifying tree stands tall with \
        its ghoulish companions and spooky Jack-O\'-Lanterns.'
    )
    new_product.suppliers = [halloweentown.id, hauntedlabrynth.id]
    db.session.add(new_product)
    db.session.commit()

# https://www.gemmy.com/ecto-1-with-slimer-out-of-window/
if Product.query.filter_by(name='Slimer in Ghostbusters Mobile').first():
    pass
else:
    new_product = Product(
        name='Slimer in Ghostbusters Mobile',
        description='There\'s something strange in your neighborhood! \
            This Airblown® Slimer looks spooky as he greets guests from \
            The Ghostbusters Ecto-1. It comes with everything needed for \
            easy outdoor setup.'
    )
    new_product.suppliers = [halloweentown.id, hauntedlabrynth.id]
    db.session.add(new_product)
    db.session.commit()

black_cat = Product.query.all()[0]
beetlejuice_sandworm = Product.query.all()[1]
audrey_plant = Product.query.all()[2]
dragon_with_globe = Product.query.all()[3]
zero_with_doghouse = Product.query.all()[4]
two_headed_dragon = Product.query.all()[5]
haunted_castle_archway = Product.query.all()[6]
green_and_black_spider = Product.query.all()[7]
tree_with_pumpkins = Product.query.all()[8]
slimer_with_ghostbusters_mobile = Product.query.all()[9]
print('\n\nCreated {} products: \n'.format(Product.query.count()))
for p in Product.query.all():
    print(p)


# seed with 5 orders

if Order.query.count() != 5:
    order_1 = Order(customer_id=kat.id)
    db.session.add(order_1)

    order_2 = Order(customer_id=clarence.id)
    db.session.add(order_2)

    order_3 = Order(customer_id=fred.id)
    db.session.add(order_3)

    order_4 = Order(customer_id=lana.id)
    db.session.add(order_4)

    order_5 = Order(customer_id=millie.id)
    db.session.add(order_5)

    db.session.commit()

order_1 = Order.query.all()[0]
order_2 = Order.query.all()[1]
order_3 = Order.query.all()[2]
order_4 = Order.query.all()[3]
order_5 = Order.query.all()[4]
print('\n\nCreated {} orders: \n'.format(Order.query.count()))
for o in Order.query.all():
    print(o)


# seed with 10 shipments


if Shipment.query.count() != 10:

    shipment_1 = Shipment(products=[beetlejuice_sandworm.id])
    shipment_1.order_id = order_1.id
    shipment_1.supplier_id = 2
    shipment_1.tracking_no = '238763482394276021111'
    db.session.add(shipment_1)

    shipment_2 = Shipment(products=[zero_with_doghouse.id])
    shipment_2.order_id = order_1.id
    shipment_2.supplier_id = 3
    shipment_2.tracking_no = '238763482394276022222'
    db.session.add(shipment_2)

    shipment_3 = Shipment(products=[tree_with_pumpkins.id])
    shipment_3.order_id = order_2.id
    shipment_3.supplier_id = 1
    shipment_3.tracking_no = '238763482394276023333'
    db.session.add(shipment_3)

    shipment_4 = Shipment(products=[slimer_with_ghostbusters_mobile.id])
    shipment_4.order_id = order_2.id
    shipment_4.supplier_id = 3
    shipment_4.tracking_no = '238763482394276024444'
    db.session.add(shipment_4)

    shipment_5 = Shipment(products=[green_and_black_spider.id])
    shipment_5.order_id = order_3.id
    shipment_5.supplier_id = 2
    shipment_5.tracking_no = '238763482394276025555'
    db.session.add(shipment_5)

    shipment_6 = Shipment(products=[two_headed_dragon.id])
    shipment_6.order_id = order_3.id
    shipment_6.supplier_id = 1
    shipment_6.tracking_no = '238763482394276026666'
    db.session.add(shipment_6)

    shipment_7 = Shipment(products=[black_cat.id, haunted_castle_archway])
    shipment_7.order_id = order_4.id
    shipment_7.supplier_id = 3
    shipment_7.tracking_no = '238763482394276027777'
    db.session.add(shipment_7)

    shipment_8 = Shipment(products=[audrey_plant.id])
    shipment_8.order_id = order_5.id
    shipment_8.supplier_id = 1
    shipment_8.tracking_no = '238763482394276029999'
    db.session.add(shipment_8)

    shipment_9 = Shipment(products=[dragon_with_globe.id])
    shipment_9.order_id = order_5.id
    shipment_9.supplier_id = 2
    shipment_9.tracking_no = '238763482394276021010'
    db.session.add(shipment_9)

    db.session.commit()

print('\nCreated {} shipments:\n'.format(Shipment.query.count()))
for s in Shipment.query.all():
    print(s)
print('\n\n')