import argparse
from pdf_splitter import PDFSplitter

parser = argparse.ArgumentParser(description='Manipulate and convert e-book files.')
parser.add_argument('action', 
                    type=str,
                    choices=['pdf-to-cbz', 'pdf-to-jpgs', 'cbr-to-cbz'],
                    help='blablabla')

args = parser.parse_args()
print(args.action)
if args.action == 'pdf-to-cbz':
    pdf_splitter = PDFSplitter()
    pdf_splitter.to_images('jpg', 'test2.pdf')