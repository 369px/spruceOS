import json
import os

# Itera su ogni directory delle console
for console in os.listdir('.'):
    json_path = os.path.join(console, 'games.json')
    readme_path = os.path.join(console, 'README.md')
    
    # Procede solo se esiste il file games.json nella directory
    if os.path.exists(json_path):
        with open(json_path) as f:
            games = json.load(f)
        
        # Crea il contenuto per il README
        content = f"# Check out these games for {console}!\n\n"
        
        for game in games:
            content += f'<img width="123" src="{game["cover"]}">\n'
            content += '<div style="background-color:#eeeeee">\n'
            content += f'<details>\n  <summary>{game["name"]}</summary>\n  <br>\n'
            content += '  <i>Recommended by:</i>\n  <br>\n'
            
            # Aggiungi il link e l'avatar di ciascun collaboratore
            for user in game['recommended_by']:
                content += f'  <a href="https://github.com/{user}/">\n'
                content += f'  <img src="https://avatars.githubusercontent.com/{user}?s=24" align="left"/></a> {user}\n  <br>\n'
            
            content += '  <br></details></div>\n\n'
        
        # Confronta con il contenuto esistente e aggiorna solo se è cambiato
        if os.path.exists(readme_path):
            with open(readme_path, 'r') as f:
                existing_content = f.read()
            
            # Scrivi il nuovo contenuto solo se è diverso
            if content != existing_content:
                with open(readme_path, 'w') as f:
                    f.write(content)
                print(f"README.md updated for {console}")
            else:
                print(f"No changes in README.md for {console}")
        else:
            # Crea il file README.md se non esiste
            with open(readme_path, 'w') as f:
                f.write(content)
            print(f"README.md created for {console}")

print("README.md files generation completed.")
