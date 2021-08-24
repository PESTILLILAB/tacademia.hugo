# plab.hugo

Customizable Hugo wesbite template

## Features

  

- Customisable Home Page with sliders, infobox and featurettes

- Create slides using markdown

- Create featurette using markdown

- Show research papers using PubMed Api

- Show funding using NIH

- Auto Update research papers and funding

- Create and Update Team members using ORCID and Markdown
- Add Team members using [Linkedin Authentication](https://github.com/PESTILLILAB/Linkedin-Auth-Node)

  

### Create slides using markdown

To edit and show more slides

create a new file in content/home

  

`hugo new home/slide_example.md`

  

Specify the following parameters

    ---
    
        title: Example Slide
        
        align : text-left
        
        image : img/man-kid.jpg
        
        tags : ['slider']
    
    ---
### Create InfoBox using mardown

Create a new file in content/home

`hugo new home/infobox.md`

Specify the following parameters

	---
	title: TEAM
	description : Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. 
	image : img/group.svg
	url : '/team'
	tags : ['infobox']
	---

### Creating Banner or Jumbotron for Pages 
`hugo new pagename/banner.md`

Specify the following parameters:

---
title: Example Slide
image : /img/image_path.jpg
tags : ['banner']
---

### Create feature using markdown

To edit and show more feature blocks on home page

create a new file in content/home

  

`hugo new home/feature_name.md`

  

Specify the following parameters

    ---
    
    title: Your Title
    
    subtitle : your subtitle
    
    description : sample description
    
    image : path of the image (Ex img/500_500.svg)
    
    tags : ['feature']
    
    ---

## Configure PubMed Api and NSF data

Edit the file `gen_data.py` 

    nih_link = 'put your pubmed rss url'
    nsf_data_link = 'https://api.nsf.gov/services/v1/awards.json?keyword="your keywords"&printFields=startDate,expDate,id,title,awardee,agency,awardeeName,piFirstName,piLastName,coPDPI'
Save and close the file 



Run the file using python

    python3 /plab/plab.hugo/gen_data.py
By default the update time is set 10 seconds 
to change or set the interval update the value in seconds

    sch = scheduler()
    
    sch.add_job(myfn, 'interval', seconds=10)
    
    sch.start()

## Updating Team using ORCID
Open the team.json file

    plab/plab.hugo/static/assets/team.json
Add a json entry 
 Example : 
   
    "Franco Pestilli" : {
    
	    "type" : "active",
	    
	    "ORCID":"true",
	    
	    "image": "https://brainlife.io/images/avatar/franco.jpg",
	    
	    "id": "0000-0002-2469-0494",
	    
	    "summary": "A small description",
	    
	    "externals" : {
	    
		    "twitter" : "url",
		    
		    "facebook" : "url",
		    
		    "scholar" : "url",
		    "github" : "url"
	    
    }
    
    },

Save and then run the file team.py 

    python3 /plab/plab.hugo/team.py
    
## Updating Team using Hugo

`hugo new team/examplename.md`

Open the file and provide the following entries

    ---
    
    name : User Name
    
    image : image path [Example : /img/user.png]
    
    position : Example Text
    
    facebook : url
    
    scholar : url
    
    linkedin : url
    
    twitter : url
    
    github : url
    
    weight: 100
    
    tags : ['active']

    ---




