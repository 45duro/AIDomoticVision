import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess



block_blob_service = BlockBlobService(account_name='storagejonathan', account_key='uG4ysRyztb86C2wlg+MOrDc+3P/prPWgUlALwGkq6xpPCT2tsQFTMG+cut6MyCHiebRvf+O6kDxvufGmuFpcpw==')

# Create a container called 'quickstartblobs'.
container_name ='joder3'
block_blob_service.create_container(container_name)

# Create a file in Documents to test the upload and download.
local_path=os.path.expanduser("~/Documents")
local_file_name ="video" + str(uuid.uuid4()) + ".avi"
full_path_to_file =os.path.join(local_path, local_file_name)

# Write text to the file.
#file = open("output.avi",  'r')

print("Temp file = " + full_path_to_file)
print("\nUploading to Blob storage as blob" + local_file_name)

# Upload the created file, use local_file_name for the blob name
block_blob_service.create_blob_from_path(container_name, local_file_name, "output.avi")

#Listar los blobs en el contenedor
print("\nList blobs in the container")
generator = block_blob_service.list_blobs(container_name)
for blob in generator:
    print("\t Blob name: " + blob.name)
    

#BAjar datos del blob
full_path_to_file2 = os.path.join(local_path, str.replace(local_file_name ,'.avi', '_DOWNLOADED.avi'))
print("\nDownloading blob to " + full_path_to_file2)
block_blob_service.get_blob_to_path(container_name, local_file_name, full_path_to_file2)

sys.stdout.write("Sample finished running. When you hit <any key>, the sample will be deleted and the sample "
                 "application will exit.")
sys.stdout.flush()
input()

#file.close()

