import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ProductListing from './pages/ProductListing'
import ProductDetail from './pages/ProductDetail'
import './App.css'
import Cart from './pages/Cart'
import Login from './pages/Login'
import ProtectedRoute from './components/ProtectedRoute'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/login' element={<Login />} />
        
        <Route path='/' element={<ProtectedRoute><ProductListing /></ProtectedRoute>} />
        <Route path='/products/:id/' element={<ProductDetail />} />
        <Route path='/cart' element={<Cart />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
