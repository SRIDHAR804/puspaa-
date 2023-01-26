# Kanged By © @always_hungry365
# Owner Mayank
# All rights reserved. © Alisha © Onelove © Yukki

from OneloveMusic.core.bot import OneloveBot
from OneloveMusic.core.dir import dirr
from OneloveMusic.core.git import git
from OneloveMusic.core.userbot import Userbot
from OneloveMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = OneloveBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
