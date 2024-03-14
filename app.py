from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '678965431123445'

quiz_questions = [
  {
    'question': 'What is the capital of France?',
    'options': ['Paris', 'London', 'Berlin', 'Rome'],
    'correct_answer': 'Paris'
  },
  {
    'question': 'What is the largest planet in our solar system?',
    'options': ['Jupiter', 'Saturn', 'Neptune', 'Earth'],
    'correct_answer': 'Jupiter'
  },
]

@app.route('/')
def index():
  if 'current_question_index' not in session:
    session['current_question_index'] = 0
  if 'score' not in session:
    session['score'] = 0

  if session['current_question_index'] >= len(quiz_questions):
    return redirect(url_for('result'))

  question = quiz_questions[session['current_question_index']]
  return render_template('quiz.html', question=question, current_question_index=session['current_question_index'], total_questions=len(quiz_questions), score=session['score'])

@app.route('/submit', methods=['POST'])
def submit():
  user_answer = request.form.get('answer')

  # Increment current_question_index regardless of the answer
  session['current_question_index'] += 1

  if session['current_question_index'] <= len(quiz_questions):
    if user_answer == quiz_questions[session['current_question_index'] - 1]['correct_answer']:
      session['score'] += 1

  return redirect(url_for('index'))

@app.route('/result')
def result():
  score = session.pop('score', 0)
  session.pop('current_question_index', None)
  return render_template('result.html', score=score, total_questions=len(quiz_questions))

if __name__ == '__main__':
  app.run(debug=True)
