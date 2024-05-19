import { useState } from "react";
import "./App.css";
import axios from "axios";
import Register from "./Register";

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [showRegister, setShowRegister] = useState(false);
  const [showSelfie, setShowSelfie] = useState(false);
  const [response, setResponse] = useState("");

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [image, setImage] = useState(null);
  const [groupphoto, setGroupPhoto] = useState(null);

  const handleToggle = () => {
    setShowRegister(!showRegister);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/pictures/",
        { name, email },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      console.log(response.data);
    } catch (error) {
      console.error("There was an error submitting the form!", error);
    }
  };

  const handleStuff = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("name", name);
    formData.append("email", email);
    formData.append("group_image", image);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/pictures/",
        formData
      );
      console.log(response.data);
    } catch (error) {
      console.error("There was an error submitting the form!", error);
    }

    if (!response.ok) {
      console.error("Failed to send data");
    }
  };

  const handleGroupStuff = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("group_image", groupphoto);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/group_pictures/",
        formData
      );
      console.log(response.data);
    } catch(error) {
      console.error("There was an error submitting the form!", error);
    }

    if (!response.ok) {
      console.error("Failed to send data");
    }
  }

  const handleEmail = async () => {
    const response = await fetch("http://localhost:8000/send_email/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: "",
    });
    if (!response.ok) {
      console.error("Failed to send email");
    } else {
      console.log("Email sent successfully");
    }
  };

  return (
    <div className="app-container">
      <h1 className="header">Yo! Send It To.me</h1>
      <div>
      <div style={{ display: 'flex', justifyContent: 'center' }}>
          <button className="button" onClick={handleToggle}>
          {showRegister ? "Register User" : "Group Photo"}
          </button>
        </div>
        {showRegister ? (
        <form onSubmit={handleStuff}>
          <div className="input-container">
            <input
              type="text"
              value={name}
              placeholder="Name"
              onChange={(e) => setName(e.target.value)}
              className="input-postgres"
            />
            <input
              type="text"
              value={email}
              placeholder="Email"
              onChange={(e) => setEmail(e.target.value)}
              className="input-postgres"
            />
            <div className="upload-container">
              <input
                type="file"
                accept="image/*"
                onChange={(e) => setImage(e.target.files[0])}
                id="selfie-upload"
                className="file-upload"
              />
              <label htmlFor="selfie-upload" className="upload-label">
                {image ? (
                  <img
                    src={image}
                    alt="Selected"
                    className="uploaded-image"
                  />
                ) : (
                  "Upload your image"
                )}
              </label>
            </div>
            <button type="submit" className="button submit-button">
              Submit
            </button>
          </div>
        </form>
        ) : (
      <form onSubmit={handleGroupStuff}>
            <div className="upload-container">
              <input
                type="file"
                accept="image/*"
                onChange={(e) => setGroupPhoto(e.target.files[0])}
                id="group-upload"
                className="file-upload"
              />
              <label htmlFor="group-upload" className="upload-label">
                {groupphoto ? (
                  <img
                    src={groupphoto}
                    alt="Selected"
                    className="uploaded-image"
                  />
                ) : (
                  "Upload your image"
                )}
              </label>
            </div>
            <button type="submit" className="button submit-button">
              Submit
            </button>
        </form>

      // {showRegister && <Register />}
      // {response && <p>{response}</p>}
    )}
    </div>
    </div>
  );
}

export default App;
