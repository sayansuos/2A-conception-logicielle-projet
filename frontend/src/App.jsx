import React, { useState } from "react";
import ChampionSearch from "./components/ChampionSearch";
import ItemSearch from "./components/ItemSearch";
import ChampionDetails from "./components/ChampionDetails";
import ItemDetails from "./components/ItemDetails";
import "./App.css";

const App = () => {
  const [activePage, setActivePage] = useState("champion");
  const [champion, setChampion] = useState(null);
  const [item, setItem] = useState(null);
  const [user, setUser] = useState(null);

  return (
    <div className="app">
      <div className="title">
        <h1>League of Lilian</h1>
      </div>

      {/* Menu principal */}
      <div className="menu">
        <button onClick={() => setActivePage("champion")}>Find a Champion</button>
        <button onClick={() => setActivePage("item")}>Find an Item</button>
        <button onClick={() => setActivePage("best-champion")}>Find the best champion to play</button>
        <button onClick={() => setActivePage("save-build")}>Save a build</button>
        <button onClick={() => setActivePage("find-build")}>Find a build</button>
      </div>

      {/* Affichage en fonction du menu sélectionné */}
      {activePage === "champion" && (
        <>
          <ChampionSearch setChampion={setChampion} />
          <ChampionDetails champion={champion} />
        </>
      )}
      {activePage === "item" && (
        <>
          <ItemSearch setItem={setItem} />
          <ItemDetails item={item} />
        </>
      )}
      {/* Logique pour les nouveaux boutons */}
      {activePage === "best-champion" && (
        <div>
          <h2>Best Champion to Play</h2>
          {/* Contenu de la page "Best Champion" */}
        </div>
      )}
      {activePage === "save-build" && (
        <div>
          <h2>Save a Build</h2>
          {/* Contenu de la page "Save Build" */}
        </div>
      )}
      {activePage === "find-build" && (
        <div>
          <h2>Find a Build</h2>
          {/* Contenu de la page "Find Build" */}
        </div>
      )}
    </div>
  );
};

export default App;
