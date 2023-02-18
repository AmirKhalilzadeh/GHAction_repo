import nbformat
import pandas as pd
from glob import glob

def read_nb(nb_filename):
    """Read notebooks and return content."""
    with open(nb_filename, "rb") as nb_file:
        txt = nb_file.read()
    return nbformat.reads(txt, nbformat.NO_CONVERT)

#/Users/khalilza/Github_clones/adsml-units/03_-_C/03_-_CS/03_-_U/notebook.ipynb
#                                       0[12345]*/      */     */notebook.ipynb
# Collect list of 'pre_converted' notebooks
notebooks = sorted(glob("*.ipynb"))


# nb_filename= 'P1.ipynb'

# Go through all notebooks
print("Start checking Markdown comments")
for nb in notebooks:

    print("Looking at notebook %s" % nb)
    # Load notebook
    nb_json = read_nb(nb)

    # Collect markdowns 
    MD = []
    for c in nb_json['cells']:
        if c['cell_type']=='markdown':
            MD.append(c['source'])
        

    # Exclude the headers
    md=[]
    for i in range(len(MD)):
        if MD[i].startswith('#') is False:
            md.append(MD[i])

   # total number of words in the Markdown cells
    if len(md):
        print('total # of words is: ' pd.Series(MD).apply(lambda x: len(x.split())).sum())  
        print('but excluding headers there are: ' pd.Series(md).apply(lambda x: len(x.split())).sum())  
