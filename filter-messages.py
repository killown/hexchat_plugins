#killown irc
#note in case you need to send additional message
#hexchat.command('SAY {}'.format("ok man, this is working!"))

__module_name__ = "filter"
__module_version__ = "1.0"
__module_description__ = "Filter messages"

import hexchat

filters = ["https://bit.ly", "https://bpa.st/"]

def replace_url(word, word_eol, userdata):
	# Skip replacement if string does not match
    if not any(filter for filter in filters if filter in word_eol[0]) and "://" in word_eol[0]:
        url = [i for i in word_eol[0].split() if "://" in i][0]
        hexchat.prnt('You cannot send this message because this URL {0} is not into the filter list'.format(url))
        
        return hexchat.EAT_ALL

hexchat.hook_command("", replace_url)
