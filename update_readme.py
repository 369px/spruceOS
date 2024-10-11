import json
import os

# Contatore per i file modificati
files_modified = 0

for console in os.listdir('.'):
    json_path = os.path.join(console, 'games.json')
    readme_path = os.path.join(console, 'README.md')

    if os.path.exists(json_path):
        print(f"Processing {json_path}")  # Stampa di debug

        with open(json_path) as f:
            games = json.load(f)
        
        content = f"# Check out these games for {console}!\n\n"
        
        for game in games:
            content += f'<img width="123" src="{game["cover"]}">\n'
            content += '<div style="background-color:#eeeeee">\n'
            content += f'<details>\n  <summary>{game["name"]}</summary>\n  <br>\n'
            content += '  <i>Recommended by:</i>\n  <br>\n'
            
            for user in game['recommended_by']:
                content += f'  <a href="https://github.com/{user}/">\n'
                content += f'  <img src="https://avatars.githubusercontent.com/{user}?s=24" align="left"/></a> {user}\n  <br>\n'
            
            content += '  <br></details></div>\n\n'
        
        # Se esiste il README, controlla il contenuto
        if os.path.exists(readme_path):
            with open(readme_path, 'r') as f:
                existing_content = f.read()
            
            if content != existing_content:
                with open(readme_path, 'w') as f:
                    f.write(content)
                files_modified += 1
        else:
            # Crea il file README se non esiste
            with open(readme_path, 'w') as f:
                f.write(content)
            files_modified += 1

print("README.md files generated for each console.")

# Termina con un errore se nessun file è stato modificato (opzionale)
if files_modified == 0:
    print("No README.md files were updated.")
