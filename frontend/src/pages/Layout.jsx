import React from 'react'
import Header from '../components/Header'
import { Outlet } from 'react-router-dom'
import Footer from '../components/Footer'


function Layout() {
  return (
   <div>
        <Header />
        <main className='min-h-[calc(100vh-60px)] grid place-content-center'><Outlet /></main>
        <Footer />
   </div>
  )
}

export default Layout
