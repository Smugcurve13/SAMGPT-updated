# SamGPT

SamGPT is a local web application designed to interact with OpenAI's GPT-3.5-turbo model. This project provides a simple, user-friendly interface to chat with GPT, specifically tailored for various use cases including answering questions based on provided documents.

## Features

- Chat interface to interact with OpenAI's GPT-3.5-turbo model.
- Real-Time chat using OpenRouter API Key.
- Clean and intuitive user interface.

## Project Structure
  
 ```sh

SamGPT/
├── app.py
├── flask_app.spec
├── requirements.txt
├── templates/
│ └── index.html
├── static/
│ ├── css/
│ │ └── styles.css
│ └── js/
│ └── scripts.js
└── README.md

```

## Setup

### Prerequisites

- Python 3.12 or later
- Virtual environment tool (optional but recommended)
- Flask
- OpenAI API key

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/SamGPT.git
    cd SamGPT
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key:**

    Create a `.env` file in the root directory and add your OpenAI API key:

    ```
    OPENAI_API_KEY=your-openai-api-key
    ```

### Running the Application

1. **Run the Flask application:**

    ```sh
    python app.py
    ```

2. **Access the application:**

    Open your web browser and go to `http://localhost:5000`

### Building an Executable (Optional)

To create an executable version of the application using PyInstaller:

1. **Install PyInstaller:**

    ```sh
    pip install pyinstaller
    ```

2. **Run PyInstaller with the spec file:**

    ```sh
    pyinstaller flask_app.spec
    ```

3. **Run the executable:**

    Navigate to the `dist` directory and run the executable:

    ```sh
    ./dist/flask_app/flask_app
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs, feature requests, or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](./License.txt) file for details.


## Acknowledgements
- [OpenRouter](https://openrouter.ai/docs/quick-start)  for providing the framework of usage of OpenRouter API key.
- [OpenAI](https://www.openai.com/) for providing the GPT-3.5-turbo model.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [PyInstaller](https://www.pyinstaller.org/) for creating standalone executables.

