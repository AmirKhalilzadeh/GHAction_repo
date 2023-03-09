import os
import glob
import base64
import nbformat
import numpy as np
import pandas as pd
from github import Github

#------------------------------------------------------------
def get_notebooks(user, remote_repo_name, local_repo_name):
    """
    Uses Github API to get notebooks
    
    Parameters
    ----------  
    
    Yields
    ------
    """

    cnt=0
    for repo in user.get_repos():
 
        if any(word in repo.full_name for word in remote_repo_name):

            print("Full name:", repo.full_name)
            if '2422-1295' in repo.full_name:
                continue

            for content in repo.get_contents(""):
                
                print(content.path, content.type)
                
                if content.type == 'dir':
                    
                    for subcontent in repo.get_contents(content.path):
                        
                        if subcontent.path.endswith(".ipynb"):
                            print(subcontent.path, subcontent.type, subcontent.encoding)

                            if subcontent.encoding == 'base64':
                                filename = os.path.join(local_repo_name, f"{repo.full_name.replace('/', '-')}-{subcontent.path.replace('/', '-')}") 
                                with open(filename, "wb") as f:
                                    f.write(subcontent.decoded_content)                   

                            elif subcontent.encoding != 'base64':

                                tmp = repo.get_git_blob(subcontent.sha)
                                content64 = base64.b64decode(tmp.content)

                                filename = os.path.join(local_repo_name, f"{repo.full_name.replace('/', '-')}-{subcontent.path.replace('/', '-')}") 
                                with open(filename, "wb") as f:
                                    f.write(content64.decode("utf8").encode())
                                                
                else:
                    if content.path.endswith(".ipynb"):
                        print(content.path, content.encoding)

    #                    repo_name.append(repo.full_name)

                        if content.encoding == 'base64':
                            filename = os.path.join(local_repo_name, f"{repo.full_name.replace('/', '-')}-{content.path}") 
                            with open(filename, "wb") as f:
                                f.write(content.decoded_content)                   

                        elif content.encoding != 'base64':

                            tmp = repo.get_git_blob(content.sha)
                            content64 = base64.b64decode(tmp.content)

                            filename = os.path.join(local_repo_name, f"{repo.full_name.replace('/', '-')}-{content.path}") 
                            with open(filename, "wb") as f:
                                f.write(content64.decode("utf8").encode())
            cnt+=1    
    return cnt

#------------------------------------------------------------
def count_words(notebooks):
    """
    Read notebooks and return word count
    
    Parameters
    ----------  
    
    Yields
    ------
    """
    
    word_count = []
    cnt=0
    stop_words = ['final','revised','modified','resubmit','feedback','corrected', 'update','new','suggestion', 'checkpoints','v2','v3','v4','v5','v6']
    for nb in sorted(notebooks): # 

            if all(x not in nb for x in stop_words):

                # Load notebook
                nb_json = read_nb(nb)

                # Collect markdowns 
                MD = []
                for c in nb_json['cells']:
                    if c['cell_type']=='markdown':
                        MD.append(c['source'])

                word_count.append([nb, pd.Series(MD).apply(lambda x: len(x.split())).sum()])
                cnt+=1                    
    return word_count, cnt

#------------------------------------------------------------
def read_nb(nb_filename):
    """
    Read notebooks and return content

    Parameters
    ----------  
    
    Yields
    ------
    """
    with open(nb_filename, "rb") as nb_file:
        txt = nb_file.read()
    return nbformat.reads(txt, nbformat.NO_CONVERT)

