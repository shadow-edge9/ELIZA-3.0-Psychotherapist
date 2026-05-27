# ELIZA-3.0: A Deterministic Psychotherapist

A minimalist, rule-based conversational agent implemented in Python, designed to simulate the classic Rogerian psychotherapist, ELIZA.

## Overview
ELIZA-3.0 is a deterministic chatbot that utilizes regular expression (regex) pattern matching to engage in "conversational" therapy. Unlike modern LLMs that rely on probabilistic models and massive datasets, this implementation uses a structured rule-based engine to reflect user inputs and steer the dialogue through clinical deflection.

## Interactive Audio Interface
ELIZA-3.0 is more than a simple terminal-based text processor. It incorporates an integrated Text-to-Speech (TTS) engine, transforming the session into an interactive verbal experience. The system provides immediate, synthetic-voice feedback, creating a dynamic and responsive clinical simulation that requires the user to engage in a back-and-forth dialogue.

## Technical Specifications
* **Engine:** Python 3.x
* **Logic:** Deterministic finite-state matching via `re` (Regular Expressions).
* **Speech Synthesis:** `pyttsx3` with an asynchronous queue management system.
* **Architecture:** Modular design separating dialogue rules, reflection logic, and input handling.

## Key Features
* **Rule-Based Deflection:** Uses a keyword-priority system to identify and redirect conversational topics (e.g., family, hobbies, school) back to the user.
* **State-Based Behavior:** Includes a `termination_counter` to handle and punish uncivilized input, giving the system a sense of "agency."
* **Reflective Logic:** A custom reflection dictionary transforms user statements (e.g., "I am" $\rightarrow$ "You are") to simulate active listening.
* **Zero-Persistence:** Built as a stateless system; the conversation remains private and is cleared entirely upon termination.

## Getting Started

### Prerequisites
You will need `pyttsx3` installed.
```bash
pip install pyttsx3 
```
### Installation
Clone this repository: git clone [https://github.com/shadow-edge9/ELIZA-3.0-Psychotherapist/tree/main]
Navigate to the directory: cd ELIZA-3.0-Psychotherapist
Run the script: python eliza.py
