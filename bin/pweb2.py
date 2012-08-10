# coding: utf-8
import sys
import os,os.path
import signal
from p2_opts import Parser, Option, BooleanOption, IntOption
from p2_web import p2_main

PROOT=os.environ["PROOT"]

if not PROOT:
    print "root_path variable is not configured in /etc/rnet.conf"
    sys.exit(0)

os.chdir("%s/web"%PROOT)

parser = Parser(options={
       "daemon":BooleanOption("d","daemon", default=False,short_description=u"Запустить сервер в фоне"),
       "uid":IntOption("u", "uid", default=1000, short_description=u"UID для привилегий сервера"),
       "gid":IntOption("g", "gid", default=1000, short_description=u"GID для привилегий сервера")
})
options, arguments = parser.evaluate()

if len(arguments) == 0:
    print "Try pweb start2 or pweb2 stop"
    sys.exit(0)
if arguments[0] == "start":
    print "Starting rnet server"
    p2_main(PROOT, options)    
elif arguments[0] == "stop":
    print "Stopping rnet webserver"
    if os.path.isfile("%s/var/rnet.pid"%PROOT):
        os.kill(int(open("%s/var/rnet.pid"%PROOT).read()), signal.SIGTERM)
    else:
        print "None found"
else:
    print "Unknown command, try pweb2 start or pweb2 stop"
#