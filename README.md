# ollama_langhcain_fn_calling
A simple repository that houses a basic Ollama + LangChain setup for function calling with LLMs. Simple flow is as follows:

```
User --(prompt)--> Ollama + LangChain --(function call)--> Function Caller 
```

The user provides a prompt to Ollama + LangChain, which then uses the model to generate a function call. The function caller then executes the function call and returns the result to the user.

<h1> <b>BEWARE: This is a very basic setup and is not meant to be used in production. It's merely meant to be a starting point for more complex setups, might not work for your use case. </b> </h1>

# Setup

## Requirements
- Python 3.10.12+
- [Ollama](https://github.com/ollama/ollama)

## Installation

### Ollama

Ollama has a dedicated [installation and setup guide](https://github.com/ollama/ollama) that you can use to get the model you want up and running.

### Function Calling

To get the function calling setup running, you need to install the Python dependencies (Creating a virtual environment is recommended):

```bash
python -m venv fn_env
source fn_env/bin/activate
pip install -r requirements.txt
```

Then, you need to add the functions you want the model to "call" in the `function_calling/tools.py` file. 

```python

# Usage

To run the function calling setup, you can use the following command:

```bash
cd function_calling
python main.py
``` 

