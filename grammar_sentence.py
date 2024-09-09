import os
import sys
import google.generativeai as genai

def configure_api():
    # Configure the API with the necessary settings
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Please set the GEMINI_API_KEY environment variable.")
        sys.exit(1)

    genai.configure(api_key=api_key)

def correct_sentence(text):
    # Create the model
    generation_config = {
        "temperature": 0.0,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Prompt for correcting the grammar
    prompt_correction = f"Correct the grammar of the following sentence:\nOriginal: {text}\nFixed Grammar:"

    # Send the user's input to the model
    response = model.generate_content(prompt_correction)

    # Extract the corrected sentence
    corrected_text = response.text.strip()

  # Check if the response indicates a correction
    if corrected_text == text.strip():
        print("Correct")
    else:
        print("Incorrect")
        print("Corrected Sentence:")
        print(corrected_text)

def main():
    # Configure the API
    configure_api()

    while True:
        # Prompt the user for input
        text_to_generate = input("Enter a sentence to check (or type 'exit' to quit): ")

        if text_to_generate.lower() == 'exit':
            break

        # Check grammar using the Gemini API
        correct_sentence(text_to_generate)

if __name__ == "__main__":
    main()
