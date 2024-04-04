import tools

class FunctionCaller:
    """
    A class to call functions from tools.py.
    """

    def __init__(self):
        # Initialize the functions dictionary
        self.functions = {function_name:function for function_name, function in tools.__dict__.items() if callable(function)}
    
    def call_function(self, function):
        """
        Call the function from tools.py with the given input.

        Args:
            function (dict): A dictionary containing the function details.
        """
        def format_function_input(function_input: str) -> dict:
            # Remove the curly braces from the string
            function_input = function_input[1:-1]
            # Split the string by commas
            function_input = function_input.split(",")
            # Split each item in the list by colons and save them as key-value pairs in a dictionary
            function_input = {item.split(":")[0].strip(): item.split(":")[1].strip() for item in function_input}
            # Remove the double quotes from the keys and values
            return {key[1:-1]: value[1:-1] for key, value in function_input.items()}
        
        # Get the function name from the function dictionary
        function_name = function["name"]
        
        # Get the function input from the function dictionary
        function_input = function["arguments"] if "arguments" in function else ""
        function_input = format_function_input(function_input) if function_input else None
    
        # Call the function from tools.py with the given input
        # pass all the arguments to the function from the function_input
        return self.functions[function_name](**function_input) if function_input else self.functions[function_name]()