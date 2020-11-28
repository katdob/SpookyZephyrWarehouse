const getOrders = async () => {
  const returnOrders = await fetch(
    'http://127.0.0.1:5000/orders',
    {
      method: 'GET',
      cache: 'no-cache',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
        'x-requested-with': ''
      },
      redirect: 'follow',
      referrer: 'no-referrer',
      'Access-Control-Allow-Origin': 'http://localhost:3000'
    }
  ).then(response => response.json())

  return returnOrders
}
  
export default getOrders