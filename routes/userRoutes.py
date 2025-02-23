from fastapi import APIRouter, Depends
from controllers.UserController import UserController

router = APIRouter()

router.get("/users")(UserController.get_all_users)
router.post("/users")(UserController.create_user)
router.get("/users/{id}")(UserController.get_user_by_id)
router.put("/users/{id}")(UserController.update_user)
router.delete("/users/{id}")(UserController.delete_user)