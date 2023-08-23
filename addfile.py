# STEP 2
import sys
import os
import shutil
import csv

# Verifico che sia stato specificato un solo argomento dalla linea di comando
if len(sys.argv) != 2:
    print("Usage: python addfile.py <filename>")
    sys.exit(1)

# Ottengo il nome del file, imposto il percorso della cartella e costruisco il percorso del file
filename = sys.argv[1]
folder_path = 'files'
filepath = os.path.join(folder_path, filename)

# Verifico se il file esiste, altrimenti stampa un messaggio e termina lo script
if not os.path.exists(filepath):
    print(f"File {filename} does not exist.")
    sys.exit(1)

# Ottengo l'estensione del file
ext = os.path.splitext(filename)[1]

# Distinguo il tipo di file in base all'estensione, altrimenti stampa un messaggio e termina lo script
if ext in ['.mp3', '.wav']:
    file_type = 'audio'
elif ext in ['.txt', '.odt', '.docx']:
    file_type = 'doc'
elif ext in ['.png', '.jpg', '.jpeg']:
    file_type = 'image'
else:
    print(f"File type not supported.")
    sys.exit(1)

# Creo la sottodirectory se non esiste
sub_dir = os.path.join(folder_path, file_type + 's')
if not os.path.exists(sub_dir):
    os.makedirs(sub_dir)

# Sposto il file nella sottodirectory appropriata
shutil.move(filepath, os.path.join(sub_dir, filename))

# Aggiorno il file recap.csv
recap_file = os.path.join(folder_path, 'recap.csv')
with open(recap_file, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([filename, file_type])