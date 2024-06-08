import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ProductListing from './pages/ProductListing'
import ProductDetail from './pages/ProductDetail'
import './App.css'
import Cart from './pages/Cart'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<ProductListing />} />
        <Route path='/products/:id/' element={<ProductDetail />} />
        <Route path='/cart' element={<Cart />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
