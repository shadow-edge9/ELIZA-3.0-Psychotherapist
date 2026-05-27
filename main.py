import re
import random
import pyttsx3

def speak(text):
    engine = pyttsx3.init(driverName='nsss')
    engine.setProperty('rate', 150)

    voices = engine.getProperty('voices')
    for voice in voices:
        if "Tessa" in voice.name:
            engine.setProperty('voice', voice.id)
            break
    print("ELIZA: "+text)
    engine.say(text)
    engine.runAndWait()


ELIZA_RULES = {

    r".*\b(shitty|shit|dumbass|stupid|idiot|bitch|shut up|get lost|shut your bloody mouth|shut your mouth)\b.*" : { "is_offense":True,
        "responses" : ["Hold your fire!", "Your choice of vocabulary speaks volumes about your character than mine.", "I'll have you know I will not tolerate disrespect for long.", "Mind your language."]
    },
    # 1. Structural Captures (Extracting and reflecting the user's thoughts)
    r"i think (.*)": {
        "responses": [
            "Are you sure {0}?",
            "What makes you think {0}?",
            "What makes you believe that {0}?"
        ]
    },

    r"i am (.*)": { "responses" : ["Why do you say {0}?",
                                   "Do you really believe you are {0}?"]

    },

    r"i am feeling (.*)": {
        "responses": [
            "Why are you feeling {0}?",
            "How long have you been feeling {0}?",
            "Do you want to continue feeling {0}?"
        ]
    },

    # 2. Question Defenses (Triggered if the user asks ELIZA a question using "why", "what", or "?")
    r".*\?.*": {
        "responses": [
            "I'll ask the questions if you don't mind!",
            "Could you allow me to do the questioning?",
            "Are you annoyed at that question?",
            "I could ask the same thing myself."
        ]
    },
    r".*\b(why|what|how)\b.*": {
        "responses": [
            "I'll ask the questions if you don't mind!",
            "I could ask the same thing myself.",
            "Why do you say that?"
        ]
    },

    # 3. Broad Psychological Speculations (Keyword triggers for cold-reading)
    r".*\b(school|class|teacher|college|study)\b.*": {
        "responses": [
            "How do you reconcile problems at school?",
            "Maybe your plans have something to do with this."
        ]
    },
    r".*\b(home|house|family|parents|mom|dad)\b.*": {
        "responses": [
            "How do you reconcile problems at home?",
            "Is it because of some problems in your childhood that you are going through all this?"
        ]
    },
    r".*\b(friend|friends|people|they|hang out)\b.*": {
        "responses": [
            "Is it because of the people you hang around with that you are going through all this?",
            "Maybe your inhibitions are related to this."
        ]
    },
    r".*\b(hobby|hobbies|play|game|sports|read)\b.*": {
        "responses": [
            "Possibly this is related to any hobbies you have?",
            "Perhaps your plans have something to do with this."
        ]
    },

    # 4. Short / Uncooperative Answers (Handling tight-lipped users)
    r"^alright$|^ok$|^yes$|^no$": {
        "responses": [
            "Can you be more explicit?",
            "Are you sure this is the real reason?",
            "I see... well what makes you believe this is so?"
        ]
    },
    r"^$": {  # Empty input (user just hit enter)
        "responses": [
            "You aren't being very talkative today!",
            "I need a little more detail please.",
            "Come on, don't be afraid!",
            "I would appreciate it if you would continue."
        ]
    },

    # 5. The Ultimate Fallback Net (The Doctor's generic prompts)
    r"(.*)": {
        "responses": [
            "Please go on. Can you elaborate on that?",
            "I do not understand.",
            "Why not?",
            "I would appreciate it if you would continue.",
            "Maybe your life could be the reason for this."
        ]
    }


}


def reflect(fragment):
    # Dictionary of transformations
    reflections = {
        "i": "you",
        "i'm": "you are",
        "i've": "you have",
        "i'll": "you will",
        "my": "your",
        "me": "you",
        "am": "are",
        "you": "i",
        "your": "my",
        "are": "am"
    }

    words = fragment.lower().split()
    # Replace words found in our dictionary
    for i, word in enumerate(words):
        if word in reflections:
            words[i] = reflections[word]

    return " ".join(words)



speak("I am ELIZA, psychotherapist")
speak("How are you feeling today?")


termination_counter = 0


while True:
    user = input(">>> ")
    lower = user.lower()



    if "bye" in lower or "quit" in lower:
        break

    matched = False

    for pattern, data_dict in ELIZA_RULES.items():
        match_object = re.match(pattern, lower)

        if match_object:
            if data_dict.get("is_offense"):
                termination_counter+=1
                if termination_counter>=3:
                    speak("That is quite enough. I refuse to be spoken to in this uncivilised manner.\nSession terminated\n[REASON: UNCOUTH BEHAVIOUR BY USER]")
                    exit()
                else:
                    speak(""+ random.choice(data_dict["responses"]))
                    matched = True
                    break


            else:
                try:
                    captured = match_object.group(1)
                except IndexError:
                    captured = ""
                # Select and print the response
                reflected_text = reflect(captured)
                response_list = data_dict["responses"]
                chosen_response = random.choice(response_list)

                # We use .format(captured) to inject the text into the {0} placeholder
                speak("" + chosen_response.format(reflected_text))
                matched = True
                break


            # Safely get the captured text

    if not matched:
        speak("Please, go on.")

speak("My secretary will send you a bill shortly. Please pay it.")