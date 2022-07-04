#killown irc
__module_name__ = "filter"
__module_version__ = "1.0"
__module_description__ = "Filter messages"

import hexchat
from pathlib import Path
import os

path = os.path.join(Path.home(), ".config/hexchat/addons/filter-words-list.txt")
if not os.path.exists(path):
    os.mknod(path)

filters = [i.strip() for i in open(path, "r").readlines()]

#do not send the message if it contains an url that isn't in the filter list
def FilterMessage(word, word_eol, userdata):
    if not any(filter for filter in filters if filter in word_eol[0]) and "://" in word_eol[0]:
        url = [i for i in word_eol[0].split() if "://" in i][0]   
        hexchat.prnt("You cannot send this message because URL {0}\nAdd url into the filter list {1}".format(url, path))
        #hexchat.command('SAY {}'.format("ok man, this is working!"))
        return hexchat.EAT_ALL

hexchat.hook_command("", FilterMessage)
