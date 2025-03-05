import React from "react";
import ChampionDetails from "./ChampionDetails";
import ItemDetails from "./ItemDetails";
import "../styles/BuildDetails.css";

const BuildDetails = ({ builds }) => {
  if (!builds || builds.length === 0) {
    return <p className="no-builds">No builds available.</p>;
  }

  return (
    <div className="build-details">
      {builds.map((build, index) => (
        <div key={index} className="build-card">
          <div className="build-id">
            <h3>Build #{index + 1}</h3>
          </div>

          {/* Conteneur des éléments du build : champion + items */}
          <div className="card-content">
            {/* Affichage du champion */}
            {build.champion && (
              <div className="champion-container">
                <ChampionDetails champion={build.champion} />
              </div>
            )}

            {/* Affichage des items */}
            <div className="items-container">
              {["item1", "item2", "item3", "item4", "item5"].map((itemKey, itemIndex) => {
                const item = build[itemKey];
                return item ? <ItemDetails key={itemIndex} item={item} /> : null;
              })}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default BuildDetails;
