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
    "title": "Python Developer for Oil & Gas",
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
    "tagline": (
        "Python developer building monitoring, automation and data tools "
        "for oil and gas. I turn production data into decisions people can act on."
    ),
    "about": [
        "I'm a Python developer who wants to work where software meets engineering. "
        "I care about tools that give operators clearer visibility and take "
        "repetitive manual work off their plate.",
        "My Oilfield Management System grew out of that interest: watching pressure, "
        "oil rate and water cut together, and spotting operational risks early.",
        "I graduated from Enugu State University of Science and Technology (ESUT). "
        "I'm looking to grow across software development, automation and the energy "
        "industry, and to collaborate with professionals on practical problems.",
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
    {"slug": "decline-curve-analyzer", "title": "Decline Curve Analyzer",
     "category": "Forecasting", "year": "2026", "status": "In progress",
     "image": "images/me.jpg", "stack": "Python, SciPy, Matplotlib", "role": "Development",
     "summary": "Fit Arps decline models to rate data and forecast production.",
     "desc": "A tool that fits exponential, hyperbolic and harmonic decline models to production data and forecasts future rates.",
     "url": "https://github.com/wazicode"},
    {"slug": "well-anomaly-detector", "title": "Well Anomaly Detector",
     "category": "Automation & Monitoring", "year": "2026", "status": "Planned",
     "image": "images/me.jpg", "stack": "Python, Pandas", "role": "Development",
     "summary": "Flag sudden pressure drops and rising water cut from well data.",
     "desc": "Rule-based and statistical checks that flag abnormal pressure drops and rising water cut so engineers see problems early.",
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
