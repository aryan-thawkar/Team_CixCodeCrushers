# AI Interview Prep Bot

## Overview
The AI Interview Prep Bot is a chatbot designed to conduct mock technical interviews for AI/ML roles. It provides real-time feedback, evaluates responses, and offers guidance to help candidates improve their interview performance.

## Features
- Conducts mock technical interviews for AI/ML roles.
- Provides real-time feedback on answers.
- Evaluates coding proficiency and problem-solving skills.
- Offers hints and guidance during the interview.
- Analyzes performance and suggests areas for improvement.
- Supports multiple interview formats (behavioral, coding, theoretical).

## Technologies Used
- **Natural Language Processing (NLP):** For understanding and evaluating user responses.
- **Machine Learning:** To assess coding efficiency and problem-solving ability.
- **Google's Conversational Agent (Vertex AI Preview):** For advanced chatbot interactions.
- **Python (Flask/FastAPI):** Backend development.
- **OpenAI API / LLMs:** To generate responses and feedback.
- **Frontend:** React.js for UI (optional, if web-based interface is needed).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-interview-prep-bot.git
   cd ai-interview-prep-bot
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables (e.g., API keys for OpenAI and Vertex AI).
5. Run the application:
   ```bash
   python app.py
   ```

## Usage
- Start the bot and interact via a command-line interface or web UI.
- Choose an interview type: Coding, Theoretical, or Behavioral.
- Answer the questions, and receive real-time feedback.
- View a performance summary at the end of the session.

## Future Enhancements
- Integration with LeetCode-style coding challenges.
- Personalized learning paths based on performance.
- Multi-language support.
- Voice-enabled interview experience.

## Contributing
Pull requests are welcome! Please open an issue first to discuss any changes.

## License
This project is licensed under the MIT License.
