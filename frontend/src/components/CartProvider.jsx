import React, { useEffect, useState, createContext } from 'react';

// Crie o contexto do carrinho
export const CartContext = createContext();

export default function CartProvider({ children }) {
  const [cartItems, setCartItems] = useState([]);

  const addToCart = (item) => {
    console.log("Add to cart: ", item)
    const isItemInCart = cartItems.find((cartItem) => cartItem.id === item.id);

    if (isItemInCart) {
      setCartItems(
        cartItems.map((cartItem) =>
          cartItem.id === item.id
            ? { ...cartItem, quantity: cartItem.quantity + 1 }
            : cartItem
        )
      );
    } else {
    //   setCartItems([...cartItems, { ...item, quantity: 1 }]);
    setCartItems((prevItems) => [...prevItems, { ...item, quantity: 1 }]);
      console.log("Novo item adicionado:", cartItems); // Log para depuração
    }
  };

  return (
    <CartContext.Provider value={{ cartItems, addToCart }}>
      {children}
    </CartContext.Provider>
  );
}


