# HackNC2022

## Presentation
https://docs.google.com/presentation/d/1TQ1v1xH5o4ROK_jFznIh74HyHleVJx7SARHkdD9IOsA/edit?usp=sharing

## Demo
https://youtu.be/2Be_7df7l-s

## Inspiration
With us being in voting season and midterm elections just around the corner, we wanted to create an educational dashboard that not only educates students on voting but also sheds lights on the progress elected officials have made during their time in term.

## What it does
Our dashboard webscrapes data from accredited government sites about the past three Presidents' platform and beliefs, then uses a collection of works from other resources (CDC, EPA, WhiteHouse.gov) to determine the extent to which promises made have been met through a series of data visualizations . To make the information more N.C.-specific, the same was also done for two prominent N.C Officials, Tom Thillis and Graig Meyer.

# Installation & Run Instructions

## 1. Open the terminal on your local machine and clone our repository from Github into your IDE.
 - https://github.com/DheyaM/HackNC2022.git
## 2. Open a new terminal in your IDE to install dependencies. Make sure you install all the required dependencies listed below.
 - pip3 install {dependency names}
## 3. After installing all the dependencies, you can run the project.
- python app.py
## 4. Then, open the Browser(ex: Chrome, Safari) and copy & paste the following link in your web browser to land to the home page of our web application.
- http://152.23.57.228:4040/

## Dependency List: 
- flask
- twilio.twiml.messaging_response,
- pandas, plotly, numpy
- more dependencies included at the top of the app.py 

## How we built it
We built our web portal using HTML/CSS, Python, and Flask. We also integrated the Twilio API to let users know if updates have been made on our website or progress has been made by an official

## Challenges we ran into
We ran into some issues connecting the webscraped data and visualizations to the Flask on the frontend, especially since this was our first time webscraping data or working with Flask, but we ended up not only integrating both but also adding in the Twilio API.

## Accomplishments that we're proud of
We're proud of integrating so much in the limited time that we had.

## What we learned
We learned how to integrate APIs, webscrape data, and use Flask with HTML and CSS, all while creating an accessible, easy-to-navigate website

## What's next for Track my Leader
Moving forward, we want to make our dashboard extendable by adding more elected officials, more categories, and adding in machine learning to make the category classification process more automated. Ultimately, we hope our dashboard serves as a holistic tool that equips students with the knowledge and context needed to make an educated vote.

## Resources Used: 

https://www.tillis.senate.gov/infrastructure-disaster-relief
https://www.politifact.com/

For the NC Officials:
https://www.whitehouse.gov/wp-content/uploads/2022/08/North-Carolina-BIL-Fact-Sheet.pdf

https://www.epa.gov/newsreleases/epa-announces-199211000-water-infrastructure-projects-north-carolina#:~:text=EPA%20Announces%20%24199%2C211%2C000%20for%20Water%20Infrastructure%20Projects%20in%20North%20Carolina,-EPA%20Announces%20Water&text=ATLANTA%20(Dec.,Bipartisan%20Infrastructure%20Law%20in%202022.

https://www.tillis.senate.gov/2022/10/tillis-announces-1-4-billion-for-north-carolina-bridges-and-highways

https://www.ednc.org/perspective-no-time-to-pit-highways-vs-schools/

https://broadbandnow.com/North-Carolina

https://experience.arcgis.com/experience/1ca29805a2454ffab6b9579702b99e59/page/page_0/

HBCU funding in 2020: $50,000,000
https://lrs.sog.unc.edu/bill/unc-hbcu-funding-paritync-aampt-doc-programs-0

HBCU funding in 2022: $307,000,000
https://www.whitehouse.gov/wp-content/uploads/2022/03/ARP-Higher-Ed-North-Carolina.pdf

Projected NC emissions in 2020 and 2022 due to transportation:
https://deq.nc.gov/media/27070/download?attachment

Student Loan Debt
https://ticas.org/wp-content/uploads/2021/11/Student-Debt-for-College-Graduates-in-North-Carolina.pdf
https://educationdata.org/student-loan-debt-by-state#north-carolina

## What we Did
- Webscraping, Data Filtering and Processing
- Frontend in HTML/CSS and Flask
- Use of Twilio API 
