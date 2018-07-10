import os
def workflow(in_Path,out_Path):
	for filename in os.listdir(in_Path):
#		com= "Vaa3D_CentOS_64bit_v3.200/vaa3d -x libvn2 -f app2 -i "+in_Path+filename+ "-o out.swc"
		com= "Vaa3D_CentOS_64bit_v3.458/vaa3d -x libvn2 -f app2 -i "+os.path.join(in_Path,filename)+ "-o out.swc"
		os.system(com)
