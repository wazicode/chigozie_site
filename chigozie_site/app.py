"""Personal portfolio site for Agbo Chigozie Anthony, built with Flask.

Preview locally:  python app.py
Build for GitHub: python build.py   (writes static HTML to the build/ folder)
"""
from datetime import datetime

from flask import Flask, render_template

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
    {
        "title": "Oilfield Management System",
        "summary": "Python desktop app for production monitoring: pressure and oil-rate "
                   "analysis, water-cut tracking, trends and risk flags.",
        "stack": "Python, Tkinter, Matplotlib",
        "year": "2025",
        "status": "Built",
        "url": "https://github.com/wazicode",
    },
    # Replace the two below with real projects as you finish them.
    {
        "title": "Decline Curve Analyzer",
        "summary": "Fit Arps decline models to rate data and forecast production.",
        "stack": "Python, SciPy, Matplotlib",
        "year": "2026",
        "status": "In progress",
        "url": "https://github.com/wazicode",
    },
    {
        "title": "Well Anomaly Detector",
        "summary": "Flag sudden pressure drops and rising water cut from well data.",
        "stack": "Python, Pandas",
        "year": "2026",
        "status": "Planned",
        "url": "https://github.com/wazicode",
    },
]

SKILLS = {
    "Software": ["Python", "Tkinter desktop apps", "Flask web apps", "Git and GitHub"],
    "Data": ["Matplotlib visualization", "Production data analysis", "Trend and well diagnostics"],
    "Industry": ["Digital oilfield systems", "Industrial automation", "Operational monitoring"],
}


@app.context_processor
def inject_globals():
    return {"p": PROFILE, "year": datetime.now().year}


@app.route("/")
def home():
    return render_template("home.html", projects=PROJECTS[:3])


@app.route("/work")
def work():
    return render_template("work.html", projects=PROJECTS)


@app.route("/about")
def about():
    return render_template("about.html", skills=SKILLS)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
