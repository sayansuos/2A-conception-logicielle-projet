import React from "react";
import "../styles/ChampionDetails.css";
import typeColors from "../styles/typeColors";

const ChampionDetails = ({ champion, language = "en" }) => {
  if (!champion) {
    return (
      <p className="no-champion">
        {language === "fr" ? "Aucun champion sélectionné." : "No champion selected."}
      </p>
    );
  }

  // Sécurise difficulty pour éviter l'erreur
  const renderDifficulty = (difficulty) => {
    const validDifficulty = Math.max(0, Math.min(difficulty, 5));
    return "⭐".repeat(validDifficulty) + "☆".repeat(5 - validDifficulty);
  };

  return (
    <div className="champion-details">
      <h2 className="champion-name">{champion.name} #{champion.champ_id}</h2>

      <div className="champion-image-container">
        <img src={champion.image} alt={champion.name} className="champion-image" />
      </div>

      <p className="champion-blurb">{champion.blurb}</p>

      <div className="champion-roles">
        {champion.tags.map((tag, index) => (
          <span
            key={index}
            className="role-chip"
            style={{ backgroundColor: typeColors[tag] || typeColors.Default }}
          >
            {tag}
          </span>
        ))}
      </div>

      <div className="champion-attributes">
        <p>
          <strong>{language === "fr" ? "Difficulté" : "Difficulty"} :</strong> {renderDifficulty(champion.info.difficulty)}
        </p>
      </div>

      <div className="champion-stats">
        <h3>{language === "fr" ? "Statistiques" : "Statistics"}</h3>
        <p><strong>{language === "fr" ? "Points de vie" : "HP"} :</strong> {champion.stats.hp}</p>
        <p><strong>{language === "fr" ? "Attaque" : "Attack"} :</strong> {champion.info.attack}</p>
        <p><strong>{language === "fr" ? "Défense" : "Defense"} :</strong> {champion.info.defense}</p>
        <p><strong>{language === "fr" ? "Magie" : "Magic"} :</strong> {champion.info.magic}</p>
      </div>
    </div>
  );
};

export default ChampionDetails;
