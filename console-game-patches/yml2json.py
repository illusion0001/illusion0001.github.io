import glob
from pathlib import Path
import yaml
import os
import struct

title_str           = 'title'
app_ver_str         = 'app_ver'
app_titleid_str     = 'app_titleid'
app_elf_str         = 'app_elf'
patch_ver_str       = 'patch_ver'
name_str            = 'name'
author_str          = 'author'
note_str            = 'note'

# https://stackoverflow.com/a/6117042
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

rlist = { '\n': '\\n', '\"': '\\"', '\x00' : '' }

for patches in glob.glob('_patch0/orbis/*.yml', recursive=True):
  json_str = ''
  convert_text_byte = False
  with open(patches, 'r') as file:
    patch_file = yaml.safe_load(file)
    json_str += '{\n'
    json_str += '  "patch": [\n'
    for i in range(0, len(patch_file)):
      if (patch_file[i].get(title_str,'') == 'Gravity Rush 2 (Gravity Daze 2)'):
        convert_text_byte = True
      json_str += '    {\n'
      json_str += ('      "{}": "{}",\n'.format(title_str, patch_file[i].get(title_str,'')))
      json_str += ('      "{}": [ '.format(app_titleid_str))
      for ids in range(0, len(patch_file[i][app_titleid_str])):
        json_str += ('\"{}\", '.format(patch_file[i].get(app_titleid_str,'')[ids]))
      json_str += ('],\n')
      json_str += ('      "{}": "{}",\n'.format(app_ver_str, patch_file[i].get(app_ver_str,'')))
      json_str += ('      "{}": "{}",\n'.format(app_elf_str, patch_file[i].get(app_elf_str,'')))
      json_str += ('      "{}": "{}",\n'.format(patch_ver_str, patch_file[i].get(patch_ver_str,'')))
      json_str += ('      "{}": "{}",\n'.format(name_str, patch_file[i].get(name_str,'')))
      json_str += ('      "{}": "{}",\n'.format(author_str, patch_file[i].get(author_str,'')))
      json_str += ('      "{}": "{}",\n'.format(note_str, replace_all(patch_file[i].get(note_str,''),rlist)))
      json_str += ('      "patch_list": [\n')
      for patch_data in patch_file[i]['patch_list']:
        bytes = ''
        if (patch_data[0] == 'bytes'):
          json_str += ('        { "type": "%s", "addr": "0x%08x", "value": "%s" },\n' % (patch_data[0],patch_data[1],patch_data[2].replace(' ', '')))
        elif (patch_data[0] == 'byte'):
            json_str += ('        { "type": "%s", "addr": "0x%08x", "value": "0x%02x" },\n' % (patch_data[0],patch_data[1],patch_data[2]))
        elif (patch_data[0] == 'bytes16'):
            json_str += ('        { "type": "%s", "addr": "0x%08x", "value": "0x%04x" },\n' % (patch_data[0],patch_data[1],patch_data[2]))
        elif (patch_data[0] == 'bytes32'):
            json_str += ('        { "type": "%s", "addr": "0x%08x", "value": "0x%08x" },\n' % (patch_data[0],patch_data[1],patch_data[2]))
        elif (patch_data[0] == 'bytes64'):
            json_str += ('        { "type": "%s", "addr": "0x%08x", "value": "0x%016x" },\n' % (patch_data[0],patch_data[1],patch_data[2]))
        elif (patch_data[0] == 'float32' or patch_data[0] == 'float64'):
            json_str += ('        { "type": "%s", "addr": "0x%08x", "value": "%s" },\n' % (patch_data[0],patch_data[1],patch_data[2]))
        elif (patch_data[0] == 'utf8'):
            bytes = ''
            if (convert_text_byte == True):
              for byte in patch_data[2]:
                  bytes += byte.encode('utf-8').hex()
              json_str += ('        { "type": "%s", "addr": "0x%08x", "value": "%s" },\n' % ('bytes',patch_data[1],bytes))
            else:
              json_str += ('        { "type": "%s", "addr": "0x%08x", "value": "%s" },\n' % (patch_data[0],patch_data[1],replace_all(patch_data[2],rlist)))
        elif (patch_data[0] == 'utf16'):
            bytes = ''
            if (convert_text_byte == True):
              for byte in patch_data[2]:
                  bytes += byte.encode('utf-16le').hex()
              json_str += ('        { "type": "%s", "addr": "0x%08x", "value": "%s" },\n' % ('bytes',patch_data[1],bytes))
            else:
              json_str += ('        { "type": "%s", "addr": "0x%08x", "value": "%s" },\n' % (patch_data[0],patch_data[1],replace_all(patch_data[2],rlist)))
      json_str += '      ]\n'
      json_str += '    },\n'
      file = Path(patches.replace('.yml','.json')).name
      newfile = ('_patch0/orbis_new/{}'.format(file))
      with open(newfile, 'w') as fr1:
        fr1.write(json_str)
      for title_ids in patch_file:
        for ids in range(0, len(title_ids[app_titleid_str])):
          output = ("output/json/{}.json".format(title_ids[app_titleid_str][ids]))
          with open(output, 'w') as fw:
            fw.write(json_str)
