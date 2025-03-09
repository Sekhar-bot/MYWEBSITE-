# AI News Aggregator

## Overview
AI News Aggregator is a Django-powered platform that collects news from various sources, categorizes them using AI, and provides users with a personalized news feed. It also features text-to-speech (TTS) for reading news aloud and sentiment analysis for insights into trending topics.

## Features
- AI-driven news summarization and categorization
- User authentication for personalized feeds
- Image support for news articles
- Text-to-speech (TTS) functionality
- Trending topic visualizations
- Secure authentication system
- Django-powered backend with a modern frontend (Next.js/Vue.js planned)

## Installation
### Clone the Repository
```bash
git clone https://github.com/Sekhar-bot/MYWEBSITE-
cd project1
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Database
```bash
python manage.py migrate
```

### Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Run Development Server
```bash
python manage.py runserver
```

## Using Ngrok for Public Access
If you want to expose your local Django server publicly using Ngrok:

1. Install Ngrok (if not already installed):
   ```bash
   wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
   unzip ngrok-stable-linux-amd64.zip
   ```
2. Start Ngrok for port 8000:
   ```bash
   ./ngrok http 8000
   ```
3. Copy the provided public URL and use it to access the site externally.

## Running the Project with Docker (Optional)
To run the project in a containerized environment:
```bash
docker-compose up --build
```

## API Endpoints
- `GET /` - Home page with the latest news
- `POST /add-article/` - Add a new article (requires authentication)
- `GET /login/` - User login
- `GET /logout/` - User logout (redirects to home)

## Contributing
Feel free to submit issues and pull requests! Contributions are welcome.

## License
MIT License

