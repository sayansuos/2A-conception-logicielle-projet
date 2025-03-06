import React, { useState } from "react";
import axios from "axios";
import "../styles/BuildSave.css";

const BuildSave = () => {
  const [saveChampion, setSaveChampion] = useState("");
  const [saveItem1, setSaveItem1] = useState("");
  const [saveItem2, setSaveItem2] = useState("");
  const [saveItem3, setSaveItem3] = useState("");
  const [saveItem4, setSaveItem4] = useState("");
  const [saveItem5, setSaveItem5] = useState("");
  const [saveUser, setSaveUser] = useState("");

  const handleSearch = async () => {
    if (
      !saveChampion ||
      !saveItem1 ||
      !saveItem2 ||
      !saveItem3 ||
      !saveItem4 ||
      !saveItem5 ||
      !saveUser
    ) {
      alert("Please fill every detail.");
      return;
    }

    try {
      const params = new URLSearchParams();
      params.append("champion_name", saveChampion);
      params.append("item1_name", saveItem1);
      params.append("item2_name", saveItem2);
      params.append("item3_name", saveItem3);
      params.append("item4_name", saveItem4);
      params.append("item5_name", saveItem5);
      params.append("pseudo", saveUser);

      const url = `/api/build/create?${params.toString()}`;

      const response = await axios.post(url, {
        champion_name: saveChampion,
        item1_name: saveItem1,
        item2_name: saveItem2,
        item3_name: saveItem3,
        item4_name: saveItem4,
        item5_name: saveItem5,
        pseudo: saveUser
      });

      console.log("Build saved successfully:", response.data);
      alert("Build saved successfully!");

      setSaveChampion("");
      setSaveItem1("");
      setSaveItem2("");
      setSaveItem3("");
      setSaveItem4("");
      setSaveItem5("");
      setSaveUser("");
    } catch (error) {
      console.error("Error while saving the build:", error);
      alert("An error occurred while saving the build.");
    }
  };

  return (
    <div className="build-save">
      <label htmlFor="save-input">Save a new Build :</label>
      <div className="save-container">
        <input
          id="save-champion"
          type="text"
          value={saveChampion}
          onChange={(e) => setSaveChampion(e.target.value)}
          placeholder="Type the champion's name"
        />
        <input
          id="save-item1"
          type="text"
          value={saveItem1}
          onChange={(e) => setSaveItem1(e.target.value)}
          placeholder="Type the 1st item's name"
        />
        <input
          id="save-item2"
          type="text"
          value={saveItem2}
          onChange={(e) => setSaveItem2(e.target.value)}
          placeholder="Type the 2nd item's name"
        />
        <input
          id="save-item3"
          type="text"
          value={saveItem3}
          onChange={(e) => setSaveItem3(e.target.value)}
          placeholder="Type the 3rd item's name"
        />
        <input
          id="save-item4"
          type="text"
          value={saveItem4}
          onChange={(e) => setSaveItem4(e.target.value)}
          placeholder="Type the 4th item's name"
        />
        <input
          id="save-item5"
          type="text"
          value={saveItem5}
          onChange={(e) => setSaveItem5(e.target.value)}
          placeholder="Type the 5th item's name"
        />
        <input
          id="save-user"
          type="text"
          value={saveUser}
          onChange={(e) => setSaveUser(e.target.value)}
          placeholder="Type your user's pseudo"
        />

        <button id="save-button" onClick={handleSearch}>
          Save
        </button>
      </div>
    </div>
  );
};

export default BuildSave;
