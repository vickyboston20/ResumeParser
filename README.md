# ResumeParser
Extracting Informations from Candidate Resume for Requirement Processs.

# Installation

* For extracting information from Doc and Pdf files
pip install pdfminer.six   
pip install doc2text

* For NLP operations we use spacy and nltk. Install them using:
# spaCy
pip install spacy
python -m spacy download en_core_web_sm

# nltk
pip install nltk
python -m nltk nltk.download('words')

* For Installing Dependencies we have
pip install -r requirements.txt

* Place all the resumes that you want to parse in resumes/ directory

* Run resume_parser.py

* For extracting data from a single resume file, use
python cli.py -f <resume_file_path>

* For extracting data from several resumes, place them in a directory and then execute
python cli.py -d <resume_directory_path>

# GUI with Django

* For running GUI execute:

# python manage.py makemigrations

# python manage.py migrate

# python manage.py runserver
