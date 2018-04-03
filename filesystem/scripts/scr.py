import os
import sys
def Unmounting(loc):
    unmount_cmd = 'umount '+loc
    os.system('gksudo '+unmount_cmd)


def MakeExt4System(loc):
    ext_format_cmd = 'mkfs.ext4 '+loc
    os.system('gksudo '+ext_format_cmd)


def MakeNtfsSystem(loc):
    ntfs_format_cmd = 'mkfs.ntfs '+loc
    os.system('gksudo '+ntfs_format_cmd)


def MakeFat32System(loc):
    fat32_format_cmd = 'mkfs.vfat '+loc
    os.system('gksudo '+fat32_format_cmd)

def MakeBtrfsSystem(loc):
    btrfs_format_cmd = 'mkfs.btrfs -f '+loc
    os.system('xterm -e sudo '+btrfs_format_cmd)

def MakeReiserfsSystem(loc):
    reiserfs_format_cmd = 'mkfs.reiserfs '+loc
    os.system('xterm -e sudo '+reiserfs_format_cmd)

def main(type1,loc):
    if type1 == "ext4":
        Unmounting(loc)
        MakeExt4System(loc)
    elif type1 == "ntfs":
        Unmounting(loc)
        MakeNtfsSystem(loc)
    elif type1 == "fat32":
        Unmounting(loc)
        MakeFat32System(loc)
    elif type1 == "reiserfs":
        Unmounting(loc)
        MakeReiserfsSystem(loc)
    elif type1 == "btrfs":
        Unmounting(loc)
        MakeBtrfsSystem(loc)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
