const express = require('express');
const path = require('path');
const mongoose = require('mongoose');
require('dotenv').config();  // ✅ Load .env file
const connectDB = require('./db');
const authRoutes = require('./routes/authRoutes');

const app = express();
const PORT = 3000;

// ✅ Connect to MongoDB
connectDB();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// ✅ Serve static frontend files
app.use(express.static(path.join(__dirname, 'routes/university-management-frontend')));

// ✅ API routes
app.use('/api/auth', authRoutes);

// ✅ Default route
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'routes/university-management-frontend', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});

  