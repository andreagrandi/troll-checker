import facebook
import os


FB_ACCESS_TOKEN = os.environ.get('FB_ACCESS_TOKEN')
MAX_NUMBER_OF_COMMENTS = 100


graph = facebook.GraphAPI(FB_ACCESS_TOKEN)
profile = graph.get_object(id='me')
posts = graph.get_all_connections(profile['id'], 'posts')

posts_count = 0
comments_count = 0

with open('comments.tsv', 'w') as f:
    for post in posts:
        posts_count += 1
        print('Post: {0}'.format(posts_count))
        comments = graph.get_all_connections(id=post['id'], connection_name='comments')

        for comment in comments:
            comments_count += 1
            print('Comment: {0} - {1}'.format(comments_count, comment['message']))
            message = comment['message'].replace('\n', '')
            f.write(comment['id'] + "\t" + message + "\n")
            if comments_count >= MAX_NUMBER_OF_COMMENTS:   # Stop after 100 comments
                break

        if comments_count >= MAX_NUMBER_OF_COMMENTS:   # Stop after 100 comments
                break
