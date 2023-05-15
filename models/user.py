#!/usr/bin/python3

"""User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Class` User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, *8kwargs):
        """Initialize User Instance."""
        super().__init__(*args, **kwargs)
