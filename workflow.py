import os
def workflow(in_Path,out_Path):
        print("Starting workflow!")
        print(os.listdir(in_Path))
        for filename in os.listdir(in_Path):
                print('---------------------------')
                print('---------------------------')
                print('---------------------------')
                print('doing '+filename)
                com= "/usr/bin/xvfb-run -a Vaa3D_CentOS_64bit_v3.458/vaa3d -x libvn2 -f app2 -i "+os.path.join(in_Path,filename)+ " -o " + os.path.join(out_Path,filename[:-4])+ ".swc"
                os.system(com)
                #TODO: error handling...

