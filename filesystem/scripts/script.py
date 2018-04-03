import os
import sys
def Unmounting(loc):
    print("unmounting file system : ")
    unmount_cmd = 'umount '+loc
    os.system('gksudo '+unmount_cmd)


def MakeExt4System(loc):
    ext_format_cmd = 'mkfs.ext4 '+loc
    print("formating file system ")
    os.system('gksudo '+ext_format_cmd)


def MakeNtfsSystem(loc):
    ntfs_format_cmd = 'mkfs.ntfs '+loc
    print("formating file system ")
    os.system('gksudo '+ntfs_format_cmd)


def MakeFat32System(loc):
    fat32_format_cmd = 'mkfs.vfat '+loc
    print("formating file system ")
    os.system('gksudo '+fat32_format_cmd)


def main(type1,loc):
    if type1 == "ext4":
        Unmounting(loc)
        MakeExt4System(loc)
    elif type1 == "ntfs":
        Unmounting(loc)
        MakeNtfsSystem(loc)
    elif type1 == "fat32":
        print("fat")
        Unmounting(loc)
        MakeFat32System(loc)
    #else:
    #    print ("jhgdsaj")
if __name__ == '__main__':
    print(sys.argv[1]+" "+sys.argv[2])
    main(sys.argv[1],sys.argv[2])