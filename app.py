from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample notes data
notes = ["This is sample note for managing anshika ","practice piano","make reel"]

@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/api/notes', methods=['POST'])
def add_note():
    new_note = request.get_json()
    if 'title' not in new_note or 'content' not in new_note:
        return jsonify({"error": "Title and Content fields are required"}), 400
    notes.append(new_note)
    return jsonify(new_note), 201

if __name__ == '__main__':
    app.run(debug=True)
