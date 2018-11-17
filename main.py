import argparse
from pdf_splitter import PDFSplitter

parser = argparse.ArgumentParser(description='Manipulate and convert e-book files.')
parser.add_argument('action', 
                    type=str,
                    choices=['pdf-to-cbz', 'pdf-to-jpgs', 'cbr-to-cbz'],
                    help='blablabla')
parser.add_argument('--input', type=str)

args = parser.parse_args()
if args.action == 'pdf-to-cbz':
    pdf_splitter = PDFSplitter()
    pdf_splitter.to_images('jpg', args.input)