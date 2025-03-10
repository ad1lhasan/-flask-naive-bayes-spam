# Flask Naive Bayes Spam Classifier

A simple Flask-based web application that classifies messages as spam or ham using a Naive Bayes classifier.

## Features
- Train a Naive Bayes model on a dataset of spam and ham messages
- Predict whether a given message is spam or not
- Simple web UI built with Flask

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ad1lhasan/flask-naive-bayes-spam.git
   cd flask-naive-bayes-spam
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000/`

## API Endpoints

- `POST /predict` - Accepts a JSON payload with a message and returns whether it's spam or ham.

## Example Request
```json
{
  "message": "Congratulations! You've won a free iPhone. Click here to claim."
}
```

## Example Response
```json
{
  "prediction": "spam"
}
```

## Dataset
The model is trained on a dataset of labeled spam and ham messages. You can replace `spam.csv` with your own dataset if needed.

## Contributing
Feel free to submit issues and pull requests if you find bugs or have suggestions for improvements.

## License
This project is licensed under the MIT License.

