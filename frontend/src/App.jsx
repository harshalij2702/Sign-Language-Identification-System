import React, { useState } from 'react'
import axios from 'axios'
import { Button } from '@mui/material'

const App = () => {

  const [image, setImage] = useState(null)
  const [prediction, setPrediction] = useState("")

  // Store selected image
  const handleImage = (e) => {

    console.log(e.target.files[0]);

    setImage(e.target.files[0]);

  }

  // Send image to Flask
    const uploadImage = async () => {
      try {

        console.log("Button clicked");

        const formData = new FormData();

        formData.append("image", image);

        const result = await axios.post(
          "http://127.0.0.1:5000/predict",
          formData
        );

        console.log("API Response:", result.data);

        setPrediction(result.data.prediction);

      } catch (error) {

        console.log("Error:", error);

      }
  }

  return (
    <div style={{ padding: "20px" }}>

      <h1>Image Prediction App</h1>

      <input
        type="file"
        onChange={handleImage}
      />

      <br /><br />

      <Button onClick={uploadImage}>
        Upload & Predict
      </Button>

      <h2>Prediction: {prediction}</h2>

    </div>
  )
}

export default App      
