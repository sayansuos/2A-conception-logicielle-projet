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
      const response = await axios.get(`/api/champion/id_name/${searchTerm.toLowerCase()}`);
      console.log("Données reçues :", response.data);
      setChampion(response.data);
      console.log("✅ Champion mis à jour :", response.data);

    } catch (error) {
      console.error("Erreur lors de la récupération du champion :", error);
      alert("Champion introuvable.");
    }
  };

  return (
    <div className="champion-search">
      <label htmlFor="search-input">Find a Champion :</label>
      <div className="search-container">
        <input
          id="search-input"
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Type a champion's ID or name"
        />
        <button id="search-button" onClick={handleSearch}>
          Search
        </button>
      </div>
    </div>
  );
};

export default ChampionSearch;
