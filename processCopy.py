import shutil
import multiprocessing as mp

# The benchmark function
def processCopy(segmentLists, dest):
    copyPool = mp.Pool(processes=len(segmentLists))
    for sgLs in segmentLists:
        copyPool.apply_async(copyFiles, [sgLs, dest])
    copyPool.close()
    copyPool.join()

# Function for copying given files
def copyFiles(srcDir, target):
    for fileName in srcDir:
        shutil.copy("./from/file%s.bin" % fileName, target)