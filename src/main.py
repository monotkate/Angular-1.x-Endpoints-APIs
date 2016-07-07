"""This is an test API design.

This code implements several APIs to learn how Google Endpoints works.

"""

import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote
import MySQLdb


class APIMessage(messages.Message):
    """APIMessage that stores a message."""
    message = messages.StringField(1)


USER_RESOURCE = endpoints.ResourceContainer(
    Comment=messages.StringField(1, required=True))

@endpoints.api(name='comment', version='v1')
class SubmitCommentApi(remote.Service):
    """Implements an API to add a comment to the database"""
    @endpoints.method(
        USER_RESOURCE,
        APIMessage,
        path='comments/submit',
        http_method='POST',
        name='submit')
    def submit_comment(self, request):
        host = '<insert the IP address of your Cloud SQL db here>'
        user = 'root'
        passwd = '<insert the root password of your Cloud SQL db here>'
        database = '<insert the data base name here>'

        # Connect to db
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database)
        cursor = db.cursor()

        # Insert data into db
        select_stmt = (
          'INSERT INTO commentTable (Comment) VALUES (%s)'
        )
        values = [
            request.Comment
        ]

        a = cursor.execute(select_stmt, values)

        # Check to make sure lines have changed and commit changes
        if a > 0 :
            cursor.execute('COMMIT')
            return APIMessage(message='Created User Successfully')

        raise endpoints.NotFoundException(message='User Not Created')

@endpoints.api(name='get_comments', version='v1')
class GetCommentsApi(remote.Service):
    """Implements an API to get the comments from the database"""
    @endpoints.method(
        message_types.VoidMessage,
        APIMessage,
        path='comments',
        http_method='GET',
        name='list')
    def list_comments(self, unused_request):
        host = '<insert the IP address of your Cloud SQL db here>'
        user = 'root'
        passwd = '<insert the root password of your Cloud SQL db here>'
        database = '<insert the data base name here>'
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database)
        cursor = db.cursor()
        select_stmt = (
            'SELECT * FROM commentTable'
        )
        a = cursor.execute(select_stmt)
        m = cursor.fetchall()
        return APIMessage(message=str(m))

api = endpoints.api_server([SubmitCommentApi, GetCommentsApi])
