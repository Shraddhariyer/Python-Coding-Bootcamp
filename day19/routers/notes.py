from fastapi import APIRouter
from schema.notes import NoteCreate
router=APIRouter(prefix="/notes",tags=["Notes"])
@router.post("/")
def create_note(note:NoteCreate):
    return note

@router.get("/")
def get_notes():
    return{"notes":[]}