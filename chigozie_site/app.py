"""Personal portfolio site for Agbo Chigozie Anthony, built with Flask.

Preview locally:  python app.py
Build for GitHub: python build.py   (writes static HTML to the build/ folder)
"""
from datetime import datetime

from flask import Flask, abort, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Your content lives here. Edit these and the whole site updates.
# ---------------------------------------------------------------------------
PROFILE = {
    "name": "Agbo Chigozie Anthony",
    "short_name": "Chigozie Agbo",
    "title": "Python Developer",
    "location": "Lagos, Nigeria",
    "email": "",  # add your email to show an Email button, e.g. "you@example.com"
    # Contact form on a static site needs a form service. Create a free form at
    # formspree.io and paste its URL here, e.g. "https://formspree.io/f/abcdwxyz".
    # Leave empty to hide the form and show only your links.
    "form_endpoint": "",
    "phone": "",  # e.g. "+234 800 000 0000"
    "photo": "images/me.jpg",
    "edition": "2026",
    "github": "https://github.com/wazicode",
    "linkedin": "https://www.linkedin.com/in/agbo-chigozie-017192213",
    "tagline": "Python developer focused on software, data and automation for the oil and gas industry.",
    "about": [
        "I'm a Python developer with a strong interest in the oil and gas industry, industrial automation and digital oilfield technologies. I graduated from Enugu State University of Science and Technology (ESUT).",
        "I build tools that connect programming, data analysis and industrial processes: production monitoring, well diagnostics, pressure and oil-rate analysis, water-cut tracking and early detection of operational risks.",
        "My goal is to grow at the intersection of software development, automation and the energy industry, and to work with professionals on practical problems in the field.",
    ],
}

PROJECTS = [
    {"slug": "oilfield-management-system", "title": "Oilfield Management System",
     "category": "Software & Data Visualization", "year": "2025", "status": "Built",
     "image": "images/me.jpg",  # swap for a screenshot of the app: static/images/oilfield.png
     "stack": "Python, Tkinter, Matplotlib", "role": "Design & Development",
     "summary": "Desktop app for production monitoring: pressure and oil-rate analysis, water-cut tracking, trends and risk flags.",
     "desc": "A Python desktop application built around oilfield monitoring. It plots production trends, pressure and oil rate, tracks water cut, and highlights potential operational risks so decisions can be made from data.",
     "url": "https://github.com/wazicode"},
]

SKILLS = {
    "Software": ["Python", "Tkinter desktop apps", "Flask web apps", "Git and GitHub"],
    "Data": ["Matplotlib visualization", "Production data analysis", "Trend and well diagnostics"],
    "Industry": ["Digital oilfield systems", "Industrial automation", "Operational monitoring"],
}


@app.context_processor
def inject_globals():
    return {"p": PROFILE, "year": datetime.now().year, "n_projects": len(PROJECTS)}


@app.route("/")
def home():
    return render_template("home.html", projects=PROJECTS[:3])


@app.route("/work")
def work():
    return render_template("work.html", projects=PROJECTS)


@app.route("/work/<slug>")
def project(slug):
    pr = next((x for x in PROJECTS if x["slug"] == slug), None)
    if pr is None:
        abort(404)
    return render_template("project.html", pr=pr)


@app.route("/about")
def about():
    return render_template("about.html", skills=SKILLS)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
