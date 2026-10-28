# Chigozie's portfolio (Flask, hosted on GitHub Pages)

## Preview locally
    python -m venv venv
    venv\Scripts\activate        # Windows  (macOS/Linux: source venv/bin/activate)
    pip install -r requirements.txt
    python app.py
Open http://127.0.0.1:5000

## Edit your content
Everything (profile, projects, skills) is at the top of `app.py`.

## Publish on GitHub Pages
1. Create a GitHub repo. Name it `wazicode.github.io` to get https://wazicode.github.io
   (any other name works too, the site will live at /repo-name).
2. Push this folder to the `main` branch.
3. In the repo: Settings > Pages > Source: choose "GitHub Actions".
4. The workflow in `.github/workflows/deploy.yml` builds and publishes on every push.

## Contact form
GitHub Pages has no server, so the form needs a form service. Create a free form at
formspree.io and paste its URL into `form_endpoint` in `app.py`.
