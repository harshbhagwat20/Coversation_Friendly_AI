import tkinter as tk

responses ={
    "Hi there! How’s your day going so far?": "That’s great to hear! 😊",
    "What’s something that made you smile today?": "Even small moments can brighten the day!",
    "Are you more of a morning or night person?": "Same here! Those quiet hours are the best.",
    "Do you prefer coffee, tea, or something else?":"Nice choice! Comfort in a cup.",
    "What’s your favorite movie or TV show?": "I’ll have to check that out sometime.",
    "Got any fun plans this weekend?": "Sounds like a fun time ahead!",
    "What kind of music do you usually listen to?": "You’ve got good taste 🎵",
    "Do you like reading books? Any favorites?": "I’ll add that to my virtual reading list!",
    "Would you rather go to the mountains or the beach?": "Nature is healing, right?",
    "If you could have any pet, what would it be?": "Cute! I think you'd be a great pet owner.",
    "What’s your favorite food?": "Yum! That sounds delicious.",
    "Do you like playing video games or board games?": "Nice! I’d totally play that with you if I could.",
    "What’s something you’re really good at?": "That’s awesome—go you! 💪",
    "Do you have a dream travel destination?": "Let’s manifest that trip someday!",
    "If you could learn any new skill instantly, what would it be?": "That’d be such a cool superpower!",
    "What helps you relax after a long day?": "We all need our chill time.",
    "Do you enjoy spending time alone or with others more?": "Totally get that.",
    "Are you someone who likes trying new things?": "That’s the spirit!",
    "Do you believe in aliens? 👽": "The universe is a wild place!",
    "Ever had a funny or embarrassing moment you laugh about now?": "LOL! That’s a great story.",
    "If your life were a movie, what genre would it be?": "I’d totally watch that!",
    "What’s your go-to comfort show or movie?": "Solid choice. Feels like a warm hug.",
    "Have you ever had a silly nickname?": "Haha, that’s adorable.",
    "What's a random fact you love?": "Here’s one from me: Bananas are berries, but strawberries aren’t!",
    "If you had a time machine, what era would you visit?": "Interesting! Time travel would be wild.",
    "What motivates you when you're feeling low?": "That’s powerful. Keep holding on to that.",
    "Do you like rainy days or sunny days more?": "There’s something magical about both.",
    "Would you rather live in a city or countryside?": "Each has its own charm.",
    "What's your favorite holiday or celebration?": "I love that festive vibe too!",
    "Are you a planner or more spontaneous?":"Both ways have their fun!",
    "Do you enjoy cooking or baking?": "I bet your food would smell amazing!",
    "What’s one thing you can’t live without?": "That’s special. Totally get that.",
    "Do you like watching the stars at night?": "Stargazing always feels peaceful.",
    "If you wrote a book, what would it be about?": "I’d read that for sure.",
    "Do you have a favorite childhood memory?": "Aww, that’s sweet.",
    "What's your idea of a perfect weekend?": "That sounds so relaxing.",
    "Have you ever tried something outside your comfort zone?": "That’s how we grow!",
    "Do you like surprises or do you prefer knowing things in advance?": "Totally understandable.",
    "Are you more into cats, dogs, or something else?": "Furry friends are the best.",
    "What’s your favorite season?": "I love how each one has its vibe.",
    "Do you collect anything?": "That's a cool hobby!",
    "What's something you'd like to improve about yourself?": "Growth mindset—respect!",
    "Do you believe in luck or fate?": "That’s a deep one.",
    "What kind of people do you feel most comfortable around?": "Being understood is everything.",
    "What's one thing that instantly makes you happy?": "That's so wholesome!",
    "Would you rather live in the past or future?": "Tough choice, right?",
    "What’s one thing you’ve always wanted to try?": "Let’s add it to the bucket list!",
    "Should we chat again sometime soon?": "I’d love that! You’re a great friend. 😊"
}

def type_response(message, index=0):
    if index < len(message):
        chat_label.config(text=message[:index+1])
        root.after(100, type_response, message, index+1)  # Simulated typing delay
    else:
        entry.config(state=tk.NORMAL)  # Enable entry field after response

def send_message():
    user_message = entry.get().lower()
    response = responses.get(user_message, "I'm not sure how to respond to that.")

    chat_label.config(text="")  # Clear previous text
    entry.delete(0, tk.END)  # Clear input field
    entry.config(state=tk.DISABLED)  # Disable entry field during typing animation
    
    root.after(500, type_response, response)  # Start typing animation

root = tk.Tk()
root.title("Animated Chatbot")

chat_label = tk.Label(root, text="", font=("Arial", 14))
chat_label.pack(pady=20)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()