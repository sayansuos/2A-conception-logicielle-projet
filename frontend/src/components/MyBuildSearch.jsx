import React, { useState } from "react";
import "../styles/MyBuildSearch.css";
import axios from "axios";

const MyBuildSearch = ({ setMyBuilds }) => {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = async () => {
    if (!searchTerm.trim()) {
      alert("Please type an user's pseudo.");
      return;
    }

    try {
      const response = await axios.get(`/api/build/user?user_pseudo=${searchTerm.toLowerCase()}`);
      console.log("Données reçues :", response.data);
      setMyBuilds(response.data);
      console.log("✅ Builds mis à jour :", response.data);
    
      setSearchTerm("");

    } catch (error) {
      console.error("Erreur lors de la récupération du build :", error);
      alert("Build introuvable.");
    }
  };

  return (
    <div className="my-build-search">
      <label htmlFor="search-input">See my Builds :</label>
      <div className="search-container">
        <input
          id="search-input"
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Type your user's pseudo."
        />
        <button id="search-button" onClick={handleSearch}>
          Search
        </button>
      </div>
    </div>
  );
};

export default MyBuildSearch;
