#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)
messages = []
count = 0

@app.route('/codingchallenge/api/v1.0/messages', methods=['GET']) #return all messages
def get_all_messages():
    return jsonify({'messages': messages})

@app.route('/codingchallenge/api/v1.0/messages/<int:message_id>', methods=['GET']) # return specific message
def get_message(message_id):
    for message in messages:
        print(str(message_id) == message['id'])
        
    message = [message for message in messages if message['id'] == str(message_id)]
    if len(message) == 0: # not found
        abort(404)
    return jsonify({'message': message[0]})

@app.route('/codingchallenge/api/v1.0/messages', methods=['POST']) # add a new message
def create_message():
    global count #access and modify global count
    
    message = [message for message in messages if message['id'] == request.json['id']]
    if (len(message) != 0):
        abort(400, "You have already used this id") #custom error for bad request
    count += count_words(request.json['text'])
    message = {
        'id': request.json['id'],
        'text': request.json['text'],
    }
    messages.append(message)
    return jsonify({'count': count}), 201 #successful

@app.route('/codingchallenge/api/v1.0/messages/<int:message_id>', methods=['PUT'])
def update_message(message_id):

    message = [message for message in messages if message['id'] == str(message_id)]
    print(message)
    if (len(message) == 0):
        abort(404)
    message[0]['id'] = request.json.get('id', message[0]['id'])
    message[0]['text'] = request.json.get('text', message[0]['text'])
    return jsonify({'message': message[0]})



@app.route('/codingchallenge/api/v1.0/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = [message for message in messages if message['id'] == str(message_id)]
    if (len(message) == 0):
        abort(404) 
    messages.remove(message[0])
    return jsonify({'result': True})

def count_words(text):
    count = 0 # local count
    words = text.split(" ") # get all words in order to count them up
    for word in words: #iterate through message 
        count += 1
    return count

if __name__ == '__main__':
    app.run(debug=True)
