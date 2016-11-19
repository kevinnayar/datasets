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
    'Rank', 
    'Country',
    'Score'
  ])

  data = input_file['data']

  for d in data:
    output_file.writerow([
      d['gpi_rank'], 
      d['country'],
      d['gpi_score'],
    ])

###################################################################
# Handle command row args
###################################################################
def main(argv):
  usage = 'usage: %prog [options] arg'
  parser = OptionParser(usage)
  parser.add_option('-i', '--input', help='json input file', action='store', dest='input')
  parser.add_option('-o', '--output', default='data.csv', help='csv output file', action='store', dest='output')
  
  (options, args) = parser.parse_args()
  if not options.input:
    parser.error('Input file path (-i or --input) is required')
  if not options.output:
    parser.error('Output file path (-o or --output) is required')
  else:
    transform_data(options)

if __name__ == "__main__":
  main(sys.argv[1:])  




