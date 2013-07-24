# botlib/plugs/day.py
#
#

""" show the day. """

from jsb.lib.O import cmnds

def day(event):
    if event.args: day = event.args[0]
    else: day = event.day
    event.direct("\nresults for %s:\n" % day)
    for obj in sorted(event.objects(day)): event.reply("%s %s" % (obj.time, obj.txt))
 
cmnds.register("day", day)