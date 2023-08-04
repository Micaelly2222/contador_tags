import axios from 'axios';

// URL base da API
const API_BASE_URL = 'http://localhost:8000';

// Instância do Axios com a URL base da API
const axiosInstance = axios.create({
  baseURL: API_BASE_URL,
});

export default axiosInstance;
