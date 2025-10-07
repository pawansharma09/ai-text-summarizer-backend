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
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the server:
   ```bash
   uvicorn main:app --reload

### Docker SetUp
1. Build the image:
   ```bash
   docker build -t summarizer-api.
2. Run the container:
   ```bash
   docker run -p 8000:8000 summarizer-api

### API Endpoints
POST /summarize
Summarize input text.

GET /health
Health check endpoint.

### Environment Variables
None required. All configuration is done through API parameters.

### Deployment
Render: Use render.yaml for 1-click deployment
Other platforms: Set start command to uvicorn main:app --host 0.0.0.0 --port $PORT
Model Information
Model: sshleifer/distilbart-cnn-12-6
Max Input Length: 1024 tokens
Recommended Input: News articles, formal documents

### License
MIT
