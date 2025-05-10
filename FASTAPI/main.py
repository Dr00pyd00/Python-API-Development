from fastapi import FastAPI, Body

app = FastAPI()

# pour lancer server uvicorn :
    # > uvicorn main:app --reload  
        # main : nom du fichier python
        # app : nom de l'instance FastApi


# je donne un url puis dedans je retourne un json:
@app.get('/')
def root():
    return {"message": "Welcome to my API !"}


@app.get('/posts')
def get_posts():
    return {"data":"This is ou posts !"}



@app.post('/createposts')
def create_posts(payLoad: dict = Body(...)):
    print('ma data recu :')
    print( payLoad)
    return {'new_post':f'title = {payLoad['title']}, content = {payLoad['content']}'}