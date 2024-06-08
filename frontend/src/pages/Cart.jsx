import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Cart() {
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState('');
  const [totals, setTotals] = useState({
    subtotal: 0,
    shipping: 0,
    tax: 0,
    total: 0,
  });

  const navigate = useNavigate();
  useEffect(() => {
    const getOrders = async () => {
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/store/orders/', {withCredentials: true});
        setOrders(res.data);
        calculateTotals(res.data);
      } catch (error) {
        setError('Error fetching orders');
        console.error('Error fetching orders:', error);
      }
    };
    getOrders();
  }, [navigate]);

  const calculateTotals = (orders) => {
    let subtotal = 0;
    orders.forEach((order) => {
      order.items.forEach((item) => {
        subtotal += item.price * item.quantity;
      });
    });
    const shipping = subtotal > 0 ? 5 : 0; // Simulação de custo de envio
    const tax = subtotal * 0.1; // Simulação de taxa de 10%
    const total = subtotal + shipping + tax;
    setTotals({ subtotal, shipping, tax, total });
  };

  const incrementQuantity = (orderId, itemId) => {
    const updatedOrders = orders.map((order) => {
      if (order.id === orderId) {
        order.items = order.items.map((item) => {
          if (item.id === itemId) {
            item.quantity += 1;
          }
          return item;
        });
      }
      return order;
    });
    setOrders(updatedOrders);
    calculateTotals(updatedOrders);
  };

  const decrementQuantity = (orderId, itemId) => {
    const updatedOrders = orders.map((order) => {
      if (order.id === orderId) {
        order.items = order.items.map((item) => {
          if (item.id === itemId && item.quantity > 1) {
            item.quantity -= 1;
          }
          return item;
        });
      }
      return order;
    });
    setOrders(updatedOrders);
    calculateTotals(updatedOrders);
  };

  const removeItem = (orderId, itemId) => {
    const updatedOrders = orders.map((order) => {
      if (order.id === orderId) {
        order.items = order.items.filter((item) => item.id !== itemId);
      }
      return order;
    }).filter(order => order.items.length > 0);
    setOrders(updatedOrders);
    calculateTotals(updatedOrders);
  };

  const addToFavorites = (itemId) => {
    // Lógica para adicionar item aos favoritos
    console.log(`Item ${itemId} added to favorites`);
  };

  return (
    <section className="bg-white py-8 antialiased dark:bg-gray-900 md:py-16">
      <div className="mx-auto max-w-screen-xl px-4 2xl:px-0">
        <h2 className="text-xl font-semibold text-gray-900 dark:text-white sm:text-2xl">Shopping Cart</h2>
        {error && <p className="text-red-500">{error}</p>}
        <div className="mt-6 sm:mt-8 md:gap-6 lg:flex lg:items-start xl:gap-8">
          <div className="mx-auto w-full flex-none lg:max-w-2xl xl:max-w-4xl">
            <div className="space-y-6">
              {orders.map((order) => (
                order.items.map((item) => (
                  <div key={item.id} className="rounded-lg border border-gray-200 bg-white p-4 shadow-sm dark:border-gray-700 dark:bg-gray-800 md:p-6">
                    <div className="space-y-4 md:flex md:items-center md:justify-between md:gap-6 md:space-y-0">
                      <a href="#" className="shrink-0 md:order-1">
                        <img className="h-20 w-20 dark:hidden" src="https://flowbite.s3.amazonaws.com/blocks/e-commerce/imac-front.svg" alt="imac image" />
                        <img className="hidden h-20 w-20 dark:block" src="https://flowbite.s3.amazonaws.com/blocks/e-commerce/imac-front-dark.svg" alt="imac image" />
                      </a>
                      <label htmlFor="counter-input" className="sr-only">Choose quantity:</label>
                      <div className="flex items-center justify-between md:order-3 md:justify-end">
                        <div className="flex items-center">
                          <button type="button" id="decrement-button" data-input-counter-decrement="counter-input" className="inline-flex h-5 w-5 shrink-0 items-center justify-center rounded-md border border-gray-300 bg-gray-100 hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700" onClick={() => decrementQuantity(order.id, item.id)}>
                            <svg className="h-2.5 w-2.5 text-gray-900 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 2">
                              <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M1 1h16" />
                            </svg>
                          </button>
                          <input type="text" id="counter-input" data-input-counter className="w-10 shrink-0 border-0 bg-transparent text-center text-sm font-medium text-gray-900 focus:outline-none focus:ring-0 dark:text-white" placeholder="" value={item.quantity} required readOnly />
                          <button type="button" id="increment-button" data-input-counter-increment="counter-input" className="inline-flex h-5 w-5 shrink-0 items-center justify-center rounded-md border border-gray-300 bg-gray-100 hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700" onClick={() => incrementQuantity(order.id, item.id)}>
                            <svg className="h-2.5 w-2.5 text-gray-900 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                              <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 1v16M1 9h16" />
                            </svg>
                          </button>
                        </div>
                        <div className="text-end md:order-4 md:w-32">
                          <p className="text-base font-bold text-gray-900 dark:text-white">${item.price}</p>
                        </div>
                      </div>
                      <div className="w-full min-w-0 flex-1 space-y-4 md:order-2 md:max-w-md">
                        <a href="#" className="text-base font-medium text-gray-900 hover:underline dark:text-white">{item.product}</a>
                        <div className="flex items-center gap-4">
                          <button type="button" className="inline-flex items-center text-sm font-medium text-gray-500 hover:text-gray-900 hover:underline dark:text-gray-400 dark:hover:text-white" onClick={() => addToFavorites(item.id)}>
                            <svg className="me-1.5 h-5 w-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                              <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12.01 6.001C6.5 1 1 8 5.782 13.001L12.011 20l6.23-7C23 8 17.5 1 12.01 6.002Z" />
                            </svg>
                            Add to Favorites
                          </button>
                          <button type="button" className="inline-flex items-center text-sm font-medium text-red-600 hover:underline dark:text-red-500" onClick={() => removeItem(order.id, item.id)}>
                            <svg className="me-1.5 h-5 w-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                              <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18 17.94 6M18 18 6.06 6" />
                            </svg>
                            Remove
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                ))
              ))}
            </div>
            <div className="hidden xl:mt-8 xl:block">
              <h3 className="text-2xl font-semibold text-gray-900 dark:text-white">People also bought</h3>
              <div className="mt-6 grid grid-cols-3 gap-4 sm:mt-8">
                {/* Suggested products code here */}
              </div>
            </div>
          </div>
          <div className="mx-auto mt-6 max-w-4xl flex-1 space-y-6 lg:mt-0 lg:w-full">
            <div className="space-y-4 rounded-lg border border-gray-200 bg-white p-4 shadow-sm dark:border-gray-700 dark:bg-gray-800 sm:p-6">
              <p className="text-xl font-semibold text-gray-900 dark:text-white">Order summary</p>
              <div className="space-y-4">
                <div className="flex items-center justify-between">
                  <p className="text-sm font-medium text-gray-900 dark:text-white">Subtotal</p>
                  <p className="text-sm font-medium text-gray-900 dark:text-white">${totals.subtotal.toFixed(2)}</p>
                </div>
                <div className="flex items-center justify-between">
                  <p className="text-sm font-medium text-gray-900 dark:text-white">Shipping estimate</p>
                  <p className="text-sm font-medium text-gray-900 dark:text-white">${totals.shipping.toFixed(2)}</p>
                </div>
                <div className="flex items-center justify-between">
                  <p className="text-sm font-medium text-gray-900 dark:text-white">Tax estimate</p>
                  <p className="text-sm font-medium text-gray-900 dark:text-white">${totals.tax.toFixed(2)}</p>
                </div>
                <div className="flex items-center justify-between">
                  <p className="text-sm font-medium text-gray-900 dark:text-white">Total</p>
                  <p className="text-sm font-medium text-gray-900 dark:text-white">${totals.total.toFixed(2)}</p>
                </div>
              </div>
              <button type="button" className="w-full rounded-md bg-blue-600 px-4 py-3 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
                Checkout
              </button>
            </div>
            <div className="rounded-lg border border-gray-200 bg-white p-4 shadow-sm dark:border-gray-700 dark:bg-gray-800 sm:p-6">
              <p className="text-base font-medium text-gray-900 dark:text-white">No shipping options available for your location.</p>
              <a href="#" className="mt-6 inline-flex text-sm font-medium text-blue-600 hover:underline dark:text-blue-500">Shipping policy</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Cart;
