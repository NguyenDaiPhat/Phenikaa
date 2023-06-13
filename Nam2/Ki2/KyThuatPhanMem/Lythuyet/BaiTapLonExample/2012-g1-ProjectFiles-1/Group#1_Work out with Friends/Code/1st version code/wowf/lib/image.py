'''
Image manipulation helper functions.
'''

import os
import shutil
from PIL import Image, ImageOps
from pyramid.asset import abspath_from_asset_spec


def make_thumbnail(infile, outpath, size):
    '''
    Create a thumbnail copy of the given image file.

    @param infile Source image file
    @param outpath Destination path of the thumbnail
    @param size Thumbnail dimensions
    '''
    infile.seek(0)
    outpath = abspath_from_asset_spec(outpath)
    if isinstance(size, int):
        size = (size, size)
    image = Image.open(infile)
    if image.mode not in ('L', 'RGB'):
        image = image.convert('RGB')
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image.save(outpath, quality=100)


def upload_and_make_thumbnails(infile, upload_dir, filename, versions=None):
    '''
    Upload the original image file, and create the necessary thumbnail versions.

    @param versions Dictionary of key => dimensions
    '''
    filepath = os.path.join(upload_dir, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    shutil.copyfileobj(infile, open(filepath, 'wb'))
    if versions:
        for subdir, size in versions.items():
            filepath = os.path.join(upload_dir, subdir, filename)
            make_thumbnail(infile, filepath, size)


class StoredImage(unicode):
    '''
    Utility class for thumbnailed images, used to access both the original
    as well as all thubnail versions of the image.
    '''

    def __new__(self, root_dir, filename, versions=None):
        self.root_dir = root_dir
        self.filename = filename
        self.versions = versions
        return unicode.__new__(self, os.path.join(root_dir, filename))

    def __getattr__(self, name):
        if name not in self.versions:
            raise AttributeError('Image does not have a %s version' % name)
        return os.path.join(self.root_dir, name, self.filename)