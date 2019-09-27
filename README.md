# Copy strategy Benchmarking

The scripts presented here try to solve the problem of copying big amount of files from one directory to another using single thread, multiple threads and processes. Definitions for each file and the results of tests are written below. Our strategy of testing will include copying **1,2** and **3GB** of files from one directory to another. Measured execution times present here will differ from your computers since the conducted test heavily depends on the type of hardware that we use. Our initial guess about tests is, that parallel processes/threads will have a better running time.

# Script structure

Different copy types are divided into modules and imported in the main test script. The multithreading and process methods use 4 threads/methods for copying the files. The naming convention for the generated files is file***.bin and all the files are seeded into the folder named **from** after which are copied to the folder named **to**. All the file names are segmented i.e. divided into 4 parts of names and each thread/process takes care of copying one of those parts. For example, if we generate 100 files (which is the case) we will divide it to parts like 0->25, 26->50,51->75,76->99 and for example first thread will copy first 25 files, the second one next 25 files and so on. In order to conduct a test run the fileCopyBenchmark.py script by using:

```
pyton ./fileCopyBenchmark.py
```

Or you can make it executable and simply run it like `./fileCopyBenchmark.py`. For making the file executable you may need to run:

```
chmod +x fileCopyBenchmark.py
```

| File | Description |
| --- | --- |
| fileCopyBenchmark.py | The main script file that runs all tests and prints results  |
| regularCopy.py | Module for copying files with single thread |
| threadCopy.py | Module for copying files with multiple threads |
| processCopy.py | Module for copying files with multiple processes |
| genFiles.sh | Shell script for generating the data to be copied |

## Testing results

There are 4 types of situations tested and those situations differ in file size that has to be copied. The performance for each case is shown in the table below. All the tests were executed 20 times and a sample of 20 execution times was collected. Mean of the execution time is chosen to be an estimator.

| Size | Single Thread | 4 Threads | 4 Processes |
| --- | --- | --- | --- |
| **1GB** | 1.880059161150001 | 1.2220340130999994 | 1.1681056276499995 |
| **2GB** | 3.744077671799997 | 2.1066945315500023 | 2.2774515955555555 |
| **3GB** | 6.689873728549995 | 4.0677183790499966 | 4.0242131774499966 |
| **5GB** | 12.44549148619999 | 10.202657355899984 | 8.3506162059000022 |

## Conclusion

We can see that our initial guess was right, as all the parallelized methods had better performance. We can also notice that the difference between single-threaded and parallelized implementations starts to get noticeable as the size of transferred files increases. We can also notice from the last row of the table that processes start to gain the advantage over threads when the size increases too.
