try:
    import weechat as wc
except ImportError:
    print "This script must be run under WeeChat"
    exit()
    
import codecs as c

# startup message
wc.register("encrypt", "lostorbit", "0.1", "GPL3", "two way encryption", "", "")

## ===============================================================
# user-callable encryption function
def do_encrypt(data, buffer, args):
    wc.command(buffer, "##"+enc(args)[0])
    return wc.WEECHAT_RC_OK


# capture encrypted data sent from server
def mod_unencrypt(data, modifier, modifier_data, string):
    wc.prnt(wc.current_buffer(), "===>\tentered mod_unencrypt")
    return "%s %s" % (string, modifier_data)



def do_unencrypt(data, signal, signal_data):
    #wc.prnt(wc.current_buffer(), "===>\tentered do_unencrypt")

    dict = wc.info_get_hashtable("irc_message_parse", { "message": signal_data } )
    #for d in dict:
    #    wc.prnt(wc.current_buffer(), "==>\t%s" % d)
    #    wc.prnt(wc.current_buffer(), "===>\t%s" % dict[d])

    # channel info
    nick = dict['nick']
    server = signal.split(",")[0]
    channel = dict['channel']
    buffer = wc.info_get("irc_buffer", "%s,%s" % (server, channel) )

    # get and unencrypt
    dirty = dict['arguments'].split(':')[1]
    clean = dirty[2:] #clean = dirty[-2:]
    clean = enc(clean)[0]


    ## put the data back onto the screen
    if dirty[0]=='#' and dirty[1]=='#':
        if buffer:
            wc.prnt(buffer, "[%s]\t%s" % (nick, clean))
    return wc.WEECHAT_RC_OK
## ===============================================================

# start our encoder
enc = c.getencoder( "rot-13" )
wc.prnt(wc.current_buffer(), "===>\tencrypt 0.1 activated")

# main 
#hook2 = wc.hook_modifier("*,irc_in2_privmsg", "mod_unencrypt", "")
hook2 = wc.hook_signal("*,irc_in2_privmsg", "do_unencrypt", "")
hook1 = wc.hook_command("enc", "encrypts a message to the current channel", "", "", "", "do_encrypt", "")

