import os
import shortuuid
import time


class FileManipulator():
    """ Class for manipulating files, folders -- create, delete etc. """
    def __init__(self, target_dir, sleep_time):
        self.target_dir = target_dir
        self.sleep_time = sleep_time

    def create_folder(self):

        while True:
            folder = shortuuid.uuid()
            print('[INFO] Creating {}'.format(folder))
            os.makedirs(os.path.join(self.target_dir, folder))

            time.sleep(self.sleep_time)

    def delete_files(self, last_modified=30):
        """ 
        Deletes files from a target dir periodically
    
        Args:
            last_modified:  last modified time in minutes            

        """

        while True:
            current_time = int(time.time())
            files = os.listdir(self.target_dir)
            for file in files:
                try:
                    file_path = os.path.join(self.target_dir, file)
                    file_ctime = os.path.getctime(file_path)                                        

                    # Deletes a file if its last modified time exceeds 'last_modified'
                    if (current_time - file_ctime)//60 >= last_modified:
                        os.unlink(file_path)
                        print('{} deleted'.format(file))

                except Exception as e:
                    print(e)

            time.sleep(self.sleep_time)
