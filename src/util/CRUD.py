"""
        title: "Feynman lectures on physics",
        description: "high quality up-to-date copy of Feynman's legendary lectures totallly free.",
        url: "https://www.feynmanlectures.caltech.edu/",
        img: './math2.png',
        type: TYPES[1],
        topic: TOPICS[0]
        
        
        const TYPES = ["Course", "Book", "Blog", "Repository"];
        const TOPICS = [
  "Mathematics",
  "Machine Learning",
  "Programming Languages",
  "Computer Science",
  "Design",
  "Data Science",
];

"""

def createEntry(title, description, url, img, typeOfEntry, topic):
    """
    this function create an entry for the API and print in console 
    the result.
    """
    
    print("{")
    print(f'title: "{title}",')
    print(f'description: "{description}",')
    print(f'url: "{url}",')
    print(f'img: "{img}",')
    print(f'type: {typeOfEntry},')
    print(f'topic: {topic}')
    print("}")

createEntry("OSSu Math", "Path to a free self-taught education in Math!", "https://github.com/ossu/math", './math6.png', "TYPES[3]","TOPICS[0]")