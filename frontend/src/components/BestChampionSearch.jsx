import React, { useState } from "react";
import "../styles/BestChampionSearch.css";
import axios from "axios";

const BestChampionSearch = ({ setBestChampion }) => {
  const [searchTermRole, setSearchTermRole] = useState("");
  const [searchTermTeam, setSearchTermTeam] = useState("");
  const [searchTermEnnemy, setSearchTermEnnemy] = useState("");
  const [searchTermBan, setSearchTermBan] = useState("");

  const handleSearch = async () => {
    if (!searchTermRole.trim()) {
      alert("Please enter your role.");
      return;
    }

    try {
      const params = new URLSearchParams();

      // Ajout du rôle
      params.append("role", searchTermRole.trim());

      // Séparation des teammates avec des virgules
      if (searchTermTeam.trim()) {
        searchTermTeam.split(",").forEach(teammate =>
          params.append("teammates", teammate.trim())
        );
      }

      // Séparation des ennemis avec des virgules
      if (searchTermEnnemy.trim()) {
        searchTermEnnemy.split(",").forEach(ennemy =>
          params.append("ennemies", ennemy.trim())
        );
      }

      // Séparation des bans avec des virgules
      if (searchTermBan.trim()) {
        searchTermBan.split(",").forEach(ban =>
          params.append("bans", ban.trim())
        );
      }

      // Envoi de la requête avec les paramètres
      const response = await axios.get(`/api/champion/besttoplay?${params.toString()}`);
      setBestChampion(response.data);
      console.log("✅ Best Champions:", response.data);
    } catch (error) {
      console.error("Erreur lors de la récupération du champion :", error);
      alert("An error occurred while fetching champions.");
    }
  };

  return (
    <div className="best-champion-search">
      <label htmlFor="search-input">Find the best champions to play :</label>
      <div className="search-container">
        <input
          id="search-input-role"
          type="text"
          value={searchTermRole}
          onChange={(e) => setSearchTermRole(e.target.value)}
          placeholder="Type your role (TOP, JGL, MID, BOT or SUPP)"
        />
        <input
          id="search-input-team"
          type="text"
          value={searchTermTeam}
          onChange={(e) => setSearchTermTeam(e.target.value)}
          placeholder="Champions picked by your team (separate with commas)"
        />
        <input
          id="search-input-ennemy"
          type="text"
          value={searchTermEnnemy}
          onChange={(e) => setSearchTermEnnemy(e.target.value)}
          placeholder="Champions picked by the enemy team (separate with commas)"
        />
        <input
          id="search-input-ban"
          type="text"
          value={searchTermBan}
          onChange={(e) => setSearchTermBan(e.target.value)}
          placeholder="Champions banned (separate with commas)"
        />
        <button id="search-button" onClick={handleSearch}>
          Search
        </button>
      </div>
    </div>
  );
};

export default BestChampionSearch;
