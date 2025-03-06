import React, { useState } from "react";
import "../styles/ItemSearch.css";
import axios from "axios";

const ItemSearch = ({ setItem }) => {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = async () => {
    if (!searchTerm.trim()) {
      alert("Veuillez entrer un nom d'item.");
      return;
    }

    try {
      const response = await axios.get(`/api/item/id_name/${searchTerm.toLowerCase()}`);
      console.log("Données reçues :", response.data);
      setItem(response.data);
      console.log("✅ Item mis à jour :", response.data);

    } catch (error) {
      console.error("Erreur lors de la récupération de l'item :", error);
      alert("Item introuvable.");
    }
  };

  return (
    <div className="item-search">  
      <label htmlFor="search-input">Find an Item :</label>
      <div className="search-container">
        <input
          id="search-input"
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Type an item's name."
        />
        <button id="search-button" onClick={handleSearch}>
          Search
        </button>
      </div>
    </div>
  );
};

export default ItemSearch;
