import json
import os

# Contenuto da aggiungere
setup_content = """
## How to set up covers for your games:
1. Download the `.PNG` cover you want to use for your game
2. Make sure the `.PNG` file you just downloaded is `498x680px`
3. Change its name to the exact name of its game (eg. `my_game.png` and `my_game.gb`)
4. Put the image in the `imgs` subfolder and you're done!
"""

# Iterate over each console directory
for console in os.listdir('.'):
    json_path = os.path.join(console, 'games.json')
    readme_path = os.path.join(console, 'README.md')
    
    # Process only if games.json exists in the directory
    if os.path.exists(json_path):
        with open(json_path) as f:
            games = json.load(f)
        
        # Begin building the README content
        content = f"# Check out these {console} games!\n\n"
        
        for game in games:
            content += f'<img width="123" src="{game["cover"]}">\n'
            content += '<div style="background-color:#eeeeee">\n'
            content += f'<details>\n  <summary>{game["name"]}</summary>\n  <br>\n'
            content += '  <i>Recommended by:</i>\n  <br>\n'
            
            # Add each collaborator's GitHub link and avatar
            for user in game['recommended_by']:
                content += f'  <a href="https://github.com/{user}/">\n'
                content += f'  <img src="https://avatars.githubusercontent.com/{user}?s=24" align="left"/></a> {user}\n  <br>\n'
            
            content += '  <br></details></div>\n\n'
        
        # Read existing README content if it exists
        if os.path.exists(readme_path):
            with open(readme_path, 'r') as f:
                existing_content = f.read()
                
            # Check if setup_content is already present
            if "How to set up covers for your games" not in existing_content:
                existing_content += setup_content  # Append setup instructions

            # Combine new content with existing content
            content = existing_content + content

        # Write the README.md for the specific console
        with open(readme_path, 'w') as f:
            f.write(content)

print("README.md files generated for each console.")
