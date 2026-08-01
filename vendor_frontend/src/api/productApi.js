import apiFetch from "./api";

export async function getProducts(search = "",page = 1) {
    const response = await apiFetch(
        `/api/products/?search=${encodeURIComponent(search)}&page=${page}`
    );

    return response.json();
}

export async function createProduct(productData) {
    return await apiFetch("/api/products/", {
        method: "POST",
        body: JSON.stringify(productData),
    });
}

export async function updateProduct(productId, productData) {
    return await apiFetch(`/api/products/${productId}/`, {
        method: "PATCH",
        body: JSON.stringify(productData),
    });
}

export async function deleteProduct(productId) {
    return await apiFetch(`/api/products/${productId}/`, {
        method: "DELETE",
    });
}