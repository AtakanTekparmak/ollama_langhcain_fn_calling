from model import OLlamaFunctionsModel
from utilities import get_functions
from function_caller import FunctionCaller

def setup():
    # Set constants
    MODEL_NAME = "openhermes2.5_gguf:latest"
    TOOLS_FILE_PATH = "tools.py"

    # Create the model and the function caller
    model = OLlamaFunctionsModel(model_name=MODEL_NAME)
    function_caller = FunctionCaller()

    # Get all the functions from tools.py
    functions = get_functions(tools_path=TOOLS_FILE_PATH)

    # Bind the functions to the model
    model.bind(functions=functions)

    return model, function_caller

def main():
    # Load the model and the function caller
    model, function_caller = setup()

    # Get the function call
    prompt_1 = "what is the weather in San Francisco?"
    prompt_2 = "Can you give me a random number please?"
    prompt_3 = "Can you give me a random city please?"
    model_output_1 = model.get_function_call(prompt_1)
    model_output_2 = model.get_function_call(prompt_2)
    model_output_3 = model.get_function_call(prompt_3)

    # Call the function
    output_1 = function_caller.call_function(model_output_1)
    output_2 = function_caller.call_function(model_output_2)
    output_3 = function_caller.call_function(model_output_3)

    print(f"Output 1: {output_1}")
    print(f"Output 2: {output_2}")
    print(f"Output 3: {output_3}")

if __name__ == "__main__":
    main()