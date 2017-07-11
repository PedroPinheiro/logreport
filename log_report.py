import sys
import re
import operator

patternUrl = re.compile('(?:request_to=\")(https?:\/\/[^(\")]+)')
patternStatus = re.compile('(?:status=\")([0-9]+)(?:\")')
url_list = dict()
status_list = dict()

def process_line(line):
    mUrl = patternUrl.search(line)
    mStatus = patternStatus.search(line)
    
    if mUrl and mStatus:
        url = mUrl.group(1)
        status = mStatus.group(1)

        url_list[url] = url_list.get(url,0) + 1
        status_list[status] = status_list.get(status,0) + 1

def process_file(file):
    with open(file) as f:
        for line in f:
            process_line(line)

    print_result()

def print_result() :

    orderedUrls = sorted(url_list.items(), key=operator.itemgetter(1), reverse=True)
    top3Urls = []

    for i in range(3):
        top3Urls.append(orderedUrls[i])

    print "Top 3 Urls:"
    for k,v in top3Urls:
        print "%s - %s" % (k, v)

    orderedStatus = sorted(status_list.items(), key=operator.itemgetter(1), reverse=True)

    print ""
    print "Status:"
    for k,v in orderedStatus:
        print "%s - %s" % (k, v)

def main():
    if len(sys.argv) < 2:
        print "usage:\nlog_report.py $file"
    else:
        file = sys.argv[1]
        process_file(file)

if __name__ == '__main__':
    main()