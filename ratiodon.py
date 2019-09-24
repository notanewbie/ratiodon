#
#
#  notanewbie made this.
#  ____________________
# |  ________________  |
# | |________________| |
# |                    |
# |  ________________  |
# | |                | |
# | |   __________   | |
# | |  |          |  | |
# | |__|          |__| |
# |____________________|
#
#
#

import urllib2;
import time;
def GetURL2(link):
    req = urllib2.Request(link, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
    response = urllib2.urlopen(req).read()
    return response;
def main():
    url = raw_input("What post would you like to get the ratio of? \n");
    #core = GetURL2(url.split("/")[len(url.split("/")) - 1]);
    core = url.split("/")[len(url.split("/")) - 1]
    site = url.split("/")[2];
    #print core;
    #print site;
    api = GetURL2("https://" + site + "/api/v1/statuses/" + core);
    replies = int(api.split('"replies_count":')[1].split(',')[0]);
    reposts = int(api.split('"reblogs_count":')[1].split(',')[0]);
    likes = int(api.split('"favourites_count":')[1].split(',')[0]);
    print "Ratio: " + str(reposts + likes) + "/"  + str(replies)
    main();
main();
