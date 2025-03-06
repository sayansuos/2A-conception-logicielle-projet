import React from "react";
import ChampionDetails from "./ChampionDetails";
import "../styles/BestChampionDetails.css";

const BestChampionDetails = ({ champions, language = "en" }) => {
  if (!champions || champions.length === 0) {
    return (
      <p className="no-champion">
        {language === "fr" ? "Aucun champion trouvé." : "No champions found."}
      </p>
    );
  }

  return (
    <div className="best-champion-details">
      <h2>{language === "fr" ? "Meilleurs champions à jouer" : "Best Champions to Play"}</h2>
      <div className="champion-list">
        {champions.map((champion) => (
          <ChampionDetails key={champion.champ_id} champion={champion} language={language} />
        ))}
      </div>
    </div>
  );
};

export default BestChampionDetails;
