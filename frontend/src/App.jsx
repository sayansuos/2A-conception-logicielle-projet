import React, { useState } from "react";
import ChampionSearch from "./components/ChampionSearch";
import ItemSearch from "./components/ItemSearch";
import BestChampionSearch from "./components/BestChampionSearch";
import BuildSearch from "./components/BuildSearch";
import BuildSave from "./components/BuildSave";
import UserCreate from "./components/UserCreate"
import MyBuildSearch from "./components/MyBuildSearch";
import ChampionDetails from "./components/ChampionDetails";
import ItemDetails from "./components/ItemDetails";
import BestChampionDetails from "./components/BestChampionDetails";
import BuildDetails from "./components/BuildDetails";
import "./App.css";

const App = () => {
  const [activePage, setActivePage] = useState("best-champion");
  const [champion, setChampion] = useState(null);
  const [item, setItem] = useState(null);
  const [bestchampion, setBestChampion] = useState(null);
  const [builds, setBuilds] = useState([]);
  const [build, setBuild] = useState(null);
  const [user, setUser] = useState(null);
  const [mybuilds, setMyBuilds] = useState([]);

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
        <button onClick={() => setActivePage("save-build")}>Save a Build</button>
        <button onClick={() => setActivePage("find-build")}>See all Builds</button>
        <button onClick={() => setActivePage("find-my-build")}>See my Builds</button>
        <button onClick={() => setActivePage("create-user")}>Create an User</button>
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
          <BuildSave setBuild={setBuild} />
        </div>
      )}

      {activePage === "find-build" && (
        <div>
          <BuildSearch setBuild={setBuilds} />
          <BuildDetails builds={builds} /> 
        </div>
      )}

      {activePage === "find-my-build" && (
        <div>
          <MyBuildSearch setMyBuilds={setMyBuilds} />
          <BuildDetails builds={mybuilds} /> 
        </div>
      )}


      {activePage === "create-user" && (
        <div>
          <UserCreate setUser={setUser} />
        </div>
      )}
    </div>
  );
};

export default App;
