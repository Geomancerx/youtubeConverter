import os
import sys
import youtube_dl

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QFileDialog, QMessageBox
from PyQt5 import QtGui


class VideoConverterGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.url_label = QLabel("YouTube URL:", self)
        self.url_label.move(20, 20)
        self.url_label.setFixedWidth(105)

        self.url_entry = QLineEdit(self)
        self.url_entry.move(110, 20)
        self.url_entry.resize(270, 20)

        self.output_label = QLabel("Output file path:", self)
        self.output_label.move(20, 60)
        self.output_label.setFixedWidth(105)

        self.output_entry = QLineEdit(self)
        self.output_entry.move(110, 60)
        self.output_entry.resize(270, 20)

        self.browse_button = QPushButton("Browse", self)
        self.browse_button.move(500, 60)
        self.browse_button.resize(80, 20)
        self.browse_button.clicked.connect(self.browse_file_path)

        self.mp3_radio = QRadioButton("MP3", self)
        self.mp3_radio.move(110, 100)

        self.mp4_radio = QRadioButton("MP4", self)
        self.mp4_radio.move(190, 100)
        self.mp4_radio.setChecked(True)

        self.convert_button = QPushButton("Convert", self)
        self.convert_button.move(20, 140)
        self.convert_button.clicked.connect(self.download_and_convert_video)

        # Set font size and color
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)

        self.url_label.setFont(font)
        self.url_entry.setFont(font)
        self.output_label.setFont(font)
        self.output_entry.setFont(font)
        self.browse_button.setFont(font)

        self.url_entry.setStyleSheet("color: black;")
        self.output_entry.setStyleSheet("color: black;")

        # Set horizontal spacing between widgets
        self.url_entry.move(110 + self.url_label.width() + 10, 20)
        self.output_label.move(20, 60)
        self.output_entry.move(110 + self.output_label.width() + 10, 60)

        self.resize(900, 300)
        self.setWindowTitle("YouTube Converter")
        self.show()

    def browse_file_path(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Select output file", os.path.expanduser("~"), "*.mp3;;*.mp4")
        if file_name:
            self.output_entry.setText(file_name)

    def download_and_convert_video(self):
        url = self.url_entry.text()
        output_file = self.output_entry.text()
        extension = "mp3" if self.mp3_radio.isChecked() else "mp4"

        ydl_opts = {
            'outtmpl': output_file + '.' + extension,
        }

        if extension == "mp3":
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        else:
            ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        QMessageBox.information(self, "Download Complete", "Video conversion complete!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoConverterGUI()
    sys.exit(app.exec_())
