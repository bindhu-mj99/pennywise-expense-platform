from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from datetime import date
from pathlib import Path
import sqlite3
app=FastAPI(title="Pennywise API")
DB=Path(__file__).resolve().parent.parent/"pennywise.db"
def db():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
with db() as c:c.execute("CREATE TABLE IF NOT EXISTS tx(id INTEGER PRIMARY KEY,title TEXT,amount REAL,kind TEXT,category TEXT,day TEXT)")
class Tx(BaseModel):
 title:str=Field(min_length=1,max_length=100);amount:float=Field(gt=0);kind:str=Field(pattern="^(income|expense)$");category:str;day:date
@app.get("/health")
def health():return {"status":"ok"}
@app.get("/transactions")
def list_tx():
 with db() as c:return [dict(x) for x in c.execute("SELECT * FROM tx ORDER BY day DESC").fetchall()]
@app.post("/transactions",status_code=201)
def add_tx(x:Tx):
 with db() as c:
  cur=c.execute("INSERT INTO tx(title,amount,kind,category,day) VALUES(?,?,?,?,?)",(x.title.strip(),x.amount,x.kind,x.category,x.day.isoformat()))
  return dict(c.execute("SELECT * FROM tx WHERE id=?",(cur.lastrowid,)).fetchone())
@app.delete("/transactions/{tid}",status_code=204)
def delete_tx(tid:int):
 with db() as c:
  cur=c.execute("DELETE FROM tx WHERE id=?",(tid,))
  if not cur.rowcount:raise HTTPException(404,"Transaction not found")
