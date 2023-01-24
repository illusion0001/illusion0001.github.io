import glob
from pathlib import Path
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    # assume CI is in GH folder
    for patches in glob.glob('patches/xml/*.xml', recursive=True): 
        with open(patches, 'r') as file:
          md = open('_patch/_template.md', 'r')
          md_body = open('_patch/_template_body.md', 'r')
          template = md.read()
          with open(patches, 'r') as fr:
            string_data = fr.read()
            root = ET.fromstring(string_data)
            meta_tag = root.find('Metadata')
            title = meta_tag.attrib['Title']
            file_header = template.format(patches, title)
            file_body = md_body.read()
            file_body = file_body.replace('REPLACE_DATA', string_data)
            src = Path(patches).name
            dest = src.replace('.xml', '.md')
            dest_path = f'_patch/{dest}'
            dest_cont = f'{file_header}{file_body}'
            dest_file = open(dest_path, 'w')
            dest_file.write(dest_cont)
            dest_file.close()
            print('Saved generated file to:', dest_path)
            md = open(dest_path, 'r')
