import gym
import numpy as np
from stable_baselines3 import PPO
from env import PacAIEnv  # Importa l'ambiente (modifica se necessario)

# Carica il modello salvato
model = PPO.load("./Pac-AI/models/final_model")

# Crea l'ambiente di gioco
env = PacAIEnv()  # Assicurati che l'ambiente sia configurato correttamente

# Reset dell'ambiente
obs = env.reset()

# Esegui il gioco fino al termine
done = False
while not done:
    # L'agente prende una decisione
    action, _states = model.predict(obs, deterministic=False)
    
    # Fai eseguire l'azione all'ambiente
    obs, reward, done, info = env.step(action)
    
    # Renderizza l'ambiente per visualizzare il gioco
    env.render()

# Chiudi l'ambiente quando il gioco finisce
env.close()