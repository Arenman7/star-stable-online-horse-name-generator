# 🐴✨ Star Stable Online Horse Name Generator 🌟

![Star Stable Online Horse Name Generator](https://images.unsplash.com/photo-1553284965-83fd3e82fa5a?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80)

Generate unique and thematic horse names for Star Stable Online using AI-powered language models!

## 📖 About

This app was made for my girlfriend who asks me for help when naming her horses, (I am not creative so I made this).

This Streamlit app generates 10 unique horse names for Star Stable Online based on a user-provided theme. Each name consists of exactly two words that relate to the theme, with the first word chosen from a predefined list of first name options and the second word chosen from a list of second name options.

The app uses [Groq](https://docs.groq.com/api/) for the Large Language Model (LLM) and [Streamlit](https://docs.streamlit.io/) for the user interface.

## 🚀 Features

- Generate 10 unique horse names based on a given theme
- Choose from multiple AI models provided by Groq
- View available name options in the sidebar
- Easy-to-use interface with emoji enhancements

## 🛠️ Installation

1. Clone this repository: `git clone https://github.com/Arenman7/star-stable-online-horse-name-generator.git
cd star-stable-online-horse-name-generator  `

2. Create a virtual environment and activate it: `` python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`   ``

3. Install the required packages: `pip install -r requirements.txt  `

4. Set up your Groq API key:
   - Copy the `.env.example` file to `.env`: `cp .env.example .env    `
   - Open the `.env` file and replace `your_groq_api_key_here` with your actual Groq API key.

## 🏃‍♂️ Usage

1. Run the Streamlit app: `streamlit run app.py  `

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Enter a theme for your horse names in the text input field.

4. Select an AI model from the dropdown menu.

5. Click the "Generate Names" button to get your unique horse names!

## 📁 Project Structure

- `app.py`: Main Streamlit application file
- `name_list.py`: Helper function to clean and process the name list
- `name_list.txt`: Text file containing the available name options
- `requirements.txt`: List of Python dependencies
- `.env.example`: Example environment file for API key
- `README.md`: This file, containing project information and instructions

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Arenman7/star-stable-online-horse-name-generator/issues).

## 🙏 Acknowledgements

- [Groq](https://docs.groq.com/api/) for providing the AI models
- [Streamlit](https://docs.streamlit.io/) for the amazing web app framework
- [Unsplash](https://unsplash.com/) for the cover image

## 📞 Contact

Check out my website, my info is there: [anbtech.xyz](https://anbtech.xyz)

Happy naming! 🎠✨

## 📜 License

This project is licensed under the MIT License. View it [here](LICENSE).
