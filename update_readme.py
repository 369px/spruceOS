import json
import os

# Base directory for ROMs
roms_dir = 'Roms'
files_modified = 0

# Content to add at the beginning
setup_content = """
## How to set up covers for your games:
1. Download the `.PNG` cover you want to use for your game
2. Make sure the `.PNG` file you just downloaded is `498x680px`
3. Change its name to the exact name of its game (eg. `my_game.png` and `my_game.gb`)
4. Put the image in the `imgs` subfolder and you're done!
"""

# Iterate over each console in the Roms directory
for console in os.listdir(roms_dir):
    console_path = os.path.join(roms_dir, console)

    if os.path.isdir(console_path):
        json_path = os.path.join(console_path, 'games.json')
        readme_path = os.path.join(console_path, 'README.md')

        if os.path.exists(json_path):
            with open(json_path) as f:
                data = json.load(f)

            # Access the list of games using the "games" key
            games = data.get("games", [])

            content = setup_content

            if isinstance(games, list):
                content += f"# Check out these {console} games!\n\n"

                # Start the Markdown table
                content += "|        |        |        |        |\n"
                content += "|:----   | :----  | :----  | :----  |\n"

                row_elements = []  # List to keep track of current row elements

                for game in games:
                    if isinstance(game, dict):  # Check if game is a dictionary
                        cover = game.get("cover")
                        name = game.get("name")
                        recommended_by = game.get("recommended_by", [])

                        if cover and name:
                            # Create a table cell with the cover image and game details
                            cell_content = f'<img height="139" src="{cover}">'
                            cell_content += f'<div style="background-color:#eeeeee"><details><summary>{name}</summary><br><i>Recommended by:</i><br>'
                            
                            for user in recommended_by:
                                cell_content += f'<a href="https://github.com/{user}/"><img src="https://avatars.githubusercontent.com/{user}?s=24" align="left"/></a> {user}<br>'
                            
                            cell_content += '</details></div>'
                            
                            row_elements.append(cell_content)  # Add the cell to the current row

                            # If we have 4 elements, complete the row
                            if len(row_elements) == 4:
                                content += '| ' + ' | '.join(row_elements) + ' |\n'
                                row_elements = []  # Reset for the next row
                        else:
                            print(f"Invalid cover or name for game in {console}: {game}")

                    else:
                        print(f"Invalid element in games.json for {console}: {game}")

                # If there are remaining elements in the row, close the last row
                if row_elements:
                    content += '| ' + ' | '.join(row_elements) + ' |\n'

                # Close the Markdown table
                content += '|        |        |        |        |\n'

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
                print(f"The file {json_path} does not contain a list of games.")

if files_modified == 0:
    raise ValueError("No README.md files were updated.")
else:
    print(f"{files_modified} README.md files were updated.")
