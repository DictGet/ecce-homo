# ecce-homo
A simple micro application to serve images with customized cropping
![True ecce homo](http://ep00.epimg.net/cultura/imagenes/2012/08/23/actualidad/1345709139_149007_1345712998_noticia_normal.jpg)

## Introduction
This micro application resizes existing images according to given query parameters.
The application returns the image and saves the image as the previous filename suffixed with the query params.
The intended usage is with a file server which will return this new image the second time when the url matches the new filename.

E.g. for an existing image `image.jpg` we use `image.jpg?w=200` to set the width to 200 and save the new file as `image.jpg?w=200`

## Configuration
The settings are read from environment variables.
#### ECCEOMO_MEDIA_ROOT
The absolute path to the root directory common to all media files.
e.g. `export ECCEHOMO_MEDIA_ROOT='/www/media'`
#### ECCEHOMO_MEDIA_URL
Optional URL between domain and filename.
e.g. `export ECCEHOMO_MEDIA_URL='media'`
#### ECCEHOMO_DEFAULT_METHOD
Set to `contain` if left unset. Defines a default method to use when height `h` and width `w` are specified with a without a method `t`.
e.g. `export ECCEHOMO_DEFAULT_METHOD='crop'`
#### ECCEHOMO_MINIMUM_LENGTH
Sets a minimum accepted length for the width `w` and height `h` parameters.
e.g. `export ECCEHOMO_MINIMUM_LENGTH=10`
## Usage
There are three query parameters. Height `h`, Width, `w`, and method type `t`.  Method defintions in [python-resize-image readme]('https://github.com/charlesthk/python-resize-image')

They should be used always in the same order as the filename will be saved with the querystring as part of its filename.   
With example values given.  
Resize width:  
`?w=100`  
Resize height:  
`?h=100`  
Resize default e.g. contain:  
`?w=100&h=50`  
Resize crop:  
`?w=100&h=50&t=crop`  
Resize thumbnail:  
`?w=100&h=50&t=thumbnail`  
Resize cover:  
`?w=100&h=50&t=cover`  
## Notes: ##
Files are saved with url path as filename.
If trailing slash present in url will be removed for filename
`{domain}/{media_url}/path/to/file.jpg/?w=100` -> `{media_directory}/path/to/file.jpg?w=100`


