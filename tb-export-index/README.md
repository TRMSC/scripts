# TB Export Index

## Description
TB-export-index is a tool for generating an index file for all exported mails from Thunderbird.

## How to
Use the Thunderbird plugin [ImportExportTools NG](https://addons.thunderbird.net/de/thunderbird/addon/importexporttools-ng/) for creating exports of your mails e.g. as *.eml-files.  
Each run creates a folder with the latest export files and an index.html for this folder.  
Run tb-export-index.py in the folder with all the different exported subfolders.
After that you will have a html file with a full index of your exported mails. 

## To do
It is planned to build the script for creating the index not only for the different folders rather for another level of folders. 
With this step it will be possible to build a more far-reaching structure of different folders e.g. for several mail accounts.
