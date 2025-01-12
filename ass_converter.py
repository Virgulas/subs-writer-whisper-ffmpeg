import json
from helper import get_video_size

def format_time(time):
    hours = int(time // 3600)
    minutes = int((time % 3600) // 60)
    seconds = int(time % 60)
    milliseconds = int((time % 1) * 100)  

    return f"{hours:01d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"

def write_ass_skeleton(output_path, x, y):
    header = f"[Script Info]\nTitle: Untitled\nScriptType: v4.00+\nPlayResX: {x}\nPlayResY: {y}\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, TertiaryColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Default,Arial,20,&Hffffff,&Hffffff,&H0,&H0,0,0,0,0,100,100,0,0,1,1.5,0,2,10,10,10,1\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"

    with open(output_path, 'w') as file:
        file.write(header)
        
def append_dialogue(output_path, start, end, color, font, size, text, pos):
    dialogue = f"Dialogue: 0,{start},{end},Default,,0,0,0,,{{\\fn{font}\c&{color}&\\fs{size}&\pos{pos}}}{text}\n"

    with open(output_path, 'a') as file:
        file.write(dialogue)

def convert_json_to_ass(file, input_path, output_path):
    x, y = get_video_size(file)
    write_ass_skeleton(output_path, x, y)
    
    with open(input_path) as file:
        data = json.load(file)
        
        for caption in data:
            start = format_time(caption['start'])
            end = format_time(caption['end'])
            color = caption['color']
            size = caption['size']
            font = caption['font']
            
            for text in caption['texts']:
                pos = (text['pos'][0], text['pos'][1])
                append_dialogue(output_path, start, end, color, font, size, text['text'], pos)
    return output_path