import React, { useState } from "react";
import { Container, TextField, Button, Paper, Typography } from "@mui/material";
import axios from "axios";

const App = () => {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    try {
      const res = await axios.post("http://localhost:8000/api/chatbot", { query });
      setResponse(res.data.response);
    } catch (error) {
      setResponse("Error: Unable to fetch response.");
    }
  };

  return (
    <Container maxWidth="sm">
      <Paper elevation={3} sx={{ padding: 3, marginTop: 5 }}>
        <Typography variant="h5" gutterBottom>
          DB Chatbot
        </Typography>
        <TextField
          fullWidth
          label="Ask something..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          variant="outlined"
        />
        <Button onClick={handleSubmit} variant="contained" color="primary" sx={{ marginTop: 2 }}>
          Send
        </Button>
        <Typography variant="body1" sx={{ marginTop: 3 }}>
          Response: {response}
        </Typography>
      </Paper>
    </Container>
  );
};

export default App;
