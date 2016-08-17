import os
import sys
import pickle

def basic_file_write(BS_Object_prettified, file_path, append=False):
    if os.path.exists(file_path):
        if append == True:
            pyfile = open(file_path, 'ab')
        else:
            while True:
                print('this will overwrite the file.')
                ans = input('enter y to continue, n to exit')
                if ans.lower() == 'n':
                    sys.exit()
                elif ans.lower() == 'y':
                    break
                else: pass
            pyfile = open(file_path, 'wb')
            print('fillepath {} was overwritten.'.format(file_path))
    else:
        if append == True:
            while True:
                print('file does not exist. create new?')
                ans = input('enter y to continue, n to break')
                if ans.lower() == 'n':
                    exit()
                elif ans.lower() == 'y':
                    break
                else: pass
        pyfile = open(file_path, 'wb')
        print('fillepath {} was created.'.format(file_path))

    ##########################################
    ##This is potentially dangerous###########
    pickle.dump(BS_Object_prettified, pyfile)#
    ##########################################

    print('write appears successful. check file.')
    pyfile.close()

def title_to_filename(BS_object):
    return '{}.htm'.format(str(BS_object.title.contents).strip("']").lstrip("[u'").replace(' ', '_'))

def dummy_func():
    print('this_func_is_far_away')
    print(__file__)