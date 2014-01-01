import pickle

def list_pickler(list, file_path):
    '''
    Pickle the list at the given file path
    Returns True if pickling is successful, False otherwise
    '''
    success = False
    try:
        with open(file_path,'wb') as pickle_file:
            pickle.dump(list, pickle_file)
        success = True
    except IOError:
        print 'I/O error in pickling file'
    return success

def unpickler(file_path):
    '''
    Unpickle the file at the given path and return the object
    Returns None if unpickling is unsuccessful
    '''
    pickled_object = None
    try:
        with open(file_path,'rb') as pickle_file:
            pickled_object = pickle.load(pickle_file)
    except IOError:
        print 'I/O error in unpickling file'
    return pickled_object