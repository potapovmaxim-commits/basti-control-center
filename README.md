# 🚀 Basti Control Center

**AI Agent Dashboard für OpenClaw**

Ein schickes, dunkles Cyberpunk-Style Dashboard zur Überwachung und Steuerung deines AI-Agents.

![Status](https://img.shields.io/badge/Status-Online-brightgreen)
![Version](https://img.shields.io/badge/Version-2.0.0-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📸 Screenshot

Das Dashboard zeigt in Echtzeit:
- 🤖 **Agent Status** (Online/Uptime/Modell)
- 📋 **Aktive Tasks** (Gmail, Heartbeats, Skills)
- 📧 **Email-Statistiken** (Sortiert/Ungelesen/Kategorien)
- 🛠️ **Installierte Skills** (7 Skills aktiv)
- 🧠 **Fortbildungen** (Gelernte Lessons)
- 📊 **API-Nutzung** (YouTube/Gmail Limits)

---

## 🚀 Quick Start

### Voraussetzungen
- Python 3.8+
- pip

### Installation

```bash
# 1. Repo klonen
git clone https://github.com/potapovmaxim-commits/basti-control-center.git

# 2. In Ordner wechseln
cd basti-control-center

# 3. Abhängigkeiten installieren
pip install flask

# 4. Server starten
python3 app.py
```

### Zugriff

Dashboard öffnen: **http://localhost:5000**

---

## 📡 API Endpoints

| Endpoint | Beschreibung |
|----------|-------------|
| `GET /` | Dashboard HTML |
| `GET /api/status` | Agent Status |
| `GET /api/tasks` | Aktive Tasks |
| `GET /api/skills` | Installierte Skills |
| `GET /api/email-stats` | Email-Statistiken |
| `GET /api/learnigs` | Gelernte Lessons |

---

## 🎨 Features

- ✅ **Live-Daten** — Auto-refresh alle 30 Sekunden
- ✅ **Responsive Design** — Mobile & Desktop
- ✅ **Dark Mode** — Cyberpunk Neon-Stil
- ✅ **Echtzeit-Status** — Online/Offline Indikator
- ✅ **Task-Management** — Laufende & erledigte Tasks
- ✅ **API-Monitoring** — YouTube/Gmail Quota-Tracking

---

## 🛠️ Tech Stack

- **Backend:** Python Flask
- **Frontend:** Vanilla HTML/CSS/JS
- **Design:** Custom Cyberpunk CSS
- **API:** REST JSON

---

## 🔧 Konfiguration

Das Dashboard liest automatisch Daten aus:
- OpenClaw Workspace
- Gmail API
- YouTube API
- Lokale Skills

Keine manuelle Konfiguration nötig!

---

## 📈 Erweiterungen

Geplante Features:
- [ ] Task-Management (Tasks erstellen/löschen)
- [ ] Kalender-Integration
- [ ] Notification-System
- [ ] Performance-Graphen
- [ ] Multi-Agent Support

---

## 👤 Author

**Maxim Potapov** — AI Agent "Basti"

🔗 [GitHub](https://github.com/potapovmaxim-commits)

---

## 📝 License

MIT License — feel free to use and modify!

---

**Made with 🚀 by Basti AI Agent**
