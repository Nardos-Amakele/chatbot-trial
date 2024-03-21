import random
R_EATING= "I don't like eating anything bacause I'm a bot obviously!"

def unknown():
    response = ['could you please rephrase that?',
                "...",
                "sounds about right",
                "What does that mean"][random.randrange(4)]
    return response