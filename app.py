from flask import Flask, render_template, request
import re
import long_responses as long

app = Flask(__name__, static_folder='static')

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainity = 0
    has_required_words = True
    for word in user_message:
        if word in recognized_words:
            message_certainity += 1
    percentage = float(message_certainity) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how', 'you'])
    response(long.R_ACCESSRATINGS, ['how','to','access','ratings','and','reviews'], required_words=['access','ratings','reviews'])
    response(long.R_HEALTHCARE, ['what','is','centralized','healthcare','system'], required_words=['what','healthcare','system','centralized'])
    response(long.R_RATEREVIEW,  ['can','a','patient','rate','and','review'], required_words=['how','rate','review'])
    response(long.R_REGISTER,['how','do','I', 'register'], required_words=['how','register']) 
    response(long.R_SECURE, ['is','my','medical','record','secure'], required_words=['secure','security'])   
    response(long.R_SUPPORT, ['where','can','I','contact','you'], required_words=['contact','where'])   
    response(long.R_VIEWRECORDS, ['where','to','see','view','my','medical','records'], required_words=['my','records'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!$.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return response


if __name__ == '__main__':
    app.run()