import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";

export default function Selfie() {
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