🎮 Seven — A 2D Arcade Shooter Game (Python + Arcade Library)

Seven is a fast-paced 2D top-down shooter built in Python using the Arcade framework.
You control a player who can move freely, shoot enemies, pick up upgrades (coming soon), and survive as long as possible while the game gets harder over time.

🚀 Features
✅ Core Gameplay

Smooth WASD movement

Shoot using SPACE

Increasing difficulty (enemy speed scales with score)

Animated health bar

Score counter

Background changes every 100 points

Custom player & enemy sprites

Explosion effect on enemy death

Game Over screen with restart option

🎧 Audio

Background music

Shooting sound

Game Over sound

🎆 Effects

Particle-based explosion when enemies die

Enemy spawn logic improves with score

🕹️ Controls
Key	Action
W / A / S / D	Move player
SPACE	Shoot
R	Restart after Game Over


🛠️ Installation
1️⃣ Clone the repository
git clone https://github.com/<your-username>/Seven.git
cd Seven

2️⃣ Create virtual environment (recommended)
python -m venv .venv


Activate:

Windows PowerShell

.\.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt


If you don’t have requirements.txt, generate one:

pip freeze > requirements.txt

4️⃣ Run the game
python seven/main.py

📁 Project Structure
Seven/
│
├── seven/
│   ├── assets/
│   │   ├── images/
│   │   └── sounds/
│   │
│   ├── entities/
│   │   ├── player.py
│   │   ├── enemy.py
│   │   ├── bullet.py
│   │   ├── explosion.py
│   │   └── powerup.py   (coming soon)
│   │
│   ├── utils/
│   │   └── collisions.py
│   │
│   ├── game.py
│   ├── main.py
│   └── settings.py
│
├── .gitignore
└── README.md

🧭 Roadmap
🎯 Current Todo List

 Enemy types (fast, zig-zag, tank)

 Power-ups (shield, spread-shot, rapid fire)

 Boss fight every 500 score

 Smoke & spark explosion upgrade

 Screen shake effect on kills

 Better UI (health icons, animated score)

 Game logo & title screen

🎮 Future Enhancements

 Save high score

 Settings menu (sound volume, controls)

 Mobile support / touch controls

 Optional story mode (campaign)

🤝 Contributing

Pull requests are welcome.
If you’re adding large features, open an issue first to discuss the change.



💬 Developed by

Anirudh
Built with ❤️ using Python + Arcade