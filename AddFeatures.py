import os
import sys
import subprocess
import xml.etree.ElementTree as ET

def add_permissions_to_manifest(apk_file):
    # Use apktool to decompile the APK
    subprocess.run(['apktool', 'd', apk_file])
    
    # Get the name of the decompiled directory
    decompiled_dir = os.path.splitext(apk_file)[0]
    
    # Go to manifestfile.xml
    manifest_file = os.path.join(decompiled_dir, 'AndroidManifest.xml')
    
    # Parse the manifest file
    tree = ET.parse(manifest_file)
    root = tree.getroot()
    
    # Add the permissions to the manifest
    permissions = {
        'uses-permission': [
            'android.permission.ACCESS_NETWORK_STATE',
            
        ],
        'app_permissions': [
            'android.permission.WRITE_EXTERNAL_STORAGE',
            'android.permission.RECEIVE_BOOT_COMPLETED',
            'android.permission.READ_PHONE_STATE',
            'android.permission.ACCESS_FINE_LOCATION',
            'android.permission.DISABLE_KEYGUARD',
            'android.permission.WAKE_LOCK',
            'android.permission.INTERNET',
            'android.permission.VIBRATE',
        ],
        'api_permissions': [
        	'android.permission.VIBRATE',
        	'android.permission.INTERNET',
        	'android.permission.READ_CONTACTS',
        	'android.permission.ACCESS_NETWORK_STATE',
        ]
    }
    for permission_type, permission_list in permissions.items():
        for permission in permission_list:
            ET.SubElement(root, permission_type, {'android:name': permission})
    tree.write(manifest_file)
    # Recompile the APK
    subprocess.run(['apktool', 'b', decompiled_dir])

# Get the directory containing the APK files
directory = sys.argv[1]

# Loop through all the APK files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.apk'):
        apk_file = os.path.join(directory, filename)
        add_permissions_to_manifest(apk_file)
            
    	


print("Finished modifying all APK files.")

