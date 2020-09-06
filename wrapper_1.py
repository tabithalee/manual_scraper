from PIL import Image
import requests
import math
from PyPDF2 import PdfFileMerger


from downloader_2 import download_from_url
from pdf_merger_2 import merge_pdfs

#from large_wms_bly_midway_color_books_config import large_color_list
#from wms_bly_schematic_books_config import schematic_book_list
#from bly_parts_manual_config import bly_parts_list
from wms_parts_books_config import wms_parts_list

division_size = 100

for manual in wms_parts_list:
	last_page_number = manual['last_page_number']
	manual_name = manual['manual_name']
	id = manual['id']
	
	download_from_url(last_page_number, manual_name, id)

	if last_page_number > division_size:
		merge_pdfs(last_page_number, manual_name)
