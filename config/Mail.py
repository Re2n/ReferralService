from fastapi_mail import ConnectionConfig
from config.Environment import get_environment_variables

env = get_environment_variables()

conf = ConnectionConfig(
    MAIL_USERNAME=env.MAIL_USERNAME,
    MAIL_PASSWORD=env.MAIL_PASSWORD,
    MAIL_PORT=env.MAIL_PORT,
    MAIL_SERVER=env.MAIL_SERVER,
    MAIL_STARTTLS=env.MAIL_STARTTLS,
    MAIL_SSL_TLS=env.MAIL_SSL_TLS,
    MAIL_FROM=env.MAIL_FROM,
)
