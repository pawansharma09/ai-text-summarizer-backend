# Text Summarization API

FastAPI backend for AI text summarization using the DistilBART CNN model.

## Features
- Summarize text using `sshleifer/distilbart-cnn-12-6` model
- Adjustable summary length parameters
- Health check endpoint
- Docker support

## Requirements
- Python 3.9+
- Docker (optional)

## Installation

### Local Setup
1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
