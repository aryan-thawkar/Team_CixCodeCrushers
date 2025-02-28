# AI Interview Chatbot with Resume Analyzer, Code Editor, and Preparation Videos

## Overview
This project is an AI-powered interview chatbot designed to help users prepare for technical interviews. It features:
- **AI Interview Chatbot**: Conducts mock technical interviews with real-time feedback.
- **Resume Analyzer**: Extracts key points from uploaded resumes to provide insights.
- **Code Editor**: Allows users to write, edit, and run code in a built-in editor.
- **Preparation Videos**: Provides recommended learning resources for interview preparation.

## Features
### AI Interview Chatbot
- Conducts technical interviews with AI-powered responses.
- Provides structured and formatted feedback.
- Includes text-to-speech functionality.
- Option to mute/unmute AI voice.

### Resume Analyzer
- Allows users to upload resumes in PDF format.
- Extracts key details like skills, experience, and education.
- Provides insights on resume improvement.

### Code Editor
- Enables users to write and execute code in various programming languages.
- Supports syntax highlighting and error checking.

### Preparation Videos
- Provides curated videos on coding, algorithms, and interview strategies.
- Offers interactive learning experiences.

## How to Use
1. **Chatbot:** Enter a message in the text box and click "Send" to receive a response.
2. **Resume Analyzer:** Upload a PDF resume and click "Analyze Resume" to extract key points.
3. **Code Editor:** Write and test code directly in the web interface.
4. **Preparation Videos:** Watch recommended videos for technical interview preparation.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/aryan-thawkar/Team_CixCodeCrushers.git
   cd ai-interview-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open the application in a web browser:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints
- **`/chat`** (POST): Sends a message to the chatbot and returns a response.
- **`/toggle_mute`** (POST): Toggles the chatbot's voice on/off.
- **`/get_mute_status`** (GET): Returns the mute status.
- **`/analyze_resume`** (POST): Uploads a resume and extracts key points.

## Technologies Used
- Flask (Python backend)
- Ollama for AI-based responses
- pyttsx3 for text-to-speech
- JavaScript & jQuery for frontend interactions
- HTML/CSS for UI design

## License
This project is open-source and available under the MIT License.

## Contributors
- Aryan Thawkar
- Ishan Pote
- Ajinkya Mariche
- Nishant Gakare

For any issues, feel free to raise an issue or contribute to the repository!