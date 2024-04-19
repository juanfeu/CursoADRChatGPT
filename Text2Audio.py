import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QFileDialog

class TextToSpeechConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Conversor de texto a audio')
        self.layout = QVBoxLayout()

        self.label = QLabel('Escribe tu texto:')
        self.layout.addWidget(self.label)

        self.text_entry = QLineEdit()
        self.layout.addWidget(self.text_entry)

        self.convert_button = QPushButton('Convierte a audio')
        self.convert_button.clicked.connect(self.convert_to_speech)
        self.layout.addWidget(self.convert_button)

        self.status_label = QLabel('')
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)
    
    def convert_to_speech(self):
        input_text = self.text_entry.text()
        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "MP3 files (*.mp3)")
        
        if not save_path or not input_text:
            return

        url = "https://api.openai.com/v1/audio/speech"
        headers = {
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "tts-1",
            "input": input_text,
            "voice": "alloy"
        }
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            self.status_label.setText(f"Fichero guardado con éxito: {save_path}")
        else:
            self.status_label.setText("Error: No se ha podido hacer la conversión.")

def main():
    app = QApplication(sys.argv)
    ex = TextToSpeechConverter()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()