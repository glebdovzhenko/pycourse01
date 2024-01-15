import os
import shutil


USERS_LIST = [
    'gr-000-ivanov',
    'gr-000-petrov',
    'gr-000-sidorov'
]


source_addr = 'assignments/01_pset.ipynb'
dest_addr = ''


if __name__ == '__main__':
    abs_source_addr = os.path.join(os.path.dirname(__file__), source_addr)
    source_basename = os.path.basename(source_addr)
    if not os.path.exists(abs_source_addr):
        raise FileNotFoundError(
            'Source file %s does not exist' % abs_source_addr
        )


    for uname in USERS_LIST:
        abspath_uhome = os.path.join('/', 'home', 'jupyter-' + uname)
        if not os.path.exists(abspath_uhome):
            raise FileNotFoundError(
                'User home dir %s does not exist' % abspath_uhome
            )
        
        abspath_dest = os.path.join(abspath_uhome, source_basename)
        shutil.copy(
            abs_source_addr,
            abspath_dest
        )
        shutil.chown(
            abspath_dest,
            user=uname,
            group=uname
        )
