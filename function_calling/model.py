from langchain_experimental.llms.ollama_functions import OllamaFunctions

class OLlamaFunctionsModel:
    """
    Class to facilitate the use of the OllamaFunctions model.

    Args:
        model_name (str): The name of the model to use.
    """
    def __init__(self, model_name: str):
        self.model = OllamaFunctions(model=model_name)

    def bind(self, functions):
        """
        Binds the functions to the model.

        Args:
            functions (list): A list of dictionaries containing the function details.
        """
        self.model = self.model.bind(functions=functions)

    def invoke(self, user_input):
        # Invoke the model with the user input, make sure it doesn't print the output
        return self.model.invoke(user_input)
    
    def get_function_call(self, user_input):
        model_output = self.invoke(user_input)
        return model_output.additional_kwargs["function_call"]