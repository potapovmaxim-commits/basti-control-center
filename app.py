#!/usr/bin/env python3
"""
Basti Control Center - Backend API
Liefert Live-Daten für das Dashboard
"""

from flask import Flask, jsonify, render_template_string
import json
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/status')
def api_status():
    """System-Status"""
    return jsonify({
        "agent_name": "Basti",
        "status": "online",
        "uptime": get_uptime(),
        "version": "2.0.0",
        "model": "Kimi 2.6",
        "last_heartbeat": datetime.now().strftime("%H:%M:%S")
    })

@app.route('/api/tasks')
def api_tasks():
    """Aktuelle Tasks"""
    return jsonify({
        "pending": [
            {"task": "Gmail-Sortierung", "status": "running", "next_run": "13:30"},
            {"task": "Heartbeat-Check", "status": "running", "next_run": "13:30"},
            {"task": "Skills laden", "status": "completed", "time": "12:56"}
        ],
        "completed_today": 42
    })

@app.route('/api/skills')
def api_skills():
    """Installierte Skills"""
    skills = [
        {"name": "skill-vetter", "version": "1.0.0", "status": "active"},
        {"name": "self-improving-agent", "version": "3.0.18", "status": "active"},
        {"name": "humanizer", "version": "1.0.0", "status": "active"},
        {"name": "github", "version": "1.0.0", "status": "active"},
        {"name": "ontology", "version": "1.0.4", "status": "active"},
        {"name": "business", "version": "1.1.0", "status": "active"},
        {"name": "openclaw-youtube", "version": "1.0.0", "status": "active"}
    ]
    return jsonify({"total": len(skills), "skills": skills})

@app.route('/api/email-stats')
def api_email():
    """Email-Statistiken"""
    return jsonify({
        "today_sorted": 7,
        "total_unread": 20,
        "categories": {
            "arbeit": 6,
            "newsletter": 7,
            "werbung": 7
        }
    })

@app.route('/api/learnigs')
def api_learnigs():
    """Gelernte Lessons"""
    return jsonify({
        "total_learnings": 3,
        "recent": [
            {"lesson": "Nur lauffähigen Code schreiben", "date": "2026-04-25"},
            {"lesson": "Rate-Limiting für Business", "date": "2026-04-30"},
            {"lesson": "Keine doppelten Nachrichten", "date": "2026-04-30"}
        ]
    })

def get_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
        hours = int(uptime_seconds // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        return f"{hours}h {minutes}m"
    except:
        return "unknown"

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 Basti Control Center</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0a0a1a;
            color: #fff;
            font-family: 'Segoe UI', sans-serif;
            min-height: 100vh;
        }
        .header {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            padding: 20px 40px;
            border-bottom: 2px solid #e94560;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .header h1 {
            font-size: 2em;
            background: linear-gradient(45deg, #e94560, #ff6b6b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .status-badge {
            background: #00d9ff;
            color: #0a0a1a;
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: bold;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
        .container {
            padding: 30px 40px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            max-width: 1400px;
            margin: 0 auto;
        }
        .card {
            background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%);
            border-radius: 15px;
            padding: 25px;
            border: 1px solid rgba(233, 69, 96, 0.3);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(233, 69, 96, 0.3);
        }
        .card h2 {
            color: #e94560;
            margin-bottom: 15px;
            font-size: 1.3em;
        }
        .stat-row {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        .stat-value {
            color: #00d9ff;
            font-weight: bold;
        }
        .progress-bar {
            background: rgba(255,255,255,0.1);
            height: 8px;
            border-radius: 4px;
            margin-top: 5px;
            overflow: hidden;
        }
        .progress-fill {
            background: linear-gradient(90deg, #e94560, #00d9ff);
            height: 100%;
            border-radius: 4px;
            transition: width 0.5s;
        }
        .skill-tag {
            display: inline-block;
            background: rgba(0, 217, 255, 0.2);
            color: #00d9ff;
            padding: 4px 12px;
            border-radius: 12px;
            margin: 3px;
            font-size: 0.85em;
        }
        .task-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .task-status {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-right: 10px;
        }
        .status-running { background: #00ff88; animation: pulse 1.5s infinite; }
        .status-completed { background: #00d9ff; }
        .status-pending { background: #ffd700; }
        .learning-item {
            background: rgba(255,255,255,0.05);
            padding: 10px;
            border-radius: 8px;
            margin: 8px 0;
            border-left: 3px solid #e94560;
        }
        .footer {
            text-align: center;
            padding: 20px;
            color: rgba(255,255,255,0.5);
            font-size: 0.9em;
        }
        .refresh-btn {
            background: #e94560;
            color: white;
            border: none;
            padding: 10px 25px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 1em;
            margin-top: 10px;
        }
        .refresh-btn:hover { background: #ff6b6b; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 Basti Control Center</h1>
        <span class="status-badge">● ONLINE</span>
    </div>
    
    <div class="container">
        <!-- Status Card -->
        <div class="card">
            <h2>🤖 Agent Status</h2>
            <div class="stat-row">
                <span>Name</span>
                <span class="stat-value">Basti</span>
            </div>
            <div class="stat-row">
                <span>Status</span>
                <span class="stat-value" style="color: #00ff88;">Online</span>
            </div>
            <div class="stat-row">
                <span>Uptime</span>
                <span class="stat-value" id="uptime">Lädt...</span>
            </div>
            <div class="stat-row">
                <span>Modell</span>
                <span class="stat-value">Kimi 2.6</span>
            </div>
            <div class="stat-row">
                <span>Letzter Heartbeat</span>
                <span class="stat-value" id="last-beat">Jetzt</span>
            </div>
        </div>
        
        <!-- Tasks Card -->
        <div class="card">
            <h2>📋 Aktive Tasks</h2>
            <div id="tasks-list">
                <div class="task-item">
                    <div style="display: flex; align-items: center;">
                        <span class="task-status status-running"></span>
                        <span>Gmail-Sortierung</span>
                    </div>
                    <span style="color: #00ff88; font-size: 0.9em;">Läuft</span>
                </div>
                <div class="task-item">
                    <div style="display: flex; align-items: center;">
                        <span class="task-status status-running"></span>
                        <span>Heartbeat-Check</span>
                    </div>
                    <span style="color: #00ff88; font-size: 0.9em;">Läuft</span>
                </div>
                <div class="task-item">
                    <div style="display: flex; align-items: center;">
                        <span class="task-status status-completed"></span>
                        <span>Skills laden</span>
                    </div>
                    <span style="color: #00d9ff; font-size: 0.9em;">Fertig</span>
                </div>
            </div>
            <div class="stat-row" style="margin-top: 15px;">
                <span>Heute erledigt</span>
                <span class="stat-value">42 Tasks</span>
            </div>
        </div>
        
        <!-- Email Stats -->
        <div class="card">
            <h2>📧 Email-Statistiken</h2>
            <div class="stat-row">
                <span>Heute sortiert</span>
                <span class="stat-value">7x</span>
            </div>
            <div class="stat-row">
                <span>Ungelesen</span>
                <span class="stat-value">20</span>
            </div>
            <div style="margin-top: 15px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span style="font-size: 0.9em;">Arbeit</span>
                    <span style="font-size: 0.9em; color: #00d9ff;">6</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 30%"></div>
                </div>
            </div>
            <div style="margin-top: 10px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span style="font-size: 0.9em;">Newsletter</span>
                    <span style="font-size: 0.9em; color: #00d9ff;">7</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 35%"></div>
                </div>
            </div>
            <div style="margin-top: 10px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span style="font-size: 0.9em;">Werbung</span>
                    <span style="font-size: 0.9em; color: #00d9ff;">7</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 35%"></div>
                </div>
            </div>
        </div>
        
        <!-- Skills Card -->
        <div class="card">
            <h2>🛠️ Skills (7 Aktiv)</h2>
            <div id="skills-list" style="margin-top: 10px;">
                <span class="skill-tag">skill-vetter</span>
                <span class="skill-tag">self-improving</span>
                <span class="skill-tag">humanizer</span>
                <span class="skill-tag">github</span>
                <span class="skill-tag">ontology</span>
                <span class="skill-tag">business</span>
                <span class="skill-tag">youtube</span>
            </div>
            <div class="stat-row" style="margin-top: 15px;">
                <span>Gesamt installiert</span>
                <span class="stat-value">7 Skills</span>
            </div>
            <button class="refresh-btn" onclick="location.reload()">🔄 Aktualisieren</button>
        </div>
        
        <!-- Learnings Card -->
        <div class="card">
            <h2>🧠 Fortbildungen</h2>
            <div id="learnings-list">
                <div class="learning-item">
                    <strong style="color: #e94560;">Lesson #1</strong><br>
                    <span style="font-size: 0.9em;">Nur lauffähigen Code schreiben</span><br>
                    <span style="font-size: 0.8em; color: rgba(255,255,255,0.5);">2026-04-25</span>
                </div>
                <div class="learning-item">
                    <strong style="color: #e94560;">Lesson #2</strong><br>
                    <span style="font-size: 0.9em;">Rate-Limiting für Business</span><br>
                    <span style="font-size: 0.8em; color: rgba(255,255,255,0.5);">2026-04-30</span>
                </div>
                <div class="learning-item">
                    <strong style="color: #e94560;">Lesson #3</strong><br>
                    <span style="font-size: 0.9em;">Keine doppelten Nachrichten</span><br>
                    <span style="font-size: 0.8em; color: rgba(255,255,255,0.5);">2026-04-30</span>
                </div>
            </div>
            <div class="stat-row" style="margin-top: 15px;">
                <span>Gesamt gelernt</span>
                <span class="stat-value">3 Lessons</span>
            </div>
        </div>
        
        <!-- API Usage -->
        <div class="card">
            <h2>📊 API-Nutzung</h2>
            <div class="stat-row">
                <span>YouTube API</span>
                <span class="stat-value">4/8.000</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 0.5%"></div>
            </div>
            <div class="stat-row" style="margin-top: 15px;">
                <span>Gmail API</span>
                <span class="stat-value">7/Tag</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 1%"></div>
            </div>
            <div class="stat-row" style="margin-top: 15px;">
                <span>Kimi 2.6</span>
                <span class="stat-value">Kostenlos</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 100%; background: #00ff88;"></div>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>🚀 Basti Control Center v2.0 | OpenClaw Agent | Maxim Potapov</p>
        <p style="margin-top: 5px; font-size: 0.8em;">Letzte Aktualisierung: <span id="update-time"></span></p>
    </div>
    
    <script>
        document.getElementById('update-time').textContent = new Date().toLocaleString('de-DE');
        
        // Auto-refresh alle 30 Sekunden
        setInterval(() => {
            fetch('/api/status')
                .then(r => r.json())
                .then(data => {
                    document.getElementById('uptime').textContent = data.uptime;
                    document.getElementById('last-beat').textContent = data.last_heartbeat;
                });
        }, 30000);
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
