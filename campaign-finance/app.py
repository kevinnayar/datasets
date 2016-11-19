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
    'Candidate', 
    'Party', 
    'Funds raised from Outside Groups',
    'Funds raised by the Campaign Committee',
    'Total funds raised'
  ])

  candidates = input_file['data']['candidates']

  for candidate in candidates:
    output_file.writerow([
      candidate['candidate'], 
      candidate['party'],
      convert_to_dollars(candidate['funds_raised']['outside_groups']),
      convert_to_dollars(candidate['funds_raised']['campaign_committee']),
      convert_to_dollars(candidate['funds_raised']['total'])
    ])


def convert_to_dollars(num):
  return '${:,}'.format(num)


###################################################################
# Handle command row args
###################################################################
def main(argv):
  usage = 'usage: %prog [options] arg'
  parser = OptionParser(usage)
  parser.add_option('-i', '--input', help='Location of the TSV input file', action='store', dest='input')
  parser.add_option('-o', '--output', default='output.txt', help='Location of the output log file', action='store', dest='output')
  
  (options, args) = parser.parse_args()
  if not options.input:
    parser.error('Input file path (-i or --input) is required')
  if not options.output:
    parser.error('Output file path (-o or --output) is required')
  else:
    transform_data(options)

if __name__ == "__main__":
  main(sys.argv[1:])  




