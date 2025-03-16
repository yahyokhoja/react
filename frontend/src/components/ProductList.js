import React, { useEffect, useState } from 'react';

function ProductList() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/products') // Заменить на реальный эндпоинт
            .then(response => response.json())
            .then(data => setProducts(data))
            .catch(error => console.error('Ошибка загрузки данных:', error));
    }, []);

    return (
        <div>
            <h2>Список продуктов</h2>
            {products.length > 0 ? (
                <ul>
                    {products.map(product => (
                        <li key={product.id}>{product.name} - ${product.price}</li>
                    ))}
                </ul>
            ) : (
                <p>Нет доступных продуктов</p>
            )}
        </div>
    );
}

export default ProductList;