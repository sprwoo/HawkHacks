import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios"

function Register() {
  const [selectedImage, setSelectedImage] = useState(null);
  
  const nameRef = useRef();
  const emailRef = useRef();
  const phoneRef = useRef();

  const handleImageUpload = (event) => {
    if (event.target.files && event.target.files[0]) {
      setSelectedImage(URL.createObjectURL(event.target.files[0]));
    }
  };

  return (
    <div className="register-container">
      <div className="upload-container">
        <input
          type="file"
          accept="image/*"
          onChange={handleImageUpload}
          id="file-upload"
          className="file-upload"
        />
        <label htmlFor="file-upload" className="upload-label">
          {selectedImage ? (
            <img
              src={selectedImage}
              alt="Selected"
              className="uploaded-image"
            />
          ) : (
            "Upload your image"
          )}
        </label>
      </div>
      <div className="form-container">
        <input type="text" placeholder="Name" className="form-input" ref={nameRef} />
        <input type="email" placeholder="Email" className="form-input" ref={emailRef} />
        <input type="tel" placeholder="Phone Number" className="form-input" ref={phoneRef} />
        <button type="submit" className="submit-button">
          Submit
        </button>
      </div>
    </div>
  );
}

function Selfie() {
  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageUpload = (event) => {
    if (event.target.files && event.target.files[0]) {
      setSelectedImage(URL.createObjectURL(event.target.files[0]));
    }
  };

  return (
    <div className="upload-container">
      <input
        type="file"
        accept="image/*"
        onChange={handleImageUpload}
        id="selfie-upload"
        className="file-upload"
      />
      <label htmlFor="selfie-upload" className="upload-label">
        {selectedImage ? (
          <img src={selectedImage} alt="Selected" className="uploaded-image" />
        ) : (
          "Upload your image"
        )}
      </label>
    </div>
  );
}
function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [showRegister, setShowRegister] = useState(false);
  const [showSelfie, setShowSelfie] = useState(false);
  const [response, setResponse] = useState("");

  // form stuff to check if azure works
  const [id, setId] = useState("");
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const handleImageUpload = (event) => {
    if (event.target.files && event.target.files[0]) {
      setSelectedImage(URL.createObjectURL(event.target.files[0]));
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/pictures/",
        { name, description },
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

  const handleStuff = async () => {
    const formData = new FormData();
    formData.append('image', selectedImage);
    formData.append('name', nameRef.current.value);
    formData.append('email', emailRef.current.value);
    formData.append('phone', phoneRef.current.value);
  
    const response = await fetch('http://localhost:8000/register_img', {
      method: 'POST',
      body: formData
    });
  
    if (!response.ok) {
      console.error('Failed to send data');
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
        <button onClick={handleStuff} className="button">
          Clcik
        </button>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
          <button type="submit" className="button">
            send to azure
          </button>
        </form>
      </div>
      {showRegister && <Register />}
      {showSelfie && <Selfie />}
      {response && <p>{response}</p>}
    </div>
  );
}

export default App;
