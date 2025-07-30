from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open("data/projects.json") as f:
        projects = json.load(f)
    return render_template("index.html", projects=projects)

@app.route('/about')
def about():
    with open("data/profile.json", "r") as f:
        profile_data = json.load(f)
    return render_template("about.html", profile=profile_data)




@app.route('/resume')
def resume():
    with open("data/education.json", encoding="utf-8") as f:
        education = json.load(f)
    with open("data/certifications.json", encoding="utf-8") as f:
        certifications = json.load(f)
    with open("data/experience.json", encoding="utf-8") as f:
        experience = json.load(f)
    return render_template('resume.html', education=education, certifications=certifications, experience=experience)


if __name__ == '__main__':
    app.run(debug=True)
