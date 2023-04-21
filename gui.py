from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QRadioButton
from PyQt5.QtGui import QIcon
from pytube import YouTube
from moviepy.editor import VideoFileClip

class VideoConverterGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the URL label and entry box
        url_label = QLabel("Enter YouTube URL:")
        self.url_entry = QLineEdit()

        # Create the output file label and entry box
        output_label = QLabel("Enter output file name and path:")
        self.output_entry = QLineEdit()

        # Create the format label and radio buttons
        format_label = QLabel("Select output format:")
        self.mp4_radio = QRadioButton("MP4")
        self.mp3_radio = QRadioButton("MP3")

        # Create the download button
        download_button = QPushButton("Download and Convert")
        download_button.clicked.connect(self.download_and_convert_video)

        # Create the status label
        self.status_label = QLabel("")

        # Create the layout
        vbox = QVBoxLayout()
        vbox.addWidget(url_label)
        vbox.addWidget(self.url_entry)
        vbox.addWidget(output_label)
        vbox.addWidget(self.output_entry)
        vbox.addWidget(format_label)
        vbox.addWidget(self.mp4_radio)
        vbox.addWidget(self.mp3_radio)
        vbox.addWidget(download_button)
        vbox.addWidget(self.status_label)
        self.setLayout(vbox)

        # Set the window properties
        self.setGeometry(700, 700, 700, 200)
        self.setWindowTitle("YouTube Video Downloader and Converter")
        self.setWindowIcon(QIcon("icon.png"))

    def download_and_convert_video(self):
        # Get the URL of the YouTube video
        url = self.url_entry.text()

        # Download the video using PyTube
        yt = YouTube(url)
        video = yt.streams.first()
        video.download()

        # Convert the video to the selected format using MoviePy
        if self.mp4_radio.isChecked():
            codec = 'libx264'
            extension = 'mp4'
        elif self.mp3_radio.isChecked():
            codec = 'libmp3lame'
            extension = 'mp3'
        else:
            raise ValueError("No format selected")

        clip = VideoFileClip(video.default_filename)
        clip.write_videofile(self.output_entry.text() + '.' + extension, codec=codec)

        # Print a message to indicate that the conversion is complete
        self.status_label.setText("Video conversion complete!")

if __name__ == '__main__':
    app = QApplication([])
    window = VideoConverterGUI()
    window.show()
    app.exec_()
