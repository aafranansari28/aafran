import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x aafran')
    os.system('./aafran')
elif bit == '32bit':
    os.system('chmod +x aafran32')
    os.system('./aafran32')
else:
    print('device not supported')
