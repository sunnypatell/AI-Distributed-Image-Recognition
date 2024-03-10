// src/App.js

import React, { useState } from 'react';
import { Container, Typography, Button, TextField, Paper, Grid, Box } from '@mui/material';
import { makeStyles } from '@mui/styles';

const useStyles = makeStyles((theme) => ({
  root: {
    marginTop: theme.spacing(4),
  },
  paper: {
    padding: theme.spacing(2),
  },
  imagePreview: {
    maxWidth: '100%',
    maxHeight: '300px',
    marginBottom: theme.spacing(2),
  },
}));

function App() {
  const classes = useStyles();
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
    setImagePreview(URL.createObjectURL(selectedFile));
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
    <Container className={classes.root}>
      <Typography variant="h3" align="center" gutterBottom>
        Image Recognition App
      </Typography>
      <Grid container spacing={3} justifyContent="center">
        <Grid item xs={12} sm={6}>
          <Paper className={classes.paper} elevation={3}>
            <input
              accept="image/*"
              style={{ display: 'none' }}
              id="upload-button"
              type="file"
              onChange={handleFileChange}
            />
            <label htmlFor="upload-button">
              <Button variant="contained" component="span" fullWidth>
                Upload Image
              </Button>
            </label>
            {imagePreview && (
              <Box mt={2}>
                <img src={imagePreview} alt="Preview" className={classes.imagePreview} />
              </Box>
            )}
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.paper} elevation={3}>
            <Button variant="contained" color="primary" fullWidth onClick={handleSubmit}>
              Predict
            </Button>
            {prediction && (
              <Box mt={2}>
                <Typography variant="h6" gutterBottom>
                  Prediction Results:
                </Typography>
                <ul>
                  {prediction.map((pred, index) => (
                    <li key={index}>
                      <strong>{pred.label}</strong>: {pred.probability.toFixed(2)}
                    </li>
                  ))}
                </ul>
              </Box>
            )}
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
}

export default App;
