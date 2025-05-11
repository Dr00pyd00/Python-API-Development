# pour lancer server uvicorn :
    # > uvicorn main:app --reload  
        # main : nom du fichier python
        # app : nom de l'instance FastApi


from fastapi import FastAPI, Body, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange
app = FastAPI()


class Post(BaseModel): 
    title: str
    content: str
    published: bool = True  # default
    rating: Optional[int] = None


# variable pour sotcker les datas:
my_posts = [{'title':'title of post 1', 'content':'content of post 1', 'id':1},
            {'title':'favorite food','content':'I like pizza', 'id':2}]


def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post

def find_index_post(id):
    for index, content in enumerate(my_posts):
        if content['id'] == id:
            return index



@app.get('/')
def root():
    return {"message": "Welcome to my API !"}


@app.get('/posts')
def get_posts():
    return {"data":my_posts}



@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100000)
    my_posts.append(post_dict)
    print(post_dict)
    print(my_posts)
    return {'data': post_dict}
# we want title: str / content: str




# retrieve a post :
@app.get('/posts/{id}')
def get_a_post(id:int):
    post = find_post(id)
    print(post)
    if not post:    
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id of {id} was not found!')  
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'post':f' id:{id} Not Found !'}
    
    return {'post_detail':f'Here is post {id}',
            'the post': post}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    post_index = find_index_post(id)
    if post_index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id {id} not exist!')
    my_posts.pop(post_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


    # update qq chose :

@app.put('/posts/{id}')
def update_post_kappa(id:int, post: Post):

    post_index = find_index_post(id)
    if post_index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id {id} not exist!')
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[post_index] = post_dict
    return {'post updated:':post_dict}