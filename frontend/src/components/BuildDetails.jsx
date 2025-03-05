import React, { useState } from "react";
import ChampionDetails from "./ChampionDetails";
import ItemDetails from "./ItemDetails";
import "../styles/BuildDetails.css";

const BuildDetails = ({ builds }) => {
  const [hoveredItem, setHoveredItem] = useState(null);

  if (!builds || builds.length === 0) {
    return <p className="no-builds">No builds available.</p>;
  }

  return (
    <div className="build-details">
      {builds.map((build, index) => (
        <div key={index} className="build-card">
          <h3 className="build-id">Build #{index + 1}</h3>
          
          <div className="card-content">
            {/* Affichage du champion */}
            <div className="champion-container">
              <ChampionDetails champion={build.champion} />
            </div>

            {/* Affichage des items à droite du champion */}
            <div className="items-container">
              {["item1", "item2", "item3", "item4", "item5"].map((itemKey, itemIndex) => {
                const item = build[itemKey];
                return (
                  item && (
                    <div
                      key={itemIndex}
                      className="item-wrapper"
                      onMouseEnter={() => setHoveredItem(item)}
                      onMouseLeave={() => setHoveredItem(null)}
                    >
                      <img src={item.image} alt={item.name} className="item-image" />
                      {hoveredItem === item && (
                        <div className="item-details-popup">
                          <ItemDetails item={item} />
                        </div>
                      )}
                    </div>
                  )
                );
              })}
            </div>
          </div>
        </div>
      ))}
    </div>

  );
};

export default BuildDetails;
