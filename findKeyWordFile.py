import os

def whichFile(query, directory):
    for root, dirs, files in os.walk(directory):
        for fname in files:
            if os.path.isfile(fname) and os.access(fname, os.R_OK): 
                with open(fname) as f:
                    if query in f.read():
                        print 'found %s in file %s' %(query, fname)
                        f.close()
                    

if __name__ == '__main__':
    directory = input('search directory :')
    query = input('search keyword :')
    whichFile(query, directory)
