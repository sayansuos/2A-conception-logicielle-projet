import React from "react";
import "../styles/ChampionDetails.css";
import typeColors from "../styles/typeColors"; // Import des couleurs

const ChampionDetails = ({ champion }) => {
  if (!champion) return <p>Aucun champion sélectionné</p>;

  const renderDifficulty = (difficulty) => {
    return "⭐".repeat(difficulty) + "☆".repeat(5 - difficulty);
  };

  return (
    <div className="champion-details">
      <h2 className="champion-name">{champion.name}</h2>

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
        <p><strong>Difficulté :</strong> {renderDifficulty(champion.info.difficulty)}</p>
      </div>

      <div className="champion-stats">
        <h3>Statistiques</h3>
        <p><strong>HP :</strong> {champion.stats.hp}</p>
        <p><strong>Mana :</strong> {champion.stats.mp}</p>
        <p><strong>Armure :</strong> {champion.stats.armor}</p>
        <p><strong>Résistance Magique :</strong> {champion.stats.spellblock}</p>
        <p><strong>Vitesse :</strong> {champion.stats.movespeed}</p>
        <p><strong>AD :</strong> {champion.stats.attackdamage}</p>
        <p><strong>AS :</strong> {champion.stats.attackspeed}</p>
      </div>
    </div>
  );
};

export default ChampionDetails;
