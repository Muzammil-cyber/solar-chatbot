# Solar Chatbot

A simple Flask-based chatbot that provides information about solar panels, installation, estimates, and maintenance services.

## Features

- Semantic search using sentence transformers
- RESTful API endpoint for chat interactions
- Pre-trained knowledge base about solar services
- Input cleaning and preprocessing

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Flask App

Start the Flask server:

```bash
python app.py
```

The server will run on `http://localhost:5000`

### API Usage

Send POST requests to `/chat` endpoint:

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "How long does installation take?"}'
```

Response:

```json
{
  "response": "Our standard installation time is 7–10 working days."
}
```

### Testing

Run the test script to verify the chatbot functionality:

```bash
python test_chatbot.py
```

## Project Structure

```bash
solar_chatbot/
├── app.py                 # Flask app
├── chatbot.py             # AI logic using sentence similarity
├── utils.py               # Optional helper functions
├── data/
│   └── knowledge.txt      # Your company’s custom solar knowledge
├── requirements.txt       # Python dependencies
├── test_chatbot.py        # Test script for verification
├── .gitignore              # Ignore files for git
└── README.md              # This file
```

## Dependencies

- Flask - Web framework
- sentence-transformers - Semantic search
- torch - PyTorch for tensor operations
- transformers - Hugging Face transformers
