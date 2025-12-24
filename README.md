Структура проекта:
Office_TweaksPRO/
├── officetweaks2/
│   ├── dist/
│   ├── cleaner.py
│   ├── cli_parser.py
│   ├── converter.py
│   ├── file_manager.py
│   ├── image_processor.py
│   ├── interactive_menu.py
│   ├── office_tweaks.py
│   ├── utils.py
│   └── requirements.txt
├── venv/
└── office_tweaks.log
Инструкция по подготовке виртуального окружения:
Создание виртуального окружения (через консоль)
В терминале VS Code (находясь в корне проекта):

python -m venv venv

Активация окружения
cmd
venv\Scripts\activate
Установка зависимостей
pip install -r requirements.txt

pip install pdf2docx docx2pdf Pillow colorama tqdm
Интерактивный режим:
Office_Tweaks.exe -i
# или
Office_Tweaks.exe

Конвертация через аргументы:
Office_Tweaks.exe --pdf2docx "document.pdf"

Сжатие изображений с параметрами:
Office_Tweaks.exe --compress-images "photo.jpg" --quality 75
Описание поддерживаемых аргументов CLI с примерами:
Конвертация PDF → DOCX
Office_Tweaks.exe --pdf2docx all --workdir "C:\PDF_Files"
Office_Tweaks.exe --pdf2docx "document.pdf"

Конвертация DOCX → PDF
Office_Tweaks.exe --docx2pdf all --workdir "./documents"
Office_Tweaks.exe --docx2pdf "report.docx"

Сжатие изображений
Office_Tweaks.exe --compress-images all --workdir "./photos" --quality 75
Office_Tweaks.exe --compress-images "photo.jpg" --quality 90

Удаление файлов
Office_Tweaks.exe --delete --mode extension --pattern ".tmp"
Office_Tweaks.exe --delete --mode startswith --pattern "temp_"
Office_Tweaks.exe --delete --mode endswith --pattern "_backup"
Office_Tweaks.exe --delete --mode contains --pattern "draft"
Office_Tweaks.exe --delete --mode extension --pattern ".log" --delete-dir "C:\Logs"



## Автор  
ФИО: Малов Игнат Станиславович 
Группа: ФГиИБ-ПИ-1б
