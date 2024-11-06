Grammar Correction Script using Google Generative AI

This Python script, grammar_sentence.py, leverages Google’s Generative AI API (Gemini) to check and correct the grammar of user-provided sentences. It’s ideal for anyone needing automated grammar verification, such as writers, editors, or developers.
Features

    API Configuration: Integrates with Google’s Generative AI API, requiring a valid GEMINI_API_KEY.
    Grammar Correction: Analyzes and corrects sentence structure, punctuation, and syntax errors.
    User-Friendly Interaction: Accepts input through the console, showing corrections or confirming grammatical accuracy.
    Looped Input: Continuously prompts for sentences until the user types 'exit'.

Usage

Set up API Key: Make sure GEMINI_API_KEY is set with a valid API key.

    export GEMINI_API_KEY="your_api_key_here"

Run the Script: Start the grammar correction tool.

    python grammar_sentence.py

Enter Sentences: Input a sentence to check its grammar. Correct sentences will be confirmed; incorrect ones will display a corrected version.

Code Breakdown

    configure_api(): Configures the API using the GEMINI_API_KEY. Exits with an error if the key is missing.
    correct_sentence(text): Utilizes the gemini-1.5-flash model to check and correct grammar. Outputs either confirmation or the corrected sentence.
    main(): Runs a loop to prompt users for input and applies grammar correction until 'exit' is typed.

Requirements

    Python 3.x
    Google Generative AI Client: Install with pip install google-generative-ai.

Example

$ python grammar_sentence.py
Enter a sentence to check (or type 'exit' to quit): He go to the store.
Incorrect
Corrected Sentence:
He goes to the store.
Enter a sentence to check (or type 'exit' to quit): exit

This script offers an efficient, easy-to-use way to improve sentence quality!
