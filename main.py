import time
import os
import subprocess

def main():

    def test(sTime, path):
        testFile = os.path.join(path, 'testfile') 
        f = open(testFile,'wb+')
        print 'testing ...'
        for i in range(0,1600000):
           f.write('we are testing write speed')
        f.close()
        diff = time.clock() - sTime
        speed = (os.stat(testFile).st_size/1048576)/diff
        os.unlink(testFile)
        startTime = time.clock()
        return speed

    def selectPath():
        path = os.path.curdir
        # path option provided after detecting operating system
        if os.name == 'posix':
            print subprocess.check_output("df")
            path = raw_input("Please type the mounted on path of disk e.g /Volumes/ABC ")
        if os.name == 'nt':
            path = raw_input("Enter the Drive Letter of Removale Drive. e.g I ")
            path= path.split(":")
    
        if not os.path.exists(path):
            print 'please enter a valid path'
            selectPath()
            
        return path

    path = selectPath()
    #testFile = path+":/speedTest"
    print "Checking your Removable Drive Speed......"
    startTime = time.clock()
    speed = test(startTime, path)
    print "Your disk drive speed is %s mb/sec" %speed


if __name__ == "__main__":
    main()
    
