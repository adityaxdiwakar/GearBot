from tornado.web import removeslash

from Other import BackendUtils
from Other.Handlers import PrimaryHandler


class DiscordOAuthCallback(PrimaryHandler):
    @removeslash
    async def get(self):
        auth_code = self.get_query_argument("code")

        bearer_token = await BackendUtils.get_bearer_token(auth_code=auth_code, refresh=False)

        userID = await BackendUtils.get_user_id(bearer_token)
        await BackendUtils.get_guild_list(userID, token=bearer_token)  # Puts the data in the cache

        self.set_secure_cookie(
            name="userauthtoken",
            value=str(userID)
        )

        self.redirect("/dashboard")