import os

from dotenv import load_dotenv

load_dotenv()

"""Positive"""
valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

"""Negative"""
invalid_email1 = os.getenv('invalid_email')
invalid_password1 = os.getenv('invalid_password')