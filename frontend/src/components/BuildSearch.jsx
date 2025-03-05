import React, { useState } from "react";
import "../styles/BuildSearch.css";
import axios from "axios";

const BuildSearch = ({ setBuild }) => {
  const handleSearch = async () => {
    try {
      // Utilisation du proxy défini dans vite.config.js
      const response = await axios.get(`/api/build/all`);
      console.log("Données reçues :", response.data);
      setBuild(response.data);
      console.log("✅ Builds mis à jour :", response.data);
    } catch (error) {
      console.error("Erreur lors de la récupération des builds :", error);
      alert("Build introuvable.");
    }
  };
};

export default BuildSearch;
