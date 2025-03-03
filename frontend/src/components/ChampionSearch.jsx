import React, { useState } from "react";
import "../styles/ChampionSearch.css";
import axios from "axios";

const ChampionSearch = ({ setChampion }) => {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = async () => {
    if (!searchTerm.trim()) {
      alert("Veuillez entrer un nom de champion.");
      return;
    }

    try {
      // Utilisation du proxy défini dans vite.config.js
      const response = await axios.get(`/api/champion/name/${searchTerm.toLowerCase()}`);
      setChampion(response.data);
    } catch (error) {
      console.error("Erreur lors de la récupération du champion :", error);
      alert("Champion introuvable.");
    }
  };

  return (
    <div className="champion-search">
      <label htmlFor="search-input">Rechercher un champion :</label>
      <div className="search-container">
        <input
          id="search-input"
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Entrez un nom"
        />
        <button id="search-button" onClick={handleSearch}>
          Chercher
        </button>
      </div>
    </div>
  );
};

export default ChampionSearch;
