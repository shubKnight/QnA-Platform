const mongoose = require('mongoose');

// This is the blueprint for our question data
const questionSchema = new mongoose.Schema({
  questionText: {
    type: String,
    required: true, // This field must be provided
  },
  domain: {
    type: String,
    required: true,
  },
  status: {
    type: String,
    default: 'unanswered', // Default value if none is provided
  },
  answerText: {
    type: String,
    default: '',
  },
  aiDraftAnswer: {
    type: String,
    default: '',
  },
}, {
  timestamps: true, // Automatically adds createdAt and updatedAt fields
});

// Create a model from the schema to interact with the 'questions' collection
const Question = mongoose.model('Question', questionSchema);

module.exports = Question;