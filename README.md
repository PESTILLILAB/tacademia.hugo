# tacademia.hugo

### Timeline-oriented academic website design.

The work of scientific and academic laboratories builts on innovation and reputation. Two critical aspects of the work of a modern scientific laboratory are often underestimated:
- The ability to generate scientific products (discoveries, reagents, software, or artifacts)
- The success in training the next generation of scientists (students and postdocs). 

Both scientific and training contributions for a scientific laboratory are critical to establish the standing of the lab, understand the climate of the lab and gauge the potential success for trainees and future opportunities for research and collaboration. Because of these reasons, demonstrating the scientific work over time, the impact on training is generally used as a key aspect of the evaluation process of the scientific laboratory. Contribution to science and training over the lifespan of a laboratory can be formalized as timelines. 

This website template takes the concept of timeline and proposes an open-science approach to demonstrating the contributions. The first version of the template suggests organizing the work of scientists into three primary timelines: 

- The RESEARCH axis: projects are conceptualized as a timeline of projects and grants.
- The TEAM axis: conceptualized as a composition of the current team and a timeline of lab alumni with their first job after leaving the lab
- The PUBLICATIONS axis: fetched directly from PubMed and organized into a timeline 
 
The template is built using [Hugo](https://github.com/gohugoio/hugo).

\- Dheeraj Bhatia and Franco Pestilli, The University of Texas at Austin

## Features

- Customisable Home Page with image sliders, infobox and featurettes
- Create slides using markdown
- Create featurette using markdown
- Automatically retrieves research papers using PubMed API
- Automatically retrieves funding information using NIH
- Create and update team members using ORCID and Markdown
- Add team members using [Linkedin Authentication](https://github.com/PESTILLILAB/Linkedin-Auth-Node)
  

### Create front-page slides using markdown

To edit and show more slides, create a new file in content/home:
```
hugo new home/slide_example.md
```


Specify the following parameters

```yaml
---
title: Example Slide
align: text-left
image: img/man-kid.jpg
tags: ['slider']
---
```

Note: At least one of the sliders need to have active tag to show sliders

### Create InfoBox using markdown

Create a new file in content/home

`hugo new home/infobox.md`

Specify the following parameters

```yaml
---
title: TEAM
description: Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. 
image: img/group.svg
url: '/team'
tags: ['infobox']
---
```

### Create feature using markdown

To edit and show more feature blocks on home page, create a new file in content/home

```
hugo new home/feature_name.md
```

Specify the following parameters

```yaml
---
title: Your Title
subtitle: your subtitle
image: path of the image (Ex img/500_500.svg)
tags: ['feature']
---
Content or Description here
```

## Configure PubMed Api and NSF data

Edit the file `gen_data.py` 

```python
nih_link = 'put your pubmed rss url'
nsf_data_link = 'https://api.nsf.gov/services/v1/awards.json?keyword="your keywords"&printFields=startDate,expDate,id,title,awardee,agency,awardeeName,piFirstName,piLastName,coPDPI'
```

Save and close the file 

Run the file using python

```
python /plab/plab.hugo/gen_data.py
```

By default the update time is set 10 seconds. To change or set the interval update the value in seconds:

```python
sch = scheduler()
sch.add_job(myfn, 'interval', seconds=10)
sch.start()
```

## Updating Team using ORCID
Open the team.json file

```
plab/plab.hugo/static/assets/team.json
```

Add a json entry:
```json
"Franco Pestilli": {
    "type": "active",
    "ORCID":"true",
    "image": "https://brainlife.io/images/avatar/franco.jpg",
    "id": "0000-0002-2469-0494",
    "summary": "A small description",
    "externals": {
        "twitter": "url",
        "facebook": "url",
        "scholar": "url",
        "github": "url"
    }
},
```

Save and then run the file team.py 

```
python /plab/plab.hugo/team.py
```
    
## Updating Team using Hugo

```
hugo new team/examplename.md
```

Open the file and provide the following entries

```yaml
---
name: User Name
image: /img/user.png
position: Example Text
startDate: 2012-09-01 # for alumni entries
facebook: url
scholar: url
linkedin: url
twitter: url
github: url
weight: 100
tags: ['active'] # valid values: collaborator, alumni, active
---
```