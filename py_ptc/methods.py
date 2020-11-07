from os import listdir, mkdir, rmdir
from shutil import rmtree
from PIL import Image
    
def extract(inGif, outFolder, frame_name):
    gif = Image.open(inGif)
    frames = gif.n_frames 

    for i in range(frames):
        gif.save(f'{outFolder}/{frame_name}-{i}.png')
        gif.seek(i)
    return True

def convert(
    gif:str, 
    folder:str,
    frame_name:str
    ):
    ls = listdir(path=".")

    if gif in ls:
        if folder in ls:
            rmtree(folder)
         
        mkdir(folder)
        extract(gif, folder, frame_name)
        
        return (True, 'Conversion completed')

    else:
        return (False, 'File not found')

def main():
    extract('g.gif', 'out')