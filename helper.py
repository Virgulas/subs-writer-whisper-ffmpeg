import os
from moviepy import VideoFileClip
from PIL import Image, ImageFont, ImageDraw

def get_video_size(file):
    video = VideoFileClip(file)
    size = video.size
    video.close()
    return size

def calculate_text_size(text, font_path, font_size):
    image = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    text_width = draw.textlength(text, font=font)
    text_height = font_size

    return (text_width, text_height)

def text_break_line(text, width, font_path, font_size):
    current_text = text
    current_width = (calculate_text_size(current_text, font_path, font_size))[0]
    next_text = ''
    split_texts = []
    
    while current_width > width:
        split_text = current_text.split(' ')
        next_text = split_text.pop() + ' ' + next_text
        current_text = ' '.join(split_text)
        current_width = (calculate_text_size(current_text, font_path, font_size))[0]
        
        if current_width <= width:
            split_texts.insert(0, {'text': current_text.strip(), 'width': current_width})
            
            if next_text != '':
                current_text = next_text
                next_text = ''
                current_width = (calculate_text_size(current_text, font_path, font_size))[0]
                
    if not current_text.isspace():
        split_texts.insert(0, {'text': current_text.strip(), 'width': current_width})    
    
    return split_texts

def make_dir(filename, path='output/', extension = ''):
    dir_name = filename.split('.')[0]
    directory = path + dir_name + extension
    os.makedirs(directory, exist_ok=True)
    return directory + '/'