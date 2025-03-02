import React, { useState } from "react";
import axios from "axios";
import API from "../api/apiClient.js";

function ChampionSearch({ setChampion }) {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = async () => {
      if (!searchTerm.trim()) {
        alert("Veuillez entrer un nom ou un ID de Champion.");
        return;
      }
  
      try {
        const response = await API.get(`champion/${searchTerm.toLowerCase()}`);
        setChampion(response.data);
      } catch (error) {
        const errorMessage = error.response
          ? `Erreur ${error.response.status}: ${
              error.response.data || "Erreur inconnue"
            }`
          : "Erreur de réseau";
        alert(errorMessage);
      }
    };

  return (
    <div className="champion-search">
      <label htmlFor="search-input">Rechercher un Champion :</label>
      <div className="search-container">
        <input
          id="search-input"
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Entrez un nom ou un ID"
        />
        <button id="search-button" onClick={handleSearch}>
          Chercher
        </button>
      </div>
    </div>
  );
}

export default ChampionSearch