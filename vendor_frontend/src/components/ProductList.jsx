function ProductList({ products, onDelete, onEdit }) {

    if (products.length === 0) {
    return (
        <div className="card">
            <p>No products available.</p>
        </div>
    );
    }
    return (
        <table className="product-table">

            <thead>
                <tr>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Stock</th>
                    <th>Actions</th>
                </tr>
            </thead>

            <tbody>

                {products.map((product) => (

                    <tr key={product.id}>

                        <td>{product.name}</td>

                        <td>₹{Number(product.price).toLocaleString("en-IN")}</td>

                        <td>{product.stock} units</td>

                        <td>

                            <button
                                onClick={() => onEdit(product)}
                            >
                                Edit
                            </button>

                            <button
                                className="delete-btn"
                                onClick={() => {
                                    if (
                                        window.confirm(
                                            "Delete this product?"
                                        )
                                    ) {
                                        onDelete(product.id);
                                    }
                                }}
                            >
                                Delete
                            </button>

                        </td>

                    </tr>

                ))}

            </tbody>

        </table>
    );
}

export default ProductList;