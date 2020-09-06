from PIL import Image

# imported the requests library 
import requests 

current_page = 1
last_page_number = 839
division_number = 100

manual_name = "BLY_Parts_Yellow_16-9147-B"
id = "7782816368"

folder_path = "C:\\Users\\tabit\\Desktop\\Williams_Bally_Parts_Manuals\\"

imagelist = []


def save_pdf(page_no):
	save_path = folder_path + manual_name + "_" + str(page_no) + ".pdf"
	imagelist[0].save(save_path, format='PDF', save_all=True, append_images=imagelist[1:])
	imagelist.clear()

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

	with open(folder_path + "temp.jpg",'wb') as f: 

		# Saving received content as a png file in 
		# binary format 

		# write the contents of the response (r.content) 
		# to a new file in binary mode. 
		f.write(r.content)
		f.close()

	img = Image.open(folder_path + "temp.jpg")
	im = img.convert('RGB')

	imagelist.append(im)

	if (current_page % division_number == 0):
		save_pdf(current_page)

	current_page += 1

save_pdf(current_page - 1)
