import os
import sys
from pytube import YouTube
from moviepy.editor import *

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QRadioButton

class VideoConverterGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.url_label = QLabel("Enter YouTube video URL:")
        self.url_entry = QLineEdit()
        self.format_label = QLabel("Select output format:")
        self.mp4_radio = QRadioButton("MP4")
        self.mp3_radio = QRadioButton("MP3")
        self.output_label = QLabel("Enter output file name:")
        self.output_entry = QLineEdit()
        self.download_button = QPushButton("Download and Convert")
        self.browse_button = QPushButton("Browse")

        vbox = QVBoxLayout()
        vbox.addWidget(self.url_label)
        vbox.addWidget(self.url_entry)
        vbox.addWidget(self.format_label)
        vbox.addWidget(self.mp4_radio)
        vbox.addWidget(self.mp3_radio)
        vbox.addWidget(self.output_label)
        vbox.addWidget(self.output_entry)
        vbox.addWidget(self.browse_button)
        vbox.addWidget(self.download_button)

        self.setLayout(vbox)

        self.download_button.clicked.connect(self.download_and_convert_video)
        self.browse_button.clicked.connect(self.browse_output_directory)

        self.setWindowTitle("YouTube Video Converter")
        self.show()

    def browse_output_directory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        output_directory = QFileDialog.getExistingDirectory(self, "Select Output Directory", options=options)
        self.output_entry.setText(output_directory + "/output")

    def download_and_convert_video(self):
        url = self.url_entry.text()
        if not url:
            print("Please enter a YouTube video URL.")
            return

        if self.mp4_radio.isChecked():
            extension = "mp4"
            codec = "libx264"
        elif self.mp3_radio.isChecked():
            extension = "mp3"
            codec = None
        else:
            print("Please select an output format.")
            return

        output_file_path = self.output_entry.text()
        if not output_file_path:
            print("Please enter an output file name.")
            return

        try:
            yt = YouTube(url)
            video = yt.streams.first()
            video.download()

            clip = VideoFileClip(video.default_filename)
            clip.write_videofile(output_file_path + '.' + extension, codec=codec)

            print("Video conversion complete!")
        except Exception as e:
            print("An error occurred while converting the video:", e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoConverterGUI()
    sys.exit(app.exec_())
