from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import Session,sessionmaker
from dbconfig import Base,SessionLocal,engine

app = FastAPI()

class UserSchema(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    


Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class User(BaseModel):
    name : str
    
class UserReturn(BaseModel):
    id : int
    name : str


@app.post("/api/newuser",response_model=UserReturn)
def add_new_user(new_user : User,db: Session = Depends(get_db)):
    new_user_info = UserSchema(**new_user.model_dump())
    db.add(new_user_info)
    db.commit()
    db.refresh(new_user_info)
    print(new_user_info)
    return new_user_info


@app.get("/api/allusers")
def get_all_users(db : Session = Depends(get_db)):
    all_users = db.query(UserSchema).all()
    return all_users
    
    
@app.get("/api/getuser/{id}")
def get_specific_user(id:int,db : Session = Depends(get_db)):
    search_user = db.query(UserSchema).filter(UserSchema.id == id).all()
    if search_user != None:
        return search_user
    raise HTTPException(status_code=400,detail="User not exist")
    

@app.put("/api/updateuser/{usr_id}",response_model=UserReturn)
def update_user(usr_id : int, up_user : User,db : Session = Depends(get_db)):
    find_user = db.query(UserSchema).filter(UserSchema.id == usr_id).first()
    if find_user != None:
        find_user.name = up_user.name
        db.commit()
        db.refresh(find_user)
        return find_user
    raise HTTPException(status_code=400,detail="User does not exist")  
    


@app.delete("/api/delete/{usr_id}")
def delete_single_usr(usr_id : int,db : Session = Depends(get_db)):
    get_user = db.query(UserSchema).filter(UserSchema.id == usr_id).first()
    if get_user != None : 
        db.delete(get_user)
        db.commit()
        return {"success" : "User deleted Success"}

    raise HTTPException(status_code=401,detail="User not found")    