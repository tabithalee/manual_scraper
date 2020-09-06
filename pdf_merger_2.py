import math
from PyPDF2 import PdfFileMerger

def merge_pdfs(end_page_number, manual_name):
	division_number = 100

	folder_path = "C:\\Users\\tabit\\Desktop\\Williams_Bally_Parts_Manuals\\"

	pdfs = []

	num_pdfs = math.ceil(end_page_number / division_number)

	for x in range(1, num_pdfs):
		pdfs.append(folder_path + manual_name + "_" + str(x * division_number) + ".pdf")


	pdfs.append(folder_path + manual_name + "_" + str(end_page_number) + ".pdf")


	merger = PdfFileMerger()

	for pdf in pdfs:
		merger.append(pdf)


	merger.write(folder_path + manual_name + "_" + str(end_page_number) + "_merged.pdf")
	merger.close()