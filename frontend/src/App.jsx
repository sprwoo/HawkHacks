import { useState } from "react";
import "./App.css";

function Register() {
  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageUpload = (event) => {
    if (event.target.files && event.target.files[0]) {
      setSelectedImage(URL.createObjectURL(event.target.files[0]));
    }
  };

  return (
    <div className="register-container">
      <div className="upload-container">
        <input type="file" accept="image/*" onChange={handleImageUpload} id="file-upload" className="file-upload" />
        <label htmlFor="file-upload" className="upload-label">
          {selectedImage ? <img src={selectedImage} alt="Selected" className="uploaded-image" /> : 'Upload your image'}
        </label>
      </div>
      <div className="form-container">
        <input type="text" placeholder="Name" className="form-input" />
        <input type="email" placeholder="Email" className="form-input" />
        <input type="tel" placeholder="Phone Number" className="form-input" />
        <button type="submit" className="submit-button">Submit</button>
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
      <input type="file" accept="image/*" onChange={handleImageUpload} id="selfie-upload" className="file-upload" />
      <label htmlFor="selfie-upload" className="upload-label">
        {selectedImage ? <img src={selectedImage} alt="Selected" className="uploaded-image" /> : 'Upload your image'}
      </label>
    </div>
  );
}
function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [showRegister, setShowRegister] = useState(false);
  const [showSelfie, setShowSelfie] = useState(false);

  const handleImageUpload = (event) => {
    if (event.target.files && event.target.files[0]) {
      setSelectedImage(URL.createObjectURL(event.target.files[0]));
    }
  };

  return (
    <div className="app-container">
      <div>
        <button onClick={() => setShowRegister(prev => !prev)} className="button">Register</button>
        <button onClick={() => setShowSelfie(prev => !prev)} className="button">Selfie</button>
      </div>
      {showRegister && <Register />}
      {showSelfie && <Selfie />}
    </div>
  );
}

export default App;