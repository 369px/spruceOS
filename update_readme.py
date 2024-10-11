import json
import os

# Directory base delle ROMS
roms_dir = 'Roms'
files_modified = 0

# Itera su ogni console nella directory Roms
for console in os.listdir(roms_dir):
    console_path = os.path.join(roms_dir, console)
    
    # Procedi solo se è una directory
    if os.path.isdir(console_path):
        json_path = os.path.join(console_path, 'games.json')
        readme_path = os.path.join(console_path, 'README.md')
        
        # Processa solo se esiste games.json
        if os.path.exists(json_path):
            with open(json_path) as f:
                games = json.load(f)
            
            # Costruisci il contenuto del README
            content = f"# Check out these games for {console}!\n\n"
            for game in games:
                content += f'<img width="123" src="{game["cover"]}">\n'
                content += '<div style="background-color:#eeeeee">\n'
                content += f'<details>\n  <summary>{game["name"]}</summary>\n  <br>\n'
                content += '  <i>Recommended by:</i>\n  <br>\n'
                
                # Aggiungi ogni collaboratore con link GitHub e avatar
                for user in game['recommended_by']:
                    content += f'  <a href="https://github.com/{user}/">\n'
                    content += f'  <img src="https://avatars.githubusercontent.com/{user}?s=24" align="left"/></a> {user}\n  <br>\n'
                
                content += '  <br></details></div>\n\n'
            
            # Aggiorna o crea il README.md
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

# Controlla se sono stati modificati file
if files_modified == 0:
    raise ValueError("No README.md files were updated.")
else:
    print(f"{files_modified} README.md files were updated.")
