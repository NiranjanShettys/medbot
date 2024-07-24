
---

# MedBot - First Aid Assistant

MedBot is a first aid assistant developed by Niranjan and team. It leverages Google's Gemini AI to provide detailed and accurate first aid instructions based on the image of an injury uploaded or the input text described by the user. This application ensures that the advice is clear, actionable, and prioritizes the safety and well-being of the individual.

## Features

- **Image Upload:** Users can upload images of injuries, and MedBot will provide appropriate first aid instructions.
- **Text Input:** Users can describe injuries in text, and MedBot will respond with relevant first aid advice.
- **Chat History:** Maintains a chat history to keep track of all interactions.

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/your-username/medbot-first-aid-assistant.git
    cd medbot-first-aid-assistant
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```
    streamlit run app.py
    ```

## Configuration

To use MedBot, you need to configure the Google Gemini API:

1. Obtain an API key from [Google Generative AI](https://developers.generativeai.google.com/).
2. Replace the placeholder API key in the code with your actual API key:
    ```python
    gemini_api_key = "YOUR_API_KEY_HERE"
    genai.configure(api_key=gemini_api_key)
    ```

## Usage

1. **Image Upload:**
   - Upload an image of the injury using the file uploader.
   - MedBot will process the image and provide first aid instructions.

2. **Text Input:**
   - Type a description of the injury in the chat input box.
   - MedBot will respond with relevant first aid advice.

## Development

### Adding Features

To add new features or improve existing ones, follow these steps:

1. **Fork the repository:**
   - Click the "Fork" button on the top right corner of the repository page.

2. **Create a new branch:**
    ```sh
    git checkout -b feature-branch
    ```

3. **Make your changes and commit them:**
    ```sh
    git commit -m "Add new feature"
    ```

4. **Push to the branch:**
    ```sh
    git push origin feature-branch
    ```

5. **Create a pull request:**
   - Go to the repository on GitHub and click "Pull Requests."
   - Click "New Pull Request" and select your branch.

### Issues

If you encounter any issues or have suggestions, please create an issue on the [GitHub Issue Tracker](https://github.com/your-username/medbot-first-aid-assistant/issues).

## Contributors

- Niranjan and team

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--
