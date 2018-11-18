import argparse
from pdf_splitter import PDFSplitter
from image_collector import ImageCollector

parser = argparse.ArgumentParser(description='Manipulate and convert e-book files.')
parser.add_argument('action', 
                    type=str,
                    choices=['pdf-to-cbz', 'pdf-to-jpgs', 'cbr-to-cbz'],
                    help='blablabla')
parser.add_argument('--input', type=str)
# parser.add_argument('--output', type=str)

args = parser.parse_args()
if args.action.startswith('pdf-to'):
    pdf_splitter = PDFSplitter()
    pdf_splitter.to_images('jpg', args.input)

    if args.action == 'pdf-to-cbz':
        image_collector = ImageCollector()
        image_collector.collect_files_from()
