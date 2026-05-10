# 🐍 Python Portfolio Website

A personal portfolio website built with **Flask** + **CSS** to showcase your Python programming journey.

## 📁 Project Structure

```
portfolio/
├── app.py                  ← Flask app & all data (profile, projects, skills)
├── requirements.txt
├── templates/
│   ├── base.html           ← Shared layout (nav + footer)
│   ├── index.html          ← Home page
│   ├── projects.html       ← All projects
│   ├── about.html          ← About + skills + journey
│   └── contact.html        ← Contact form
└── static/
    ├── css/style.css       ← All styles
    └── js/main.js          ← Animations & interactions
```

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
```
http://127.0.0.1:5000
```

## ✏️ Customising

All content lives in **`app.py`** — just edit these dictionaries:

| Variable  | What it controls                       |
|-----------|----------------------------------------|
| `PROFILE` | Name, bio, email, GitHub, LinkedIn     |
| `SKILLS`  | Skill name, emoji icon, level (0–100)  |
| `PROJECTS`| Title, description, tags, colour       |
| `JOURNEY` | Timeline milestones                    |

## 📄 Pages

| Route       | Page            |
|-------------|-----------------|
| `/`         | Home            |
| `/projects` | All projects    |
| `/about`    | About + skills  |
| `/contact`  | Contact form    |

## 🎨 Design Features

- Dark editorial aesthetic with teal accent colour
- Animated skill bars and scroll-triggered reveals
- Animated number counters on the hero section
- Responsive mobile layout with hamburger menu
- Noise texture overlay for depth
- Sticky glassmorphism navigation
