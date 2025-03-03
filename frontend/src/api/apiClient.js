import axios from "axios";

const apiUrl = import.meta.env.VITE_API_URL;

export default axios.create({
  baseURL: "https://lol.kub.sspcloud.fr",
});