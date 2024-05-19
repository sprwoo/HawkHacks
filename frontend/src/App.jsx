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
      <div>
        <button
          onClick={() => setShowRegister((prev) => !prev)}
          className="button"
        >
          Register
        </button>
        <button
          onClick={() => setShowSelfie((prev) => !prev)}
          className="button"
        >
          Selfie
        </button>
        <button onClick={() => handleEmail()} className="button">
          Send email
        </button>
        <button onClick={handleStuff} className="button">
          Click
        </button>

        <form onSubmit={handleStuff}>
          <div className="input-container">
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="input-postgres"
            />
            <input
              type="text"
              value={email}
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
      </div>
      <form onSubmit={handleGroupStuff}>
            <div className="upload-container">
              <input
                type="file"
                accept="image/*"
                onChange={(e) => setImage(e.target.files[0])}
                id="selfie-upload"
                className="file-upload"
              />
              <label htmlFor="selfie-upload" className="upload-label">
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
      {showRegister && <Register />}
      {response && <p>{response}</p>}
    </div>
  );
}

export default App;
