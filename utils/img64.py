import base64

def read_image_base64(img_path):
    #img_path = r"data\invoices\1.jpg"
    with open(img_path,'rb') as img_data:
        img_base64 = base64.b64encode(img_data.read()).decode("utf-8")
    return img_base64
