from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidates_by_name, get_candidates_by_skill, \
    get_candidate_by_id

app = Flask(__name__)

@app.route('/')
def page_main():
    candidates = load_candidates_from_json()
    """
    Главная страница
    """
    return render_template("list.html", candidates = candidates)

@app.route('/candidate/<uid>')
def candidate_single(uid):
    candidates = get_candidate_by_id(uid)
    """Страница про кандидата"""
    return render_template("single.html", candidates = candidates)

@app.route('/search/<candidate_name>')
def search_candidate(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html',candidates = candidates)

@app.route('/skill/<skill_name>')
def search_skills(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, candidates=candidates)

app.run()


# a=page_main()