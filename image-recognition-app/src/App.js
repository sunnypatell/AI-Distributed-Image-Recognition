// src/App.js

import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('image', file);

    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();
    setPrediction(data.predictions);
  };

  return (
    <div className="App">
      <h1>Image Recognition App</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Predict</button>
      {prediction && (
        <div>
          <h2>Prediction Results:</h2>
          <ul>
            {prediction.map((pred, index) => (
              <li key={index}>
                <strong>{pred.label}</strong>: {pred.probability.toFixed(2)}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
