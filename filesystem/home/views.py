from django.shortcuts import render
import os
import  scripts.script as sc

from django.conf.urls import url
from django.http import HttpResponse


# Create your views here.
import scripts.scr as sc
'''
<option value="ext4">1. Ext4 (Supported by Linux)</option>
<option value="fat32">2. FAT32 (Supported by most Systems)</option>
<option value="ntfs">3. NTFS (Supported by Windows)</option>
<option  value="reiserfs">4. ReiserFS (Supported by most systems)</option>
<option value="btrfs">5. Btrfs (Supported by most systems)</option>
'''

s={
    "ext4":"Ext4 (Supported by Linux)",
    "fat32":"FAT32 (Supported by most Systems)",
    "ntfs":"NTFS (Supported by Windows)",
    "reiserfs":"ReiserFS (Supported by most systems)",
    "btrfs":"Btrfs (Supported by most systems)"
}
#print(s.keys())
def home(request):
    #return HttpResponse("hello")
    data = os.popen('df -h').read()
    return render(request, 'home/seminar.html', {"data": data, "s": s})

def submit(request):
    data = os.popen('df -h').read()
    loc = request.POST["loc"]
    filesys = request.POST["filesys"]
    print(loc+" "+filesys)
    sc.main(filesys,loc)
    return render(request, "home/seminar.html",{"data": data})
    # do something with info