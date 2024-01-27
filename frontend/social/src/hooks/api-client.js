import axios from "axios";

export default function useApi() {

    const apiClient = axios.create({
        baseURL: process.env.REACT_APP_API_BASE_URL
    });

    apiClient.interceptors.request.use(config => {
        console.log(config.url)
        if (['/auth/signup', '/auth/signin'].includes(config.url)) return config;

        return {
            ...config, 
            headers: {
                Authorization: `Bearer ${sessionStorage.getItem('token')}`,
                "Content-Type": "applicaiton/json"
            }
        }
    })

    return apiClient;

}