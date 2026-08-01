
import useProducts from "../hooks/useProducts";
import { useState, useEffect } from "react";
import ProductList from "./ProductList";
import AddProductForm from "./AddProductForm";


function Dashboard() {

    const {
        products,
        loading,
        error,
        count,
        nextPage,
        previousPage,
        fetchProducts,
        removeProduct
    } = useProducts();
    const [editingProduct, setEditingProduct] = useState(null);
    const [search, setSearch] = useState("");
    const [currentPage, setCurrentPage] = useState(1);

 
    function handleEditProduct(product) {
        setEditingProduct(product);
    }
 
    async function onEditComplete() {
        setEditingProduct(null);
        await fetchProducts(search, currentPage);
    }    


    useEffect(() => {
            const timer = setTimeout(() => {
                fetchProducts(search, currentPage);
            }, 300);

            return () => clearTimeout(timer);
        }, [search, currentPage, fetchProducts]);  

    if (loading) {
            return <p>Loading products...</p>;
        }
    if (error) {
            return <p>{error}</p>;
        } 
 
        
    return(
    <div className="container">   

    <h1 className="dashboard-title">
        Vendor Management Dashboard
    </h1>     
            <AddProductForm 
    onProductAdded={() => fetchProducts(search, currentPage)}
    editingProduct={editingProduct}
    onEditComplete={onEditComplete} />


    <h2>Products ({count})</h2>

    <div className="search-container">
        <input
            type="text"
            placeholder="Search products..."
            value={search}
            onChange={(e) => {
                    setSearch(e.target.value);
                    setCurrentPage(1);
                }}
        />
    </div>


    {products.length === 0 ? (
        <p>No products found.</p>
        ) : (<ProductList products={products}
                onDelete={removeProduct} 
                onEdit={handleEditProduct}/> 
                        )}


    <div className="pagination">
            <button
                onClick={() => setCurrentPage((page) => page - 1)}
                disabled={!previousPage}
            >
                ◀ Previous
            </button>

            <span>Page {currentPage}</span>

            <button
                onClick={() => setCurrentPage((page) => page + 1)}
                disabled={!nextPage}
            >
                Next ▶
            </button>
        </div>                    
    </div>
    );

}

export default Dashboard;