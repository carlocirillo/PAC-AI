from stable_baselines3 import PPO
from env import PacAIEnv
from stable_baselines3.common.vec_env import DummyVecEnv

save_path = "./Pac-AI/models"

# Crea e wrappa l’ambiente
env = DummyVecEnv([lambda: PacAIEnv(render = False)])

# Inizializza il modello
model = PPO("MlpPolicy", env, verbose=1)

# Addestra per un certo numero di timesteps
try:
    model.learn(total_timesteps=200_000)
except KeyboardInterrupt:
    model.save(f"{save_path}/final_model")
# Salva il modello
model.save(f"{save_path}/final_model")

print("✅ Addestramento completato!")