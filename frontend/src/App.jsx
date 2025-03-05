import React, { useState } from "react";
import ChampionSearch from "./components/ChampionSearch";
import ItemSearch from "./components/ItemSearch";
import BestChampionSearch from "./components/BestChampionSearch";
import BuildSearch from "./components/BuildSearch";
import ChampionDetails from "./components/ChampionDetails";
import ItemDetails from "./components/ItemDetails";
import BestChampionDetails from "./components/BestChampionDetails";
import "./App.css";
import BuildDetails from "./components/BuildDetails";

const App = () => {
  const [activePage, setActivePage] = useState("champion");
  const [champion, setChampion] = useState(null);
  const [item, setItem] = useState(null);
  const [bestchampion, setBestChampion] = useState(null);
  const [builds, setBuilds] = useState([]); // Gérer l'état des builds

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
        <button onClick={() => setActivePage("find-build")}>See all Builds</button>
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

      {activePage === "best-champion" && (
        <>
          <BestChampionSearch setBestChampion={setBestChampion} />
          <BestChampionDetails champions={bestchampion} />
        </>
      )}

      {activePage === "save-build" && (
        <div>
          <h2>Save a Build</h2>
          {/* Contenu de la page "Save Build" */}
        </div>
      )}

      {activePage === "find-build" && (
        <div>
          <BuildSearch setBuild={setBuilds} />
          <BuildDetails builds={builds} /> {/* Affichage des builds ici */}
        </div>
      )}
    </div>
  );
};

export default App;
