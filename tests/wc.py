import nbformat
import pandas as pd

def read_nb(nb_filename):
    """Read notebooks and return content."""
    with open(nb_filename, "rb") as nb_file:
        txt = nb_file.read()
    return nbformat.reads(txt, nbformat.NO_CONVERT)

# nb_filename= 'P1.ipynb'
nb_json = read_nb(nb_filename)


    
# Collect markdowns 
MD = []
for c in nb_json['cells']:
    if c['cell_type']=='markdown':
        MD.append(c['source'])
        
# total number of words in the Markdown cells
display('this is total number of words: ' pd.Series(MD).apply(lambda x: len(x.split())).sum())

# Exclude the headers
md=[]
for i in range(len(MD)):
    if MD[i].startswith('#') is False:
        md.append(MD[i])
        
display('this is total number of words excluding headers: ' pd.Series(md).apply(lambda x: len(x.split())).sum())
