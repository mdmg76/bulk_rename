import os
# import re

# Directory path to process
root_dir = "data"

# Renaming pattern: replace '_sample_' with '_ remastered_'
# pattern = re.compile(r'_sample_')

# Loop through files and rename
for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        print(dirpath, _, filename)
        # Split filename into parts
        filename2 = filename.replace(".docx", "")
        parts = filename2.split(" (")
        new_filename = parts[0]+".docx"
        new_filename = os.path.join(dirpath, new_filename)
        os.rename(os.path.join(dirpath,filename), new_filename)
        # print(new_filename)

        # # Apply renaming logic
        # new_parts = [part for part in parts if not pattern.search(part)]
        # if new_parts:
        #     new_filename = '_'.join(new_parts)

        #     # Construct new filename
        #     new_filename = os.path.join(dirpath, new_filename)

        #     # Rename file
        #     os.rename(os.path.join(dirpath, filename), new_filename)