// backend/routes/authRoutes.js
const express = require('express');
const router = express.Router();
const authController = require('../controllers/authController');

router.post('/signup', authController.signup); // ✅ Should match exported function
router.post('/login', authController.login);   // ✅ Should match exported function

module.exports = router;

