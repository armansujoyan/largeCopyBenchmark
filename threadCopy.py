import threading
import shutil

# Create the threads for copying
class copyThread (threading.Thread):
    def __init__(self, srcFiles, target):
        threading.Thread.__init__(self)
        self.srcFiles = srcFiles
        self.target = target
    def run(self):
        copyFiles(self.srcFiles, self.target)

# Function for copying given files
def copyFiles(srcDir, target):
    for fileName in srcDir:
        shutil.copy("./from/file%s.bin" % fileName, target)

# The benchmark function
def threadCopy(segmentLists, target):
    threads = []
    for segmentList in segmentLists:
        thread = copyThread(segmentList, target)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()