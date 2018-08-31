import os
from datetime import datetime
from jinja2 import Environment, PackageLoader
from markdown2 import markdown 
from os.path import isfile

def main():
    #print('entered')
    POSTS = {}

    env = Environment(loader = PackageLoader('ssg'))#if the location of templates is not given, Package loader assumes the location of "templates" folder on the same directory containing the file running this code

    index_template = env.get_template('index.html')
    post_template = env.get_template('post-details.html')
    
    markdown_posts = filter(isfile,
                            map(lambda x: os.path.join('./content', x),
                                os.listdir('./content')))
                            
    #print('markdown posts', list(markdown_posts))

    for markdown_post in markdown_posts: 
        with open(markdown_post, 'r') as file:

            parsed_page = markdown(file.read(), extras=['metadata'])
            #print('parsed page', parsed_page)

            slug_html = parsed_page.metadata['slug'].replace('.md', '.html')
            parsed_page.metadata['slug_html'] = slug_html #custom metadata for a href working hackkk!!! improve it
            parsed_page.metadata['content'] = parsed_page #remove it early

            post_html_content = post_template.render(post=parsed_page.metadata)
            #print('metadata', parsed_page.metadata)
            output_post_path = './output/' + slug_html
            with open(output_post_path, 'w') as write_file:
                #print(post_html_content)
                write_file.write(post_html_content)
            
            POSTS[markdown_post] = parsed_page

    #to do sort posts in chronological order
    index_post_metadata = [POSTS[p].metadata for p in POSTS]
    index_html_content = index_template.render(posts=index_post_metadata)
    
    #print(index_post_metadata)
    #print(index_html_content, type(index_html_content))
    with open('./index.html', 'w') as file:
        file.write(index_html_content)
    


if __name__ == '__main__':
    main()

