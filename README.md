# Python_GUI_Music_Player
Python GUI Based Music Player for Windows

Music Player

This Python code implements a music player application using tkinter and Pygame libraries. It allows users to:

* Browse and add music files from a selected directory.
* View a list of added songs.
* Play, stop, pause, and unpause the selected song.
* Display the currently playing song's title.
* Access an "About" dialog for application information.

**Features:**

* User-friendly interface with tkinter for buttons and list display.
* Pygame integration for music playback functionalities.
* Song browsing and adding capabilities.
* Song playback controls (play, stop, pause, unpause).
* Informative "About" dialog.

**How to Use:**

1. Clone or download the repository containing this code.
2. Install the required libraries: `pip install tkinter pygame`
3. Run the script: `python music_player.py` (replace with the actual filename)
4. Use the "Browse" button to select a directory containing music files.
5. Music files from the selected directory will be added to the list.
6. Select a song from the list and use the playback controls.
7. Click "About" for application information.

**Dependencies:**

* tkinter (part of Python standard library, may need installation on some systems)
* Pygame (https://www.pygame.org/)

**Author:**
  RAGHUL V

**Version:**
  1.0

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


![music_player](https://github.com/RAGHULV75/Python_GUI_Music_Player/assets/168255383/74b79a6d-25a6-4186-9b63-7323ff2e3745)
