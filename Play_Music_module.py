import os
def play_music():
     music_dir='D:\\music\\New Folder'
     songs=os.listdir(music_dir)
     random = os.startfile(os.path.join(music_dir, songs[1]))
     return 'playing music'


