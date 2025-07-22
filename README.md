# Notes Web App

A simple, modern, and responsive Notes application built with **Flask** (Python) and **SQLite**. Features include CRUD operations, search functionality, and a dark mode toggle.

## ✨ Features

- **Create, Read, Update, Delete (CRUD) Notes**
- **Search Notes** - Instantly filter notes by keyword (client-side and server-side search)
- **Dark/Light Mode Toggle** - Persists user preference using `localStorage`
- **Responsive Design** - Works on mobile, tablet, and desktop
- **Clean and Modern UI** - Card-based layout with smooth animations
- **Timestamps** - Automatically tracks when notes are created/updated

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd notes_app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` doesn't exist, install Flask manually: `pip install flask`)*

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in your browser**
   Visit [http://localhost:5000](http://localhost:5000)

## 🛠️ Project Structure

```
notes_app/
├── app.py              # Flask application
├── notes.db            # SQLite database (auto-created on first run)
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # CSS styles
└── templates/
    ├── base.html      # Base template
    ├── index.html     # Main page (list + create notes)
    └── edit_note.html # Edit note page
```

## 📱 Features in Detail

### Dark Mode
- Toggle between light and dark themes.
- Preference is saved in the browser.

### Search
- Real-time filtering of notes as you type.
- Searches both note titles and content.

### Responsive Design
- Adapts to different screen sizes (mobile, tablet, desktop).
- Touch-friendly buttons and inputs.

## 🔧 Dependencies

- **Flask** - Web framework
- **SQLite** - Database (built-in with Python)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

Built with ❤️ for your coding assessment.
