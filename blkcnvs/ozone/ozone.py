
import time

from blkcnvs.ozone import model, method # ipython patch
#from blkcnvs import model, method # works in vscode
unpck=lambda lst: " ".join(map(str, lst))

pthsrch=method.pathsearch
psx=method.posix
pk=method.peek
nxjsn=method.nexjsons
dcd=method.json_decode
ecd=method.json_encode
dctdeets=method.dctdetails


def main():
    ozones={pth.parent.name: pth.parent for pth in Path.home().glob('*/.meta')}
    bklnks=nxjsn('buk')
    clipsnips=nxjsn('clipr')
    taskdeets=nxjsn('taskr')


def filerename(dirpath, replace=True):
    import os
    if replace:
        for count, fname in enumerate(pk(dirpath)):
            dst=method.rplace(psx(fname))
            src=os.path.join(dirpath, fname)
            dst=os.path.join(dirpath, dst)
            print(
                f"dst: {dst}\n"
                f"src: {src}\n"
                f"{count} files renamed"
            )
