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

def cleanUpUrl(url):
    #extract the domain
    url = url.split('://')[-1]
    if '/' in url:
        url = url.split('/')[0]
    url = "https://{0}\n".format(url)
    return url

def IsURLAllowed(message):
    #only if the url isn't found in the filter list
    if not any(filter for filter in filters if filter in message) and "://" in message:
        return [i for i in message.split() if "://" in i][0]
    else:
        return None

def FilterMessage(word, word_eol, userdata):
    url = IsURLAllowed(word_eol[0])
    if url is not None:
        hexchat.prnt("You cannot send this message because URL {0}\n".format(url))
        hexchat.prnt("Add the domain {0} into the filter list {1}\n".format(cleanUpUrl(url), path))
        hexchat.prnt("/addurl {0}".format(cleanUpUrl(url)))
        return hexchat.EAT_ALL

def AddFilter(word, word_eol, userdata):
    url = IsURLAllowed(word_eol[0])
    if url is not None:
        #append the url to the list
        with open(path, 'a') as filter_list:
            filter_list.writelines(cleanUpUrl(url))
            filter_list.close()
        hexchat.prnt("/reload filter-words.py")
        hexchat.command('/reload filter-words.py')

hexchat.hook_command("", FilterMessage)
hexchat.hook_command("addurl", AddFilter)
