def transform_image(img, 
                    size=(100,100)):
  
  '''re-sizes and crops background images'''
  
  img_ratio = img.size[0] / float(img.size[1])
  ratio = size[0] / float(size[1])
  if ratio > img_ratio:
    img = img.resize((size[0], int(round(size[0] * img.size[1] / img.size[0])),
                      Image.ANTIALIAS)
    box = (0, 
           int(round((img.size[1] - size[1]) / 2)),
           img.size[0],
           int(round((img.size[1] + size[1]) / 2))
           )
    img = img.crop(box)   # middle crop
  elif ratio < img_ratio:
    img = img.resize((int(round(size[1] * img.size[0] / img.size[1])),size[1]),
                      Image.ANTIALIAS)
    box = (int(round((img.size[0] - size[0]) / 2)),
           0,
           int(round((img.size[0] + size[0]) / 2)),
           img.size[1])
    img = img.crop(box)
  else:
        img = img.resize((size[0],size[1]),
                          Image.ANTIALIAS)
  return img
