# NBStoLUA
A Python script to convert Open Note Block Studio files (.nbs) into .lua files for ComputerCraft and its speaker system.

## Usage
This project requires [pynbs](https://github.com/OpenNBS/pynbs)

1. Download the repository, and move nbstolua.py to the same folder as your .nbs file<br>
2. Open nbstolua.py with command prompt and enter the name of the .nbs file<br>
3. Once it's finished, find the noteblock.lua file in the same folder as the other two files<br>
4. Move noteblock.lua into ComputerCraft and run it. Make sure your Computer has a speaker installed!<br>

## Limitations
ComputerCraft speakers only let you play 8 notes at a time. This shouldn't be an issue for most songs, but a few of the official Note Block Studio songs are affected by this.<br>
Higher tempos might be an issue? The sleep function can't be lower than 0.05, and I assume it could get around there at extremely high tempos. Shouldn't be an issue for most songs though.



