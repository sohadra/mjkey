import os
import pred
import commands
import json


def add_to_playlist(fpath, mood):
    os.system("mpc clear")
    os.system("mpc load " + mood)
    os.system(""" mpc add '{0}'""".format(fpath))
    os.system("mpc rm " + mood)
    os.system("mpc save " + mood)


if __name__ == "__main__":
    dict_all = {}
    music_files = commands.getoutput("mpc listall").split("\n")
    home_path = commands.getoutput("echo $HOME")
    examples = open(os.path.join(home_path , "dump.txt")).read().split("\n\n")
    tested_files = []
    for exj in examples[:-1]:
        ex = json.loads(exj)
        tested_files.append(ex["path"])

#    print tested_files
#    print "\n\n"

    music_dir = "/var/lib/mpd/music"
    tmp = []
    for a in music_files:
        tmp.append(os.path.join(music_dir, a))
#    print music_files
    music_files = tmp

    for a in music_files:
        if tested_files.__contains__(a):
            continue
        else:
            print a
            pred.pred(a)
        
    
#    mood = pred.pred(fpath)
#    add_to_playlist(mood, fpath)
    
