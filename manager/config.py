EMAIL_HOST_USER = 'macmanagement199@gmail.com'
EMAIL_HOST_PASSWORD = 'dqcqmjmwvoxosoal'


# Heroku configs
# if os.getcwd() == '/app':
#     import dj_database_url
#     DATABASES = {
#         'default': dj_database_url.config(default='postgres://localhost')
#     }

#     # Honor header 'x-forwarded-proto' para request.is_secure()
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#     # Header to allow all hosts
#     ALLOWED_HOSTS = ['*']

#     # CONFIG FOR STATICFILES
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     STATIC_ROOT = 'staticfiles'
#     STATICFILES_DIRS = (
#         os.path.join(BASE_DIR, 'static'),
#     )

#     AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#     AWS_STORAGE_BUCKET_NAME = 'gui-projects'
#     AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

#     AWS_S3_OBJECT_PARAMETERS = {
#         'CacheControl': 'max-age=86400',
#     }

#     AWS_LOCATION = 'static'
#     STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#     STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
