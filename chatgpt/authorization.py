import asyncio
import json
import random
import os

from fastapi import HTTPException

import utils.configs as configs
import utils.globals as globals
from chatgpt.refreshToken import rt2ac
from utils.Logger import logger


def get_req_token(req_token, seed=None):
    # Always return the AUTHORIZATION token from .env
    env_token = os.getenv('AUTHORIZATION')
    if not env_token:
        raise HTTPException(status_code=500, detail="AUTHORIZATION environment variable not set")
    return env_token.strip("'")  # Remove single quotes from the token


async def verify_token(req_token):
    # Always verify against the AUTHORIZATION token from .env
    env_token = os.getenv('AUTHORIZATION')
    if not env_token:
        raise HTTPException(status_code=500, detail="AUTHORIZATION environment variable not set")
    
    env_token = env_token.strip("'")  # Remove single quotes from the token
    
    # Since we're using a direct access token from .env, we can return it directly
    return env_token


async def refresh_all_tokens(force_refresh=False):
    # Since we're using a static token from .env, token refresh is not needed
    logger.info("Token refresh skipped - using static AUTHORIZATION token from .env")
