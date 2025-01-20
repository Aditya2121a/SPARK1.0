import threading
import sys
import time
import webbrowser
import wikipedia
from Head.Mouth import speak


def load_qa_data(file_path):
    qa_dict = {}
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")
                if len(parts) != 2:
                    continue
                q, a = parts
                qa_dict[q] = a
        print("QA data loaded successfully.")
    except Exception as e:
        print(f"Error loading QA data: {e}")
    return qa_dict


qa_file_path = r'C:\My Project\SPARK 1.0\Data\brain_data\qna_data.txt'
qa_dict = load_qa_data(qa_file_path)


def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)
    print()


def save_qa_data(file_path, qa_dict):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for q, a in qa_dict.items():
                f.write(f"{q}:{a}\n")
        print("QA data saved successfully.")
    except Exception as e:
        print(f"Error saving QA data: {e}")


def wiki_search(prompt):
    search_prompt = prompt.replace("spark", "")
    search_prompt=search_prompt.replace("wikipedia", "")
    try:
        wiki_summary = wikipedia.summary(search_prompt, sentences=2)
        print(f"Wiki summary found: {wiki_summary}")
        animate_thread = threading.Thread(target=print_animated_message, args=(wiki_summary,))
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))

        animate_thread.start()
        speak_thread.start()

        animate_thread.join()
        speak_thread.join()

        qa_dict[search_prompt] = wiki_summary
        save_qa_data(qa_file_path, qa_dict)
    except wikipedia.exceptions.DisambiguationError:
        speak("There is a disambiguation page for the given query. Please provide more specific information.")
        print("There is a disambiguation page for the given query. Please provide more specific information.")
    except wikipedia.exceptions.PageError:
        google_search(prompt)

def google_search(query):
    query = query.replace("who is ", "").strip()
    if query:
        url = "https://www.google.com/search?q=" + query
        print(f"Attempting to open browser with URL: {url}")  # Debugging statement
        try:
            if not webbrowser.open_new_tab(url):
                print("Failed to open new tab, trying open_new.")
                if not webbrowser.open_new(url):
                    print("Failed to open new, trying open.")
                    if not webbrowser.open(url):
                        raise Exception("All methods to open the browser failed.")
            speak("You can see search results for " + query + " in Google on your screen.")
            print("You can see search results for " + query + " in Google on your screen.")
        except Exception as e:
            print(f"Error opening browser: {e}")
            speak("I couldn't open the web browser.")
    else:
        speak("I didn't catch what you said.")
        print("I didn't catch what you said.")


