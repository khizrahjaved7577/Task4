import nltk
import random
from nltk.stem import PorterStemmer
from data import data 
nltk.download('punkt')
nltk.download('punkt_tab')
stemmer=PorterStemmer()
print(data["greetings"]) 
# mapping categories to their corresponding categories
instant_responce_map={
    "greetings":"responses",
    "farewells":"farwell_responses",
    "questions":"question_responses",
    "small_talk":"small_talk_responses"
}
def preprocessing(sentence):
    tokens=nltk.word_tokenize(sentence.lower())
    for token in tokens:
        return stemmer.stem(token)
def get_response(user_input):
    preprocessed_input=preprocessing(user_input)
# check for all pattern categories
    for intent_category,response_category  in  instant_responce_map.items():
        for pattern in data[intent_category]:
             processed_pattern=preprocessing(pattern)
             if all(word in preprocessed_input for word in processed_pattern):
                return random.choice(data[response_category])
    # fall back for unknown inputs
    return "I am not sure to response to that.Could u rephrase that?"
def chat():
    print("Chatbot:Hello! I'm your friendly chatbot.type 'exit' to end the conversation.")
    while True:
        user_input=input("You: ").strip()
        if user_input.lower()=="exit":
            print("Chatbot:Goodbye! Have a great day!")
            break
        response=get_response(user_input)
        print(f"Chatbot{response}")
if __name__=="__main__":
    chat()