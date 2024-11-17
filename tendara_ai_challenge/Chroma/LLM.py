from openai import OpenAI
import ollama
import yaml


class OpenAI:
    def __init__(self, api_key: str, model: str):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def get_embedding(self, text: str):
        response = self.client.embeddings.create(input=text, model=self.model)
        return response.data[0].embedding


class Ollama:
    def __init__(self, model: str):
        self.model = model
        print("start")

    def get_embedding(self, text: str):
        embedding = ollama.embeddings(
            model=self.model,
            prompt=text,
        )
        return embedding['embedding']


class LLM:
    def __init__(self, config_file: str = 'config.yaml'):
        self.config = self.load_config(config_file)
        self.client = None
        self.model = self.config.get('model_name', 'default-model')

        if 'openai_api_key' in self.config:
            print("Using OpenAI API Key")
            self.client = OpenAI(self.config['openai_api_key'], self.model)
        elif 'ollama_api_key' in self.config:
            print("Using Ollama")
            self.client = Ollama(self.model)
        else:
            raise ValueError("No valid API key found in the config file.")

    def load_config(self, config_file: str):
        """Load configuration from YAML file."""
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)

    def get_embedding(self, text: str):
        """Get embedding based on the selected client (OpenAI or Ollama)."""
        if self.client is None:
            raise ValueError("No client initialized. Check your configuration.")
        return self.client.get_embedding(text)
