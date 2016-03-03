import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', action='store', dest='log_file', help='Log file', required=True)
parser.add_argument('-o', action='store', dest='out_file', help='Output file', required=True)
parser.add_argument('-s', action='store', dest='search_term', help='Search term')
parser.add_argument('-t', action='store', dest='time', help='time')
parser.add_argument('-r', action='store', dest='timeRange', nargs=2, help='Enter two time')

args = parser.parse_args()

def searchTime(time, outfile):
	of = open(outfile, 'a')
	result = False
	with open(args.log_file) as fp:
		for line in fp:
			if time in line[17:22]:
				of.write(line)
				result = True
	of.close()
	return result

def searchString(string, outfile):
	of = open(outfile, 'a')
	result = False
	with open(args.log_file) as fp:
		for line in fp:
			if string in line:
				of.write(line)
				result = True
	of.close()
	return result

def searchTimeString(time, string, outfile):
	of = open(outfile, 'a')
	result = False
	with open(args.log_file) as fp:
		for line in fp:
			if time in line[17:22] and string in line:
				of.write(line)
				result = True
	of.close()
	return result

def searchTimeRange(timeRange, outfile):
	of = open(outfile, 'a')
	inRange = False
	result = False
	with open(args.log_file) as fp:
		for line in fp:
			if timeRange[0] in line[17:22]:
				inRange = True
			if timeRange[1] in line[17:22]:
				inRange = False
			if inRange:
				of.write(line)
				result = True
	of.close()
	return result

def searchTimeRangeString(timeRange, string, outfile):
	of = open(outfile, 'a')
	inRange = False
	result = False
	with open(args.log_file) as fp:
		for line in fp:
			if timeRange[0] in line[17:22]:
				inRange = True
			if timeRange[1] in line[17:22]:
				inRange = False
			if inRange and string in line:
				of.write(line)
				result = True
	of.close()
	return result

if args.time and args.search_term:
	if not searchTimeString(args.time, args.search_term, args.out_file):
		print('No Results')
elif args.timeRange and args.search_term:
	if not searchTimeRangeString(args.timeRange, args.search_term, args.out_file):
		print('No Results')
elif args.timeRange:
	if not searchTimeRange(args.timeRange, args.out_file):
		print('No Results')
elif args.time:
	if not searchTime(args.time, args.out_file):
		print('No Results')
elif args.search_term:
	if not searchString(args.search_term, args.out_file):
		print('No Results')

