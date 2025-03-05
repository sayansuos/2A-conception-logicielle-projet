import React, { useState } from "react";
import "../styles/ChampionSearch.css";
import axios from "axios";

const UserSearch = ({ setUser }) => {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = async () => {
    if (!searchTerm.trim()) {
      alert("Veuillez entrer un nom d'utilisateur.");
      return;
    }

    try {
      // Utilisation du proxy défini dans vite.config.js
      const response = await axios.get(`/api/user/${searchTerm.toLowerCase()}`);
      console.log("Données reçues :", response.data);
      setUser(response.data);
      console.log(" Utilisateur mis à jour :", response.data);

    } catch (error) {
      console.error("Erreur lors de la récupération de l'utilisateur :", error);
      alert("Utilisateur introuvable.");
    }
  };

  return (
    <div className="utilisateur-search">
      <label htmlFor="search-input">Find an user :</label>
      <div className="search-container">
        <input
          id="search-input"
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Type an user's pseudo."
        />
        <button id="search-button" onClick={handleSearch}>
          Search
        </button>
      </div>
    </div>
  );
};

export default UserSearch;
