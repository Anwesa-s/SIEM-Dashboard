import axios from "axios";

const API = axios.create({
  baseURL: "https://siem-dashboard-qz46.onrender.com"
});

export default API;