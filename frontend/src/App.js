import React, { useEffect, useState } from 'react';

function App() {
  const [users, setUsers] = useState([]);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5001/users")
      .then(res => res.json())
      .then(data => setUsers(data));
    fetch("http://localhost:5002/products")
      .then(res => res.json())
      .then(data => setProducts(data));
  }, []);

  return (
    <div>
      <h1>Three-Tier Microservices App</h1>
      <h2>Users:</h2>
      <ul>
        {users.map(u => <li key={u.id}>{u.name}</li>)}
      </ul>

      <h2>Products:</h2>
      <ul>
        {products.map(p => <li key={p.id}>{p.name}</li>)}
      </ul>
    </div>
  );
}

export default App;
