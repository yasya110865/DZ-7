import os.path


def save_listdir():
    '''

    :return: сохранение содержимого рабочей директории в файл
    '''
    import os
    import json
    if os.path.exists('listdir.json'):
        with open('listdir.json', 'r') as f:
            listdir = json.load(f)
    else:
        listdir = {}

    path = os.getcwd()
    dirlist = [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))]
    listdir['dirs'] = dirlist
    filelist = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))]
    listdir['files'] = filelist
    with open('listdir.json', 'w') as f:
        json.dump(listdir, f)

save_listdir()

def test_savelistdir():
    assert os.path.exists('listdir.json') == True