import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
defaults_dir = os.path.join(script_dir, "defaults")
result_dir = os.path.join(script_dir, "../result")

try:
    settings_file = os.path.join(result_dir, "settings")
    if not os.path.exists(settings_file):
        default_settings_file = "./defaults/settings"
        shutil.copy(default_settings_file, settings_file)
except FileNotFoundError:
    print(f"File '{default_settings_file}' not found.")
except PermissionError:
    print(f"Permission denied for '{settings_file}'.")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    index_file = os.path.join(result_dir, "index")
    if not os.path.exists(index_file):
        default_index_file = "./defaults/index"
        shutil.copy(default_index_file, index_file)
except FileNotFoundError:
    print(f"File '{default_index_file}' not found.")
except PermissionError:
    print(f"Permission denied for '{index_file}'.")
except Exception as e:
    print(f"An error occurred: {e}")