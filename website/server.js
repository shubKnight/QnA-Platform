// Import necessary libraries
const express = require('express');
const cors = require('cors');
require('dotenv').config(); // Load environment variables from .env file

// Import our custom modules
const connectDB = require('./config/db');
const questionRoutes = require('./routes/questionRoutes');

// Connect to the database
connectDB();

const app = express();
const PORT = process.env.PORT || 5000;

// Set up middleware
app.use(cors());
app.use(express.json());

// Define a basic route
app.get('/', (req, res) => {
  res.send('Hello from the Zine Q&A Backend!');
});

// --- Use the CRUD routes ---
// Any request starting with '/api/questions' will be handled by our questionRoutes
app.use('/api/questions', questionRoutes);

// Start the server
app.listen(PORT, () => {
  console.log(`🚀 Server is running on http://localhost:${PORT}`);
});