import os
import time
import sys
from subprocess import call
from cytomine.models import Job
import imageio as imgio
from swc_to_tiff_stack import swc_to_tiff_stack

def workflow(in_images, out_path):
    print("Starting workflow!")
    #print(os.listdir(in_path))
    for neubias_input_image in in_images:
        print('---------------------------')
        print('---------------------------')
        print('---------------------------')
        file_path=neubias_input_image.filepath
        filename = neubias_input_image.filename
        out_file_path = os.path.join(out_path, filename)
        print('doing '+file_path)
        #Invert the xy axis by 180 degrees
        print('invert the xy axis by 180 degrees for '+file_path)
        #com = "/usr/bin/xvfb-run -a Vaa3D_CentOS_64bit_v3.458/vaa3d -x Rotate_Image -f xy180 -i "
        # + file_path+ " -o " + os.path.join(out_path,filename)
        command = "/usr/bin/xvfb-run Vaa3D_CentOS_64bit_v3.458/vaa3d -x Rotate_Image -f xy180 -i "+ \
            file_path+ " -o "+ out_file_path
        return_code = call(command, shell=True, cwd="/") # waits for the subprocess to return
        time.sleep(2)#Wait 2 seconds because it can't process all the images for some reason
        #os.system(command)
        print("Runned :"+command)
        #Compute the neuron tracing
        
        command = "/usr/bin/xvfb-run Vaa3D_CentOS_64bit_v3.458/vaa3d -x libvn2 -f app2 -i " + \
            out_file_path + " -o " + out_file_path[:-4]+ ".swc"
        return_code = call(command, shell=True, cwd="/") # waits for the subprocess to return
        time.sleep(2)#Wait 2 seconds because it can't process all the images for some reason
        #os.system(command)
        print("Runned :"+command)
        #im_size = imgio.imread(os.path.join(out_path, filename)).shape
        im_size = imgio.volread(out_file_path).shape #Size is Depth,Height,Width
        im_size = im_size[::-1] #Invert the size order to Width,Height,Depth
        print(im_size)
        #Rename the swc file form *.tif_ini.swc to *.swc
        #Needed for some vaa3d workflow where the output path is not taken into account.
        os.rename(out_file_path[:-4]+".tif_ini.swc", out_file_path[:-4]+ ".swc")
        print("Run:"+' swc_to_tiff_stack('+ out_file_path[:-4] +'.swc, '+ out_path +','+ str(im_size)+')')
        
        # Convert the .swc tracing result to tiff stack files
        swc_to_tiff_stack(out_file_path[:-4]+ ".swc", out_path, im_size)
        #TODO: error handling...
        
    print("Done")    
