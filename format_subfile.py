import json
from helper import calculate_text_size, get_video_size, text_break_line

def format_subfile(file_path, path_raw, path_formatted, font, size, color):
    video_data = []
    video_width, video_height = get_video_size(file_path)
    initial_y_pos = video_height - 40
    x_pos = video_width//2

    with open(path_raw) as file_raw:
        data = json.load(file_raw)
        
        for sentence in data['segments']:
            start, end, text = sentence['start'], sentence['end'], sentence['text']
            texts = []
            text_width, text_height = calculate_text_size(text, font, size)
            text_y_offset = text_height // 2

            if text_width > video_width:
                split_texts = text_break_line(text, video_width, font, size)
                
                for i, split_text in enumerate(split_texts):
                    y_pos = initial_y_pos - (text_height + text_y_offset) * i
                    
                    texts.insert(0, {'text': split_text['text'], 'pos': (x_pos, y_pos)})
            else:
                texts.append({'text': text, 'pos': (x_pos, initial_y_pos)})
            
            video_data.append({'start': start, 'end': end, 'texts': texts, 'color': color, 'font': font.split(".")[0], 'size': size})
        file_raw.close()
        
    with open(path_formatted, "w") as file_formmated:
        json.dump(video_data, file_formmated, indent=4)
        file_formmated.close()
        
    return path_formatted
            
