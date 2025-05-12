import glob
from pathlib import Path
import json

for patches in glob.glob('patches/json/*.json', recursive=True): 
    with open(patches, 'r') as file:
      md = open('_patch/_template.md', 'r')
      md_body = open('_patch/_template_body.md', 'r')
      template = md.read()
      cont = json.load(file)
      blank = ''
      data = cont['patch']
      title = data[0].get('title', blank)
      site_title = data[0].get('site_game_title', blank)
      extras = data[0].get('site_header_info', blank)
      dest_patch = data[0].get('file', 'Decrypted eboot.bin')
      if (site_title != blank):
        title = site_title # prefer page title over games (may have more than one)
      file_header = template.format(patches, title, extras, dest_patch)
      file_body = md_body.read()
      src = Path(patches).name
      dest = src.replace('.json', '.md')
      dest_path = f'_patch/{dest}'
      dest_cont = f'{file_header}{file_body}'
      dest_file = open(dest_path, 'w')
      dest_file.write(dest_cont)
      dest_file.close()
      print('Saved generated file to:', dest_path)
      md = open(dest_path, 'r')
      #print(f'File: {dest_path}\n{md.read()}')
