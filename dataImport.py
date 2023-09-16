import json
from redis import Redis
from urllib.request import urlopen

redis = Redis(
    host="shahredis",
    port=6379,
    password="foo",
    db=0,
    decode_responses=True
)


def import_data(category):
    # check if the data is already in redis or not
    if redis.get(category) is None:
        # import data from json files from my GitHub ripo
        url = 'https://raw.githubusercontent.com/shahmarasy/website-data/main/' + category + '.json'
        with urlopen(url) as response:
            source = response.read()
            data = json.loads(source)
            # import data to redis
            redis.set(category, json.dumps(data))
            # return the result
            return json.loads(redis.get(category))
    else:
        return json.loads(redis.get(category))


def about_me():
    my_text = '''
    Hi there, I'm Bahman and I'm a developer based in Istanbul. I was born on February 2nd, 1990 in Tabriz and I started
     programming at the young age of 13. Since then, I've developed a strong passion for programming and have gained 
     experience in various programming languages and frameworks.
    <br><br>
    I'm skilled in PHP, JavaScript, and Python, and have extensive knowledge in HTML/CSS markup language. I have worked
     with various PHP frameworks such as Laravel, Symfony, Codeigniter, and Leaf, and also have experience working 
     with JS/TS frameworks and libraries such as JQuery, VueJS, Express and NestJS.
    <br><br>
    In addition,I'm familiar with Python frameworks like Django, Flask, and FastAPI, and have worked with CSS frameworks 
    like Bootsrap and Tailwind CSS. I'm comfortable working with APIs and have experience in RESTful, 
    JSON and GraphQL.
    <br><br>
    When it comes to databases, I have experience with MySQL, MariaDB, PostgreSQL, MongoDB, and SQLite.I'm also 
    familiar with caching and message brokers such as Redis, RabitMQL, and Kafka. And for version control, I use Git 
    and have experience with package managers such as NPM, Yarn, Composer, and PIP.
    <br><br>
    Overall, I'm a well-rounded developer with a passion for creating high-quality, efficient, and user-friendly 
    software applications.
    '''
    return {'content': my_text}


# remove all data from redis
def flush_all():
    redis.flushall()
    return {'result': 'done'}
