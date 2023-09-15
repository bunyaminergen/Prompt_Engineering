# Article Generation and Querying using OpenAI's GPT-3

This project demonstrates how to generate an article using OpenAI's GPT-3.5-turbo model and how to query the generated article for specific information.

## Requirements

- Python 3.x
- OpenAI Python package
- python-docx package

## Installation with Poetry

First, make sure you have Poetry installed. If not, you can install it as follows:

```bash
curl -sSL https://install.python-poetry.org | python -
```

Then, clone the repository and navigate to the project folder:

```bash
git clone https://github.com/bunyaminergen/Prompt_Engineering.git
cd your_project_folder
```

Now, install the dependencies:

```bash
poetry install
```

## Setup

1. Clone the repository.
2. Get your OpenAI API key from [OpenAI website](https://beta.openai.com/signup/).
3. Add your OpenAI API Key to `config.py` file like this:

```python
api_key = "YOUR_OPENAI_API_KEY"
```

## Usage

### Article Generation

The script `main.py` generates an article based on a given prompt and language preference. It uses the GPT-3.5-turbo model to generate an article on the topic "remote work" in Turkish (Türkçe).

Run the script to generate an article and save it as a Word document:

```bash
python main.py
```

### Article Querying

The script `Q&A.py` reads the generated Word document and allows you to query it using a user-provided question. The GPT-3.5-turbo model processes the question and the article to generate an answer.

Run the script to query the generated article:

```bash
python Q&A.py
```

## Files

- `main.py`: Script to generate an article.
- `Q&A.py`: Script to query the generated article.
- `config.py`: Configuration file containing your OpenAI API key.

## How It Works

### `main.py`

1. Initializes the OpenAI API key.
2. Sets the article prompt and preferred language.
3. Uses GPT-3.5-turbo model to generate the article.
4. Saves the generated article as a Word document.

### `Q&A.py`

1. Reads the generated Word document into a string.
2. Takes a user question as input.
3. Uses GPT-3.5-turbo model to generate an answer based on the article.
4. Prints the answer to the console.

## Author

[Bünyamin Ergen](https://www.linkedin.com/in/bunyaminergen/)
