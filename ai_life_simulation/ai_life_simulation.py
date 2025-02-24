"""
This file contains code for the life simulation game "AI Life Simulation".
Author: SoftwareApkDev
"""


# Game version: 1


# Importing necessary libraries


import google.generativeai as genai
import os
from dotenv import load_dotenv
from google.generativeai import GenerativeModel
from langchain_ollama import OllamaLLM
import subprocess


# Creating static functions to be used in this game.


def ai_response(model: GenerativeModel or OllamaLLM, prompt: str) -> str:
    if isinstance(model, GenerativeModel):
        return str(model.generate_content(prompt).text)
    elif isinstance(model, OllamaLLM):
        return model.invoke(prompt)
    return ""


# Creating static variables to be used throughout the game.


MODELS: list = ["llama3.2", "llama3.2:1b", "llama3.1", "llama3.1:70b", "llama3.1:405b", "phi3", "phi3:medium",
                "gemma2:2b", "gemma2", "gemma2:27b", "mistral", "moondream", "neural-chat", "starling-lm", "codellama",
                "llama2-uncensored", "llava", "solar"]


# Creating main function used to run the game.


def main() -> int:
    """
    This main function is used to run the game.
    :return: an integer
    """

    # Loading Gemini API Key
    load_dotenv()
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])

    # Gemini Generative Model
    model: GenerativeModel = genai.GenerativeModel("gemini-pro")

    # Ollama LLM Model
    print("LLM Models:")
    for i, model in enumerate(MODELS, 1):
        print(f"{i}. {model}")

    choice: str = input("Please enter the number of the LLM model you want to use: ")
    while choice not in [str(i) for i in range(1, len(MODELS) + 1)]:
        print("Options:")
        for i, model in enumerate(MODELS, 1):
            print(f"{i}. {model}")

        choice = input("Sorry, invalid input! Please enter the number of the LLM model you want to use: ")

    chosen_model: str = MODELS[int(choice) - 1]
    output: subprocess.CompletedProcess[str] = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
    output_str: str = output.stdout
    if chosen_model not in output_str:
        print("Cannot run " + str(chosen_model) + "! Please manually pull " + str(chosen_model) + " first!")
        return 1

    llm: OllamaLLM = OllamaLLM(model=chosen_model)
    while True:
        prompt: str = input("> ")
        response: str = llm.invoke(prompt)
        print("AI: " + str(response))


if __name__ == "__main__":
    main()
