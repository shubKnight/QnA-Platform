const express = require('express');
const router = express.Router();
const Question = require('../models/Question'); // Import our Question model

// --- 1. CREATE a new question (POST) ---
router.post('/', async (req, res) => {
  try {
    // Create a new question document using the data from the request body
    const newQuestion = new Question({
      questionText: req.body.questionText,
      domain: req.body.domain, // This might come from your classification model
    });

    // Save the new question to the database
    const savedQuestion = await newQuestion.save();
    res.status(201).json(savedQuestion); // Send back the created question
  } catch (error) {
    res.status(500).json({ message: 'Error creating question', error: error });
  }
});

// --- 2. READ questions (GET) ---
// Get all questions, with an option to filter by domain
router.get('/', async (req, res) => {
  try {
    const query = {};
    // If a 'domain' query parameter is provided (e.g., /api/questions?domain=AI/ML)
    if (req.query.domain) {
      query.domain = req.query.domain;
    }
    const questions = await Question.find(query);
    res.json(questions);
  } catch (error) {
    res.status(500).json({ message: 'Error fetching questions', error: error });
  }
});

// --- 3. UPDATE a question (PUT) ---
// This is used when a Zine member posts an answer
router.put('/:id', async (req, res) => {
  try {
    const updatedQuestion = await Question.findByIdAndUpdate(
      req.params.id, // The ID of the question to update
      req.body,     // The data to update with (e.g., { answerText: "...", status: "answered" })
      { new: true } // Option to return the document after it's been updated
    );
    if (!updatedQuestion) {
      return res.status(404).json({ message: 'Question not found' });
    }
    res.json(updatedQuestion);
  } catch (error) {
    res.status(500).json({ message: 'Error updating question', error: error });
  }
});

// --- 4. DELETE a question (DELETE) ---
router.delete('/:id', async (req, res) => {
  try {
    const deletedQuestion = await Question.findByIdAndDelete(req.params.id);
    if (!deletedQuestion) {
      return res.status(404).json({ message: 'Question not found' });
    }
    res.json({ message: 'Question deleted successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Error deleting question', error: error });
  }
});

module.exports = router;