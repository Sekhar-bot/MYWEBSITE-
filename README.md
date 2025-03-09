# AI News Aggregator

## Description
AI News Aggregator is a Django-based web application that fetches news articles from various sources, processes them using AI for summarization, categorization, and sentiment analysis, and presents them in a user-friendly interface.

## Features
- Fetches news from multiple sources
- AI-powered summarization and categorization
- Personalized news feed based on user preferences
- Sentiment analysis of news articles
- Text-to-speech (TTS) for reading articles aloud
- Image support for news articles
- User authentication for personalized feeds
- Trending topic visualizations
- Responsive UI using Bootstrap

## Tech Stack
- **Backend:** Django, MySQL  
- **Frontend:** HTML, CSS, Bootstrap (Future plans: Next.js/Vue.js)  
- **AI Features:** NLP for summarization & sentiment analysis  
- **Deployment:** Firebase (planned for app & website)  

## Setup Instructions

### 1. Clone the repository
```sh
git clone https://github.com/Sekhar-bot/MYWEBSITE-
cd project1
```

### 2. Create a virtual environment and activate it
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Run migrations
```sh
python manage.py migrate
```

### 5. Start the development server
```sh
python manage.py runserver
```

### 6. Access the application
Open your browser and go to:  
`http://127.0.0.1:8000/`

## Future Enhancements
- Implement a Next.js/Vue.js frontend for a more dynamic user experience.
- Add real-time news updates using WebSockets.
- Improve AI models for better summarization and categorization.
- Deploy the application on Firebase for better scalability.

## Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any queries or collaborations, feel free to reach out at `your-email@example.com`. 🚀

