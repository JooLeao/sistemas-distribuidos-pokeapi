import os
import requests

SAVE_DIR = "pokemon_images"

def download_pokemon_image(poke_id):
    """Faz o download da imagem de um Pokémon específico pelo seu ID."""
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR, exist_ok=True)
        
    url = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
    
    try:
        response = requests.get(url).json()
        img_url = response.get('sprites', {}).get('front_default')
        
        if img_url:
            img_data = requests.get(img_url).content
            file_path = os.path.join(SAVE_DIR, f"{poke_id}.png")
            
            with open(file_path, 'wb') as handler:
                handler.write(img_data)
                
    except Exception as e:
        print(f"Erro ao descarregar o Pokémon {poke_id}: {e}")