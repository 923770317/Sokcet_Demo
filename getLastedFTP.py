import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
File = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror) as e:
        print 'ERROR cannont reach "%s"' % HOST
    print '*** Connect to host "%s"' % HOST

    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR:cannot login anonymously'
        f.quit()
        return
    print '*** Logged in as "anonymous"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR:cannot cd to "%s"' % DIRN
        f.quit()
        return
    print '*** Change to "%s"' % DIRN

    try:
        f.retrbinary('RETR %S' % File,open(File,'wb').write)
    except ftplib.error_perm:
        print 'ERROR:cannot read file "%s"' % File
        os.unlink(File)
        return

    else:
        print '*** Downloaded "%s" to CWD' % File

    f.quit()

if __name__ == "__main__":
    main()