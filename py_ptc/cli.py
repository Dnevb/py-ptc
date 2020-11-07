import typer
from os import listdir, mkdir, rmdir, chdir
from shutil import rmtree
from PIL import Image
from pathlib import Path

from . import templates


def create_theme(
    name:str = typer.Option(..., '--name', '-n'),
    file:str = typer.Option(..., '--file', '-f'),
    # path:str = typer.Option(None, '-o'),
    frame_name:str = typer.Option('frame', '-fname'),
    description:str = typer.Option('', '--description', '-d'),
):
    
    # PM_DIR = Path('/usr/share/plymouth/theme')
    BASE_DIR = Path().absolute()
    F_DIR = Path(__file__).parent.absolute()
    print(F_DIR)
    
    if Path(BASE_DIR / name).is_dir():
        ans = typer.confirm(f'"{name}" already exist, do you want to continue?', abort=True)

        if ans:
            rmtree(name)

    mkdir(name)
    chdir(name)

    with open(f'{name}.plymouth', 'w') as f:
        f.write(templates.plymouth.format(name, description))


    ls = listdir(path=".")
         
    FRAMES_DIR = 'animation'
    mkdir(FRAMES_DIR)

    gif = Image.open(Path(BASE_DIR / file))
    frames = gif.n_frames 

    for i in range(frames):
        gif.save(f'{FRAMES_DIR}/{frame_name}-{i}.png', 'PNG')
        gif.seek(i)

    with open(f'{name}.script', 'w') as f:
        f.write(templates.script.format(frames, frame_name))


def main():
    typer.run(create_theme)