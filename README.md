# PAC-AI 🧠👾

**PAC-AI** is a Reinforcement Learning (RL) agent that learns to play the classic **Pac-Man** game using **Stable-Baselines3**. The environment is built from scratch or adapted from a custom Pac-Man implementation, and the agent learns optimal strategies through trial and error using modern deep RL algorithms.

---

## 📦 Features

- 🎮 Custom Pac-Man environment compatible with OpenAI Gym interface.
- 🧠 RL agent trained using Stable-Baselines3 (PPO, A2C, DQN, etc.).
- 📈 Logging and visualization with TensorBoard.
- 💾 Model saving/loading for easy experimentation.
- 🔍 Modular and clean codebase for extensibility.

---

## 🧰 Installation

```bash
git clone https://github.com/carlocirillo/PAC-AI.git
cd PAC-AI
pip install -r requirements.txt
```

---

## 🚀 Training

Start the training by running the Pac-AI/train.py module

```bash
python .\Pac-AI\train.py
```

## 🤖 Visualize progress

You can visualize the training of the agent by running Pac-AI/play.py

```bash
python .\Pac-AI\play.py
```