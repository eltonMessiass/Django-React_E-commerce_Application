import React, { useEffect, useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import axios from 'axios';
import { Link } from 'react-router-dom';
import Pagination from '../components/Pagination';

function ProductListing() {
  const [product, setProduct] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getProducts = async () => {
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/store/products/');
        setProduct(res.data);
        console.log(res.data);
      } catch (error) {
        setError(error);
      }
    };
    getProducts();
  }, []);

  return (
    <div className='flex flex-col bg-black'>
      <Header />

      <div className='overflow-hidden mt-3'>
        <div className='grid lg:grid-cols-4 md:grid-cols-2 px-6 mt-20 w-full items-center justify-center'>
          {product.map((product) => (
            <div key={product.id} className='flex flex-col h-[400px] w-auto max-w-sm m-2 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700'>
              <Link className='w-full' to={`/products/${product.id}/`}>
                <img className='p-2 rounded-t-lg h-fit' src={`http://localhost:8000/${product.image_url}`} alt={product.name} />
              </Link>
              <div className='px-5 pb-5'>
                <h5 className='text-xl font-semibold tracking-tight text-gray-900 dark:text-white truncate'>{product.name}</h5>
                <div className='flex items-center mt-2.5 mb-5'>
                  <div className='flex items-center space-x-1 rtl:space-x-reverse'>
                    {[...Array(5)].map((_, i) => (
                      <svg key={i} className='w-4 h-4 text-yellow-300' aria-hidden='true' xmlns='http://www.w3.org/2000/svg' fill='currentColor' viewBox='0 0 22 20'>
                        <path d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z' />
                      </svg>
                    ))}
                  </div>
                  <span className='bg-blue-100 text-blue-800 text-xs font-semibold px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800 ms-3'>5.0</span>
                </div>
                <div className='flex items-center justify-between'>
                  <span className='text-3xl font-bold text-gray-900 dark:text-white'>${product.price}</span>
                  <a href='#' className='text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800'>Add to cart</a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      <Pagination />

      <Footer />
    </div>
  );
}

export default ProductListing;
