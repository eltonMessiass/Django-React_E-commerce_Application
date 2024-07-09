import React from 'react'
import { FaShoppingBag } from "react-icons/fa";
import { CiSearch } from "react-icons/ci";

function Header() {
  return (
    <nav className='h-10 w-full'>
      <ul className='flex flex-row gap-10 font-medium justify-center'>
        <li>
          <a href="#">Laptops</a>
        </li>
        <li>
          <a href="#">Monitos</a>
        </li>
        <li>
          <a href="#">PC's</a>
        </li>
        <li>
          <a href="#">Phones</a>
        </li>
        <li>
          <a href="#">TV's</a>
        </li>
        <li>
          <a href="#">Suport</a>
        </li>
        <li>
          <a href="#">Acessories</a>
        </li>
        <li className='self-center cursor-pointer'>
          <CiSearch/>
        </li>
        
        <li className='self-center'>
          <a href="#"><FaShoppingBag/></a>
        </li>
      </ul>
    </nav>
  )
}

export default Header
