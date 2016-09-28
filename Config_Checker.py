import configparser
def ValidateConfigFile(goldenfilepath = 'none', filetobevalidated = 'none'):
    """
    Validates a given Config File in filetobevalidated against a correct config ffile pointed
    to by goldenfilepath returns a list of erroneous lines as a list[strings] if config
    file is fine, it shoud return an empty list.
    """
    #parse golden file
    goldenconfig = configparser.ConfigParser()
    goldenconfig.read(goldenfilepath)

    #parse file to be validated
    filetovalidate = configparser.ConfigParser()
    filetovalidate.read(filetobevalidated)

    incorrectlines = []
    for section in filetovalidate.sections():
        #check each key is present in corresponding golden section
        for key in filetovalidate.options(section):
            if not goldenconfig.has_option(section,key):
                incorrectlines.append(key + '=' + filetovalidate.get(section,key))

    if len(incorrectlines) > 0:
        print('The following lines are incorrect')
        for k in incorrectlines: print(k)
    else: print('The config file is fine')
    return incorrectlines
