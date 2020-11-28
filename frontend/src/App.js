import React, { useState, useEffect } from 'react'
import getOrders from './components/getOrders.js'
import getProducts from './components/getProducts.js'

const App = () => {
  const [view, setView] = useState('products')
  const [products, setProducts] = useState()  // eslint-disable-line
  const [orders, setOrders] = useState()  // eslint-disable-line

  const updateProducts = async () => {
    const productsApiCall = await getProducts()
    console.log(productsApiCall)
    setProducts(() => productsApiCall)
  }

  const updateOrders = async () => {
    const ordersApiCall = await getOrders()
    console.log(ordersApiCall)
    setProducts(() => ordersApiCall)
  }

  useEffect(() => {
    if (orders === null) {
      updateOrders()
    }
    if (products === null) {
      updateProducts()
    }
  }, [updateOrders, updateProducts])

  return (
    <React.Fragment>
      <div>

        {/* products */}
        {(view === 'products') &&
          <React.Fragment>
            <div
              onClick={() => {
                setView('orders')
              }}
            >
              Products:

              {(products) &&
                <React.Fragment>
                  <div>
                    {/* {products.keys().map(k => {
                      console.log(k)
                      return (
                        <React.Fragment>
                          <div>
                            {k}
                          </div>
                        </React.Fragment>
                      )
                    })} */}
                  </div>
                </React.Fragment>
              }
            </div>
          </React.Fragment>
        }

        {/* orders */}
        {(view === 'orders') &&
          <React.Fragment>
            <div
              onClick={() => {
                setView('products')
              }}
            >
              Orders:

              {(orders) &&
                <React.Fragment>
                  <div>
                    {/* {Object(orders).keys().map(k => {
                      console.log(k)
                      return (
                        <React.Fragment>
                          <div>
                            {k}
                          </div>
                        </React.Fragment>
                      )
                    })} */}
                  </div>
                </React.Fragment>
              }
            </div>
          </React.Fragment>
        }
      </div>

    </React.Fragment>
  )
}

export default App
