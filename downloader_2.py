from PIL import Image
import requests

folder_path = "C:\\Users\\tabit\\Desktop\\Williams_Bally_Parts_Manuals\\"
imagelist = []

def save_pdf(page_no, manual_name):
	save_path = folder_path + manual_name + "_" + str(page_no) + ".pdf"
	imagelist[0].save(save_path, format='PDF', save_all=True, append_images=imagelist[1:])
	print("printed " + str(page_no))
	for x in range(len(imagelist)):
		imagelist[x].close()
	imagelist.clear()

def download_from_url(last_page_number, manual_name, id):
	current_page = 1
	division_number = 100

	while (current_page <= last_page_number):

		page_number_string = "page" + str(current_page).zfill(4)

		image_url = "http://www.planetarypinball.com/reference/partsmanuals/" \
		+ manual_name + "/files/assets/mobile/" \
		+ page_number_string \
		+ "_i2.jpg?id=" + id

		# URL of the image to be downloaded is defined as image_url 
		r = requests.get(image_url) # create HTTP response object 

		# send a HTTP request to the server and save 
		# the HTTP response in a response object called r
		# desktop_path + folder_name + page_number_string + ".jpg"

		# TODO - ping pong between temp1 and temp2 jpgs to reduce conflicts
		if current_page % 2 == 0:
			temp = "temp1.jpg"
		else:
			temp = "temp2.jpg"

		with open(folder_path + temp,'wb') as f: 

			# Saving received content as a png file in 
			# binary format 

			# write the contents of the response (r.content) 
			# to a new file in binary mode. 
			f.write(r.content)
			f.close()


		with Image.open(folder_path + temp) as img:
			imagelist.append(img.convert('RGB'))
			
			if (current_page % division_number == 0):
				save_pdf(current_page, manual_name)
				if current_page == last_page_number:
					return

		current_page += 1

	save_pdf(current_page - 1, manual_name)
