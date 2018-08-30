from markdown2 import markdown
from jinja2 import Environment, PackageLoader


with open ('./content/changing_to_SSG.md', 'r' ) as file:
        parsed_md = markdown(file.read(), extras = ['metadata'])
        env = Environment(loader=PackageLoader('ssg', 'templates'))
        post_detail_template = env.get_template('post-details.html')
        data = {
            'content': parsed_md,
            'title' : parsed_md.metadata['title'],
            'date' : parsed_md.metadata['date'],
            }
        print(post_detail_template.render(post=data))
        
