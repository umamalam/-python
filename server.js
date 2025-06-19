const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const path = require('path');
const authRoutes = require('./routes/authRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.use('/api/auth', authRoutes);

// Serve static frontend files
app.use(express.static(path.join(__dirname, 'routes/university-management-frontend')));


// Default route to load index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'routes', 'university-management-frontend', 'index.html'));
});


// MongoDB Connection
mongoose.connect('mongodb://localhost:27017/university-system', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => {
  console.log('MongoDB connected');
  app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
}).catch((err) => {
  console.error('MongoDB connection error:', err);
});

  