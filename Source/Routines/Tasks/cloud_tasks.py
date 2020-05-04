"""This file is used to hold a class whose object
is initialized with the google drive authentication
credentials and then contains the methods to manipulate
the drive files and upload images."""

#import sys
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class CTclass:
    """this class has been explained above inside
    of the docfile"""
    def __init__(self, nameIn, fileCreds):
        #Everything in the init should be necessary
        #for an object to be properly initialized.
        #self is self-explanatory, nameIn is sys.arg[1]
        #that you pass in, and fileCreds is the file
        #supposedly named "myCreds.txt" that you pass in
        #What's initialized here is the name and
        #google authentication,

        #name=sys.argv[1]
        try:
            self.name = nameIn
            self.obj_creds = fileCreds
            self.gauth = GoogleAuth()
            self.gauth.LoadCredentialsFile(self.obj_creds)
            if self.gauth.credentials is None:
                # Authenticate if they're not there
                self.gauth.LocalWebserverAuth()
            elif self.gauth.access_token_expired:
                # Refresh them if expired
                self.gauth.Refresh()
            else:
                # Initialize the saved creds
                self.gauth.Authorize()
            # Save the current credentials to a file
            self.gauth.SaveCredentialsFile(self.obj_creds)
            self.drive = GoogleDrive(self.gauth)
        except AttributeError as exc:
            #This exception will trigger if something
            #fails during initialization
            print('ERROR IN CTclassINIT:', str(exc))

    def img_upload(self, title):
        """This method essentially uploads
        and image to google drive using the
        given credentials. Need to add ability
        to this method to create more descriptive
        and flexible file naming"""
        photo = self.drive.CreateFile({'title':title})
        photo.SetContentFile(self.name)
        photo.Upload()
        os.remove(self.name)
