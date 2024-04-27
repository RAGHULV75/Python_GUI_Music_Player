# Python_GUI_Music_Player
Python GUI Based Music Player for Windows

The code is a simple music player application that uses pygame, tkinter, PySimpleGUI, and os modules. The code has the following features:

- It allows the user to browse and select a directory that contains music files.
- It displays the list of music files in the directory in a listbox widget.
- It allows the user to play, pause, stop, and resume the selected music file using buttons.
- It shows the title of the current music file in a label widget.
- It has an About button that shows a popup window with some information about the application and its developer.

The code consists of several functions and one main script. The functions are:

- add(): This function asks the user to select a directory using a file dialog. It then changes the current working directory to the selected directory and gets the list of files in it. It loops through the list and inserts each file name into the play_list listbox widget. It also initializes pygame and its mixer module.
- play(): This function loads and plays the music file that is currently selected in the play_list listbox widget. It also sets the var string variable to the file name and updates the song_title label widget with it.
- stop(): This function stops the music playback using pygame.mixer.music.stop().
- pause(): This function pauses the music playback using pygame.mixer.music.pause().
- unpause(): This function resumes the music playback using pygame.mixer.music.unpause().
- helloCallBack(): This function shows a popup window using PySimpleGUI.popup() with some information about the application and its developer.

The main script creates a Tk window with a title, geometry, and resizable settings. It also creates a label widget with some text, a button widget with an About command, a frame widget to hold the play_list listbox widget and another frame widget to hold the other button widgets. It also creates a label widget to display the song_title. It then binds each button widget to its corresponding function. Finally, it enters the main loop of tkinter.

The code uses docstrings to document each function and module according to PEP 257 conventions. It also uses type hints to provide automatic type information for parameters and return values according to PEP 484 conventions. It also uses comments to explain some parts of the code that are not obvious or need clarification.


![music_player](https://github.com/RAGHULV75/Python_GUI_Music_Player/assets/168255383/74b79a6d-25a6-4186-9b63-7323ff2e3745)
