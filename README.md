# Sequencer - Django

This is a Django project that uses the Pandas library for DNA sequence analysis and renders simple web pages with sequence tables in the browser. JavaScript is also used in this project.

## Requirements

To run this project, you need to have the following installed:

- Python (and pip)

- Django
  (pip install django)

- Pandas
  (pip install pandas)

After installing these tools, use the following command to run the project:

python(3) [py - Linux/Mac] manage.py runserver

Then, you can access the website at http://localhost:8000/admin/ where you can add and remove sequences for different species.
![image](https://github.com/MilenaJasiolek/Sequencer/assets/125980721/c4b1f4c0-4bb8-4bb3-b3b5-7dedbdfe17d7)

![image](https://github.com/MilenaJasiolek/Sequencer/assets/125980721/1e735dee-7658-4862-83f9-24a6e325e676)

Clicking on "View Site" will show you visualizations in the form of subpages containing tables with sequence information.

![image](https://github.com/MilenaJasiolek/Sequencer/assets/125980721/791a9550-6f1a-45ff-8464-7904074cde35)

Additionally, you can compare the alignment between sequences by selecting two sequences and clicking the "Compare selected sequences" button.
![image](https://github.com/MilenaJasiolek/Sequencer/assets/125980721/63f250b4-ec14-42d1-b705-24343542aa76)
