from flask import Flask, render_template

app = Flask(__name__)

# ── Data ────────────────────────────────────────────────────────────────────

PROFILE = {
    "name": "Dip Bhattacharyya",
    "tagline": "Python Developer · 300+ Exercises Completed",
    "bio": (
        "A self-driven programmer who fell in love with Python and never looked back. "
        "Started from zero, built up through 300+ hands-on exercises covering core and "
        "advanced Python — and this portfolio is proof of that journey."
    ),
    "email": "dbhattacharyya393@email.com",
    "github": "github.com/Dip393",
    "linkedin": "linkedin.com/in/dip-bhattacharyya-195929279",
}

SKILLS = [
    {"name": "Python Core",       "level": 95, "icon": "🐍"},
    {"name": "OOP & Design",      "level": 88, "icon": "🏗️"},
    {"name": "File I/O",          "level": 85, "icon": "📁"},
    {"name": "Data Structures",   "level": 82, "icon": "🗂️"},
    {"name": "Algorithms",        "level": 78, "icon": "⚙️"},
    {"name": "Flask / Web",       "level": 72, "icon": "🌐"},
    {"name": "NumPy / Pandas",    "level": 70, "icon": "📊"},
    {"name": "Git & GitHub",      "level": 80, "icon": "🔀"},
]

PROJECTS = [
    {
        "title": "Movie Recommender",
        "desc": (
            "Collaborative filtering engine that analyses user ratings to suggest "
            "personalised films. Built with Python, pandas, and a simple Flask UI."
        ),
        "tags": ["Python", "Flask", "Pandas", "ML"],
        "emoji": "🎬",
        "color": "#ff6b6b",
    },
    {
        "title": "Student Grade Tracker",
        "desc": (
            "CLI tool that records, calculates, and visualises student grades using "
            "file I/O, OOP, and matplotlib for quick bar-chart reports."
        ),
        "tags": ["Python", "OOP", "Matplotlib"],
        "emoji": "📚",
        "color": "#4ecdc4",
    },
    {
        "title": "Password Manager",
        "desc": (
            "Secure local password vault with AES encryption, a master-password gate, "
            "and clipboard integration — all built from scratch."
        ),
        "tags": ["Python", "Cryptography", "CLI"],
        "emoji": "🔐",
        "color": "#45b7d1",
    },
    {
        "title": "Web Scraper & Mailer",
        "desc": (
            "Scrapes job listings from a public board daily and e-mails a digest using "
            "BeautifulSoup + smtplib. Runs on a cron schedule."
        ),
        "tags": ["BeautifulSoup", "SMTP", "Automation"],
        "emoji": "🕷️",
        "color": "#f9ca24",
    },
    {
        "title": "Python Quiz Engine",
        "desc": (
            "Interactive quiz app with timed questions, score tracking, and JSON-driven "
            "question banks — great for practising Python concepts."
        ),
        "tags": ["Python", "JSON", "CLI"],
        "emoji": "❓",
        "color": "#6c5ce7",
    },
    {
        "title": "Expense Splitter",
        "desc": (
            "Group-expense calculator that handles unequal splits, currency formatting, "
            "and generates a per-person settlement summary."
        ),
        "tags": ["Python", "Logic", "CLI"],
        "emoji": "💰",
        "color": "#a29bfe",
    },
]

JOURNEY = [
    {"year": "Month 1–2",  "title": "Python Basics",        "desc": "Variables, loops, functions, and conditionals — the building blocks."},
    {"year": "Month 3–4",  "title": "Data Structures",      "desc": "Lists, dicts, sets, tuples, and how to pick the right one."},
    {"year": "Month 5–6",  "title": "OOP Deep Dive",        "desc": "Classes, inheritance, dunder methods, and design patterns."},
    {"year": "Month 7–8",  "title": "Advanced Python",      "desc": "Decorators, generators, context managers, and metaclasses."},
    {"year": "Month 9–10", "title": "Libraries & Projects", "desc": "Flask, pandas, matplotlib — putting it all together."},
    {"year": "Now",        "title": "300+ Exercises Done!", "desc": "Building real projects and sharing them with the world."},
]

# ── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def home():
    return render_template("index.html",
                           profile=PROFILE,
                           skills=SKILLS,
                           projects=PROJECTS,
                           journey=JOURNEY)

@app.route("/projects")
def projects():
    return render_template("projects.html", profile=PROFILE, projects=PROJECTS)

@app.route("/about")
def about():
    return render_template("about.html", profile=PROFILE, skills=SKILLS, journey=JOURNEY)

@app.route("/contact")
def contact():
    return render_template("contact.html", profile=PROFILE)

if __name__ == "__main__":
    app.run(debug=True)
