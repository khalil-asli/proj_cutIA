# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:39:08 2022

@author: acer
"""

from fileinput import filename
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory,send_file
import urllib.request
import os
from werkzeug.utils import secure_filename
import urllib.request
import moviepy.editor as mp
from moviepy.editor import concatenate_audioclips
import numpy as np
from glob import glob
from io import BytesIO
from zipfile import ZipFile
from moviepy.editor import *
import matplotlib.pyplot as plt
from remote_jinja import render_remote
app = Flask(__name__)
  
 
UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 50000 * 50000

@app.route('/')
def upload_form():
    image_names = os.listdir('./imagess')
    filelist = [ f for f in image_names ]
    for f in filelist:
        os.remove(os. path. join('imagess/',f))
    return render_template('upload.html')
# return render_remote("https://cutai.webflow.io/")

@app.route('/', methods=['POST'])
def upload_video():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	else:
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		print('upload_video filename: ' + filename)
		flash('Video successfully uploaded and displayed below')
		return redirect(url_for('get_gallery',filename=filename))

@app.route('/gallery/<filename>')
def get_gallery(filename):
    clip = mp.VideoFileClip('static/uploads/'+filename)
    cut = lambda i: clip.audio.subclip(i,i+1).to_soundarray(fps=22000)
    volume = lambda array: np.sqrt(((1.0*array)**2).mean())
    volumes = [volume(cut(i)) for i in range(0,int(clip.duration-1))]
    averaged_volumes = np.array([sum(volumes[i:i+10])/10
                                for i in range(len(volumes)-10)])

    increases = np.diff(averaged_volumes)[:-1]>=0
    decreases = np.diff(averaged_volumes)[1:]<=0
    peaks_times = (increases * decreases).nonzero()[0]
    peaks_vols = averaged_volumes[peaks_times]
    peaks_times = peaks_times[peaks_vols>np.percentile(peaks_vols,90)]

    final_times=[peaks_times[0]]
    for t in peaks_times:
        if (t - final_times[-1]) < 60:
            if averaged_volumes[t] > averaged_volumes[final_times[-1]]:
                final_times[-1] = t
        else:
            final_times.append(t)
    #final = concatenate_videoclips([clip.subclip(max(t-5,0),min(t+5, clip.duration))
                    #  for t in final_times])
    final = [clip.subclip(max(t-15,0),min(t+15, clip.duration))
                        for t in final_times]
    for i in range(len(final)):
            final[i].write_videofile('imagess/worlds_cuts_V2'+str(i)+'.mp4',fps=24)
    image_names = os.listdir('./imagess')
    print(image_names)

    return render_template("gallery.html", image_names=image_names)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("imagess", filename)

@app.route('/display/<filename>')
def display_video(filename):
    return redirect(url_for('static',filename='uploads/' + filename),code=301)

@app.route('/return-files', methods=['GET'])
def return_file():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            pass # do something
        elif  request.form.get('action2') == 'VALUE2':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        target = 'imagess/'
        image_names = os.listdir('./imagess')
        filelist = [ f for f in image_names ]
        stream = BytesIO()
        with ZipFile(stream, 'w') as zf:
            for file in glob(os.path.join(target, '*.mp4')):
                zf.write(file, os.path.basename(file))
        stream.seek(0)
    return send_file(
        stream,
        as_attachment=True,
        download_name='archive.zip'
    )
           #return send_file('images/'+f, as_attachment=True)

