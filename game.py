from speech import speech
import random
import time

# Livelli di difficoltà
livelli = {
    "facile": ["agenda", "ami", "souris"],
    "medio" : ["ordinateur", "algorithme", "développeur"],
    "difficile" : ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
}

def play_game(level):
    words = livelli.get(level, [])  # Selezione delle parole in base al livello di difficoltà
    if not words:
        print("Livello non trovato")
        return

    score = 0
    num_attempts = 3  # Il numero di tentativi per parola

    for _ in range(num_attempts):
        random_word = random.choice(words)
        print(f"Si prega di pronunciare la parola {random_word}")
        recog_word = speech("fr-FR")
        print(recog_word)

        if random_word == recog_word:
            print("Hai indovinato")
            score += 1
        else:
            print(f"La parola pronunciata non è corretta. {random_word}")
        
        time.sleep(2)
    
    print(f"Il gioco è finito. Il tuo punteggio è {score}/{len(words)}")

selected_level = input("Selezionare il livello di difficoltà (facile/medio/difficile):").lower()
