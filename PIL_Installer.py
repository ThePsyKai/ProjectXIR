import subprocess
import sys
import os
import bpy

def install_Pillow():
	print("[DEBUG] | PIL Library Verification/Location: " + str(os.getenv("APPDATA")).replace('\\', '/') + '/Blender Foundation/Blender/' + bpy.app.version_string[:bpy.app.version_string.rindex('.')] + '/scripts/addons/Project XIR/verifications/PillowInstalled')
	check = str(os.getenv("APPDATA")).replace('\\', '/') + \
			'/Blender Foundation/Blender/' + \
			bpy.app.version_string[:bpy.app.version_string.rindex('.')] + \
			'/scripts/addons/Project XIR/verifications/PillowInstalled'
	
	if not os.path.exists(check):
		# path to python.exe
		python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
		
		# upgrade pip
		subprocess.call([python_exe, "-m", "ensurepip"])
		subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
		
		# install required packages
		subprocess.call([python_exe,"-m", "pip", "install", "Pillow"])
		with open(check, "wb") as verified:
			pass
		verified.close()
