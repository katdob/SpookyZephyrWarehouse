import React, { useState } from 'react'
// components
import getOrders from './components/getOrders.js'
import getProducts from './components/getProducts.js'
// images
import audrey from './images/audrey.jpg'
import blackcat from './images/black_cat.jpg'
import globedragon from './images/globe_dragon.jpg'
import hauntedarchway from './images/haunted_archway.jpg'
import sandworm from './images/sandworm.jpg'
import slimer from './images/slimer.jpg'
import spider from './images/spider.jpg'
import tree_pumpkins from './images/tree_pumpkins.jpg'
import two_headed_dragon from './images/two_headed_dragon.jpg'
import zero_doghouse from './images/zero_doghouse.jpg'

const images = {
  'Black Cat': blackcat,
  'Beetlejuice Sandworm': sandworm,
  'Little Shop of Horrors Audrey': audrey,
  'Dragon with Globe': globedragon,
  'Zero with Doghouse': zero_doghouse,
  'Two Headed Dragon': two_headed_dragon,
  'Haunted Castle Archway': hauntedarchway,
  'Green and Black Spider': spider,
  'Slimer in Ghostbusters Mobile': slimer,
  'Tree with Pumpkins': tree_pumpkins
}

const App = () => {
  const [view, setView] = useState('Products')
  const [products, setProducts] = useState()  // eslint-disable-line
  const [orders, setOrders] = useState()  // eslint-disable-line

  const updateProducts = async () => {
    const productsApiCall = await getProducts()
    setProducts(() => productsApiCall)
  }

  const updateOrders = async () => {
    const ordersApiCall = await getOrders()
    setOrders(() => ordersApiCall)
  }

  return (
    <React.Fragment>
      <div style={{ background: '#a07ac1' }}>

        {/* title */}
        <div
          style={{
            margin: '0 0 0 0',
            padding: '4% 0 0 0',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            fontFamily: 'Griffy, cursive',
            fontSize: '500%'
          }}
        >
          Spooky Zephyr Warehouse
        </div>

        {/* description/tagline */}
        <div
          style={{
            margin: '0 0 0 0',
            padding: '5% 0 0 0',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            fontFamily: 'Griffy, cursive',
            fontSize: '150%'
          }}
        >
          Your source for quality inflatable displays for this spooky season.
        </div><br /><br /><br /><br />

        {/* menu */}
        <div
          style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            cursor: 'pointer'
          }}
          onClick={async () => {
            if (view === 'Orders') {
              await updateProducts()
              setView('Products')
            } else if (view === 'Products') {
              await updateOrders()
              setView('Orders')
            }
          }}
        >
          Products&nbsp;|&nbsp;Orders
          {/* {view} */}
        </div><br />

        {/* products */}
        {(view === 'Products') &&
          <React.Fragment>
            <div style={{ marginLeft: '10%' }}>
              Products:

              {(products) &&
                <React.Fragment>
                  {Object.keys(products).map(k => {
                    const lenSupplierList = products[k].suppliers_list.length
                    const lastSupplier = products[k].suppliers_list[lenSupplierList - 1]
                    return (
                      <React.Fragment>
                        <br />
                        <div style={{ marginLeft: '7%', display: 'flex' }}><br />
                          
                          {/* <div style={{ textDecoration: 'underline' }}>
                            Product {k}:
                          </div><br /> */}
                          
                          <div style={{ display: 'inline-block' }}>
                              {Object.keys(images).map(i => {
                                if (i === products[k].name) {
                                  return (
                                    <React.Fragment>
                                      <img
                                        style={{
                                          width: '350px',
                                          height: '350px'
                                        }}
                                        src={images[i]} />
                                    </React.Fragment>
                                  )
                                }
                              })}
                            </div>
                          
                          <div style={{ marginLeft: '5%', display: 'inline-block' }}>
                            <div>
                              {products[k].name}
                            </div><br />
                            
                            <div style={{ maxWidth: '60%'}}>
                              Description: {products[k].description}
                            </div><br />
                            
                            <div>
                              Suppliers:&nbsp;
                            
                              {Object.keys(products[k].suppliers_list).map(s => {
                                return (
                                  <React.Fragment>
                                    {(products[k].suppliers_list[s] !== lastSupplier) &&
                                      <React.Fragment>
                                        {products[k].suppliers_list[s]},&nbsp;
                                      </React.Fragment>
                                    }
                                    {(products[k].suppliers_list[s] === lastSupplier) &&
                                      <React.Fragment>
                                        {products[k].suppliers_list[s]}
                                      </React.Fragment>
                                    }
                                  </React.Fragment>
                                )
                              })}
                            </div><br />
                          </div>
                        </div>
                      </React.Fragment>
                    )
                  })}
                </React.Fragment>
              }
            </div>
          </React.Fragment>
        }

        {/* orders */}
        {(view === 'Orders') &&
          <React.Fragment>
            <div style={{ marginLeft: '15%' }}>
              Orders:
            </div><br />

            {(orders) &&
              <React.Fragment>
                {Object.keys(orders).map(o => {
                  return (
                    <React.Fragment>
                      <br />
                      <div style={{ marginLeft: '25%' }}>

                        <div style={{ textDecoration: 'underline' }}>
                          Order {o}:
                        </div>

                        <div style={{ marginLeft: '5%' }}>
                          <div>
                            Customer: {orders[o].customer}<br />
                          </div>

                          <div>
                            Order date: {orders[o].ordered_on.split('00')[0]}<br /><br />
                          </div>

                          <div>
                            Shipments: <br />
                          </div>

                          {Object.keys(orders[o].shipments).map(s => {
                            return (
                              <React.Fragment>
                                <br />
                                <div style={{ marginLeft: '5%' }}>
                                  Ships from: {orders[o].shipments[s].supplier}<br />
                                  Tracking number: <a href="">{orders[o].shipments[s].tracking_no}</a><br />
                                  Products in shipment:&nbsp;
                                  {orders[o].shipments[s].products.map(p => {
                                    const lenProducts = orders[o].shipments[s].products.length
                                    const lastProduct = orders[o].shipments[s].products[lenProducts - 1]
                                    return (
                                      <React.Fragment>
                                        {(p !== lastProduct) &&
                                          <React.Fragment>
                                            {p},&nbsp;
                                          </React.Fragment>
                                        }
                                        {(p === lastProduct) &&
                                          <React.Fragment>
                                            {p}
                                          </React.Fragment>
                                        }
                                      </React.Fragment>
                                    )
                                  })}
                                </div>
                              </React.Fragment>
                            )
                          })}
                        </div>
                      </div>
                      <br />
                    </React.Fragment>
                  )
                })}
              </React.Fragment>
            }
          </React.Fragment>
        }

        {/* footer */}
        <div
          style={{
            margin: '10% 0% 0% 0%',
            padding: '0% 0% 3% 0%',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center'
          }}
        >
          SpookyZephyrWarehouse LLC&nbsp;&nbsp;|&nbsp;&nbsp;
          Boston, MA&nbsp;&nbsp;|&nbsp;&nbsp;
          August - November&nbsp;&nbsp;|&nbsp;&nbsp;
          1-800-555-1111&nbsp;&nbsp;|&nbsp;&nbsp;
          <a href="http://localhost:3000/">SpookyZephyrWarehouse</a>
        </div>
      </div>

    </React.Fragment>
  )
}

export default App
