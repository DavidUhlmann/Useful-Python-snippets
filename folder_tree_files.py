from pathlib import Path
import os
import pandas as pd
import time

# create link to drive that needs to be scanned
dir_to_scan = 'drive:/Users/.....' #here put your folder/drive
p = Path(dir_to_scan)

folders = []
files = []

# this code (the two following functions) are taken from stackoverflow
# :https://stackoverflow.com/questions/2104080/how-to-check-file-size-in-python
def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

# this code was partly taken from http://pbpython.com/pathlib-intro.html
# a great site to look at bye the way
def print_directories():
	for entry in os.scandir(p):
	    if entry.is_dir():
	        folders.append(entry)
	    elif entry.is_file():
	        files.append(entry)

	print("Folders - {}".format(folders))
	print("Files - {}".format(files))

def main(p):
	all_files = []
	for i in p.rglob('*.*'):
	    value_size = file_size(i)
	    modify_time = time.ctime(os.path.getmtime(i))
	    all_files.append((i.name, i.parent, value_size, time.ctime(i.stat().st_ctime), modify_time))

	columns = ["Dateiname", "Pfad", "Dateigrösse", "Erstellt", "Zuletzt geändert"]
	df = pd.DataFrame.from_records(all_files, columns=columns)
	df.to_csv('output_directory.csv') #exports the file to CSV which is the first output

    # get a dataframe from excel and change it
	df_excel = pd.read_csv('output_directory.csv')
	df_output = df_excel[df_excel['Dateigrösse'].str.contains('GB|MB')==True] # works and just selets GB or MB files
	df_output.to_excel('output_directory.xlsx')
	print('Done: all files have been exported to working directory!')

if __name__ == '__main__':
	main(p)
