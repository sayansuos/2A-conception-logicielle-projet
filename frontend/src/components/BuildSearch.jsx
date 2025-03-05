import React, { useEffect } from "react";
import axios from "axios";

const BuildSearch = ({ setBuild }) => {
  useEffect(() => {
    const fetchBuilds = async () => {
      try {
        const response = await axios.get(`/api/build/all`);
        console.log("Données reçues :", response.data);
        setBuild(response.data);
      } catch (error) {
        console.error("Erreur lors de la récupération des builds :", error);
        alert("Build introuvable.");
      }
    };

    fetchBuilds();
  }, [setBuild]); // useEffect s'exécute quand `setBuild` change (au premier rendu)

  return null; // On n'affiche rien puisque les builds sont gérés par `BuildDetails`
};

export default BuildSearch;
