#! /usr/bin/env python
import sys, csv, json
from optparse import OptionParser


####################################################################
# Generate file
####################################################################
def transform_data(options):
  input_file = json.load(open(options.input, 'rU'))
  output_file = csv.writer(open(options.output, 'wb+'))
  
  output_file.writerow([
    'State',
    'Percent Educational Attainment',
    'Percent Peace Index',
    'Percent Above Poverty Rate',
    'Percent Non-religious'
  ])

  data = input_file['data']

  for d in data:
    output_file.writerow([
      d['state'],
      d['percent_educational_attainment'],
      d['percent_peace_index'],
      d['percent_above_poverty_rate'],
      d['percent_non_religious']
    ])


def convert_to_dollars(num):
  return '${:,}'.format(num)


###################################################################
# Handle command row args
###################################################################
def main(argv):
  usage = 'usage: %prog [options] arg'
  parser = OptionParser(usage)
  parser.add_option('-i', '--input', help='input JSON file', action='store', dest='input')
  parser.add_option('-o', '--output', default='data.csv', help='output CSV file', action='store', dest='output')
  
  (options, args) = parser.parse_args()
  if not options.input:
    parser.error('Input file path (-i or --input) is required')
  if not options.output:
    parser.error('Output file path (-o or --output) is required')
  else:
    transform_data(options)

if __name__ == '__main__':
  main(sys.argv[1:])  




