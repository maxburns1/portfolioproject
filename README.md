# AI Portfolio Site — Setup Guide

## 1. Initial setup

```bash
# Create project + app
django-admin startproject portfolio .
python manage.py startapp projects

# Install Pillow for ImageField support
pip install Pillow
```

## 2. Drop in the files

Place each file from this scaffold at the matching path:

```
portfolio/
├── portfolio/
│   ├── settings.py         ← merge in SETTINGS_SNIPPET.py contents
│   └── urls.py             ← replace with provided urls.py
├── projects/
│   ├── models.py           ← provided
│   ├── forms.py            ← provided
│   ├── views.py            ← provided
│   ├── urls.py             ← provided
│   └── admin.py            ← provided
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── skills.html
│   ├── contact.html
│   └── projects/
│       ├── project_list.html
│       └── project_detail.html
└── static/
    └── css/
```

## 3. Migrate and create admin user

```bash
python manage.py makemigrations projects
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` to log in.

## 4. Adding your 6 projects via Django admin

The `admin.py` file already registers `Project` and `ContactMessage`. When you log into `/admin/`, you'll see "Projects" in the sidebar. Click **Add Project** and fill in:

- **Title**: e.g. "Customer Support Chatbot"
- **Slug**: auto-fills from title (leave blank or edit)
- **Summary**: one sentence
- **Category**: pick from dropdown (AI / ML / Automation / Web / Media)
- **Image**: upload a screenshot
- **Link**: GitHub or live demo URL
- **Business Problem / Tools Used / Key Features / Role / Challenge / Lessons** — fill out each in plain text. For `key_features`, **put one feature per line** — the template renders it as a bulleted list. For `tools_used`, use **comma-separated values** (e.g. `Python, Django, OpenAI API, PostgreSQL`).
- **Is Featured**: tick this for the 3 projects you want on the home page hero
- **Order**: lower numbers display first (e.g. 1, 2, 3...)

### Suggested project entries for your interview

1. **Customer Support Chatbot** — category: AI
2. **n8n Multi-Step Agent Workflow** — category: Automation / Agents
3. **LangChain Research Agent** — category: AI
4. **Google AI Studio Media Generator** — category: Generative Media
5. **Customer Churn Predictor (scikit-learn)** — category: Machine Learning
6. **Campus SkillSwap (Django)** — category: Web Development

## 5. Customize before the interview

- Replace `Your Name` / `YourName` in `base.html` (navbar brand + footer)
- Update the bio copy in `templates/about.html`
- Fill in real company names, dates, and bullets in `templates/skills.html`
- Add your GitHub/LinkedIn URLs in the footer of `base.html`
- Drop a real headshot/logo in `static/` if you want one

## 6. Notes on the design

- **Color palette**: Slate (`#0f172a`, `#334155`), Navy (`#1e3a8a`), Accent Blue (`#3b82f6`), White
- **Typography**: Inter for body, JetBrains Mono for code/tools
- **Layout**: Card-based with subtle hover lift, generous whitespace, no gradients beyond the hero
- **Detail pages**: Each section has its own icon + heading so an interviewer can scan straight to "Biggest Challenge" or "Lessons Learned"
