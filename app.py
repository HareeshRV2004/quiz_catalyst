from flask import Flask, render_template, request

app = Flask(__name__)

# Define your quiz data
quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Rome'],
        'correct_answer': 'Paris'
    },
    # Add more questions here
]

@app.route('/')
def index():
    return render_template('quiz.html', questions=quiz_questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for question in quiz_questions:
        user_answer = request.form.get(question['question'])
        if user_answer == question['correct_answer']:
            score += 1
    return f'Your score is {score}/{len(quiz_questions)}'

if __name__ == '__main__':
    app.run(debug=True)
