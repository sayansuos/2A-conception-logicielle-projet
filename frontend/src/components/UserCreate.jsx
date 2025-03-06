import React, { useState } from "react";
import axios from "axios";
import "../styles/UserCreate.css";

const UserCreate = () => {
  const [createPseudo, setCreatePseudo] = useState("");
  const [createPwd, setCreatePwd] = useState("");


  const handleSearch = async () => {
    if (
      !createPseudo ||
      !createPwd 
    ) {
      alert("Please fill every detail.");
      return;
    }

    try {
      const params = new URLSearchParams();
      params.append("pseudo", createPseudo);
      params.append("pwd", createPseudo);

      const url = `/api/login/create?${params.toString()}`;

      const response = await axios.post(url, {
        pseudo: createPseudo,
        pwd: createPwd
      });

      console.log("User created successfully:", response.data);
      alert("User created successfully!");

      // Réinitialiser les champs du formulaire après l'envoi
      setCreatePseudo("");
      setCreatePwd("");

    } catch (error) {
      console.error("Error while creating the user:", error);
      alert("An error occurred while creating the user.");
    }
  };

  return (
    <div className="user-create">
      <label htmlFor="create-input">Create an User :</label>
      <div className="create-container">
        <input
          id="create-pseudo"
          type="text"
          value={createPseudo}
          onChange={(e) => setCreatePseudo(e.target.value)}
          placeholder="Type your pseudo"
        />
        <input
          id="create-pwd"
          type="password"
          value={createPwd}
          onChange={(e) => setCreatePwd(e.target.value)}
          placeholder="Type your password"
        />
        <button id="save-button" onClick={handleSearch}>
          Create
        </button>
      </div>
    </div>
  );
};

export default UserCreate;
