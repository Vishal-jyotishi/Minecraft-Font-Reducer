import os
import json

def create_resource_pack():
    # Pack Configuration
    pack_name = "SmallerFontPack"
    # 1.20.1 uses format 15. The 'supported_formats' range makes it compatible with newer versions (1.20.4, 1.21+)
    pack_mcmeta = {
        "pack": {
            "pack_format": 15,
            "supported_formats": {"min_inclusive": 15, "max_inclusive": 99},
            "description": "Reduces font size using a custom TTF font."
        }
    }

    # Font Configuration
    # Vanilla size is 11.0. We set it to 8.0 for smaller text.
    # You can change "size" to 6.0 for even smaller, or 9.0 for slightly smaller.
    font_json = {
        "providers": [
            {
                "type": "ttf",
                "file": "minecraft:custom_font.ttf",
                "shift": [0.0, 0.0],
                "size": 8.0,
                "oversample": 2.0
            }
        ]
    }

    # Create Directory Structure
    base_path = os.path.join(os.getcwd(), pack_name)
    font_path = os.path.join(base_path, "assets", "minecraft", "font")
    
    try:
        os.makedirs(font_path, exist_ok=True)
        print(f"Created directories at: {base_path}")
    except OSError as e:
        print(f"Error creating directories: {e}")
        return

    # Write pack.mcmeta
    with open(os.path.join(base_path, "pack.mcmeta"), "w") as f:
        json.dump(pack_mcmeta, f, indent=4)
    print("Generated pack.mcmeta")

    # Write default.json
    with open(os.path.join(font_path, "default.json"), "w") as f:
        json.dump(font_json, f, indent=4)
    print("Generated assets/minecraft/font/default.json")

    # Create a Readme/Placeholder
    readme_text = (
        "ACTION REQUIRED:\n"
        "1. Get a TrueType font file (.ttf).\n"
        "2. Rename it to 'custom_font.ttf'.\n"
        "3. Place it in this folder (assets/minecraft/font/).\n"
        "4. If you want to adjust the size, open 'default.json' and change 'size': 8.0."
    )
    with open(os.path.join(font_path, "PUT_FONT_HERE.txt"), "w") as f:
        f.write(readme_text)

    print("\nSUCCESS! Resource pack folder created.")
    print("IMPORTANT: You must place a file named 'custom_font.ttf' in:")
    print(f"{font_path}")

if __name__ == "__main__":
    create_resource_pack()
