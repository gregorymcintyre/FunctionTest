#import os
import filecmp

Directory = ['test.py', 'test_all.py']

print('Comparing files ... ')

for files in Directory:
    if filecmp.cmp(str(files), '../r-dailyprogrammer/'+str(files))==False:
        #os.system("cp ../r-dailyprogrammer/" + files + " .")
        print(files + ' contains changes')
    else:
        print(files + ' is up to date')

print("Complete")

#os.system("git status")
