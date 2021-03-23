# plab.hugo

Customizable Hugo wesbite template

## Features

  

- Customisable Home Page

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

## Show research papers using PubMed Api

