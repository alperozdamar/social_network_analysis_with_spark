from wordcloud import WordCloud
import csv
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

weights = []

with open('/Users/hpbui/Downloads/wordCloud.csv', mode='r') as infile:
    reader = csv.reader(infile)
    # with open('coors_new.csv', mode='w') as outfile:
    # writer = csv.writer(outfile)
    weights = {rows[0]:float(rows[1]) for rows in reader}
    
fireEmblem_mask = np.array(Image.open('/Users/hpbui/Downloads/fireEmblem.png'))
wc = WordCloud(
    background_color="white",
    mask=fireEmblem_mask,
    max_words=2000,
    contour_width=3, 
    contour_color='steelblue'
)

# Generate the cloud

wc.generate_from_frequencies(weights)

# Save the could to a file

wc.to_file("word_cloud.png")