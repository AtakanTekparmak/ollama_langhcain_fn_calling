import tools
import inspect
import os 
import importlib

def get_function_names_from_file(file_path: str) -> list[str]:
    """
    Returns a list of function names defined with the `def` keyword in the given Python file.
    """
    function_names = []

    with open(file_path, 'r') as file:
        source = file.read()
        tree = compile(source, file_path, 'exec', dont_inherit=True)

        for name, obj in inspect.getmembers(tree):
            if name == "co_consts":
                # Get the function names from the code object
                for const in obj:
                    # Check if the constant is a code object
                    if isinstance(const, type(tree)):
                        function_names.append(const.co_name)
    return function_names

def import_functions_by_name(tools_path: str, function_names: list[str]) -> list[tuple[str, callable]]:
    """
    Import and return a list of functions from a module by their names.

    Args:
        tools_path (str): The path to the module containing the functions.
        function_names (list[str]): A list of strings representing the names of the functions to import.

    Returns:
        list: A list of the imported functions.
    """
    module = importlib.import_module(tools_path.replace(".py", ""))
    functions = []

    for func_name in function_names:
        try:
            function = getattr(module, func_name)
            functions.append((func_name, function))
        except AttributeError:
            raise AttributeError(f"Function '{func_name}' not found in module '{tools_path}'.")

    return functions

def get_functions(tools_path: str) -> list[dict]:
    """
    Get all the functions from tools.py.
    """
    functions = []
    i = 0
    for name, function in import_functions_by_name(tools_path, get_function_names_from_file(tools_path)): #tools.__dict__.items():
        if callable(function) and not inspect.isbuiltin(function):
            i += 1
            descriptions = function.__doc__.split("\n")
            functions.append({
                "name": name,
                "description": descriptions[0],
                "parameters": {
                    "type": "object",
                    "properties": { # Get the parameters for the function
                        param_name: {
                            "type": "string",
                            "description": descriptions[i],
                        }
                        # Remove the return type from the parameters
                        for param_name, _ in function.__annotations__.items() if param_name != "return"
                    },
                        
                    "required": [param_name for param_name in function.__annotations__ if param_name != "return"],
                },
            })

    return functions