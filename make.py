import os
import shutil
import re
from subprocess import call

from translater import translate

translator = translate()

# Définitions des variables globales
project_root = os.path.dirname(os.path.abspath(__file__))
script_dir = os.path.join(project_root, 'scripts')
icon_path = os.path.join(script_dir, 'ico', '{}.ico')
spec_file_path = '{}.spec'


# Fonction d'aide pour l'étape 2
def get_verification_choice():
    while True:
        print()
        translator.print_message("Voulez-vous vérifier les fichiers après chaque réécriture?", progressive_display=True)
        print()
        translator.print_message("1 - Oui")
        translator.print_message("2 - Non")
        print()
        translator.print_message("Votre choix : ", progressive_display=True)
        choice = input()
        if choice in ['1', '2']:
            return choice
        else:
            print()
            translator.print_message("Choix invalide. Veuillez réessayer.", progressive_display=True)
            print()

# Étape 1 : Nettoyage des fichiers cache
exts_to_delete = ['.pyc', '.pyo', '~']
dirs_to_delete = ['__pycache__']
for root, dirs, files in os.walk('.', topdown=False):
    for d in dirs:
        if d in dirs_to_delete:
            shutil.rmtree(os.path.join(root, d))
    for f in files:
        if any(f.endswith(ext) for ext in exts_to_delete):
            os.remove(os.path.join(root, f))



# Étape 2 : Interrogation de l'utilisateur
translator.print_message("Veuillez entrer le nom du programme : ", progressive_display=True)
file_name = input()
print()

translator.print_message("Veuillez entrer la version du programme (sans espace ni symboles) : ", progressive_display=True)
version = input()
print()

# Vérification du format de la version
if not re.match("^[A-Za-z0-9]+$", version):
    print()
    translator.print_message("Erreur: La version ne doit contenir que des lettres et des chiffres.", progressive_display=True)
    print()
    exit()

# Demande de vérification à l'utilisateur
verification_choice = get_verification_choice()




# Étape 3 : Préparer les lignes pour le fichier .spec
file_name = file_name.lower()
icon_path = os.path.join(script_dir, 'assets', 'ico', '{}.ico'.format(file_name))  # Adjusted the path to include 'assets' folder
datas_lines = [
    (os.path.join(script_dir, f, fname).replace('/', '\\\\'), f)
    for f in os.listdir(script_dir) 
    if os.path.isdir(os.path.join(script_dir, f)) 
    for fname in os.listdir(os.path.join(script_dir, f))
]

# Ajouter la ligne pour l'icône
datas_lines.append((icon_path.replace('/', '\\\\'), 'assets'))

analysis_line = os.path.join(script_dir, 'main.py')


# Étape 4 : Création et modification du fichier .spec
spec_file_path = spec_file_path.format(file_name)
spec_content_template = '''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['{analysis_line}'],
    pathex=[],
    binaries=[],
    datas=[
    {datas_lines}
    ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={{}},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='{file_name}',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='{icon_path}')

coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=False, upx_exclude=[], name='{file_name}')
'''


new_spec_content = spec_content_template.format(
    analysis_line=analysis_line.replace('\\', '\\\\'), 
    datas_lines=',\n    '.join(str(t) for t in datas_lines), 
    icon_path=icon_path.replace('\\', '\\\\'), 
    file_name=file_name
)
with open(spec_file_path, 'w') as file:
    file.write(new_spec_content)

if verification_choice == '1':
    with open(spec_file_path, 'r') as file:
        translator.print_message(file.read())

    print()
    translator.print_message("Appuyez sur Entrée pour continuer...", progressive_display=True)
    input()
    print()



# Étape 5 : Lancement de pyinstaller
translator.print_message("Lancement de pyinstaller...")
call(f'pyinstaller {spec_file_path}', shell=True)
translator.print_message("Opération terminée.")




# Étape 6 : Création du contenu pour le fichier setup.iss
clean_program_name = re.sub(r'\W+', '', file_name)

# Trouver les paths nécessaires
icon_path = ''
license_path = ''
dist_path = os.path.join(project_root, 'dist') + "\\*"

for root, dirs, files in os.walk(project_root):
    for file in files:
        if file.endswith('.ico'):
            icon_path = os.path.join(root, file)
        elif 'license' in file.lower():
            license_path = os.path.join(root, file)
    if icon_path and license_path:
        break

setup_iss_content = f"""
[Setup]
SetupIconFile="{icon_path}"
AppName="{file_name.lower()}"
AppVersion={version}
DefaultDirName={{pf}}\\{file_name.lower()}
OutputBaseFilename={clean_program_name}_installer_{version}
ArchitecturesInstallIn64BitMode=x64
LicenseFile="{license_path}"
WizardStyle=modern
WizardResizable=yes
DisableDirPage=no
AlwaysShowDirOnReadyPage=yes
AppendDefaultDirName=yes

[Files]
Source: "{dist_path}"; DestDir: "{{app}}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Tasks]
Name: "desktopicon"; Description: "{{cm:CreateDesktopIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"; Flags: unchecked

[Icons]
Name: "{{commondesktop}}\\{clean_program_name}"; Filename: "{{app}}\\{clean_program_name}\\{clean_program_name}.exe"; Tasks: desktopicon

[Run]
Filename: "{{app}}\\{clean_program_name}\\{clean_program_name}.exe"; Description: "{{cm:LaunchProgram, {clean_program_name}}}"; Flags: nowait postinstall skipifsilent
"""

# Écrire le contenu dans le fichier setup.iss
setup_iss_path = os.path.join(os.getcwd(), 'setup.iss')
with open(setup_iss_path, 'w') as setup_file:
    setup_file.write(setup_iss_content)
print()
translator.print_message("Le fichier setup.iss a été modifié avec succès.", progressive_display=True)
print()


# Étape 7 : Lancement du fichier .iss
print()
translator.print_message("Lancement du fichier setup.iss...", progressive_display=True)
print()
call(f'{setup_iss_path}', shell=True)

print()
translator.print_message("Travail terminé.", progressive_display=True)
print()
exit()