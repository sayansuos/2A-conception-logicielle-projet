import React from "react";
import "../styles/ItemDetails.css";

const parseDescription = (description) => {
  if (!description) return "Pas de description disponible.";

  return description
    .replace(/<\/?mainText>/g, "")
    .replace(/<\/?stats>/g, "")
    .replace(/<\/?passive>/g, "")
    .replace(/<\/?OnHit>/g, "")
    .replace(/<\/?healing>/g, "")
    .replace(/<\/?gold>/g, "")
    .replace(/<\/?attention>/g, "")
    .replace(/<br>/g, "<br/>");
};

const ItemDetails = ({ item, language = "fr" }) => {
  if (!item) {
    return <p className="no-item">No item selected.</p>;
  }

  return (
    <div className="item-details">
      <h2 className="item-name">{item.name} #{item.item_id}</h2>

      <div className="item-image-container">
        <img src={item.image} alt={item.name} className="item-image" />
      </div>

      <p className="item-description" dangerouslySetInnerHTML={{ __html: parseDescription(item.description) }}></p>

      <div className="item-roles">
        {item.tags.map((tag, index) => (
          <span key={index} className="item-chip">
            {tag}
          </span>
        ))}
      </div>
    </div>
  );
};

export default ItemDetails;
