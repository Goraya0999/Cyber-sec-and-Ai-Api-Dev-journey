import sqlite3
from schema import ShipmentCreate,ShipmentUpdate
from typing import Any



class Database:
    def connect_to_db(self):
        self.conn=sqlite3.connect("sqlite.db",check_same_thread=False)
        #get cursor to execuate sql commands 
        self.cur=self.conn.cursor()
        print("Connected to the database successfully")
    
    def crete_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS shipment (
                    id INTEGER PRIMARY KEY,
                    content TEXT,
                    weight REAL,
                    status TEXT        
                         )
            
        """)


    def create(self,shipment:ShipmentCreate)->int:
        self.cur.execute("SELECT MAX(id) FROM shipment")
        result=self.cur.fetchone()
        new_id=result[0] + 1
        #insert value in table
        self.cur.execute("""
        INSERT INTO shipment
        VALUES (:id,:content,:weight,:status)             
                          """,{
        "id":new_id,
        **shipment.model_dump(),
        "status":"placed",
                          })
        self.conn.commit()
        return new_id

    def get(self,id:int) ->dict[str,Any] | None:
        self.cur.execute("""
         SELECT * FROM shipment
           WHERE id=?
        """,(id,))
        row=self.cur.fetchone()
        
        return {
            "id":row[0],
            "content":row[1],
            "weight":row[2],
            "status":row[3]
        } if row else None
    
    def update(self,id:int,shipment:ShipmentUpdate) -> dict[str,Any]:
        self.cur.execute("""
        UPDATE shipment SET status = :status
                         WHERE id=:id


        """,{
             "id":id,
             **shipment.model_dump()
        }
        )
        self.conn.commit()
        return self.get(id)
    
    #delete 
    def delete(self,id:int):
        self.cur.execute("""
        DELETE FROM shipment 
                         WHERE id=?  
           """,(id,))
        self.conn.commit()
    
    def close(self):
        print("connection is closing .....")
        self.conn.close()
    
    def __enter__(self):
        print("Enter context......")
        self.connect_to_db()
        self.crete_table()
        return self
    
    def __exit__(self, *arg):
        print("existing context .....")
        self.close()

def managed_db():
    db=Database()
    #setup
    db.connect_to_db()
    db.crete_table()

    yield db

    db.close()

with Database() as db:
    print(db.get(12834))