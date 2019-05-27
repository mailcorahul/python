from FileManipulator import FileManipulator
from PyDaemon import PyDaemon

if __name__ == '__main__':
    
    file_manip = FileManipulator(
                    target_dir='/tmp/py-daemon', 
                    sleep_time=10
                )

    pydaemon = PyDaemon(
                task=file_manip.delete_files,
                log_dir='/tmp/py-daemon', 
                stdout='/tmp/py-daemon/input_cleaner_stdout.txt',
                stderr='/tmp/py-daemon/input_cleaner_stderr.txt',                
                cwd='/tmp/'
                )

    pydaemon.daemonize()