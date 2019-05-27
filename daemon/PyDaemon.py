import sys
import os

import daemon

class PyDaemon():
    """ A Generic Python Daemon class """
    def __init__(self, task, 
            log_dir, stdout, stderr, root=None, cwd='.'):
        self.task = task
        self.log_dir = log_dir
        self.root = root
        self.cwd = cwd

        # create log directory and standard input/error files
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.stdout = open(stdout, 'a')
        self.stderr = open(stderr, 'a')

    def daemonize(self):
        """ Creates a python daemon process """
        print('[INFO] Creating daemon process...')
        with daemon.DaemonContext(
            chroot_directory=self.root,
            working_directory=self.cwd,
            stdout=self.stdout,
            stderr=self.stderr):
            # daemonize the task
            self.task(last_modified=60)
