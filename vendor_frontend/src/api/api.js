const BASE_URL = import.meta.env.VITE_API_URL;

// Request a new access token using the refresh token
async function refreshAccessToken() {
    const refresh = localStorage.getItem("refresh");

    if (!refresh) {
        return null;
    }

    const response = await fetch(
        `${BASE_URL}/api/token/refresh/`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                refresh: refresh,
            }),
        }
    );

    if (!response.ok) {
        return null;
    }

    const data = await response.json();

    localStorage.setItem("token", data.access);

    return data.access;
}


async function apiFetch(endpoint, options = {}) {

    const token = localStorage.getItem("token");

    const headers = {
        "Content-Type": "application/json",
        ...options.headers,
    };

    if (token) {
        headers.Authorization = `Bearer ${token}`;
    }

    const response = await fetch(
        `${BASE_URL}${endpoint}`,
        {
            ...options,
            headers,
        }
    );


    if (response.status === 401) {

        const newAccessToken = await refreshAccessToken();

        if (newAccessToken) {

            headers.Authorization = `Bearer ${newAccessToken}`;

            const retryResponse = await fetch(
                `${BASE_URL}${endpoint}`,
                {
                    ...options,
                    headers,
                }
            );

            return retryResponse;
        }

        localStorage.removeItem("token");
        localStorage.removeItem("refresh");

        throw new Error("Session expired. Please log in again.");
    }

    return response;
}

export default apiFetch;