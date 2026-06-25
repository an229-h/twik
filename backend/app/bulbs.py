from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from app.mqtt import publish_bulb_state

router = APIRouter()

bulb_states = {1: False, 2: False, 3: False, 4: False}


@router.get("/bulbs")
def get_bulbs(username: str = Depends(get_current_user)):
    return bulb_states


@router.post("/bulbs/{bulb_id}/toggle")
def toggle_bulb(
    bulb_id: int,
    username: str = Depends(get_current_user)
):
    if bulb_id not in bulb_states:
        return {
            "success": False,
            "message": "Bulb not found"
        }

    bulb_states[bulb_id] = not bulb_states[bulb_id]

    publish_bulb_state(bulb_id, bulb_states[bulb_id])

    return {
        "success": True,
        "bulb": bulb_id,
        "state": bulb_states[bulb_id]
    }