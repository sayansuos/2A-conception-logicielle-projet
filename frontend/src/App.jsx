import React, { useState } from "react";
import ChampionSearch from "./components/ChampionSearch";
import ChampionDetails from "./components/ChampionDetails";
import "./App.css";

const App = () => {
  const [champion, setChampion] = useState(null);

  return (
    <div className="app">
      <h1>League of Lilian</h1>
      <ChampionSearch setChampion={setChampion} />
      <ChampionDetails champion={champion} />
    </div>
  );
};

export default App;
