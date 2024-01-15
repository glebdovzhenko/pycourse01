import os
import shutil


USERS_LIST = [
    'gr-000-ivanov',
    'gr-000-petrov',
    'gr-000-sidorov'
]


source_addr = 'assignments/01_pset.ipynb'
dest_addr = 'assignments'


if __name__ == '__main__':
    abs_source_addr = os.path.join(os.path.dirname(__file__), '..', source_addr)
    source_basename = os.path.basename(source_addr)
    if not os.path.exists(abs_source_addr):
        raise FileNotFoundError(
            'Source file %s does not exist' % abs_source_addr
        )

    dest_addr = dest_addr.split(os.path.sep)

    for uname in USERS_LIST:
        full_uname = 'jupyter-' + uname
        abspath_uhome = os.path.join('/', 'home', full_uname)

        if not os.path.exists(abspath_uhome):
            raise FileNotFoundError(
                'User home dir %s does not exist' % abspath_uhome
            )
        
        abspath_dest = abspath_uhome
        for subdir in dest_addr:
            abspath_dest = os.path.join(abspath_dest, subdir)
            if not os.path.exists(abspath_dest):
                os.mkdir(abspath_dest)
                shutil.chown(
                    abspath_dest,
                    user=full_uname,
                    group=full_uname
                )
        else:
            abspath_dest = os.path.join(abspath_dest, source_basename)

        shutil.copy(
            abs_source_addr,
            abspath_dest
        )
        shutil.chown(
            abspath_dest,
            user=full_uname,
            group=full_uname
        )
