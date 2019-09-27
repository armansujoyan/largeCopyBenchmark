#!/usr/bin/env python3

from subprocess import call
import processCopy as pcf
import threadCopy as tcf
import regularCopy as rcf
import timeit
import shutil
import os

filesCount = 100
filesByteSize = 512
filesFolder = "from"
dest = "./to"
samples = 10

def main():
    if not "from" in os.listdir():
        os.mkdir("from")
    if not "to" in os.listdir():
        os.mkdir("to")

    results = []
    print("Running the tests.")
    for _ in range(0,samples):
        results.append(runTest())

    stSum = 0
    mtSum = 0
    prSum = 0
    for i in range(0,samples):
        stSum += results[i][0]
        mtSum += results[i][1]
        prSum += results[i][2]
        print("Sample %i multithreading: %f" % (i+1, results[i][1]))
        print("Sample %i multiprocessing: %f" % (i+1, results[i][2]))
        print("Sample %i single threaded: %f" % (i+1, results[i][0]))
        print("---------------------------------")

    print("--------------------------------")
    print("Average running times are:")
    print("Single threaded:")
    print(stSum/samples)
    print("Multiple threaded:")
    print(mtSum/samples)
    print("Multiple processes:")
    print(prSum/samples)

    # Clear the created directories
    shutil.rmtree("./from")
    shutil.rmtree("./to")

def runTest():
    # Seed the folders with files if needed
    if not "from" in os.listdir() or len(os.listdir("from")) != 100:
        command = "./genFiles.sh %i %i %s" % (filesCount, filesByteSize, filesFolder)
        call(command, shell=True)
        print("Data is generated. Collecting test results.")

    # Generate segmentation lists
    segmentLists = []
    segmentListElement = []
    for i in range(0,filesCount):
        if(i < 10):
            segmentListElement.append("00%i" % i)
        elif(i >= 100):
            segmentListElement.append("0%i" % i)
        else:
            segmentListElement.append("0%i" % i)
        if (i % 25 == 0 and i != 0) or i == filesCount - 1:
            segmentLists.append(segmentListElement)
            segmentListElement = []

    # Copy the files using processes
    processStartTimer = timeit.default_timer()
    pcf.processCopy(segmentLists, dest)
    processTime = timeit.default_timer() - processStartTimer

    # Clear the destination folder for the next test
    clearDestDir(segmentLists)

    # Copy the files using threads
    threadedStartTimer = timeit.default_timer()
    tcf.threadCopy(segmentLists, dest)
    threadTime = timeit.default_timer() - threadedStartTimer

    # Clear the destination folder for the next test
    shutil.rmtree(dest)

    regStartTimer = timeit.default_timer()
    rcf.regCopy(filesFolder, "to")
    regTime = timeit.default_timer() - regStartTimer

    return [regTime, threadTime, processTime]

def clearDestDir(segmentLists):
    for sgLs in segmentLists:
        for el in sgLs:
            os.remove(os.path.join(dest, "file%s.bin" % el))


if __name__ == "__main__":
	main()