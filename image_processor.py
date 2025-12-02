from PIL import Image
import os

def compress_image(input_path, output_path, quality):
    img = Image.open(input_path)
    
    ext = os.path.splitext(input_path)[1].lower()
    
    if ext in ['.jpg', '.jpeg']:
        img.save(output_path, 'JPEG', quality=quality, optimize=True)
    elif ext == '.png':
        img = img.convert('P', palette=Image.ADAPTIVE, colors=256)
        img.save(output_path, 'PNG', optimize=True)
    elif ext == '.gif':
        img.save(output_path, 'GIF', optimize=True)
    else:
        img.save(output_path, quality=quality, optimize=True)
    
    original_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(output_path)
    
    return output_path