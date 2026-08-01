import { useState, useEffect } from "react";
import {createProduct,updateProduct} from "../api/productApi";

function AddProductForm({onProductAdded,editingProduct,onEditComplete}) {
    const [name, setName] = useState("");
    const [price, setPrice] = useState("");
    const [stock, setStock] = useState("");

    const productData = {
        name,
        price: Number(price),
        stock: Number(stock),
    };
    
    async function handleSubmit() {
        if (!name || !price || !stock) {
                alert("Please fill all fields.");
                return;
            }

        const isEditing = Boolean(editingProduct);

        const successCallback = isEditing
            ? onEditComplete
            : onProductAdded;

        try {
                const response = await (isEditing 
                ? updateProduct(editingProduct.id,productData) 
                : createProduct(productData) );
                    
                const data = await response.json();
                if (response.ok) {
                    successCallback();
                    if (!isEditing) {
                            setName("");
                            setPrice("");
                            setStock("");
                        }
                } else {
                    alert(data.detail || "Request Failed");
                }  
        } catch (error) {
            if (error.message === "Unauthorized") {
                alert("Session expired. Please login again.");
                // navigate to login or update app state
            }
        }     

}

    useEffect(() => {
        if (editingProduct) {
            setName(editingProduct.name);
            setPrice(editingProduct.price);
            setStock(editingProduct.stock);
        } else {
            setName("");
            setPrice("");
            setStock("");
        }
    }, [editingProduct]);


    return (
        <div className="card">
            <h2>
                {editingProduct ? "Edit Product" : "Add Product"}
            </h2>

            <form
                onSubmit={(e) => {
                    e.preventDefault();
                    handleSubmit();
                }}
            >
                <label>Product Name</label>
                <input
                    type="text"
                    placeholder="Enter Product Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <label>Price</label>
                <input
                    type="number"
                    placeholder=" Enter Price"
                    value={price}
                    onChange={(e) => setPrice(e.target.value)}
                />
                <label>Stock</label>
                <input
                    type="number"
                    placeholder="Enter Stock"
                    value={stock}
                    onChange={(e) => setStock(e.target.value)}
                />

                <button type="submit">
                    {editingProduct ? "Update Product" : "Add Product"}
                </button>
            </form>
        </div>
    );
}

export default AddProductForm;