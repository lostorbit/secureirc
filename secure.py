try:
    import weechat as wc
except ImportError:
    print "This script must be run under WeeChat"
    exit()
    
import codecs as c

## ===============================================================
# user-callable encryption function
def do_encrypt(data, buffer, args):
    wc.command(buffer, "##"+enc(args)[0])
    return wc.WEECHAT_RC_OK


def do_unencrypt(data, signal, signal_data):
    # data gotten
    nick = wc.info_get("irc_nick_from_host", signal_data)

    # data processed
    if 

    # put the data back onto the screen
    server = signal.split(",")[0]
    channel = signal_data.split(":")[-1]
    buffer = wc.info_get("irc_buffer", "%s,%s" % (server, channel))
    if buffer:
        wc.prnt(buffer, "%s> %s" % (nick, clean))
    return wc.WEECHAT_RC_OK
## ===============================================================

# start our encoder
enc = c.getencoder( "rot-13" )

# test send to test channel
buffer = wc.info_get("irc_buffer", "slacked,#testtest")
wc.command(buffer, "using encryption")


# startup message
wc.register("encrypt", "lostorbit", "0.1", "GPL3", "two way encryption", "", "")
wc.prnt(wc.current_buffer(), "===>\tencrypt 0.1 activated")

# main 
hook1 = wc.hook_command("enc", "encrypts a message to the current channel", "", "", "", "do_encrypt", "")
hook2 = wc.hook_signal("*,irc_in2_msg", "do_unencrypt", "")

