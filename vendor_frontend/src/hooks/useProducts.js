import { useState,useCallback } from "react";
import { getProducts, deleteProduct } from "../api/productApi";

function useProducts() {

    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [nextPage, setNextPage] = useState(null);
    const [previousPage, setPreviousPage] = useState(null);
    const [count, setCount] = useState(0);

    const fetchProducts = useCallback(async (search = "", page = 1) => {

        setLoading(true);
        setError("");
        try {
            const data = await getProducts(search,page);
            setProducts(data.results);
            setNextPage(data.next);
            setPreviousPage(data.previous);
            setCount(data.count);

        } catch (error) {
            setError(error.message);
            if (error.message === "Unauthorized") {
                alert("Session expired. Please login again.");
                // navigate to login or update app state
            }
        } finally {
            setLoading(false);
        }
    },[]);

    const removeProduct = useCallback(async (productId) => {

        try {
            const response = await deleteProduct(productId);

            if (response.ok) {
                await fetchProducts();
            }
        } catch (error) {
            if (error.message === "Unauthorized") {
                alert("Session expired. Please login again.");
                // navigate to login or update app state
            }
        }        
    }  ,[fetchProducts]);   

    return {
        products,
        loading,
        error,
        nextPage,
        previousPage,
        count,
        fetchProducts,
        removeProduct,
    };
}

export default useProducts;