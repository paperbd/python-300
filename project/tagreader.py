"""
MP3 Tag Reader
Author: Heather Hoaglund-Biron

"""
import mutagen
from mutagen.easyid3 import EasyID3

class TagReader:
    """
    A TagReader reads metadata from .mp3 files and returns it in a dict 
    object. The only method used outside this file will be readTags().
    
    """

    def readTags(self, top_dir):
        """
        Searches through the given directory for .mp3 files, reads the
        files' metadata, and returns it in a dict object.

        """
        files = find(top_dir)
        tags = read(files)
        return tags

    def find(self, top_dir):
        """
        Searches through the given music directory for .mp3 files and
        returns an array of files.

        """
        return 

    def read(self, music_file):
        """
        Reads the metadata from the given file and returns a dictionary object
        containing the metadata.

        """
        musicFile = EasyID3.Open(music_file)
    