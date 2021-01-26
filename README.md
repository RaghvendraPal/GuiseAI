# GuiseAI
Assignment


Success API : This api is used to upload the image to server, it will redirect you to success and failure page according to the response and network connectivity. It will also redirect you to error page if any exception comes.
If there is any error in file extension API will show: Your file extension should be .jpg, .jpeg, .png
If any Exception comes the API show : "Something went wrong!! Sorry !" message
Success message : Image Uploaded Successfully


Search API : This api is used to search the image to server, it will show you to the image if the image exist, else it will show you File Not Found Error according to the response and network connectivity. It will also redirect you to error page if any exception comes.
If File is not present API will show: File Not Found
If any Exception comes the API show : "Something went wrong!! Sorry !" message
Success message : show image with file name.

Delete API: This api is used to Delete the image from the server, It willredirct you to success and failure page according to response. It will also redirect you to error page if any exception comes.
If File is not present API will show: File Not Exist in DataBase
If any Exception comes the API show : "Something went wrong!! Sorry !" message
Success message : show deleted file name.

all_image_v2 API: This API will show you all the image that are present in server.
If any Exception comes the API show : "Something went wrong!! Sorry !" message
Success message : You will get list of file name with desending order of uploading time.
