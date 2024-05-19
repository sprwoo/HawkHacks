import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";

export default function Register() {
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
          <input
            type="text"
            placeholder="Name"
            className="form-input"
            ref={nameRef}
          />
          <input
            type="email"
            placeholder="Email"
            className="form-input"
            ref={emailRef}
          />
          <input
            type="tel"
            placeholder="Phone Number"
            className="form-input"
            ref={phoneRef}
          />
          <button type="submit" className="submit-button" onClick={handleSubmit}>
            Submit
          </button>
        </div>
      </div>
    );
  }