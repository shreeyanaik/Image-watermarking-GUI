Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
from PIL import Image
import glob
import click
import os
photoList = []
size = 1080, 1080
outputSuffix = "-screwed"
watermarkPath = "watermark.png"
watermarkSize = 128, 128
watermarkPosition = "bottomRight" 
validWatermarkPositions = "topLeft", "topRight", "bottomLeft", "bottomRight"
def resizePhoto(photo):
    print('Resizing ' + photo.filename)
    photo.thumbnail(size, Image.ANTIALIAS)
def watermarkPhoto(photo):
    print('Watermarking ' + photo.filename)
    watermark = Image.open(watermarkPath)
   watermark.thumbnail(watermarkSize, Image.ANTIALIAS)
    margin = int(round(photo.width * 0.03)) 
    
    
    watermark_width, watermark_height = watermark.size
    topLeft = (0 + margin, 0 + margin)
    topRight = (photoWidth - margin - watermark_width, 0 + margin)
    bottomLeft = (0 + margin, photoHeight - margin - watermark_height)
    bottomRight = (photoWidth - margin - watermark_width, photoHeight - margin - watermark_height)
    position = bottomRight 
    if watermarkPosition in validWatermarkPositions:
        position = eval(watermarkPosition)
        def savePhoto(photo):
    print('saving ' + photo.filename)
    
   
    saveFileName = os.path.splitext(photo.filename)[0] + outputSuffix + os.path.splitext(photo.filename)[1]
    outputFormat = photo.format # Save the photo in its original format
    try:
        photo.thumbnail(size, Image.ANTIALIAS)
        photo.save(saveFileName, outputFormat)
    except IOError as err:
        print("cannot create file for for '%s'" % photo.filename)
        print(err)
@click.command() 
@click.option('--photo-folder-path', default=".", help='Path to your photos folder', type=click.Path())
@click.option('--resize-width', default=1080, help='Resize width', type=int)
@click.option('--resize-height', default=1080, help='Resize height', type=int)
@click.option('--watermark-image-path', default="watermark.png", help='Path to your watermark', type=click.Path())
@click.option('--watermark-width', default=128, help='Watermark width', type=int)
@click.option('--watermark-height', default=128, help='Watermark height', type=int)
@click.option('--watermark-position', default="bottomRight", help='Watermark position', type=str)

def processPhotos(photo_folder_path, resize_width, resize_height, watermark_image_path, watermark_width, watermark_height, watermark_position):
    
    global photoPath
    photoPath = photo_folder_path
    global photoList
    photoList = [Image.open(item) for i in [glob.glob(photoPath + '/*.%s' % ext) for ext in ["jpg","gif","png","tga"]] for item in i]
    
    
    global size
    size = resize_width, resize_height
    global watermarkPath 
    watermarkPath= watermark_image_path
    global watermarkSize
    watermarkSize = watermark_width, watermark_height
    global watermarkPosition
    watermarkPosition = watermark_position
    
    for photo in photoList:
        print('Processing ' + photo.filename)
        resizePhoto(photo)
        watermarkPhoto(photo) 
        savePhoto(photo)
    print('Done!')

if __name__ == '__main__':
    processPhotos()

