import json
import os

# Directory base delle ROMS
roms_dir = 'Roms'
files_modified = 0

# Contenuto da aggiungere
setup_content = """
## How to set up covers for your games:
1. Download the `.PNG` cover you want to use for your game
2. Make sure the `.PNG` file you just downloaded is `498x680px`
3. Change its name to the exact name of its game (eg. `my_game.png` and `my_game.gb`)
4. Put the image in the `imgs` subfolder and you're done!
"""

# Itera su ogni console nella directory Roms
for console in os.listdir(roms_dir):
    console_path = os.path.join(roms_dir, console)
    
    if os.path.isdir(console_path):
        json_path = os.path.join(console_path, 'games.json')
        readme_path = os.path.join(console_path, 'README.md')
        
        if os.path.exists(json_path):
            with open(json_path) as f:
                data = json.load(f)

            # Accedi alla lista di giochi usando la chiave "games"
            games = data.get("games", [])
            
            if isinstance(games, list):
                # Modifica il titolo in base al nome della cartella
                content = f"# Check out these {console} games!\n\n"  # Aggiornato qui

                for game in games:
                    if isinstance(game, dict):  # Verifica che game sia un dizionario
                        cover = game.get("cover")
                        name = game.get("name")
                        recommended_by = game.get("recommended_by", [])

                        if cover and name:
                            content += f'<img width="123" src="{cover}">\n'
                            content += '<div style="background-color:#eeeeee">\n'
                            content += f'<details>\n  <summary>{name}</summary>\n  <br>\n'
                            content += '  <i>Recommended by:</i>\n  <br>\n'
                            
                            for user in recommended_by:
                                content += f'  <a href="https://github.com/{user}/">\n'
                                content += f'  <img src="https://avatars.githubusercontent.com/{user}?s=24" align="left"/></a> {user}\n  <br>\n'
                            
                            content += '  <br></details></div>\n\n'
                    else:
                        print(f"Elemento non valido in games.json per {console}: {game}")

                # Aggiungi il contenuto di setup_content se non è già presente
                if setup_content.strip() not in content:
                    content += setup_content

                if content:
                    if os.path.exists(readme_path):
                        with open(readme_path, 'r') as f:
                            existing_content = f.read()
                        
                        if content != existing_content:
                            with open(readme_path, 'w') as f:
                                f.write(content)
                            print(f"Updated README.md for {console}.")
                            files_modified += 1
                    else:
                        with open(readme_path, 'w') as f:
                            f.write(content)
                        print(f"Created README.md for {console}.")
                        files_modified += 1
            else:
                print(f"Il file {json_path} non contiene una lista di giochi.")

if files_modified == 0:
    raise ValueError("No README.md files were updated.")
else:
    print(f"{files_modified} README.md files were updated.")
