from  model.add_comments import addComments
import datetime
import json



def main_menu():
        print('Select options:')
        print('1. Create a comment. \n2. EDit comment ')
        option = input("Enter a number to choose.")
        if int(option) is  int(1):

            Comments().post_comment()

        if int(option) is  2:
            pass
        if int(option) is 3:
            pass
   
class Comments(object):
    
    list_comments = []

    def post_comment(self):
        
        comment = input("create a comment, press exit to go back to main menu.")
        
        comments_obj = addComments(1, comment , str(datetime.datetime.now()))
        
        if comment is None:
            print('please first include the comment.')

            Comments().post_comment()

        if str(comment).strip() == 'exit'.strip():
           return  main_menu()

        else:

            comments_request  = json.loads(comments_obj.json())
            Comments.list_comments.append(comments_request)
            print(Comments.list_comments)
            Comments().post_comment()



if __name__ == '__main__':
    
    main_menu()
    

    


