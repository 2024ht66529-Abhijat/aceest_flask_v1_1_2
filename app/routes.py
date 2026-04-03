from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

PROGRAMS = {
    'Fat Loss (FL)': '2000–2200 kcal, conditioning + HIIT',
    'Muscle Gain (MG)': '3000–3300 kcal, hypertrophy split',
    'Beginner (BG)': 'Maintenance calories, full‑body basics'
}

@routes.route('/', methods=['GET', 'POST'])
def home():
    selected_program = None
    if request.method == 'POST':
        selected_program = PROGRAMS.get(request.form.get('program'))
    return render_template('index.html', programs=PROGRAMS, selected=selected_program)
